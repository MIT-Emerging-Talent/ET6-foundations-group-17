"""
A module for playing a game of Rock-Paper-Scissors.

Module contents:
    - play_round: Simulates a round of Rock-Paper-Scissors where the user competes
      against the computer.

Created on 31-12-24
Updated on 09-01-25
@author: Abdulrahman Ali (Reviewed by Cody)
"""

import random

OPTIONS: list[str] = ["rock", "paper", "scissors"]


def play_round(user_input: str) -> str:
    """
    Simulates a round of Rock-Paper-Scissors with the computer.

    Parameters:
        user_input (str): The user's move ('rock', 'paper', or 'scissors').

    Returns:
        str: A string describing the result of the round and the computer's choice.

    Raises:
        TypeError: If user_input is not a string or is empty.
        ValueError: If user_input is not one of the valid options.

    Examples:
        >>> play_round('rock')
        'win! Computer's choice: scissors'

        >>> play_round('paper')
        'lose! Computer's choice: scissors'

        >>> play_round('scissors')
        'draw! Computer's choice: scissors'

        >>> play_round('invalid')
        Traceback (most recent call last):
        ...
        ValueError: Invalid input. Choose one of: rock, paper, scissors.
    """
    if not isinstance(user_input, str) or not user_input.strip():
        raise TypeError("Input must be a non-empty string.")

    user_input = user_input.strip().lower()
    if user_input not in OPTIONS:
        raise ValueError(f"Invalid input. Choose one of: {', '.join(OPTIONS)}.")

    computer_pick = random.choice(OPTIONS)

    if user_input == computer_pick:
        return f"draw! Computer's choice: {computer_pick}"
    elif (
        (user_input == "rock" and computer_pick == "scissors")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissors" and computer_pick == "paper")
    ):
        return f"win! Computer's choice: {computer_pick}"
    else:
        return f"lose! Computer's choice: {computer_pick}"
