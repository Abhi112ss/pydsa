METADATA = {
    "id": 3777,
    "name": "Minimum Deletions to Make Alternating Substring",
    "slug": "minimum-deletions-to-make-alternating-substring",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of deletions required to ensure no two adjacent characters in a string are the same.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of deletions needed to make a string alternating.
    An alternating string is defined as a string where no two adjacent characters are identical.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The minimum number of deletions required.

    Examples:
        >>> solve("aabbcc")
        3
        >>> solve("abcde")
        0
        >>> solve("aaaaa")
        4
    """
    if not s:
        return 0

    deletions_count = 0
    
    # Iterate through the string starting from the second character
    for index in range(1, len(s)):
        # If the current character is the same as the previous one,
        # it violates the alternating property and must be deleted.
        if s[index] == s[index - 1]:
            deletions_count += 1
            
    return deletions_count
