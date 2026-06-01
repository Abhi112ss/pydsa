METADATA = {
    "id": 3843,
    "name": "First Element with Unique Frequency",
    "slug": "first_element_with_unique_frequency",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the first element in an array that appears exactly once.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the first element in the input list that has a frequency of exactly one.

    Args:
        nums: A list of integers.

    Returns:
        The first integer that appears only once in the list. 
        Returns -1 if no such element exists.

    Examples:
        >>> solve([4, 5, 1, 2, 0, 4, 5, 2])
        1
        >>> solve([1, 1, 2, 2])
        -1
        >>> solve([1, 2, 3])
        1
    """
    # Dictionary to store the frequency of each number
    frequency_map: dict[int, int] = {}

    # First pass: Populate the frequency map
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Second pass: Iterate through the original list to maintain order
    # and find the first element with a frequency of 1
    for num in nums:
        if frequency_map[num] == 1:
            return num

    return -1
