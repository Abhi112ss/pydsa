METADATA = {
    "id": 1429,
    "name": "First Unique Number",
    "slug": "first_unique_number",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the first number in an array that appears exactly once.",
}

def solve(numbers: list[int]) -> int:
    """
    Finds the first number in the input list that occurs exactly once.

    Args:
        numbers: A list of integers.

    Returns:
        The first unique integer found in the list. Returns -1 if no unique 
        integer exists.

    Examples:
        >>> solve([4, 5, 1, 2, 0, 4, 5, 2])
        1
        >>> solve([1, 1, 1])
        -1
        >>> solve([1, 2, 3])
        1
    """
    # Frequency map to store the count of each number
    counts: dict[int, int] = {}

    # First pass: Populate the frequency map
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    # Second pass: Iterate through the original list to maintain order
    # and find the first number with a frequency of 1
    for num in numbers:
        if counts[num] == 1:
            return num

    return -1
