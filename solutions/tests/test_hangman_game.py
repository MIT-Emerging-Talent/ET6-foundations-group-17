"""
Unit test module for the Hangman game.
Contains tests for word selection and game logic.
Created on 11-01-25
@author: Ameen Agha
"""

import unittest
from ..hangman_game import select_random_word, play_hangman


class TestHangmanGame(unittest.TestCase):
    """
    Test cases for the Hangman game functions.
    These tests ensure random word selection and game logic work as expected.
    """

    def test_select_random_word(self):
        """Test random word selection from a valid list."""
        random_words = ["python", "hangman", "program"]
        word = select_random_word(random_words)
        self.assertIn(word, random_words)

    def test_select_random_word_invalid_input(self):
        """Test word selection with invalid input."""
        with self.assertRaises(AssertionError):
            select_random_word(123)

    def test_select_random_word_empty_list(self):
        """Test word selection with an empty list."""
        with self.assertRaises(AssertionError):
            select_random_word([])

    def test_hangman_progress(self):
        """Test progress tracking in Hangman."""
        result = play_hangman("hangman", ["h", "a", "n"])
        expected = {
            "progress": "h a n _ _ a n",
            "missed": [],
            "attempts_left": 6,
            "status": "ongoing",
        }
        self.assertEqual(result, expected)

    def test_hangman_missed_guesses(self):
        """Test missed guesses in Hangman."""
        result = play_hangman("hangman", ["x", "y", "z"])
        self.assertEqual(result["missed"], ["x", "y", "z"])

    def test_hangman_attempts_left(self):
        """Test remaining attempts after missed guesses."""
        result = play_hangman("hangman", ["h", "x", "y"])
        self.assertEqual(result["attempts_left"], 4)

    def test_hangman_won(self):
        """Test winning condition in Hangman."""
        result = play_hangman("hangman", ["h", "a", "n", "g", "m"])
        self.assertEqual(result["status"], "won")

    def test_hangman_lost(self):
        """Test losing condition in Hangman."""
        result = play_hangman("hangman", ["x", "y", "z", "w", "q", "e", "t"])
        self.assertEqual(result["status"], "lost")


if __name__ == "__main__":
    unittest.main()
