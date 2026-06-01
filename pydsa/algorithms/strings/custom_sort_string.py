METADATA = {
    "id": 791,
    "name": "Custom Sort String",
    "slug": "custom-sort-string",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
    "description": "Reorder a string s to match the custom order defined by string order.",
}

def solve(order: str, s: str) -> str:
    """
    Reorders the string s based on the custom character priority defined in order.

    Args:
        order: A string representing the custom order of characters.
        s: The string to be reordered.

    Returns:
        A string containing the characters of s rearranged according to order.

    Examples:
        >>> solve("cba", "abcd")
        'cbad'
        >>> solve("kqe", "kqe")
        'kqe'
        >>> solve("bcda", "abcd")
        'bcda'
    """
    # Count the frequency of each character in s
    # Since the character set is lowercase English letters, space is O(1)
    char_counts: dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    result_chars: list[str] = []

    # First, append characters in the order specified by 'order'
    for char in order:
        if char in char_counts:
            # Append the character as many times as it appeared in s
            count = char_counts.pop(char)
            result_chars.append(char * count)

    # Second, append all remaining characters that were not in 'order'
    # These characters can be in any order
    for char, count in char_counts.items():
        result_chars.append(char * count)

    return "".join(result_chars)
