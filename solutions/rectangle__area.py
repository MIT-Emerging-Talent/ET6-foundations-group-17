"""
Calculates the area of a rectangle.

Args:
    length (float): The length of the rectangle. Must be positive.
    width (float): The width of the rectangle. Must be positive.

Returns:
    float: The area of the rectangle (length * width).

Raises:
    ValueError: If either length or width is non-positive.
"""


def calculate_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle using the formula: area = length * width.

    >>> calculate_area(5.0, 3.0)  # Doctest: +NORMALIZE_WHITESPACE
    15.0
    >>> calculate_area(10.0, 2.5)  # Doctest: +NORMALIZE_WHITESPACE
    25.0
    """

    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")

    area = length * width
    return area