METADATA = {
    "id": 760,
    "name": "Find Anagram Mappings",
    "slug": "find_anagram_mappings",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given two integer arrays A and B of the same length where B is an anagram of A, return an index mapping array mapping from A to B.",
}


def solve(nums_a: list[int], nums_b: list[int]) -> list[int]:
    """Find the index mapping from nums_a to nums_b where nums_b is an anagram of nums_a.

    For each element in nums_a, find the corresponding index in nums_b.
    Since nums_b is an anagram of nums_a, every element in nums_a appears
    exactly once in nums_b.

    Args:
        nums_a: The source array of integers.
        nums_b: The target array (anagram of nums_a) of integers.

    Returns:
        A list of indices where result[i] is the index in nums_b
        corresponding to nums_a[i].

    Examples:
        >>> solve([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
        [1, 4, 3, 2, 0]
        >>> solve([84, 46], [84, 46])
        [0, 1]
    """
    # Build a hash map from value to its index in nums_b for O(1) lookups
    value_to_index: dict[int, int] = {}
    for index, value in enumerate(nums_b):
        value_to_index[value] = index

    # For each element in nums_a, look up its index in nums_b using the hash map
    result: list[int] = []
    for value in nums_a:
        result.append(value_to_index[value])

    return result