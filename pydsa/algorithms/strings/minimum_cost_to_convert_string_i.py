METADATA = {
    "id": 2976,
    "name": "Minimum Cost to Convert String I",
    "slug": "minimum-cost-to-convert-string-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to convert one string to another by summing the shortest distance between corresponding characters in a circular alphabet.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the minimum cost to convert word1 to word2.
    
    The cost is defined as the minimum distance between characters in a 
    circular alphabet (a-z). For each pair of characters at the same index,
    we calculate the distance moving both clockwise and counter-clockwise
    and take the minimum.

    Args:
        word1: The source string.
        word2: The target string.

    Returns:
        The total minimum cost to transform word1 into word2.

    Examples:
        >>> solve("abc", "def")
        9
        >>> solve("z", "a")
        1
        >>> solve("a", "z")
        1
    """
    total_cost = 0
    
    # Iterate through both strings simultaneously
    for char1, char2 in zip(word1, word2):
        # Convert characters to their integer positions (0-25)
        pos1 = ord(char1) - ord('a')
        pos2 = ord(char2) - ord('a')
        
        # Calculate absolute difference for direct distance
        diff = abs(pos1 - pos2)
        
        # The minimum distance in a circular alphabet of 26 letters is 
        # either the direct difference or the 'wrap-around' distance.
        # Wrap-around distance is (26 - direct_difference).
        total_cost += min(diff, 26 - diff)
        
    return total_cost
