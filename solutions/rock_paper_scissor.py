"""
A module for playing a game of Rock-Paper-Scissors.

Module contents:
    - play_round: plays a round of Rock-Paper-Scissors, the user either wins,
    loses, or draws based on the user's choice and the computer's choice

Created on 31 12 24
@author: Abdulrahman Alsir + Codi
"""

import random

options = ["rock", "paper", "scissors"]


def play_round(user_input: str) -> str:
    """
    Allows the user to play a round of Rock-Paper-Scissors with the computer.

    Parameters:
        user_input (str): The user's move ('rock', 'paper', or 'scissors')

    Returns:
        str: The result of the round (win, loss, or draw).

    Raises:
        AssertionError: If user_input is not a string or is empty.

    Examples:
        >>> play_round('rock')
        'win'  # User plays rock, and the computer picks scissors

        >>> play_round('paper')
        'lose'  # User plays paper, and the computer picks scissors

        >>> play_round('scissors')
        'draw'  # User plays scissors, and the computer picks scissors
    """
    assert (
        isinstance(user_input, str) and user_input
    ), "Input must be a non-empty string."

    computer_pick = random.choice(options)
    if user_input.lower() == computer_pick:
        return "draw"
    elif (
        (user_input.lower() == "rock" and computer_pick == "scissors")
        or (user_input.lower() == "paper" and computer_pick == "rock")
        or (user_input.lower() == "scissors" and computer_pick == "paper")
    ):
        return "win"
    else:
        return "lose"
