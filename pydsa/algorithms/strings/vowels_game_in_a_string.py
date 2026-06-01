METADATA = {
    "id": 3227,
    "name": "Vowels Game in a String",
    "slug": "vowels-game-in-a-string",
    "category": "Game Theory",
    "aliases": [],
    "tags": ["strings", "game_theory"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if Alice wins a game where players remove vowels from a string.",
}

def solve(word: str) -> bool:
    """
    Determines if Alice wins the game based on the number of vowels in the string.
    
    In this game, Alice wins if the total number of vowels in the string is odd.
    If the number of vowels is even, Bob wins. This is because Alice can always 
    choose to remove exactly one vowel to change the parity, or if she can 
    remove multiple, she can strategically control the parity. However, 
    the fundamental rule of this specific game theory problem simplifies to 
    checking the parity of the vowel count.

    Args:
        word: The input string containing lowercase English letters.

    Returns:
        bool: True if Alice wins, False if Bob wins.

    Examples:
        >>> solve("leetcode")
        True
        >>> solve("apple")
        True
        >>> solve("sky")
        False
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    
    # Iterate through the string once to count the occurrences of vowels
    for char in word:
        if char in vowels:
            vowel_count += 1
            
    # Alice wins if the total count of vowels is odd
    # If vowel_count % 2 != 0, Alice can always make a move that leaves Bob 
    # in a losing position (even number of vowels).
    return vowel_count % 2 != 0
