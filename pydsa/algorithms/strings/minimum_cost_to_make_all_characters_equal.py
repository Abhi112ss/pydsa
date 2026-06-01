METADATA = {
    "id": 2712,
    "name": "Minimum Cost to Make All Characters Equal",
    "slug": "minimum-cost-to-make-all-characters-equal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["strings", "greedy", "frequency"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to transform all characters in a string to be the same, where cost is defined by character transformations.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum cost to make all characters in the string equal.
    
    The cost is determined by the number of characters that are NOT the 
    target character. To minimize this cost, we must choose the character 
    that appears most frequently in the string as our target.

    Args:
        s: The input string of characters.

    Returns:
        The minimum number of transformations required.

    Examples:
        >>> solve("aabbbcccc")
        4
        >>> solve("abcde")
        4
        >>> solve("aaaaa")
        0
    """
    if not s:
        return 0

    # Since the character set is typically limited (e.g., lowercase English),
    # we use a fixed-size frequency array or dictionary.
    # Space complexity is O(1) because the alphabet size is constant.
    char_frequencies: dict[str, int] = {}
    
    for char in s:
        char_frequencies[char] = char_frequencies.get(char, 0) + 1
    
    # The minimum cost is the total length minus the count of the 
    # most frequent character.
    max_frequency = 0
    for count in char_frequencies.values():
        if count > max_frequency:
            max_frequency = count
            
    return len(s) - max_frequency
