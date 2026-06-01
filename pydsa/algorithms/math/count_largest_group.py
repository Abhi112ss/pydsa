METADATA = {
    "id": 1399,
    "name": "Count Largest Group",
    "slug": "count_largest_group",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["math", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the number of digit-sum groups that have the maximum size among numbers from 1 to n.",
}


def solve(n: int) -> int:
    """Count the number of groups with the largest size based on digit sums.

    Args:
        n: The inclusive upper bound of the range [1, n].

    Returns:
        The count of groups whose size equals the maximum group size.

    Examples:
        >>> solve(13)
        4
        >>> solve(1)
        1
        >>> solve(1000)
        2
    """
    # Frequency map: digit sum -> count of numbers having that sum
    digit_sum_counts: dict[int, int] = {}

    for number in range(1, n + 1):
        # Compute digit sum without converting to string for speed
        temp = number
        digit_sum = 0
        while temp > 0:
            digit_sum += temp % 10
            temp //= 10
        # Update frequency
        digit_sum_counts[digit_sum] = digit_sum_counts.get(digit_sum, 0) + 1

    # Determine the maximum group size
    max_group_size = max(digit_sum_counts.values())

    # Count how many groups have this maximum size
    largest_group_count = sum(
        1 for group_size in digit_sum_counts.values() if group_size == max_group_size
    )
    return largest_group_count