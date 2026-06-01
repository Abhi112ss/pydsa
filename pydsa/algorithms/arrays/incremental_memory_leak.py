METADATA = {
    "id": 1860,
    "name": "Incremental Memory Leak",
    "slug": "incremental_memory_leak",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "array", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Apply multiple range increments to an array and return the final state using an efficient difference array approach.",
}

def solve(n: int, queries: list[list[int]]) -> list[int]:
    """
    Applies multiple range increment queries to an array of size n.

    Each query is a list [start_index, end_index, increment_value].
    The increment is applied to all elements from start_index to end_index inclusive.

    Args:
        n: The size of the target array.
        queries: A list of queries where each query is [start, end, val].

    Returns:
        A list of integers representing the final state of the array.

    Examples:
        >>> solve(5, [[0, 2, 1], [2, 4, 2]])
        [1, 1, 3, 2, 2]
        >>> solve(3, [[0, 0, 5], [1, 2, 10]])
        [5, 10, 10]
    """
    # Initialize a difference array of size n + 1 to handle boundary conditions
    # when incrementing the end index + 1.
    diff_array = [0] * (n + 1)

    for start, end, val in queries:
        # Apply the increment at the start index
        diff_array[start] += val
        
        # Subtract the increment at the index immediately following the end index
        # to stop the range update effect.
        if end + 1 < n:
            diff_array[end + 1] -= val

    # Reconstruct the original array using the prefix sum of the difference array.
    result = [0] * n
    current_sum = 0
    for i in range(n):
        current_sum += diff_array[i]
        result[i] = current_sum

    return result
