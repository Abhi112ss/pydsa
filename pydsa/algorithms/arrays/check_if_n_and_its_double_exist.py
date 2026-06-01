METADATA = {
    "id": 1346,
    "name": "Check If N and Its Double Exist",
    "slug": "check_if_n_and_its_double_exist",
    "category": "array",
    "aliases": [],
    "tags": ["hash_set", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return true if there exists a number such that its double also appears in the array.",
}


def solve(nums: list[int]) -> bool:
    """Check if an integer and its double both appear in the list.

    Args:
        nums: List of integers to be examined.

    Returns:
        True if there exists an element x such that 2*x also exists in nums,
        otherwise False.

    Examples:
        >>> solve([10, 2, 5, 3])
        True  # 5 and its double 10 are present
        >>> solve([3, 1, 7, 11])
        False
        >>> solve([0, 0])
        True  # 0 is its own double
    """
    seen_numbers: set[int] = set()
    for current in nums:
        # If we have already seen the double of the current number, condition is satisfied.
        if current * 2 in seen_numbers:
            return True
        # If current is even and we have seen its half, condition is also satisfied.
        if current % 2 == 0 and (current // 2) in seen_numbers:
            return True
        # Record the current number for future checks.
        seen_numbers.add(current)
    return False