METADATA = {
    "id": 3794,
    "name": "Reverse String Prefix",
    "slug": "reverse_string_prefix",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverses the prefix of a string up to a given index in-place.",
}

def solve(s: list[str], k: int) -> list[str]:
    """
    Reverses the prefix of the list of characters up to index k (inclusive).

    Args:
        s: A list of characters representing the string.
        k: The ending index of the prefix to be reversed.

    Returns:
        The modified list of characters with the prefix reversed.

    Examples:
        >>> solve(['h', 'e', 'l', 'l', 'o'], 2)
        ['l', 'e', 'h', 'l', 'o']
        >>> solve(['a', 'b', 'c', 'd'], 0)
        ['a', 'b', 'c', 'd']
    """
    if not s or k <= 0:
        return s

    # Ensure k does not exceed the bounds of the list
    end_index = min(k, len(s) - 1)
    
    left_pointer = 0
    right_pointer = end_index

    # Use two pointers to swap characters from the outside in
    while left_pointer < right_pointer:
        # Perform the swap
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        
        # Move pointers towards the center
        left_pointer += 1
        right_pointer -= 1

    return s
