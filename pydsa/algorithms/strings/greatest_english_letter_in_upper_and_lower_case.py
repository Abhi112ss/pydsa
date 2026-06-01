METADATA = {
    "id": 2309,
    "name": "Greatest English Letter in Upper and Lower Case",
    "slug": "greatest-english-letter-in-upper-and-lower-case",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "bit_manipulation", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the greatest English letter that appears in both its uppercase and lowercase forms in a given string.",
}

def solve(s: str) -> str:
    """
    Finds the greatest English letter that appears in both its uppercase and lowercase forms.

    Args:
        s: The input string containing English letters.

    Returns:
        The greatest English letter in both cases, or an empty string if no such letter exists.

    Examples:
        >>> solve("aA")
        'a'
        >>> solve("abAb")
        'b'
        >>> solve("aB")
        ''
    """
    # Use bitmasks to track presence of lowercase and uppercase letters.
    # Since there are 26 letters, a 32-bit integer is sufficient.
    lower_mask = 0
    upper_mask = 0

    for char in s:
        if 'a' <= char <= 'z':
            # Map 'a'-'z' to bits 0-25
            lower_mask |= (1 << (ord(char) - ord('a')))
        elif 'A' <= char <= 'Z':
            # Map 'A'-'Z' to bits 0-25
            upper_mask |= (1 << (ord(char) - ord('A')))

    # Find the intersection of both masks
    common_mask = lower_mask & upper_mask

    # Iterate from 'z' down to 'a' to find the greatest letter
    for i in range(25, -1, -1):
        # Check if the i-th bit is set in the intersection
        if (common_mask >> i) & 1:
            return chr(ord('a') + i)

    return ""
