import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app  # noqa: E402


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c


@pytest.mark.parametrize("path", ["/", "/menu", "/menu?category=Cupcakes", "/cake/lemon-sunshine", "/cart", "/contact"])
def test_pages_render(client, path):
    assert client.get(path).status_code == 200


def test_unknown_cake_404(client):
    assert client.get("/cake/nope").status_code == 404


def test_cart_flow(client):
    client.post("/cart/add/lemon-sunshine", data={"qty": 2})
    page = client.get("/cart").get_data(as_text=True)
    assert "Lemon Sunshine" in page and "$64.00" in page

    client.post("/cart/update/lemon-sunshine", data={"qty": 0})
    assert "Your box is empty" in client.get("/cart").get_data(as_text=True)


def test_checkout(client):
    client.post("/cart/add/classic-cheesecake")
    bad = client.post("/checkout", data={"name": "A", "email": "bad", "pickup": "2026-10-20"})
    assert bad.status_code == 302

    ok = client.post("/checkout", data={"name": "Ana", "email": "a@b.co", "pickup": "2026-10-20"})
    assert "Thank you, Ana!" in ok.get_data(as_text=True)
    assert "Your box is empty" in client.get("/cart").get_data(as_text=True)


def test_contact_validation(client):
    assert client.post("/contact", data={"name": "", "email": "", "message": ""}).status_code == 400
    assert client.post("/contact", data={"name": "A", "email": "a@b.co", "message": "Hi"}).status_code == 302
