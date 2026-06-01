METADATA = {
    "id": 2782,
    "name": "Number of Unique Categories",
    "slug": "number_of_unique_categories",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_set", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of unique elements in a given list using a hash set.",
}

def solve(categories: list[int]) -> int:
    """
    Calculates the number of unique categories in the provided list.

    Args:
        categories: A list of integers representing category IDs.

    Returns:
        The count of unique category IDs present in the list.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3])
        3
        >>> solve([1, 1, 1, 1])
        1
        >>> solve([])
        0
    """
    # Using a set provides O(1) average time complexity for insertions
    # and automatically handles the removal of duplicate elements.
    unique_categories = set(categories)
    
    # The size of the set represents the count of distinct elements.
    return len(unique_categories)
