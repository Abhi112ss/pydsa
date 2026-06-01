METADATA = {
    "id": 2703,
    "name": "Return Length of Arguments Passed",
    "slug": "return-length-of-arguments-passed",
    "category": "Implementation",
    "aliases": [],
    "tags": ["implementation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the number of arguments passed to the function.",
}

def solve(*args: object) -> int:
    """
    Returns the number of arguments passed to the function.

    Args:
        *args: A variable number of arguments of any type.

    Returns:
        int: The total count of arguments provided.

    Examples:
        >>> solve(1, 2, 3)
        3
        >>> solve()
        0
        >>> solve("a", [1, 2], {"key": "val"})
        3
    """
    # In Python, the *args syntax collects all positional arguments 
    # into a tuple. We can simply return the length of this tuple.
    return len(args)