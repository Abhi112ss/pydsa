METADATA = {
    "id": 1124,
    "name": "Longest Well-Performing Interval",
    "slug": "longest-well-performing-interval",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest period in a given array where the number of hours worked is greater than 8.",
}

def solve(hours: list[int]) -> int:
    """
    Finds the length of the longest interval where the number of hours worked 
    is greater than 8.

    The problem is transformed into finding the longest subarray with a sum 
    greater than zero by mapping hours > 8 to 1 and hours <= 8 to -1.

    Args:
        hours: A list of integers representing hours worked each day.

    Returns:
        The length of the longest well-performing interval.

    Examples:
        >>> solve([9, 9, 6, 0, 6, 6, 9])
        7
        >>> solve([6, 6, 6])
        0
        >>> solve([9, 9, 9, 9])
        4
    """
    max_length = 0
    current_prefix_sum = 0
    # first_occurrence maps a prefix sum to the earliest index it was encountered
    first_occurrence: dict[int, int] = {}

    for index, hour in enumerate(hours):
        # Transform: > 8 becomes +1, <= 8 becomes -1
        current_prefix_sum += 1 if hour > 8 else -1

        # Case 1: The prefix sum itself is positive, meaning the interval [0, index] is valid
        if current_prefix_sum > 0:
            max_length = index + 1
        else:
            # Case 2: Prefix sum is <= 0. We want to find the earliest index 'i' 
            # such that prefix_sum[index] - prefix_sum[i] > 0.
            # Since prefix sums change by only 1 at a time, the first time we 
            # encounter a sum of (current_prefix_sum - 1) will be the optimal 
            # starting point to make the interval sum exactly 1.
            target_sum = current_prefix_sum - 1
            if target_sum in first_occurrence:
                max_length = max(max_length, index - first_occurrence[target_sum])
            
            # Only store the first occurrence of a prefix sum to maximize interval length
            if current_prefix_sum not in first_occurrence:
                first_occurrence[current_prefix_sum] = index

    return max_length
