METADATA = {
    "id": 2176,
    "name": "Count Equal and Divisible Pairs in an Array",
    "slug": "count_equal_and_divisible_pairs_in_an_array",
    "category": "array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Counts pairs of indices where the elements are equal and the product of 1‑based positions is divisible by that element.",
}


def solve(nums: list[int]) -> int:
    """Count equal and divisible pairs in an array.

    Args:
        nums: List of positive integers.

    Returns:
        The number of pairs (i, j) with i < j such that nums[i] == nums[j]
        and ((i + 1) * (j + 1)) is divisible by nums[i].

    Examples:
        >>> solve([2, 2, 2])
        3
        >>> solve([1, 2, 3, 4])
        0
    """
    pair_count = 0
    array_length = len(nums)

    for i in range(array_length):
        for j in range(i + 1, array_length):
            # Check equality first to avoid unnecessary modulo operations
            if nums[i] == nums[j]:
                # Verify divisibility condition: (i+1)*(j+1) % nums[i] == 0
                if ((i + 1) * (j + 1)) % nums[i] == 0:
                    pair_count += 1

    return pair_count