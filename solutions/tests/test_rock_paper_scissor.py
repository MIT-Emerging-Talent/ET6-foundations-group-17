"""
Test module for play_round function in the Rock-Paper-Scissors game.
Contains tests for standard cases, edge cases, and defensive assertions.

Test categories:
    - Standard cases: typical user inputs and expected game results
    - Edge cases: empty input, invalid input, and quitting the game
    - Defensive tests: wrong input types, assertions

Created on 31-12-24
Updated on 09-01-25
Author: Abdulrahman Ali + Cody
"""

import unittest
import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from rock_paper_scissor import play_round


class TestPlayRound(unittest.TestCase):
    """Test suite for the play_round function in the Rock-Paper-Scissors game."""

    def test_rock_beats_scissors(self):
        """Test rock wins against scissors."""
        random.choice = lambda options: "scissors"
        self.assertEqual(play_round("rock"), "win! Computer's choice: scissors")

    def test_paper_beats_rock(self):
        """Test paper wins against rock."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("paper"), "win! Computer's choice: rock")

    def test_scissors_beats_paper(self):
        """Test scissors wins against paper."""
        random.choice = lambda options: "paper"
        self.assertEqual(play_round("scissors"), "win! Computer's choice: paper")

    def test_rock_loses_to_paper(self):
        """Test rock loses to paper."""
        random.choice = lambda options: "paper"
        self.assertEqual(play_round("rock"), "lose! Computer's choice: paper")

    def test_paper_loses_to_scissors(self):
        """Test paper loses to scissors."""
        random.choice = lambda options: "scissors"
        self.assertEqual(play_round("paper"), "lose! Computer's choice: scissors")

    def test_scissors_loses_to_rock(self):
        """Test scissors loses to rock."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("scissors"), "lose! Computer's choice: rock")

    def test_rock_draws_with_rock(self):
        """Test rock draws with rock."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("rock"), "draw! Computer's choice: rock")

    def test_paper_draws_with_paper(self):
        """Test paper draws with paper."""
        random.choice = lambda options: "paper"
        self.assertEqual(play_round("paper"), "draw! Computer's choice: paper")

    def test_scissors_draws_with_scissors(self):
        """Test scissors draws with scissors."""
        random.choice = lambda options: "scissors"
        self.assertEqual(play_round("scissors"), "draw! Computer's choice: scissors")

    def test_uppercase_input(self):
        """Test uppercase input handling."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("ROCK"), "draw! Computer's choice: rock")

    def test_mixed_case_input(self):
        """Test mixed case input handling."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("RoCk"), "draw! Computer's choice: rock")

    def test_leading_whitespace(self):
        """Test leading whitespace handling."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round(" rock"), "draw! Computer's choice: rock")

    def test_trailing_whitespace(self):
        """Test trailing whitespace handling."""
        random.choice = lambda options: "rock"
        self.assertEqual(play_round("rock "), "draw! Computer's choice: rock")

    def test_empty_input(self):
        """Test empty input raises AssertionError."""
        with self.assertRaises(TypeError):
            play_round("")

    def test_invalid_word_input(self):
        """Test invalid word input raises ValueError."""
        with self.assertRaises(ValueError):
            play_round("invalid")

    def test_integer_input(self):
        """Test integer input raises TypeError."""
        with self.assertRaises(TypeError):
            play_round(123)

    def test_float_input(self):
        """Test float input raises TypeError."""
        with self.assertRaises(TypeError):
            play_round(1.23)

    def test_list_input(self):
        """Test list input raises TypeError."""
        with self.assertRaises(TypeError):
            play_round(["rock"])

    def test_dict_input(self):
        """Test dict input raises TypeError."""
        with self.assertRaises(TypeError):
            play_round({"choice": "rock"})

    def test_none_input(self):
        """Test None input raises TypeError."""
        with self.assertRaises(TypeError):
            play_round(None)

    def test_boolean_input(self):
        """Test boolean input raises TypeError."""
        with self.assertRaises(TypeError):
            play_round(True)

    def test_special_chars_input(self):
        """Test input with special characters raises ValueError."""
        with self.assertRaises(ValueError):
            play_round("rock!")


if __name__ == "__main__":
    unittest.main()
