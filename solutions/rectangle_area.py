"""
This module contains a function to calculate the area of a rectangle.

Functions:
    calculate_area(length, width):
        Returns the area of a rectangle with the given length and width.

Raises:
    ValueError: If either length or width is non-positive.
"""


def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle using the formula: area = length * width.

    Args:
        length (float): The length of the rectangle. Must be non-negative.
        width (float): The width of the rectangle. Must be non-negative.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If either length or width is negative.

    Examples:
        >>> calculate_area(5.0, 3.0)
        15.0
        >>> calculate_area(10.0, 2.5)
        25.0
        >>> calculate_area(0.0, 5.0)
        0.0
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be positive numbers.")

    return length * width

