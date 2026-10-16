# Golden Crumb — Cake Shop Website (Python / Flask)

A modern cake shop website with a warm **yellow theme** and **glassmorphism** UI
(frosted, blurred translucent panels over animated colour blobs).

## Features
- Home page with hero, featured cakes, highlights and testimonials
- Menu with category filters (Signature, Cheesecakes, Cupcakes, Celebration)
- Cake detail pages with quantity stepper and related cakes
- Session-based cake box (cart): add, update quantity, remove
- Checkout for in-store pickup with validation and order confirmation
- Contact / custom-order form with validation
- Responsive layout with mobile menu, scroll-reveal animations,
  and `prefers-reduced-motion` support

## Run it
```bash
cd cake_shop
pip install -r requirements.txt
python app.py            # http://127.0.0.1:5000
```
Set `SECRET_KEY` in production. Use `FLASK_DEBUG=1` for debug mode.

## Tests
```bash
pip install pytest
python -m pytest
```

## Structure
```
cake_shop/
├── app.py          # Flask routes, cart & checkout logic
├── data.py         # Cakes, categories, testimonials
├── templates/      # Jinja2 templates
├── static/css/     # Yellow glassmorphism styles
├── static/js/      # Nav toggle, reveal animations, qty stepper
└── tests/          # pytest suite
```
