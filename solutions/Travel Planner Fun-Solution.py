python
import random

class TravelPlanner:
    def __init__(self):
        self.destinations = [
            "Paris, France",
            "Kyoto, Japan",
            "Machu Picchu, Peru",
            "Cape Town, South Africa",
            "New York City, USA",
            "Santorini, Greece",
            "Cairo, Egypt",
            "Sydney, Australia",
            "Reykjavik, Iceland",
            "Bali, Indonesia"
        ]
        self.activities = [
            "exploring ancient ruins",
            "dining at a Michelin-star restaurant",
            "taking a hot air balloon ride",
            "relaxing on a pristine beach",
            "hiking through breathtaking trails",
            "shopping in local markets",
            "attending a cultural festival",
            "snorkeling with vibrant marine life",
            "enjoying a scenic train ride",
            "visiting world-class museums"
        ]
        self.tips = [
            "Always pack a portable charger!",
            "Learn a few phrases in the local language to impress locals.",
            "Carry a reusable water bottle to stay hydrated.",
            "Don’t forget travel insurance—it’s a lifesaver!",
            "Try street food—it’s often the tastiest and cheapest option.",
            "Keep a digital and physical copy of your passport.",
            "Research local customs to avoid awkward situations.",
            "Pack light—you’ll thank yourself later.",
            "Wake up early to enjoy tourist spots without crowds.",
            "Always have some local currency on hand for small purchases."
        ]

    def generate_destination(self):
        return random.choice(self.destinations)

    def generate_activity(self):
        return random.choice(self.activities)

    def generate_travel_tip(self):
        return random.choice(self.tips)

    def plan_trip(self):
        destination = self.generate_destination()
        activity = self.generate_activity()
        tip = self.generate_travel_tip()

        return {
            "destination": destination,
            "activity": activity,
            "tip": tip
        }

def main():
    print("Welcome to the Automated Travel Planner! \U0001F30D")
    print("Sit back and relax while we plan your next dream trip.\n")

    planner = TravelPlanner()
    trip = planner.plan_trip()

    print(f"\U0001F4CD Destination: {trip['destination']}")
    print(f"\U0001F3C3 Activity: {trip['activity']}")
    print(f"\U0001F4D6 Travel Tip: {trip['tip']}\n")

    print("Your virtual getaway is ready! Safe travels! \U0001F30F")

if __name__ == "__main__":
    main()
