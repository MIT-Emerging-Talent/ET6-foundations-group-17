"""
A module for a game called FizzBuzz.

Module contents:
    - fizz_buzz: generates a list of strings (Fizz, Buzz, or FizzBuzz)
    "Fizz" when a number is divisible by 3,
     "Buzz" if the number is divisible by 5,
     and FizzBuzz if the number is divisible by both

Created on 31-12-24
@author: Abdulrahman Alsir + Codi
"""


def fizz_buzz(start: int, end: int) -> list:
    """
    Generate a list for the FizzBuzz Game

    Parameters:
        start: start of the range of numbers (included)
        end: end of the range of numbers (excluded)

    Returns:
        list: a list containing "Fizz", "Buzz", "FizzBuzz" based on divisibility conditions
        or nothing if the number is divisible by neither 3 nor 5
    Examples:
        >>> fizz_buzz(2, 10)
        ['Fizz', 'Buzz', 'Fizz', 'Fizz']
        >>> fizz_buzz(10, 16)
        ['Buzz', 'Fizz', 'FizzBuzz']

    """
    result = []
    for number in range(start, end):
        if number % 15 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
    return result
