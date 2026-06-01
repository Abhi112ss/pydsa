METADATA = {
    "id": 1133,
    "name": "Largest Unique Number",
    "slug": "largest-unique-number",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the largest integer in an array that appears exactly once.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the largest unique number in the given list.

    Args:
        nums: A list of integers.

    Returns:
        The largest integer that appears exactly once in the list. 
        Returns -1 if no such number exists.

    Examples:
        >>> solve([5, 7, 3, 9, 4, 9, 8, 3, 1])
        8
        >>> solve([5, 5, 5])
        -1
        >>> solve([1, 2, 3, 4, 5])
        5
    """
    # Step 1: Build a frequency map to count occurrences of each number
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Iterate through the map to find the maximum key with a count of 1
    largest_unique: int = -1
    for num, count in counts.items():
        if count == 1:
            if num > largest_unique:
                largest_unique = num

    return largest_unique
