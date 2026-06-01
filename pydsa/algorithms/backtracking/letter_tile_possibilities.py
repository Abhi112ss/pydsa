METADATA = {
    "id": 1079,
    "name": "Letter Tile Possibilities",
    "slug": "letter-tile-possibilities",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(N!)",
    "space_complexity": "O(N)",
    "description": "Given a string tiles, return the number of possible sequences that can be formed using the tiles.",
}

from collections import Counter

def solve(tiles: str) -> int:
    """
    Calculates the number of unique sequences that can be formed using the given tiles.

    The algorithm uses backtracking with a frequency map to ensure that we only 
    explore unique character choices at each position in the sequence, 
    effectively handling duplicate tiles.

    Args:
        tiles: A string representing the available tiles.

    Returns:
        The total number of unique sequences possible.

    Examples:
        >>> solve("AAB")
        8
        >>> solve("AA")
        3
    """
    # Count frequency of each character to handle duplicates efficiently
    char_counts = Counter(tiles)
    unique_chars = list(char_counts.keys())
    
    def backtrack() -> int:
        """
        Recursive helper to explore all unique permutations.
        
        Returns:
            The number of unique sequences that can be formed from the current state.
        """
        count = 0
        
        # Iterate through unique characters to avoid duplicate sequences
        for char in unique_chars:
            if char_counts[char] > 0:
                # 1. Choose: Use one instance of the character
                char_counts[char] -= 1
                
                # 2. Explore: Every choice of a character counts as 1 valid sequence 
                # plus all sequences that can be formed by appending more characters.
                count += 1 + backtrack()
                
                # 3. Un-choose: Backtrack to restore the frequency map for the next branch
                char_counts[char] += 1
                
        return count

    return backtrack()
