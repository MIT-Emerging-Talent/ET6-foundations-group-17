import unittest
from unittest.mock import patch
from io import StringIO

# Assume the main Tic-Tac-Toe functions are imported from the main file
# Example: from tic_tac_toe_game import print_board, check_winner, is_full, tic_tac_toe

class TestTicTacToe(unittest.TestCase):
    def test_check_winner_rows(self):
        board = [
            ["X", "X", "X"],
            ["O", " ", "O"],
            [" ", " ", " "]
        ]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_columns(self):
        board = [
            ["X", "O", " "],
            ["X", "O", " "],
            ["X", " ", " "]
        ]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_diagonals(self):
        board = [
            ["X", "O", "O"],
            [" ", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertEqual(check_winner(board), "X")

    def test_is_full_true(self):
        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertTrue(is_full(board))

    def test_is_full_false(self):
        board = [
            ["X", "O", "X"],
            ["O", " ", "O"],
            ["O", "X", "O"]
        ]
        self.assertFalse(is_full(board))

    @patch('builtins.input', side_effect=["0 0", "0 1", "1 1", "0 2", "2 2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_tic_tac_toe_win(self, mock_stdout, mock_input):
        tic_tac_toe()
        output = mock_stdout.getvalue()
        self.assertIn("Player X wins!", output)

    @patch('builtins.input', side_effect=["0 0", "0 1", "1 1", "2 1", "2 0", "2 2", "1 0", "1 2", "0 2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_tic_tac_toe_tie(self, mock_stdout, mock_input):
        tic_tac_toe()
        output = mock_stdout.getvalue()
        self.assertIn("It's a tie!", output)

if __name__ == "__main__":
    unittest.main()
