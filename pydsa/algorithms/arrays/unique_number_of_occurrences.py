METADATA = {
    "id": 1207,
    "name": "Unique Number of Occurrences",
    "slug": "unique-number-of-occurrences",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if the number of occurrences of each value in the array is unique.",
}

def solve(arr: list[int]) -> bool:
    """
    Determines if the frequency of each integer in the input array is unique.

    Args:
        arr: A list of integers.

    Returns:
        True if the number of occurrences of each value is unique, False otherwise.

    Examples:
        >>> solve([1, 2, 2, 1, 1, 3])
        False
        >>> solve([1, 2, 3, 4])
        True
    """
    # Step 1: Count the frequency of each number using a hash map
    counts: dict[int, int] = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Extract all frequency values
    frequencies = list(counts.values())

    # Step 3: Compare the number of frequencies to the number of unique frequencies
    # If the size of the set of frequencies matches the length of the frequency list,
    # then all frequencies are unique.
    return len(frequencies) == len(set(frequencies))
