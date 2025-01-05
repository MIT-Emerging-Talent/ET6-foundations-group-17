"""
A module for sorting a list of numbers using a custom implementation of the Bubble Sort algorithm.

Module contents:
    - sort: sorts a list of numbers in ascending order using the Bubble Sort algorithm.
    - main loop: collects user input until 9 numbers are provided and sorts them.

Created on 03-01-25
@author: Abdulrahman Alsir + Cody
"""


def sort(list_of_num: list) -> list:
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters:
        list_of_num (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

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
    # Implementing the Bubble Sort algorithm
    for i in range(len(list_of_num) - 1):
        for j in range(len(list_of_num) - 1 - i):
            # Swap if the current element is greater than the next
            if list_of_num[j] > list_of_num[j + 1]:
                list_of_num[j], list_of_num[j + 1] = list_of_num[j + 1], list_of_num[j]
    return list_of_num


if __name__ == "__main__":
    num = []
    while True:
        lis = int(input("Insert a number: "))
        num.append(lis)
        if len(num) > 8:
            break

    sorted_list = sort(num)
    print("Sorted List:", sorted_list)
