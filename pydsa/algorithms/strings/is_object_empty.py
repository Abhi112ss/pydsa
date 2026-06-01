METADATA = {
    "id": 2727,
    "name": "Is Object Empty",
    "slug": "is_object_empty",
    "category": "hash_table",
    "aliases": [],
    "tags": ["hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine whether a given object (dictionary) contains any keys.",
}


def solve(obj: dict) -> bool:
    """Check if the provided dictionary has no keys.

    Args:
        obj: A dictionary representing the object to be examined.

    Returns:
        True if the dictionary is empty (has zero keys), otherwise False.

    Examples:
        >>> solve({})
        True
        >>> solve({"a": 1})
        False
    """
    # The number of keys in a dictionary can be obtained in O(1) time.
    number_of_keys: int = len(obj)
    # An empty object has zero keys.
    return number_of_keys == 0