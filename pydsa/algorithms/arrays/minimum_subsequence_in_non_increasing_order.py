METADATA = {
    "id": 1403,
    "name": "Minimum Subsequence in Non-Increasing Order",
    "slug": "minimum-subsequence-in-non-increasing-order",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest subsequence whose sum is greater than or equal to a given threshold, such that the subsequence is non-increasing.",
}

def solve(nums: list[int], threshold: int) -> list[int]:
    """
    Finds the smallest subsequence whose sum is at least the threshold.
    The resulting subsequence is returned in non-increasing order.

    Args:
        nums: A list of integers.
        threshold: The target sum that the subsequence must meet or exceed.

    Returns:
        A list of integers representing the smallest subsequence in non-increasing order.

    Examples:
        >>> solve([3, 4, 1, 1, 5, 1], 6)
        [5, 4]
        >>> solve([1, 2, 3, 4, 5], 11)
        [5, 4, 3]
    """
    # To minimize the number of elements needed to reach the threshold,
    # we should always pick the largest available elements first.
    # Sorting in descending order allows us to pick greedily.
    nums.sort(reverse=True)

    current_sum = 0
    result_subsequence = []

    for number in nums:
        # Add the largest remaining number to our subsequence
        current_sum += number
        result_subsequence.append(number)

        # Once the sum meets or exceeds the threshold, we have found
        # the smallest possible subsequence due to the greedy approach.
        if current_sum >= threshold:
            return result_subsequence

    return result_subsequence
