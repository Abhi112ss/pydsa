METADATA = {
    "id": 1772,
    "name": "Sort Features by Popularity",
    "slug": "sort_features_by_popularity",
    "category": "Sorting",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Sort a list of features based on their frequency in descending order, and then by their lexicographical order in ascending order.",
}

def solve(features: list[str]) -> list[str]:
    """
    Sorts the features based on frequency (descending) and then lexicographically (ascending).

    Args:
        features: A list of strings representing feature names.

    Returns:
        A list of strings sorted by the specified criteria.

    Examples:
        >>> solve(["apple", "banana", "apple", "cherry", "banana", "apple"])
        ['apple', 'apple', 'apple', 'banana', 'banana', 'cherry']
        >>> solve(["a", "b", "c", "a", "b", "c"])
        ['a', 'a', 'b', 'b', 'c', 'c']
    """
    if not features:
        return []

    # Step 1: Count the frequency of each feature using a hash map
    frequency_map: dict[str, int] = {}
    for feature in features:
        frequency_map[feature] = frequency_map.get(feature, 0) + 1

    # Step 2: Get unique features to sort them
    unique_features = list(frequency_map.keys())

    # Step 3: Sort the unique features.
    # We use a custom key for sorting:
    # - Primary key: -frequency_map[x] (negative for descending order)
    # - Secondary key: x (the string itself for ascending lexicographical order)
    unique_features.sort(key=lambda x: (-frequency_map[x], x))

    # Step 4: Reconstruct the full list based on the sorted unique features and their counts
    result: list[str] = []
    for feature in unique_features:
        count = frequency_map[feature]
        result.extend([feature] * count)

    return result
