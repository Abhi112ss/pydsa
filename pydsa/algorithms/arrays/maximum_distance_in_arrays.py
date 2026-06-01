METADATA = {
    "id": 624,
    "name": "Maximum Distance in Arrays",
    "slug": "maximum_distance_in_arrays",
    "category": "array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum index distance between two arrays where an element from the first array is less than or equal to an element from the second array.",
}

def solve(arrays: list[list[int]]) -> int:
    """Calculate the maximum distance between two different arrays such that an element
    from the first array is less than or equal to an element from the second array.

    Args:
        arrays: A list of non‑empty integer arrays, each sorted in non‑decreasing order.

    Returns:
        The maximum possible distance (absolute difference of array indices) satisfying
        the condition. If no such pair exists, returns 0.

    Examples:
        >>> solve([[1,4],[2,5],[3,6]])
        2
        >>> solve([[7,8,9],[0,1,2],[3,4,5]])
        2
    """
    if not arrays or len(arrays) < 2:
        return 0

    # Initialize global minimum and maximum values with the first array.
    global_min_value = arrays[0][0]
    global_min_index = 0
    global_max_value = arrays[0][-1]
    global_max_index = 0
    max_distance = 0

    for current_index in range(1, len(arrays)):
        current_array = arrays[current_index]
        current_min = current_array[0]
        current_max = current_array[-1]

        # If the current array's maximum is >= the smallest value seen so far,
        # we can form a valid pair using the global minimum as the left side.
        if current_max >= global_min_value:
            distance = current_index - global_min_index
            if distance > max_distance:
                max_distance = distance

        # If the current array's minimum is <= the largest value seen so far,
        # we can form a valid pair using the global maximum as the right side.
        if current_min <= global_max_value:
            distance = current_index - global_max_index
            if distance > max_distance:
                max_distance = distance

        # Update global minimum and maximum values and their indices.
        if current_min < global_min_value:
            global_min_value = current_min
            global_min_index = current_index
        if current_max > global_max_value:
            global_max_value = current_max
            global_max_index = current_index

    return max_distance