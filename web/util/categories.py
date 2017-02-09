CATEGORIES = [
    {
        'id': 'accessories',
        'name': 'Accessories',
        'desc': 'Scarves, hats, and hair accessories that tie it all together',
    },
    {
        'id': 'art',
        'name': 'Art & Collectibles',
        'desc': 'Paintings, prints and figurines to turn your home into a gallery',
    },
    {
        'id': 'bags_purses',
        'name': 'Bags & Purses',
        'desc': 'Handbags, clutches and totes to carry it all with you',
    },
    {
        'id': 'bath_beauty',
        'name': 'Bath & Beauty',
        'desc': 'Soap up and makeup.',
    },
    {
        'id': 'books_movies_music',
        'name': 'Books, Movies & Music',
        'desc': 'Planners, journals and notebooks because writing on paper is still a thing',
    },
    {
        'id': 'clothing',
        'name': 'Clothing',
        'desc': 'Clothing for women, men, and kids—we got you covered',
    },
    {
        'id': 'crafts_and_tools',
        'name': 'Craft Supplies & Tools',
        'desc': ('Crochet patterns, knitting patterns, and endless yards of yarn '
                 'to keep your hooks and needles in action'),
    },
    {
        'id': 'electronics_and_accessories',
        'name': 'Electronics & Accessories',
        'desc': ('Phone cases, laptop sleeves and decals to protect and '
                 'personalize your portables'),
    },
    {
        'id': 'home_and_living',
        'name': 'Home & Living',
        'desc': 'Wall decor, candles and furniture to make your home yours',
    },
    {
        'id': 'jewelry',
        'name': 'Jewelry',
        'desc': 'Rings, earrings and necklaces to instantly raise your jewelry-box game',
    },
    {
        'id': 'paper_party_supplies',
        'name': 'Paper & Party Supplies',
        'desc': ('Greeting cards, invitations and decor to make parties easy to '
                 'plan and always unforgettable'),
    },
    {
        'id': 'pet_supplies',
        'name': 'Pet Supplies',
        'desc': 'Collars, toys and custom portraits for pets. Your little fuzzball deserves it.',
    },
    {
        'id': 'shoes',
        'name': 'Shoes',
        'desc': ('Shoes for women, men, girls and boys. Shoes for anything with '
                 'human-like feet, basically.'),
    },
    {
        'id': 'toys_games',
        'name': 'Toys & Games',
        'desc': 'Stuffed animals, costumes and games for kids and the kid-like',
    },
    {
        'id': 'weddings',
        'name': 'Weddings',
        'desc': ('Wedding invitations, dresses and decorations for a big day '
                 'that’s as you as it can be'),
    }
]

CAT_NAME_LOOKUP = {c['id']: c['name'] for c in CATEGORIES}

CAT_ID_LOOKUP = {c['name']: c['id'] for c in CATEGORIES}
