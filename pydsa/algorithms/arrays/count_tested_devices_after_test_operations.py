METADATA = {
    "id": 2960,
    "name": "Count Tested Devices After Test Operations",
    "slug": "count-tested-devices-after-test-operations",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "Count how many devices have been tested at least once after performing multiple range update operations.",
}

def solve(n: int, operations: list[list[int]]) -> int:
    """
    Counts the number of devices that have been tested at least once.

    A device is considered tested if it has been included in at least one 
    test operation range [start, end].

    Args:
        n (int): The total number of devices (indexed 0 to n-1).
        operations (list[list[int]]): A list of operations where each operation 
            is [start, end] representing the range of devices tested.

    Returns:
        int: The count of devices that were tested at least once.

    Examples:
        >>> solve(5, [[0, 2], [2, 4]])
        5
        >>> solve(10, [[1, 3], [5, 7], [2, 5]])
        7
    """
    # Use a difference array to handle range updates in O(1)
    # diff[i] stores the change in the number of tests at index i
    diff = [0] * (n + 1)

    for start, end in operations:
        # Increment the start of the range
        diff[start] += 1
        # Decrement the index immediately after the end of the range
        if end + 1 < n:
            diff[end + 1] -= 1

    tested_count = 0
    current_tests = 0
    
    # Iterate through the devices and compute the prefix sum
    # The prefix sum at index i represents how many operations covered device i
    for i in range(n):
        current_tests += diff[i]
        if current_tests > 0:
            tested_count += 1

    return tested_count
