"""Catalogue data for the Golden Crumb cake shop."""

CATEGORIES = ["All", "Signature", "Cheesecakes", "Cupcakes", "Celebration"]

CAKES = [
    {
        "slug": "lemon-sunshine",
        "name": "Lemon Sunshine",
        "category": "Signature",
        "price": 32.00,
        "emoji": "🍋",
        "tagline": "Zesty lemon sponge with silky curd",
        "description": "Three layers of buttery lemon sponge, filled with house-made "
        "lemon curd and finished with a whipped mascarpone frosting and candied zest.",
        "serves": "8–10",
        "rating": 4.9,
        "badge": "Bestseller",
    },
    {
        "slug": "honey-almond",
        "name": "Honey Almond Dream",
        "category": "Signature",
        "price": 36.00,
        "emoji": "🍯",
        "tagline": "Wildflower honey & toasted almonds",
        "description": "A moist almond cake soaked in wildflower honey syrup, layered with "
        "honey buttercream and crowned with caramelised almond brittle.",
        "serves": "8–10",
        "rating": 4.8,
        "badge": "New",
    },
    {
        "slug": "mango-passion",
        "name": "Mango Passion",
        "category": "Signature",
        "price": 34.00,
        "emoji": "🥭",
        "tagline": "Tropical mousse on a coconut base",
        "description": "Alphonso mango mousse and passion fruit glaze set over a crisp "
        "coconut dacquoise. Light, bright and refreshing.",
        "serves": "6–8",
        "rating": 4.7,
        "badge": None,
    },
    {
        "slug": "classic-cheesecake",
        "name": "New York Cheesecake",
        "category": "Cheesecakes",
        "price": 30.00,
        "emoji": "🍰",
        "tagline": "Dense, creamy and timeless",
        "description": "Baked low and slow on a graham cracker crust, served with a "
        "golden apricot compote on the side.",
        "serves": "8–10",
        "rating": 4.9,
        "badge": "Classic",
    },
    {
        "slug": "salted-caramel-cheesecake",
        "name": "Salted Caramel Cheesecake",
        "category": "Cheesecakes",
        "price": 33.00,
        "emoji": "🍮",
        "tagline": "Caramel swirl with sea salt flakes",
        "description": "Our classic cheesecake swirled with buttery salted caramel and "
        "topped with a glossy caramel mirror and Maldon salt.",
        "serves": "8–10",
        "rating": 4.8,
        "badge": None,
    },
    {
        "slug": "vanilla-bean-cupcakes",
        "name": "Vanilla Bean Cupcakes",
        "category": "Cupcakes",
        "price": 18.00,
        "emoji": "🧁",
        "tagline": "Box of six, Madagascar vanilla",
        "description": "Fluffy vanilla bean cupcakes piped with Swiss meringue buttercream "
        "and finished with edible gold sprinkles. Box of six.",
        "serves": "6",
        "rating": 4.6,
        "badge": None,
    },
    {
        "slug": "banana-toffee-cupcakes",
        "name": "Banana Toffee Cupcakes",
        "category": "Cupcakes",
        "price": 19.00,
        "emoji": "🍌",
        "tagline": "Box of six, banoffee-inspired",
        "description": "Banana cupcakes with a hidden toffee centre, whipped cream frosting "
        "and a dusting of dark chocolate. Box of six.",
        "serves": "6",
        "rating": 4.7,
        "badge": "Popular",
    },
    {
        "slug": "golden-celebration",
        "name": "Golden Celebration",
        "category": "Celebration",
        "price": 58.00,
        "emoji": "🎂",
        "tagline": "Two tiers of party-ready joy",
        "description": "A two-tier vanilla and butterscotch cake with gold leaf accents, "
        "fresh flowers and a personalised message plaque.",
        "serves": "20–25",
        "rating": 5.0,
        "badge": "Premium",
    },
    {
        "slug": "sunflower-birthday",
        "name": "Sunflower Birthday",
        "category": "Celebration",
        "price": 44.00,
        "emoji": "🌻",
        "tagline": "Hand-piped sunflower bouquet",
        "description": "Orange-scented sponge with apricot jam, decorated with a bouquet of "
        "hand-piped buttercream sunflowers.",
        "serves": "12–15",
        "rating": 4.9,
        "badge": None,
    },
]

TESTIMONIALS = [
    {"name": "Priya S.", "text": "The Lemon Sunshine cake was the star of my daughter's birthday. Everyone asked where it was from!", "rating": 5},
    {"name": "Daniel R.", "text": "Ordered online, picked up the same afternoon. Beautiful presentation and tastes even better.", "rating": 5},
    {"name": "Meera K.", "text": "Their cheesecake is the creamiest I've ever had. The salted caramel one is dangerous.", "rating": 5},
]


def get_cake(slug):
    return next((c for c in CAKES if c["slug"] == slug), None)
