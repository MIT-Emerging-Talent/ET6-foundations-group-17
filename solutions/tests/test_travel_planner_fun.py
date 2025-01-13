import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from travel_planner_fun_solution import TravelPlanner


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


if __name__ == "__main__":
    unittest.main()
