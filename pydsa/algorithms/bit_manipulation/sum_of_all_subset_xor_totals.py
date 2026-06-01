METADATA = {
    "id": 1863,
    "name": "Sum of All Subset XOR Totals",
    "slug": "sum_of_all_subset_xor_totals",
    "category": "bit_manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the sum of XOR totals of all subsets of the given array.",
}


def solve(nums: list[int]) -> int:
    """Calculate the sum of XOR totals for all subsets of ``nums``.

    Args:
        nums: A list of non‑negative integers.

    Returns:
        An integer representing the sum of XOR values of every possible subset.

    Examples:
        >>> solve([1, 3])
        6
        >>> solve([5, 1, 6])
        28
        >>> solve([])
        0
    """
    # Compute the bitwise OR of all elements; each set bit will contribute.
    combined_or: int = 0
    for value in nums:
        combined_or |= value

    subset_count: int = len(nums)
    if subset_count == 0:
        return 0

    # Each bit that appears in ``combined_or`` contributes 2^(n‑1) times.
    contribution_factor: int = 1 << (subset_count - 1)
    return combined_or * contribution_factor