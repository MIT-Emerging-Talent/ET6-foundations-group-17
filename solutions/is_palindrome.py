"""
A module to check if a given string is a palindrome.

Module contents:
    - is_palindrome: checks if a string reads the same forwards and backwards.

Created on 03-01-25

"""


def is_palindrome(input_string: str) -> bool:
    """
    Checks if a string is a palindrome.

    Parameters:
        input_string (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> is_palindrome("madam")
        True

        >>> is_palindrome("hello")
        False

        >>> is_palindrome("")
        True
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")
    return input_string == input_string[::-1]
