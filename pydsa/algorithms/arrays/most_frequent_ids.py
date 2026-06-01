METADATA = {
    "id": 3092,
    "name": "Most Frequent IDs",
    "slug": "most-frequent-ids",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["arrays", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Return the top k most frequent IDs, sorted by frequency descending and then by ID value descending.",
}

def solve(ids: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent IDs from a list, with specific tie-breaking rules.

    The results are sorted primarily by frequency in descending order. 
    If two IDs have the same frequency, the larger ID value comes first.

    Args:
        ids: A list of integers representing the IDs.
        k: The number of top frequent IDs to return.

    Returns:
        A list of k integers representing the most frequent IDs.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3], 2)
        [3, 2]
        >>> solve([1, 1, 2, 2, 3, 3], 2)
        [3, 2]
    """
    # Step 1: Count the frequency of each ID using a hash map
    frequency_map: dict[int, int] = {}
    for identifier in ids:
        frequency_map[identifier] = frequency_map.get(identifier, 0) + 1

    # Step 2: Convert the map to a list of tuples (id, frequency)
    # We need to sort this list based on the custom requirements
    unique_ids = list(frequency_map.keys())

    # Step 3: Sort the unique IDs
    # Primary key: frequency (descending -> -frequency_map[x])
    # Secondary key: ID value (descending -> -x)
    # Using a lambda with negative values allows us to use a single ascending sort 
    # to achieve descending order for both criteria.
    unique_ids.sort(key=lambda x: (-frequency_map[x], -x))

    # Step 4: Return the top k elements
    return unique_ids[:k]
