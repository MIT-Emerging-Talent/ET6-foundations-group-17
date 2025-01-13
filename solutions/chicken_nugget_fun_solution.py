import random


def chicken_nugget_fun():
    print("Welcome to the Chicken Nugget Fun Zone!")

    nugget_facts = [
        "Chicken nuggets were invented in the 1950s by Robert C. Baker!",
        "The world record for eating chicken nuggets is 746 grams in 3 minutes!",
        "McDonald's nuggets come in four shapes: bell, bow-tie, ball, and boot.",
        "Try making homemade nuggets with chicken, breadcrumbs, and spices!",
        "Some people dip chicken nuggets in honey—have you tried it?",
        "Chicken nuggets are eaten by millions around the world every day!",
        "Sweet chili sauce makes chicken nuggets extra tasty!",
        "You can even make plant-based chicken nuggets now!",
    ]

    random_fact = random.choice(nugget_facts)
    print(f"Here's your nugget fun: {random_fact}")
