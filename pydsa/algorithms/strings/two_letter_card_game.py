METADATA = {
    "id": 3664,
    "name": "Two-Letter Card Game",
    "slug": "two_letter_card_game",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum score of a game based on consecutive character pairs in a string.",
}

def solve(s: str, scoring_map: dict[str, int]) -> int:
    """
    Calculates the maximum score obtained by summing values of consecutive 
    character pairs in a string based on a provided scoring map.

    Args:
        s: The input string containing characters.
        scoring_map: A dictionary mapping two-character strings to integer scores.

    Returns:
        The maximum score found among all possible overlapping pairs.

    Examples:
        >>> solve("aabb", {"aa": 1, "ab": 2, "bb": 3})
        3
        >>> solve("abcde", {"ab": 1, "bc": 5, "cd": 2})
        5
    """
    if len(s) < 2:
        return 0

    max_score = 0
    
    # Iterate through the string using a sliding window of size 2
    for i in range(len(s) - 1):
        # Extract the current pair of characters
        current_pair = s[i : i + 2]
        
        # Retrieve the score for the pair from the map, defaulting to 0 if not found
        current_score = scoring_map.get(current_pair, 0)
        
        # Update the global maximum score found so far
        if current_score > max_score:
            max_score = current_score
            
    return max_score
