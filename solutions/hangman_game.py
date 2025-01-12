"""
A module for a Hangman game.
Module contents:
    - select_random_word: Selects a random word from a list.
    - play_hangman: Manages the Hangman game logic.
Created on 11-01-25
@author: Ameen Agha
"""

import random


def select_random_word(word_list: list) -> str:
    """
    Select a random word from a given list.
    Parameters:
        word_list (list): A list of words to choose from.
    Returns:
        str: A randomly selected word from the list.
    Raises:
        AssertionError: If word_list is not a list or is empty.
    Examples:
        >>> random.seed(1)  # Fixing seed for test reproducibility
        >>> select_random_word(["python", "hangman", "program"])
        'program'
    """
    assert (
        isinstance(word_list, list) and len(word_list) > 0
    ), "Input must be a non-empty list."
    return random.choice(word_list)


def play_hangman(word: str, guesses: list) -> dict:
    """
    Manage the Hangman game logic.
    Parameters:
        word (str): The word to guess.
        guesses (list): A list of guessed letters.
    Returns:
        dict: A dictionary containing the game state with keys:
            - 'progress': The current state of the word (e.g., '_ a n g _ a n').
            - 'missed': List of incorrect guesses.
            - 'attempts_left': Number of attempts remaining.
            - 'status': 'ongoing', 'won', or 'lost'.
    Raises:
        AssertionError: If word is not a string or guesses is not a list.
    Examples:
        >>> play_hangman("hangman", ["h", "a", "z"])
        {'progress': 'h a _ _ _ a n', 'missed': ['z'], 'attempts_left': 5, 'status': 'ongoing'}
    """
    assert isinstance(word, str), "Word must be a string."
    assert isinstance(guesses, list), "Guesses must be a list."

    max_attempts = 6
    missed = [guess for guess in guesses if guess not in word]
    attempts_left = max_attempts - len(missed)

    progress = " ".join([char if char in guesses else "_" for char in word])

    if "_" not in progress:
        status = "won"
    elif attempts_left <= 0:
        status = "lost"
    else:
        status = "ongoing"

    return {
        "progress": progress,
        "missed": missed,
        "attempts_left": attempts_left,
        "status": status,
    }
