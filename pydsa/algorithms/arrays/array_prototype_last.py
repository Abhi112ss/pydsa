METADATA = {
    "id": 2619,
    "name": "Array Prototype Last",
    "slug": "array-prototype-last",
    "category": "Implementation",
    "aliases": [],
    "tags": ["array", "prototype"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a method that returns the last element of an array, or undefined if the array is empty.",
}

def solve(arr: list) -> any:
    """
    Returns the last element of the provided list.

    Args:
        arr (list): The input list of elements.

    Returns:
        any: The last element of the list, or None if the list is empty.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([])
        None
    """
    # Check if the list is empty to avoid index out of bounds
    if not arr:
        return None
    
    # Access the element at the last index (length - 1)
    # In Python, arr[-1] is the idiomatic way to access the last element
    return arr[-1]
