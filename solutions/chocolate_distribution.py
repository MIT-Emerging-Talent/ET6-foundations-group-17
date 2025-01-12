def minimize_chocolate_difference(chocolates, k):
    """
    Function to distribute chocolates to minimize the difference between the maximum
    and minimum chocolates received.

    Parameters:
    chocolates (list): List of integers representing chocolates in packets.
    k (int): Number of students.

    Returns:
    int: The minimized difference between the maximum and minimum chocolates received.
    """
    if k == 0 or len(chocolates) == 0:
        return 0

    if len(chocolates) < k:
        return -1  # Not enough packets for the students

    # Sort the packets
    chocolates.sort()

    # Initialize the minimum difference
    min_diff = float("inf")

    # Find the smallest difference for a group of k packets
    for i in range(len(chocolates) - k + 1):
        diff = chocolates[i + k - 1] - chocolates[i]
        min_diff = min(min_diff, diff)

    return min_diff


# Example usage
if __name__ == "__main__":
    chocolates = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    k = 7
    result = minimize_chocolate_difference(chocolates, k)
    print(f"Minimum difference is {result}")
