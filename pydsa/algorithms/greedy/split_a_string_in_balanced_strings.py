METADATA = {
    "id": 1221,
    "name": "Split a String in Balanced Strings",
    "slug": "split-a-string-in-balanced-strings",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Split a string into the maximum number of balanced strings where 'L' and 'R' occur in equal counts.",
}

def solve(s: str) -> int:
    """
    Splits the input string into the maximum number of balanced substrings.
    
    A string is balanced if it contains an equal number of 'L' and 'R' characters.
    The algorithm uses a greedy approach by tracking the balance of characters
    and incrementing the count every time the balance returns to zero.

    Args:
        s: A string consisting of 'L' and 'R' characters.

    Returns:
        The maximum number of balanced strings the input can be split into.

    Examples:
        >>> solve("RLRRLLRLRL")
        4
        >>> solve("LLRR")
        1
    """
    balanced_count = 0
    balance_tracker = 0

    for character in s:
        # Increment for 'R', decrement for 'L'
        # This tracks the net difference between the two characters
        if character == 'R':
            balance_tracker += 1
        else:
            balance_tracker -= 1

        # Whenever the tracker hits zero, we have found a balanced substring
        # We greedily count this as a split point
        if balance_tracker == 0:
            balanced_count += 1

    return balanced_count
