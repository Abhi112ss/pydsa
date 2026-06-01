METADATA = {
    "id": 1446,
    "name": "Consecutive Characters",
    "slug": "consecutive-characters",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains only one unique character.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring that contains only one unique character.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The length of the longest consecutive sequence of the same character.

    Examples:
        >>> solve("abbba")
        3
        >>> solve("aaabb")
        3
        >>> solve("abcde")
        1
    """
    if not s:
        return 0

    max_streak = 1
    current_streak = 1

    # Iterate through the string starting from the second character
    for index in range(1, len(s)):
        # If the current character matches the previous one, increment the streak
        if s[index] == s[index - 1]:
            current_streak += 1
        else:
            # If it's a new character, reset the streak counter
            current_streak = 1
        
        # Update the global maximum streak found so far
        if current_streak > max_streak:
            max_streak = current_streak

    return max_streak
