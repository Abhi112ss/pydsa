METADATA = {
    "id": 1684,
    "name": "Count the Number of Consistent Strings",
    "slug": "count-the-number-of-consistent-strings",
    "category": "String",
    "aliases": [],
    "tags": ["hash_set", "string_matching"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Count how many strings in a list consist only of characters present in a given allowed string.",
}

def solve(allowed: str, words: list[str]) -> int:
    """
    Counts the number of strings in 'words' that only contain characters found in 'allowed'.

    Args:
        allowed: A string containing the set of allowed characters.
        words: A list of strings to check for consistency.

    Returns:
        The count of consistent strings.

    Examples:
        >>> solve("ab", ["a", "b", "ab", "ba", "c"])
        4
        >>> solve("abc", ["a", "b", "c", "d", "e"])
        3
    """
    # Convert allowed string to a set for O(1) average time complexity lookups
    allowed_set = set(allowed)
    consistent_count = 0

    for word in words:
        is_consistent = True
        for char in word:
            # If any character in the word is not in the allowed set, it's inconsistent
            if char not in allowed_set:
                is_consistent = False
                break
        
        if is_consistent:
            consistent_count += 1

    return consistent_count
