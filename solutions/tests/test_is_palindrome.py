"""
Test module for the is_palindrome function.

Test categories:
    - Standard cases: typical strings to verify palindrome status
    - Edge cases: empty string, single-character strings
    - Defensive tests: invalid input types

Created on 03-01-25
Updated on 10-01-25

"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        """Test for a string that is a palindrome."""
        result = is_palindrome("madam")
        self.assertTrue(result)

    def test_non_palindrome(self):
        """Test for a string that is not a palindrome."""
        result = is_palindrome("hello")
        self.assertFalse(result)

    def test_empty_string(self):
        """Test for an empty string."""
        result = is_palindrome("")
        self.assertTrue(result)

    def test_single_character(self):
        """Test for a single-character string."""
        result = is_palindrome("a")
        self.assertTrue(result)

    def test_invalid_input_type(self):
        """Test for invalid input types."""
        with self.assertRaises(TypeError):
            is_palindrome(12345)


if __name__ == "__main__":
    unittest.main()
