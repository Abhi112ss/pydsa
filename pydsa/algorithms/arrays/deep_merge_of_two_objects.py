METADATA = {
    "id": 2755,
    "name": "Deep Merge of Two Objects",
    "slug": "deep-merge-of-two-objects",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["recursion", "hash_map", "dictionary"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Perform a deep merge of two objects where nested dictionaries are merged recursively and other types are overwritten.",
}

def solve(obj1: dict, obj2: dict) -> dict:
    """
    Performs a deep merge of two dictionaries.

    If a key exists in both dictionaries and both values are dictionaries, 
    the function recursively merges them. Otherwise, the value from 
    the second dictionary overwrites the value from the first.

    Args:
        obj1 (dict): The base dictionary.
        obj2 (dict): The dictionary containing updates to merge into obj1.

    Returns:
        dict: A new dictionary representing the deep merge of obj1 and obj2.

    Examples:
        >>> solve({"a": 1, "b": {"c": 2}}, {"b": {"d": 3}})
        {'a': 1, 'b': {'c': 2, 'd': 3}}
        >>> solve({"a": {"b": 1}}, {"a": 2})
        {'a': 2}
    """
    # Create a shallow copy of the first object to avoid mutating the input
    merged = obj1.copy()

    for key, value in obj2.items():
        # If the key exists in both and both values are dictionaries, recurse
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = solve(merged[key], value)
        else:
            # Otherwise, overwrite or add the value from the second object
            merged[key] = value

    return merged
