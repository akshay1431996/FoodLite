"""Golden Crumb — a small Flask website for a cake shop."""

import os
import re
from datetime import date

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

from data import CAKES, CATEGORIES, TESTIMONIALS, get_cake

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MAX_QTY = 20


def cart_items():
    """Return the cart as a list of (cake, qty, line_total) plus the grand total."""
    items, total = [], 0.0
    for slug, qty in session.get("cart", {}).items():
        cake = get_cake(slug)
        if cake:
            line = cake["price"] * qty
            items.append({"cake": cake, "qty": qty, "line_total": line})
            total += line
    return items, total


@app.context_processor
def inject_cart_count():
    return {"cart_count": sum(session.get("cart", {}).values())}


@app.template_filter("money")
def money(value):
    return f"${value:,.2f}"


@app.route("/")
def index():
    featured = [c for c in CAKES if c["badge"]][:3]
    return render_template("index.html", featured=featured, testimonials=TESTIMONIALS)


@app.route("/menu")
def menu():
    category = request.args.get("category", "All")
    if category not in CATEGORIES:
        category = "All"
    cakes = CAKES if category == "All" else [c for c in CAKES if c["category"] == category]
    return render_template("menu.html", cakes=cakes, categories=CATEGORIES, active=category)


@app.route("/cake/<slug>")
def cake_detail(slug):
    cake = get_cake(slug) or abort(404)
    related = [c for c in CAKES if c["category"] == cake["category"] and c["slug"] != slug][:3]
    return render_template("cake.html", cake=cake, related=related)


@app.post("/cart/add/<slug>")
def cart_add(slug):
    cake = get_cake(slug) or abort(404)
    qty = max(1, min(MAX_QTY, request.form.get("qty", 1, type=int) or 1))
    cart = session.get("cart", {})
    cart[slug] = min(MAX_QTY, cart.get(slug, 0) + qty)
    session["cart"] = cart
    flash(f"Added {cake['name']} to your box.", "success")
    return redirect(request.referrer or url_for("menu"))


@app.post("/cart/update/<slug>")
def cart_update(slug):
    cart = session.get("cart", {})
    qty = request.form.get("qty", 0, type=int) or 0
    if qty <= 0:
        cart.pop(slug, None)
    elif slug in cart:
        cart[slug] = min(MAX_QTY, qty)
    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    items, total = cart_items()
    return render_template("cart.html", items=items, total=total, today=date.today().isoformat())


@app.post("/checkout")
def checkout():
    items, total = cart_items()
    if not items:
        flash("Your box is empty.", "error")
        return redirect(url_for("menu"))

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    try:
        pickup = date.fromisoformat(request.form.get("pickup", "").strip())
    except ValueError:
        pickup = None
    if not name or not EMAIL_RE.match(email) or not pickup or pickup < date.today():
        flash("Please enter your name, a valid email and a pickup date from today on.", "error")
        return redirect(url_for("cart"))

    session.pop("cart", None)
    pickup_label = f"{pickup:%A, %B} {pickup.day}, {pickup.year}"
    return render_template("success.html", name=name, items=items, total=total, pickup=pickup_label)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not EMAIL_RE.match(email) or not message:
            flash("Please fill in every field with a valid email.", "error")
            return render_template("contact.html", form=request.form), 400
        flash(f"Thanks {name}! We'll get back to you within a day.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form={})


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))
