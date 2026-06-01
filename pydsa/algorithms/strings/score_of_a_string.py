METADATA = {
    "id": 3110,
    "name": "Score of a String",
    "slug": "score-of-a-string",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of the absolute differences between the ASCII values of adjacent characters in a string.",
}

def solve(s: str) -> int:
    """
    Calculates the score of a string by summing the absolute differences 
    between the ASCII values of consecutive characters.

    Args:
        s: The input string to process.

    Returns:
        The total score calculated as the sum of absolute differences.

    Examples:
        >>> solve("hello")
        13
        >>> solve("zaz")
        25
    """
    total_score = 0
    
    # Iterate from the first character to the second to last character
    for i in range(len(s) - 1):
        # Calculate the absolute difference between current and next character's ASCII value
        char_diff = abs(ord(s[i]) - ord(s[i + 1]))
        total_score += char_diff
        
    return total_score
