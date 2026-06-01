METADATA = {
    "id": 370,
    "name": "Range Addition",
    "slug": "range_addition",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum", "difference_array"],
    "difficulty": "medium",
    "time_complexity": "O(n + k)",
    "space_complexity": "O(n)",
    "description": "Given an integer n and a list of updates where each update is [start, end, inc], return an array of length n after applying all updates.",
}

def solve(length: int, updates: list[list[int]]) -> list[int]:
    """
    Applies multiple range updates to an array of a given length using a difference array.

    Args:
        length: The size of the resulting array.
        updates: A list of updates, where each update is [start_index, end_index, increment].

    Returns:
        A list of integers representing the array after all updates are applied.

    Examples:
        >>> solve(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]])
        [-2, 0, 3, 5, 3]
    """
    # Initialize the difference array with zeros.
    # The difference array allows us to perform range updates in O(1) time.
    diff_array = [0] * (length + 1)

    for start, end, inc in updates:
        # Mark the start of the range with the increment value.
        diff_array[start] += inc
        
        # Mark the index immediately after the end of the range with the negative increment.
        # This ensures the increment only affects the range [start, end].
        if end + 1 < length:
            diff_array[end + 1] -= inc

    # Reconstruct the original array by calculating the prefix sum of the difference array.
    result = [0] * length
    current_sum = 0
    for i in range(length):
        current_sum += diff_array[i]
        result[i] = current_sum

    return result
