"""
A module for a Guess the Number game.
Module contents:
    - generate_random_number: Generates a random number within a range.
    - guess_the_number: Compares a guessed number with the target and returns
      feedback.
Created on 8-01-25
@author: Ameen Agha
"""

import random

def generate_random_number(start: int, end: int) -> int:
    """
    Generates a random number within a given range (inclusive).
    Parameters:
        start (int): Start of the range (inclusive).
        end (int): End of the range (inclusive).
    Returns:
        int: A randomly generated number within the range.
    Raises:
        AssertionError: If start or end are not integers, or start >= end.
    Examples:
        >>> random.seed(1)  # Fixing seed for test reproducibility
        >>> generate_random_number(1, 10)
        3
        >>> generate_random_number(20, 30)
        24
    """
    assert isinstance(start, int) and isinstance(end, int), "Inputs must be integers."
    assert start < end, "Start must be less than end."
    return random.randint(start, end)

def guess_the_number(target: int, guess: int) -> str:
    """
    Compares a guess with the target number and provides feedback.
    Parameters:
        target (int): The target number to guess.
        guess (int): The player's guessed number.
    Returns:
        str: Feedback indicating if the guess is too low, too high, or correct.
    Raises:
        AssertionError: If target or guess are not integers.
    Examples:
        >>> guess_the_number(10, 5)
        'Too low!'
        >>> guess_the_number(10, 15)
        'Too high!'
        >>> guess_the_number(10, 10)
        'Correct!'
    """
    assert isinstance(target, int) and isinstance(guess, int), "Inputs must be integers."

    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"
