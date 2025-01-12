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
        length (float): The length of the rectangle. Must be positive.
        width (float): The width of the rectangle. Must be positive.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If either length or width is non-positive.

    Examples:
        >>> calculate_area(5.0, 3.0)
        15.0
        >>> calculate_area(10.0, 2.5)
        25.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

    return length * width


if __name__ == "__main__":
    print(
        "Example: The area of a rectangle with length 5.0 and width 3.0 is:",
        calculate_area(5.0, 3.0),
    )
