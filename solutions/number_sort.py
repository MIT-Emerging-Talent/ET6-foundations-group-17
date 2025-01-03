"""
A module for sorting a list of numbers using a custom implementation of the Bubble Sort algorithm.

Module contents:
    - sort: sorts a list of numbers in ascending order using the Bubble Sort algorithm.
    - main loop: collects user input until 9 numbers are provided and sorts them.

Created on 31 12 24
@author: Abdulrahman Ali + Cody
"""


def sort(list_of_num):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters:
        list_of_num (list): A list of numbers to be sorted.

    Returns:
        list: The sorted list of numbers.

    Examples:
        >>> sort([4, 2, 7, 1])
        [1, 2, 4, 7]

        >>> sort([10, -5, 3, 0])
        [-5, 0, 3, 10]
    """
    for i in range(len(list_of_num) - 1):
        for j in range(len(list_of_num) - 1 - i):
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
