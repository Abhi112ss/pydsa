METADATA = {
    "id": 1508,
    "name": "Range Sum of Sorted Subarray Sums",
    "slug": "range-sum-of-sorted-subarray-sums",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Calculate the sum of elements in a sorted list of all possible subarray sums within a given range [left, right], modulo 10^9 + 7.",
}

def solve(nums: list[int], left: int, right: int) -> int:
    """
    Calculates the sum of subarray sums that fall within the range [left, right].

    Args:
        nums: A list of positive integers.
        left: The lower bound of the range (inclusive).
        right: The upper bound of the range (inclusive).

    Returns:
        The sum of all subarray sums that are between left and right, inclusive,
        modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3], 2, 6)
        11
        >>> solve([1, 2, 3], 4, 4)
        1
    """
    MOD = 1_000_000_007
    n = len(nums)
    subarray_sums = []

    # Generate all possible subarray sums using a nested loop
    # The outer loop marks the start of the subarray
    for start_index in range(n):
        current_running_sum = 0
        # The inner loop expands the subarray to the right
        for end_index in range(start_index, n):
            current_running_sum += nums[end_index]
            subarray_sums.append(current_running_sum)

    # Sort the collected sums to allow range-based selection
    subarray_sums.sort()

    # Calculate the sum of elements within the [left, right] range
    # We iterate through the sorted list and accumulate values that satisfy the condition
    total_range_sum = 0
    for s in subarray_sums:
        if left <= s <= right:
            total_range_sum = (total_range_sum + s) % MOD
        elif s > right:
            # Since the list is sorted, we can break early if the sum exceeds the right bound
            break

    return total_range_sum
