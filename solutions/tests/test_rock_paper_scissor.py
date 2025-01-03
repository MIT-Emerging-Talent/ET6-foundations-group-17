"""
Test module for play_round function in the Rock-Paper-Scissors game.
Contains tests for standard cases, edge cases, and defensive assertions.

Test categories:
    - Standard cases: typical user inputs and expected game results
    - Edge cases: empty input and invalid input
    - Defensive tests: wrong input types, assertions

Created on 31-12-24
Author: Abdulrahman Alsir + Codi
"""

import unittest
import random
from ..rock_paper_scissor import play_round


class TestPlayRound(unittest.TestCase):
    """Test suite for the play_round function in the
    Rock-Paper-Scissors game."""

    def test_valid_choices(self):
        """Test valid user choices and ensure the result is valid."""
        valid_choices = ["rock", "paper", "scissors"]
        for choice in valid_choices:
            with self.subTest(choice=choice):
                result = play_round(choice)
                self.assertIn(result, ["win", "lose", "draw"])

    def test_user_wins(self):
        """Test that the user wins when playing 'rock' against 'scissors'."""
        random.choice = lambda options: "scissors"
        result = play_round("rock")
        self.assertEqual(result, "win")

    def test_user_loses(self):
        """Test that the user loses when playing 'rock' against 'paper'."""
        random.choice = lambda options: "paper"
        result = play_round("rock")
        self.assertEqual(result, "lose")

    def test_draw(self):
        """Test that the game results in a draw when both play 'scissors'."""
        random.choice = lambda options: "scissors"
        result = play_round("scissors")
        self.assertEqual(result, "draw")

    def test_empty_input(self):
        """Test that an empty input raises an AssertionError."""
        with self.assertRaises(AssertionError):
            play_round("")

    def test_invalid_input(self):
        """Test handling of invalid input and ensure a valid result
        is returned."""
        invalid_input = "invalid_choice"
        result = play_round(invalid_input)
        self.assertIn(result, ["win", "lose", "draw"])

    def test_defensive_assertions(self):
        """Test that an AssertionError is raised for non-string input."""
        with self.assertRaises(AssertionError):
            play_round(123)


if __name__ == "__main__":
    unittest.main()
