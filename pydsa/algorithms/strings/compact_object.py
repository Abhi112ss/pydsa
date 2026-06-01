METADATA = {
    "id": 2705,
    "name": "Compact Object",
    "slug": "compact-object",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a dictionary, return a new dictionary containing only the keys that have non-null values.",
}

def solve(obj: dict) -> dict:
    """
    Removes all keys from the dictionary that have a value of None.

    Args:
        obj (dict): The input dictionary containing potential null values.

    Returns:
        dict: A new dictionary containing only the key-value pairs where the value is not None.

    Examples:
        >>> solve({"a": None, "b": 1, "c": None})
        {'b': 1}
        >>> solve({"a": 1, "b": 2})
        {'a': 1, 'b': 2}
        >>> solve({"a": None})
        {}
    """
    # Use a dictionary comprehension to iterate through the items.
    # We filter out entries where the value is strictly None.
    compacted_dict = {
        key: value 
        for key, value in obj.items() 
        if value is not None
    }
    
    return compacted_dict
