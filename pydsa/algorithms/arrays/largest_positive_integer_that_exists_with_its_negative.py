METADATA = {
    "id": 2441,
    "name": "Largest Positive Integer That Exists With Its Negative",
    "slug": "largest_positive_integer_that_exists_with_its_negative",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the largest positive integer x such that both x and -x are present in the input array, or -1 if none exist."
}


def solve(nums: list[int]) -> int:
    """Find the largest positive integer that also appears as its negative.

    Args:
        nums: List of integers which may contain both positive and negative values.

    Returns:
        The largest positive integer x such that both x and -x are in nums.
        Returns -1 if no such integer exists.

    Examples:
        >>> solve([3, 2, -2, 5, -3])
        3
        >>> solve([1, 2, 3, 4])
        -1
    """
    # Store all numbers for O(1) existence checks.
    number_set = set(nums)

    max_positive = -1
    for value in nums:
        # Consider only positive numbers and check if its negative counterpart exists.
        if value > 0 and -value in number_set:
            if value > max_positive:
                max_positive = value
    return max_positive