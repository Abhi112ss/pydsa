METADATA = {
    "id": 1657,
    "name": "Determine if Two Strings Are Close",
    "slug": "determine_if_two_strings_are_close",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check if two strings can be made equal by swapping characters and globally swapping character frequencies.",
}

import sys

def solve() -> None:
    """Determine if two strings are close.

    Reads two strings from standard input (separated by whitespace or newline)
    and prints ``True`` if they are close, otherwise ``False``.

    Args:
        None (input is read from ``stdin``).

    Returns:
        None (the result is printed to ``stdout``).

    Examples:
        >>> # Input
        >>> # hello
        >>> # lehol
        >>> # Output
        >>> True
        >>> # Input
        >>> # abc
        >>> # def
        >>> # Output
        >>> False
    """
    data = sys.stdin.read().split()
    if len(data) < 2:
        return
    word1, word2 = data[0], data[1]

    # If lengths differ, they cannot be close.
    if len(word1) != len(word2):
        print(False)
        return

    # Count character frequencies for each string (only lowercase letters).
    count1 = [0] * 26
    count2 = [0] * 26
    for ch in word1:
        count1[ord(ch) - 97] += 1
    for ch in word2:
        count2[ord(ch) - 97] += 1

    # The set of characters present must be identical.
    chars1 = {i for i, c in enumerate(count1) if c > 0}
    chars2 = {i for i, c in enumerate(count2) if c > 0}
    if chars1 != chars2:
        print(False)
        return

    # The multiset of frequencies must match (order does not matter).
    if sorted(count1) != sorted(count2):
        print(False)
        return

    print(True)