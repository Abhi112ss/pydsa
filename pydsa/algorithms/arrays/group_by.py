METADATA = {
    "id": 2631,
    "name": "Group By",
    "slug": "group_by",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array", "function"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Groups elements of an array based on the result of a provided callback function.",
}

from typing import Any, Callable, List, Dict


def solve(items: List[int], callback: Callable[[int], int]) -> Dict[int, List[int]]:
    """
    Groups elements of the input list into a dictionary where keys are the 
    results of the callback function applied to each element.

    Args:
        items: A list of integers to be grouped.
        callback: A function that takes an integer and returns an integer 
            representing the group key.

    Returns:
        A dictionary where each key is a group identifier and the value 
        is a list of integers from the original input that mapped to that key.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6], lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4, 6]}
        >>> solve([1, 2, 3], lambda x: x)
        {1: [1], 2: [2], 3: [3]}
    """
    groups: Dict[int, List[int]] = {}

    for item in items:
        # Calculate the key using the provided callback function
        key = callback(item)
        
        # If the key is not yet in the dictionary, initialize a new list
        if key not in groups:
            groups[key] = []
            
        # Append the current item to the list corresponding to its key
        groups[key].append(item)

    return groups
