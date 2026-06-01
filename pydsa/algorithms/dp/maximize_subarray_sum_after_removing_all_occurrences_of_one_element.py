METADATA = {
    "id": 3410,
    "name": "Maximize Subarray Sum After Removing All Occurrences of One Element",
    "slug": "maximize_subarray_sum_after_removing_all_occurrences_of_one_element",
    "category": "dynamic_programming",
    "aliases": [],
    "tags": ["dynamic_programming", "kadane_algorithm"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the maximum subarray sum achievable after deleting all instances of a chosen element.",
}


def solve() -> None:
    """Read an integer array from standard input and print the maximum subarray sum
    after removing all occurrences of a single chosen element.

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Example:
        >>> # Input
        >>> # 5
        >>> # 1 -2 3 -2 5
        >>> # Output
        >>> # 9
        The optimal choice is to remove -2, yielding the array [1, 3, 5] with sum 9.
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    # First token may be the length; ignore it if present
    if len(data) > 1 and data[0].isdigit() and int(data[0]) == len(data) - 1:
        nums = list(map(int, data[1:]))
    else:
        nums = list(map(int, data))

    # Baseline: maximum subarray sum without removing any element
    max_without_removal = float("-inf")
    current_sum = float("-inf")
    for value in nums:
        current_sum = value if current_sum < 0 else current_sum + value
        max_without_removal = max(max_without_removal, current_sum)

    answer = max_without_removal

    unique_values = set(nums)

    for removed_value in unique_values:
        current_sum = float("-inf")
        best_sum = float("-inf")
        for value in nums:
            if value == removed_value:
                # Skip this element; it disappears after removal
                continue
            # Kadane step on the array where the removed value is omitted
            current_sum = value if current_sum < 0 else current_sum + value
            best_sum = max(best_sum, current_sum)
        # If all elements were removed, best_sum stays -inf; treat as 0
        if best_sum == float("-inf"):
            best_sum = 0
        answer = max(answer, best_sum)

    print(answer)