"""
Unit tests for the choose_difficulty function from the number guessing game module.

This module contains unit tests for the number guessing game, specifically testing
the choose_difficulty function and the number_guessing_game function.

Tests included:
- TestChooseDifficulty: Tests for the choose_difficulty function.
- TestNumberGuessingGame: Tests for the number_guessing_game function.

Author: Malak Battatt
Date: January 7th, 2025
"""

import os
import sys
import unittest

# To make the tests pass, change to an absolute import path "from number_guessing_game.py"
from ..number_guessing_game import choose_difficulty, number_guessing_game

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestChooseDifficulty(unittest.TestCase):
    """Unit tests for the `choose_difficulty` function."""

    def test_easy_difficulty(self):
        """Test Easy difficulty with expected range and attempts."""
        number, attempts, message = choose_difficulty(1)
        self.assertTrue(1 <= number <= 50)
        self.assertEqual(attempts, 15)
        self.assertEqual(message, "Easy (1 to 50) - 15 attempts")

    def test_medium_difficulty(self):
        """Test Medium difficulty with expected range and attempts."""
        number, attempts, message = choose_difficulty(2)
        self.assertTrue(1 <= number <= 50)
        self.assertEqual(attempts, 10)
        self.assertEqual(message, "Medium (1 to 50) - 10 attempts")

    def test_hard_difficulty(self):
        """Test Hard difficulty with expected range and attempts."""
        number, attempts, message = choose_difficulty(3)
        self.assertTrue(1 <= number <= 50)
        self.assertEqual(attempts, 5)
        self.assertEqual(message, "Hard (1 to 50) - 5 attempts")

    def test_invalid_input(self):
        """Test defaulting to Medium on invalid input."""
        number, attempts, message = choose_difficulty(4)
        self.assertTrue(1 <= number <= 50)
        self.assertEqual(attempts, 10)
        self.assertEqual(
            message,
            "Invalid choice! Defaulting to Medium (1 to 50) with 10 attempts.",
        )


class TestNumberGuessingGame(unittest.TestCase):
    """Unit tests for the `number_guessing_game` function."""

    def test_game_welcome_message(self):
        """Test the welcome message."""
        messages = number_guessing_game(2, [25, 30, 40, 50, 45, 48, 50, 35, 20, 15])
        self.assertIn("Welcome to the Number Guessing Game!", messages)

    def test_game_choose_difficulty(self):
        """Test the difficulty selection message."""
        messages = number_guessing_game(2, [25, 30, 40, 50, 45, 48, 50, 35, 20, 15])
        self.assertIn("Let's choose a difficulty level:", messages)

    def test_game_difficulty_message(self):
        """Test the difficulty message."""
        messages = number_guessing_game(2, [25, 30, 40, 50, 45, 48, 50, 35, 20, 15])
        self.assertIn("Medium (1 to 50) - 10 attempts", messages)

    def test_game_attempts_message(self):
        """Test the attempts message."""
        messages = number_guessing_game(2, [25, 30, 40, 50, 45, 48, 50, 35, 20, 15])
        self.assertIn("\nYou have 10 attempts left.", messages)


if __name__ == "__main__":
    unittest.main()
