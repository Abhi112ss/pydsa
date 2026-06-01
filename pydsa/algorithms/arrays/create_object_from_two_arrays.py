METADATA = {
    "id": 2794,
    "name": "Create Object from Two Arrays",
    "slug": "create-object-from-two-arrays",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Create an object by mapping keys from one array to values from another array at the same index.",
}

def solve(keys: list[str], values: list[int]) -> dict[str, int]:
    """
    Creates a dictionary mapping elements from the keys array to elements 
    from the values array based on their shared index.

    Args:
        keys: A list of strings representing the keys of the object.
        values: A list of integers representing the values of the object.

    Returns:
        A dictionary where result[keys[i]] = values[i].

    Examples:
        >>> solve(["a", "b"], [1, 2])
        {'a': 1, 'b': 2}
        >>> solve(["apple", "banana", "cherry"], [10, 20, 30])
        {'apple': 10, 'banana': 20, 'cherry': 30}
    """
    result_map: dict[str, int] = {}
    
    # Iterate through the length of the keys array.
    # Since the problem guarantees equal length, we can use the index to access both.
    for index in range(len(keys)):
        key = keys[index]
        value = values[index]
        
        # Map the key to its corresponding value in the dictionary.
        result_map[key] = value
        
    return result_map
