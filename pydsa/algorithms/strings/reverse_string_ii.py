METADATA = {
    "id": 541,
    "name": "Reverse String II",
    "slug": "reverse_string_ii",
    "category": "String",
    "aliases": ["reverse_string_2"],
    "tags": ["string_manipulation", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.",
}

def solve(s: str, k: int) -> str:
    """Reverse the first k characters for every 2k characters in the string.

    Args:
        s (str): The input string to be partially reversed.
        k (int): The number of characters to reverse in each 2k block.

    Returns:
        str: The modified string with specified portions reversed.

    Examples:
        >>> solve("abcdefg", 2)
        'bacdfeg'
        >>> solve("abcd", 2)
        'bacd'
        >>> solve("a", 1)
        'a'
    """
    # Convert string to list for in-place modification
    chars = list(s)
    length = len(chars)
    
    # Iterate through the string in steps of 2k
    for start in range(0, length, 2 * k):
        # Determine the end of the portion to reverse (first k characters of this segment)
        end = min(start + k - 1, length - 1)
        
        # Two-pointer reverse on the first k characters of this 2k block
        left = start
        right = end
        while left < right:
            # Swap characters at left and right pointers
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    return "".join(chars)