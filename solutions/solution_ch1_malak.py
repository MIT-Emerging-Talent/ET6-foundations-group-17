"""
This module implements a number guessing game where players select a difficulty
level and attempt to guess a randomly generated number within a limited number of attempts.
The difficulty levels determine the number of attempts allowed.

Contents:
- `choose_difficulty`: Function to select a difficulty level based on provided choice.
- `number_guessing_game`: Function to simulate the number guessing game.

Author: Malak Battatt
Date: January 7th, 2025
"""

import random


def choose_difficulty(choice: int) -> tuple[int, int, str]:
    """
    Selects a difficulty level for the game based on the provided choice.

    Args:
        choice (int): The user's choice for difficulty level (1-Easy, 2-Medium, 3-Hard).

    Returns:
        tuple[int, int, str]: A tuple containing the randomly generated number,
                the maximum number of attempts allowed, and a message indicating
                the difficulty level selected.

    Examples:
    >>> choose_difficulty(1)
    (random number between 1 and 50, 15, 'Easy (1 to 50) - 15 attempts')

    >>> choose_difficulty(2)
    (random number between 1 and 50, 10, 'Medium (1 to 50) - 10 attempts')

    >>> choose_difficulty(3)
    (random number between 1 and 50, 5, 'Hard (1 to 50) - 5 attempts')

    >>> choose_difficulty(4)
    (random number between 1 and 50, 10, 'Invalid choice! Defaulting to Medium (1 to 50)
    with 10 attempts.')
    """
    if choice == 1:
        return random.randint(1, 50), 15, "Easy (1 to 50) - 15 attempts"
    elif choice == 2:
        return random.randint(1, 50), 10, "Medium (1 to 50) - 10 attempts"
    elif choice == 3:
        return random.randint(1, 50), 5, "Hard (1 to 50) - 5 attempts"
    else:
        return (
            random.randint(1, 50),
            10,
            "Invalid choice! Defaulting to Medium (1 to 50) with 10 attempts.",
        )


def number_guessing_game(choice: int, guesses: list[int]) -> list[str]:
    """
    Simulates a number guessing game where the player selects a difficulty
    level and attempts to guess the randomly generated number within a
    limited number of attempts.

    Args:
        choice (int): The user's choice for difficulty level (1-Easy, 2-Medium, 3-Hard).
        guesses (list[int]): A list of integers representing the player's guesses.

    Returns:
        list[str]: A list of strings representing the game's messages.

    Examples:
    >>> number_guessing_game(2, [25, 30, 40, 50, 45, 48, 50, 35, 20, 15])
    ['Welcome to the Number Guessing Game!',
        "Let's choose a difficulty level:",
        'Medium (1 to 50) - 10 attempts',
        '\\nYou have 10 attempts left.',
        'Too high! Try a much lower number.',
        '\\nYou have 9 attempts left.',
        ...
        '🎉 Congratulations! You guessed the number in 6 attempts. 🎉']
    """
    messages = [
        "Welcome to the Number Guessing Game!",
        "Let's choose a difficulty level:",
    ]

    # Choose the difficulty level
    number_to_guess, max_attempts, difficulty_message = choose_difficulty(choice)
    messages.append(difficulty_message)
    attempts = 0
    guessed_correctly = False

    for guess in guesses:
        if attempts >= max_attempts:
            break
        messages.append(f"\nYou have {max_attempts - attempts} attempts left.")
        attempts += 1

        if guess < number_to_guess:
            if number_to_guess - guess > 10:
                messages.append("Too low! Try a much higher number.")
            else:
                messages.append("Too low, but you're close!")
        elif guess > number_to_guess:
            if guess - number_to_guess > 10:
                messages.append("Too high! Try a much lower number.")
            else:
                messages.append("Too high, but you're close!")
        else:
            guessed_correctly = True
            messages.append(
                f"🎉 Congratulations! You guessed the number in {attempts} attempts. 🎉"
            )
            break

    if not guessed_correctly:
        messages.append(
            f"You've run outta attempts. The number was {number_to_guess}. Better luck next time!"
        )

    return messages
