METADATA = {
    "id": 2839,
    "name": "Check if Strings Can be Made Equal With Operations I",
    "slug": "check-if-strings-can-be-made-equal-with-operations-i",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if two strings can be made equal by repeatedly replacing a character with its predecessor in the alphabet.",
}

def solve(s1: str, s2: str) -> bool:
    """
    Checks if two strings can be made equal by replacing any character 
    with its predecessor in the alphabet (e.g., 'c' -> 'b' -> 'a').

    The core insight is that a character can be transformed into any character 
    that comes before it in the alphabet. Therefore, for two strings to be 
    made equal, the character in s2 at any index must be less than or equal 
    to the character in s1 at the same index.

    Args:
        s1: The first input string.
        s2: The second input string.

    Returns:
        True if s1 can be transformed into s2, False otherwise.

    Examples:
        >>> solve("abc", "abc")
        True
        >>> solve("abc", "abd")
        False
        >>> solve("abc", "aac")
        True
    """
    # Since the problem implies strings are of equal length and we only 
    # move "backwards" in the alphabet, we compare character values.
    for char1, char2 in zip(s1, s2):
        # If the target character (char2) is "greater" than the source (char1),
        # it is impossible to reach char2 from char1 using only predecessor operations.
        if ord(char2) > ord(char1):
            return False
            
    return True
