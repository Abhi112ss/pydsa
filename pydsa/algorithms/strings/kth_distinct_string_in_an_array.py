METADATA = {
    "id": 2053,
    "name": "Kth Distinct String in an Array",
    "slug": "kth-distinct-string-in-an-array",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the kth distinct string in an array, where a distinct string is one that appears exactly once.",
}

def solve(arr: list[str], k: int) -> str:
    """
    Finds the kth distinct string in the given array.

    A string is considered distinct if it appears exactly once in the array.
    The order of distinct strings is determined by their first appearance in the array.

    Args:
        arr: A list of strings.
        k: The rank of the distinct string to find (1-indexed).

    Returns:
        The kth distinct string if it exists, otherwise an empty string.

    Examples:
        >>> solve(["a", "b", "c", "a", "d", "b"], 2)
        'c'
        >>> solve(["a", "b", "c", "a", "d", "b"], 3)
        'd'
        >>> solve(["a", "b", "c", "a", "d", "b"], 4)
        ''
    """
    # Step 1: Count the frequency of each string using a hash map
    frequency_map: dict[str, int] = {}
    for string in arr:
        frequency_map[string] = frequency_map.get(string, 0) + 1

    # Step 2: Iterate through the original array to maintain order
    # and identify strings with a frequency of exactly one
    distinct_count = 0
    for string in arr:
        if frequency_map[string] == 1:
            distinct_count += 1
            # If we reach the kth distinct string, return it immediately
            if distinct_count == k:
                return string

    # If the loop finishes without finding the kth distinct string, return empty string
    return ""
