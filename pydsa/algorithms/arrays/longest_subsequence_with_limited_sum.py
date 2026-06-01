METADATA = {
    "id": 2389,
    "name": "Longest Subsequence With Limited Sum",
    "slug": "longest_subsequence_with_limited_sum",
    "category": "greedy",
    "aliases": [],
    "tags": ["greedy", "binary_search"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum length of a subsequence whose sum does not exceed a given limit.",
}


def solve(nums: list[int], limit: int) -> int:
    """Return the length of the longest subsequence whose sum is at most ``limit``.

    Args:
        nums: List of non‑negative integers.
        limit: Non‑negative integer representing the maximum allowed sum.

    Returns:
        The maximum possible length of a subsequence with sum ≤ ``limit``.

    Examples:
        >>> solve([4, 2, 1, 5, 3], 7)
        3
        >>> solve([1, 2, 3, 4, 5], 10)
        4
    """
    # Sort numbers to consider the smallest elements first (greedy choice).
    sorted_nums = sorted(nums)

    current_sum = 0
    subsequence_length = 0

    for value in sorted_nums:
        if current_sum + value > limit:
            break
        current_sum += value
        subsequence_length += 1

    return subsequence_length