METADATA = {
    "id": 1784,
    "name": "Check if Binary String Has at Most One Segment of Ones",
    "slug": "check_if_binary_string_has_at_most_one_segment_of_ones",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "linear_scan"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine whether a binary string contains at most one contiguous block of '1's.",
}


def solve(s: str) -> bool:
    """Check if a binary string has at most one segment of consecutive '1's.

    Args:
        s: A binary string consisting only of characters '0' and '1'.

    Returns:
        True if the string contains zero or one contiguous block of '1's; otherwise False.

    Examples:
        >>> solve("1001")
        False
        >>> solve("110001111")
        False
        >>> solve("000")
        True
        >>> solve("111")
        True
        >>> solve("0011100")
        True
    """
    # Count how many times a transition from '0' to '1' occurs.
    transition_count: int = 0
    previous_char: str = "0"

    for current_char in s:
        if previous_char == "0" and current_char == "1":
            transition_count += 1
            if transition_count > 1:
                return False
        previous_char = current_char

    return True