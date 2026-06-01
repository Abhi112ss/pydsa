METADATA = {
    "id": 2124,
    "name": "Check if All A's Appear Before All B's",
    "slug": "check_if_all_as_appear_before_all_bs",
    "category": "String",
    "aliases": [],
    "tags": ["string_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return true if every 'a' in the string appears before any 'b', otherwise false.",
}


def solve(s: str) -> bool:
    """Check if all 'a' characters appear before any 'b' characters.

    Args:
        s: A string consisting only of characters 'a' and 'b'.

    Returns:
        True if no 'a' occurs after a 'b' in the string; otherwise False.

    Examples:
        >>> solve("aaabbb")
        True
        >>> solve("abab")
        False
        >>> solve("bbb")
        True
        >>> solve("aaa")
        True
    """
    seen_b = False  # flag indicating that a 'b' has been encountered
    for char in s:
        if char == 'b':
            seen_b = True
        elif char == 'a' and seen_b:
            # an 'a' appears after a 'b' -> condition violated
            return False
    return True