METADATA = {
    "id": 3361,
    "name": "Shift Distance Between Two Strings",
    "slug": "shift-distance-between-two-strings",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "modulo_arithmetic"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total minimum shift distance between two strings of equal length considering a circular alphabet.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the total minimum shift distance between two strings of equal length.
    The alphabet is circular, meaning 'a' and 'z' are adjacent.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        The sum of the minimum distances between corresponding characters in both strings.

    Examples:
        >>> solve("abc", "def")
        9
        >>> solve("a", "z")
        1
    """
    total_distance = 0
    
    # Iterate through both strings simultaneously
    for char1, char2 in zip(word1, word2):
        # Convert characters to their integer positions (0-25)
        val1 = ord(char1) - ord('a')
        val2 = ord(char2) - ord('a')
        
        # Calculate the absolute difference in a linear space
        diff = abs(val1 - val2)
        
        # The shortest distance in a circular alphabet of 26 characters
        # is the minimum of the direct distance and the wrap-around distance.
        # Wrap-around distance is (26 - direct distance).
        total_distance += min(diff, 26 - diff)
        
    return total_distance
