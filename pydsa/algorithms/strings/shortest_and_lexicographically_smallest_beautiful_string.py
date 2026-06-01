METADATA = {
    "id": 2904,
    "name": "Shortest and Lexicographically Smallest Beautiful String",
    "slug": "shortest-and-lexicographically-smallest-beautiful-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Construct the shortest and lexicographically smallest string of length n such that every substring is beautiful.",
    "is_beautiful": "A string is beautiful if every substring is beautiful, which implies the string must be a repetition of a single character 'a'."
}

def solve(n: int) -> str:
    """
    Constructs the shortest and lexicographically smallest beautiful string of length n.
    
    A string is beautiful if every substring is beautiful. For a string to satisfy 
    this property, every character must be the same. To make it lexicographically 
    smallest, we must choose the smallest possible character, which is 'a'.

    Args:
        n: The required length of the string.

    Returns:
        The shortest and lexicographically smallest beautiful string of length n.

    Examples:
        >>> solve(3)
        'aaa'
        >>> solve(1)
        'a'
    """
    # The definition of a "beautiful" string where EVERY substring must be beautiful
    # is extremely restrictive. If a string contains two different characters, 
    # say "ab", the substring "ab" is not beautiful (it doesn't consist of 
    # identical characters). Therefore, all characters in the string must be identical.
    # To be lexicographically smallest, we use 'a'.
    
    return "a" * n
