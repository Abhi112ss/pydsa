METADATA = {
    "id": 2697,
    "name": "Lexicographically Smallest Palindrome",
    "slug": "lexicographically-smallest-palindrome",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace the minimum number of characters in a string to make it a palindrome that is lexicographically smallest.",
}

def solve(s: str) -> str:
    """
    Transforms a string into the lexicographically smallest palindrome by 
    replacing the minimum number of characters.

    Args:
        s: The input string.

    Returns:
        The lexicographically smallest palindrome possible.

    Examples:
        >>> solve("eggy")
        'egge'
        >>> solve("xyzzba")
        'abzzba'
    """
    # Convert string to list because strings are immutable in Python
    chars = list(s)
    left_index = 0
    right_index = len(chars) - 1

    # Use two pointers to meet in the middle
    while left_index < right_index:
        char_left = chars[left_index]
        char_right = chars[right_index]

        if char_left != char_right:
            # To make it lexicographically smallest, we pick the 
            # character that comes earlier in the alphabet.
            if char_left < char_right:
                chars[right_index] = char_left
            else:
                chars[left_index] = char_right
        
        left_index += 1
        right_index -= 1

    return "".join(chars)
