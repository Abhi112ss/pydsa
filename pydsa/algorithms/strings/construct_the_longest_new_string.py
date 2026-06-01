METADATA = {
    "id": 2745,
    "name": "Construct the Longest New String",
    "slug": "construct-the-longest-new-string",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Construct the longest possible palindrome using characters from a given string by maximizing character counts.",
}

def solve(s: str) -> str:
    """
    Constructs the longest possible palindrome using characters from the input string.

    The strategy is to count the frequency of each character. For each character, 
    we can use an even number of its occurrences to build the sides of the palindrome. 
    If there are any characters with an odd frequency, we can pick exactly one 
    character to be the center of the palindrome.

    Args:
        s: The input string containing lowercase English letters.

    Returns:
        The longest possible palindrome string. If multiple exist, any one is valid.

    Examples:
        >>> solve("abccccdd")
        'ccddacca' (or any other valid longest palindrome like 'ccdadcc')
        >>> solve("aabb")
        'abba'
    """
    # Count frequencies of each character
    # Since input is lowercase English letters, space is O(1)
    char_counts: dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    left_side: list[str] = []
    center_char: str = ""

    # Sort keys to ensure deterministic behavior if needed, 
    # though any order works for the longest length.
    sorted_chars = sorted(char_counts.keys())

    for char in sorted_chars:
        count = char_counts[char]
        
        # Add the maximum possible even number of this character to the sides
        # e.g., if count is 5, we add 2 to the left and 2 to the right (total 4)
        num_to_add = count // 2
        left_side.append(char * num_to_add)
        
        # If we find an odd count, this character is a candidate for the center.
        # We only need one center character to make the palindrome longest.
        # We pick the first one we encounter (or we could pick the largest, 
        # but any single odd character works for length).
        if count % 2 == 1 and center_char == "":
            center_char = char

    # Construct the full string: left + center + reversed(left)
    left_str = "".join(left_side)
    return left_str + center_char + left_str[::-1]
