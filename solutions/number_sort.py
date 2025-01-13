"""
A module for sorting a list of numbers using a custom implementation of the Bubble Sort algorithm.

Module contents:
    - sort: sorts a list of numbers in ascending order using the Bubble Sort algorithm.
    - main loop: collects user input until 9 numbers are provided and sorts them.

Created on 03-01-25
@author: Abdulrahman Ali + Cody
"""


def sort(list_of_num: list) -> list:
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters:
        list_of_num (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not a number (int or float).

    Strategy:
        The function iterates through the list of numbers and compares each element with the next.
        If the current element is greater than the next, the elements are swapped.
        This process is repeated until the list is sorted in ascending order.

    Examples:
        >>> sort([4, 2, 7, 1])
        [1, 2, 4, 7]

        >>> sort([10, -5, 3, 0])
        [-5, 0, 3, 10]

        >>> sort([1, 2, 3, 4])
        [1, 2, 3, 4]
    """
    if not isinstance(list_of_num, list):
        raise TypeError("Input must be a list.")

    if not all(isinstance(x, (int, float)) for x in list_of_num):
        raise ValueError("All elements in the list must be numbers.")

    for i in range(len(list_of_num) - 1):
        for j in range(len(list_of_num) - 1 - i):
            if list_of_num[j] > list_of_num[j + 1]:
                list_of_num[j], list_of_num[j + 1] = list_of_num[j + 1], list_of_num[j]
    return list_of_num
