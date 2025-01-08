"""
A module for a game called FizzBuzz.

Module contents:
    - fizz_buzz: generates a dictionary where the key is the number and the value is the outcome of that number
    "Fizz" when a number is divisible by 3,
    "Buzz" if the number is divisible by 5,
    and "FizzBuzz" if the number is divisible by both.

Created on 31-12-24
@author: Abdulrahman Ali + Cody
"""


def fizz_buzz(start: int, end: int) -> dict:
    """
    Generate a dictionary for the FizzBuzz Game.

    Parameters:
        start (int): Start of the range of numbers (inclusive).
        end (int): End of the range of numbers (exclusive).

    Returns:
        dict: A dictionary where keys are the numbers and values are the outcome
              of that number, which can be "Fizz", "Buzz", "FizzBuzz", or omitted
              if none apply.

    Raises:
        AssertionError: If the start or end are not integers.

    Examples:
        >>> fizz_buzz(2, 10)
        {3: 'Fizz', 5: 'Buzz', 6: 'Fizz', 9: 'Fizz'}
        >>> fizz_buzz(10, 16)
        {10: 'Buzz', 12: 'Fizz', 15: 'FizzBuzz'}
        >>> fizz_buzz(1, 5)
        {3: 'Fizz', 5: 'Buzz'}
    """
    assert isinstance(start, int) and isinstance(
        end, int
    ), "Start and end must be integers."

    results = {}
    # Iterate through the range of numbers
    for number in range(start, end):
        if number % 15 == 0:
            results[number] = "FizzBuzz"
        elif number % 3 == 0:
            results[number] = "Fizz"
        elif number % 5 == 0:
            results[number] = "Buzz"
    return results
