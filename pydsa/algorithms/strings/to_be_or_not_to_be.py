METADATA = {
    "id": 2704,
    "name": "To Be Or Not To Be",
    "slug": "to_be_or_not_to_be",
    "category": "Implementation",
    "aliases": [],
    "tags": ["strings", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return \"YES\" if the input boolean is true, otherwise return \"NO\".",
}


def solve(is_true: bool) -> str:
    """Convert a boolean value to its corresponding string representation.

    Args:
        is_true: The boolean value to be converted.

    Returns:
        "YES" if ``is_true`` is ``True``, otherwise "NO".

    Examples:
        >>> solve(True)
        'YES'
        >>> solve(False)
        'NO'
    """
    # Direct mapping from boolean to required string literal
    return "YES" if is_true else "NO"