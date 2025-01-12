import sys
import unittest
from io import StringIO
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from chicken_nugget_fun_solution import chicken_nugget_fun


class TestChickenNuggetFun(unittest.TestCase):
    """Test cases for the `chicken_nugget_fun` function."""

    def test_output(self):
        """Test if the output contains a valid chicken nugget fact."""
        # Backup original stdout
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # Run the function
            chicken_nugget_fun()

            # Get the output
            output = sys.stdout.getvalue()

            # Check if the output contains a nugget fact
            self.assertTrue(
                any(
                    fact in output
                    for fact in [
                        "Chicken nuggets were invented",
                        "The world record for eating chicken nuggets",
                        "McDonald's nuggets come in four shapes",
                        "Try making homemade nuggets",
                        "Some people dip chicken nuggets in honey",
                        "Chicken nuggets are eaten by millions",
                        "Sweet chili sauce makes chicken nuggets extra tasty",
                        "You can even make plant-based chicken nuggets",
                    ]
                ),
                "Output did not contain a valid chicken nugget fact.",
            )
        finally:
            # Restore original stdout
            sys.stdout = original_stdout


if __name__ == "__main__":
    unittest.main()
