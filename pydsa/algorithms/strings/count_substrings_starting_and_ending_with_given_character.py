METADATA = {
    "id": 3084,
    "name": "Count Substrings Starting and Ending with Given Character",
    "slug": "count-substrings-starting-and-ending-with-given-character",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that start and end with a specific given character.",
}

def solve(s: str, target: str) -> int:
    """
    Counts the number of substrings in 's' that start and end with 'target'.

    Args:
        s: The input string to search within.
        target: The single character that the substrings must start and end with.

    Returns:
        The total count of substrings that start and end with the target character.

    Examples:
        >>> solve("abacaba", "a")
        16
        >>> solve("aaaaa", "a")
        15
        >>> solve("abcde", "z")
        0
    """
    # A substring starting and ending with 'target' is uniquely defined 
    # by choosing any two occurrences of 'target' (where the indices can be the same).
    # If there are 'k' occurrences of 'target', the number of ways to pick 
    # two indices (i, j) such that i <= j is the sum of 1 + 2 + ... + k.
    # This is equivalent to the combination formula for picking 2 items with replacement,
    # or simply: (k * (k + 1)) // 2.
    
    target_count = 0
    for char in s:
        if char == target:
            target_count += 1
            
    # Using the arithmetic series sum formula: n * (n + 1) / 2
    return (target_count * (target_count + 1)) // 2
