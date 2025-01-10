import unittest
from travel_planner import TravelPlanner  # Replace travel_planner with the name of your script file.

class TestTravelPlanner(unittest.TestCase):
    def setUp(self):
        self.planner = TravelPlanner()

    def test_generate_destination(self):
        destination = self.planner.generate_destination()
        self.assertIn(destination, self.planner.destinations)

    def test_generate_activity(self):
        activity = self.planner.generate_activity()
        self.assertIn(activity, self.planner.activities)

    def test_generate_travel_tip(self):
        tip = self.planner.generate_travel_tip()
        self.assertIn(tip, self.planner.tips)

    def test_plan_trip(self):
        trip = self.planner.plan_trip()
        self.assertIn(trip["destination"], self.planner.destinations)
        self.assertIn(trip["activity"], self.planner.activities)
        self.assertIn(trip["tip"], self.planner.tips)

if _name_ == "_main_":
    unittest.main()