METADATA = {
    "id": 1913,
    "name": "Maximum Product Difference Between Two Pairs",
    "slug": "maximum_product_difference_between_two_pairs",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Return the maximum product difference between two pairs of numbers in the array.",
}


def solve(nums: list[int]) -> int:
    """Calculate the maximum product difference between two pairs.

    Args:
        nums: A list of integers containing at least four elements.

    Returns:
        The maximum value of (a * b) - (c * d) where a, b, c, d are distinct
        elements from ``nums`` and (a, b) and (c, d) form two pairs.

    Examples:
        >>> solve([5, 2, 4, 1])
        20
        >>> solve([4, 2, 5, 9, 7, 4, 8])
        64
    """
    # Sort the list to bring the smallest and largest values to the ends.
    nums.sort()
    # The two largest numbers are at the end; the two smallest are at the start.
    max_product = nums[-1] * nums[-2]
    min_product = nums[0] * nums[1]
    # The maximum product difference is the difference between these products.
    return max_product - min_product