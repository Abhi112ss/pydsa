METADATA = {
    "id": 3184,
    "name": "Count Pairs That Form a Complete Day I",
    "slug": "count-pairs-that-form-a-complete-day-i",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs of indices (i, j) such that the absolute difference between the elements is exactly 1.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs (i, j) such that abs(nums[i] - nums[j]) == 1.

    Args:
        nums: A list of integers representing the days.

    Returns:
        The total count of pairs that satisfy the condition.

    Examples:
        >>> solve([1, 2, 2, 3])
        4
        # Pairs: (1,2), (1,2), (2,3), (2,3) -> indices (0,1), (0,2), (1,3), (2,3)
        >>> solve([1, 1, 1])
        0
    """
    # Frequency map to store the count of each number encountered
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    total_pairs: int = 0

    # Iterate through the unique numbers in the frequency map
    for num in counts:
        # To avoid double counting (e.g., counting both (1,2) and (2,1)),
        # we only check for the existence of num + 1.
        target = num + 1
        if target in counts:
            # If num exists 'a' times and num + 1 exists 'b' times,
            # there are a * b possible pairs.
            total_pairs += counts[num] * counts[target]

    return total_pairs
