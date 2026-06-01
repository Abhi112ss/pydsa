METADATA = {
    "id": 2649,
    "name": "Nested Array Generator",
    "slug": "nested_array_generator",
    "category": "Array",
    "aliases": [],
    "tags": ["recursion", "array_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Generate a nested array structure based on a given depth and element pattern.",
}

def solve(depth: int, element: int) -> list:
    """
    Generates a nested array structure where each level of nesting contains 
    the specified element.

    Args:
        depth (int): The number of nesting levels to create.
        element (int): The integer value to place at the deepest level.

    Returns:
        list: A nested list structure of the specified depth.

    Examples:
        >>> solve(1, 5)
        [5]
        >>> solve(2, 5)
        [[5]]
        >>> solve(3, 5)
        [[[5]]]
    """
    # Base case: If depth is 1, return the element wrapped in a single list
    if depth <= 1:
        return [element]

    # Recursive step: Wrap the result of the inner depth in another list
    # This builds the structure from the inside out
    return [solve(depth - 1, element)]
