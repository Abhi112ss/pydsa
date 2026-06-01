METADATA = {
    "id": 2823,
    "name": "Deep Object Filter",
    "slug": "deep-object-filter",
    "category": "Recursion",
    "aliases": [],
    "tags": ["recursion", "hash_map", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(D)",
    "description": "Recursively filter a nested object (dictionary) to keep only keys that satisfy a given predicate function.",
}

from typing import Any, Callable, Dict, Union

def solve(obj: Union[Dict[str, Any], list], predicate: Callable[[str], bool]) -> Union[Dict[str, Any], list]:
    """
    Recursively filters a nested object (dictionary or list) based on a predicate function applied to keys.

    Args:
        obj: The input object which can be a dictionary, a list, or a primitive value.
        predicate: A function that takes a string (key) and returns True if the key should be kept.

    Returns:
        A new object containing only the elements that satisfy the predicate. 
        If a dictionary's keys are all filtered out, the dictionary becomes empty.
        If a list contains objects, those objects are filtered recursively.

    Examples:
        >>> def is_even(k): return len(k) % 2 == 0
        >>> obj = {"a": 1, "bb": {"c": 2, "dd": 3}, "eee": [1, {"ff": 4}]}
        >>> solve(obj, is_even)
        {'bb': {'dd': 3}, 'eee': [1, {'ff': 4}]}
    """
    
    # Case 1: The object is a dictionary
    if isinstance(obj, dict):
        filtered_dict = {}
        for key, value in obj.items():
            # Check if the current key satisfies the predicate
            if predicate(key):
                # Recursively process the value to handle nested structures
                processed_value = solve(value, predicate)
                
                # In some variations of this problem, if the value is an empty dict/list 
                # after filtering, you might choose to omit it. 
                # Here we keep it to maintain structural integrity of the keys that passed.
                filtered_dict[key] = processed_value
        return filtered_dict

    # Case 2: The object is a list
    elif isinstance(obj, list):
        # For lists, we don't filter by index, but we must filter the elements inside
        # because they might be dictionaries or lists themselves.
        return [solve(item, predicate) for item in obj]

    # Case 3: The object is a primitive (int, str, bool, None, etc.)
    else:
        return obj
