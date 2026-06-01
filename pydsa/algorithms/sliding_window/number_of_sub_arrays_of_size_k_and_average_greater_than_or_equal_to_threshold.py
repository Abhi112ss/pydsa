METADATA = {
    "id": 1343,
    "name": "Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold",
    "slug": "number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of contiguous sub-arrays of size k whose average is at least the given threshold.",
}

def solve(arr: list[int], k: int, threshold: int) -> int:
    """
    Counts the number of sub-arrays of size k with an average >= threshold.

    To avoid floating point division, we compare the sum of the sub-array 
    to (threshold * k).

    Args:
        arr: A list of integers.
        k: The fixed size of the sub-arrays.
        threshold: The minimum average required.

    Returns:
        The count of sub-arrays meeting the criteria.

    Examples:
        >>> solve([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
        3
        >>> solve([1, 1, 1, 1, 1], 2, 0)
        4
    """
    # The condition (sum / k) >= threshold is equivalent to sum >= (threshold * k)
    # This avoids precision issues with floating point division.
    target_sum = threshold * k
    count = 0
    current_window_sum = 0

    # Initialize the first window of size k
    for i in range(k):
        current_window_sum += arr[i]

    # Check the first window
    if current_window_sum >= target_sum:
        count += 1

    # Slide the window across the rest of the array
    for i in range(k, len(arr)):
        # Add the new element entering the window and remove the element leaving it
        current_window_sum += arr[i] - arr[i - k]
        
        if current_window_sum >= target_sum:
            count += 1

    return count
