METADATA = {
    "id": 3866,
    "name": "First Unique Even Element",
    "slug": "first_unique_even_element",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the first even element in an array that appears exactly once.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the first even element in the input list that occurs exactly once.

    Args:
        nums: A list of integers.

    Returns:
        The first unique even integer found. Returns -1 if no such element exists.

    Examples:
        >>> solve([2, 4, 4, 6, 2, 8])
        6
        >>> solve([1, 3, 5, 7])
        -1
        >>> solve([2, 2, 4, 4])
        -1
    """
    # Frequency map to store the count of each number
    counts: dict[int, int] = {}

    # First pass: Populate the frequency map
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Second pass: Iterate through the original list to maintain order
    # Check if the number is even AND has a frequency of exactly one
    for num in nums:
        if num % 2 == 0 and counts[num] == 1:
            return num

    return -1
