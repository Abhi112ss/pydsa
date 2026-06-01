METADATA = {
    "id": 2822,
    "name": "Inversion of Object",
    "slug": "inversion_of_object",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Invert a dictionary by mapping each value to its corresponding key.",
}

def solve(input_dict: dict[str, int]) -> dict[int, str]:
    """
    Inverts the given dictionary such that the values become keys and keys become values.

    Args:
        input_dict (dict[str, int]): A dictionary where keys are strings and values are integers.

    Returns:
        dict[int, str]: A new dictionary where the original values are keys and original keys are values.

    Examples:
        >>> solve({"a": 1, "b": 2})
        {1: 'a', 2: 'b'}
        >>> solve({"x": 10, "y": 20, "z": 30})
        {10: 'x', 20: 'y', 30: 'z'}
    """
    inverted_dict: dict[int, str] = {}

    # Iterate through the key-value pairs of the input dictionary
    for key, value in input_dict.items():
        # Map the original value to the original key in the new dictionary
        # Note: If duplicate values exist in input_dict, the last key encountered 
        # for that value will overwrite previous ones in the inverted dictionary.
        inverted_dict[value] = key

    return inverted_dict
