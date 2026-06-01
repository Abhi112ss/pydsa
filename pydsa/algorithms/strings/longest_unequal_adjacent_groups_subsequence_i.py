METADATA = {
    "id": 2900,
    "name": "Longest Unequal Adjacent Groups Subsequence I",
    "slug": "longest-unequal-adjacent-groups-subsequence-i",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subsequence where no two adjacent elements are from the same group of identical characters.",
}

def solve(s: str) -> int:
    """
    Calculates the length of the longest subsequence where no two adjacent 
    elements belong to the same group of identical characters.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The length of the longest subsequence with unequal adjacent groups.

    Examples:
        >>> solve("aabbcc")
        3
        >>> solve("aaaaa")
        1
        >>> solve("ababa")
        5
    """
    if not s:
        return 0

    # The problem asks for the longest subsequence where adjacent elements 
    # are different. In a string, this is equivalent to counting the 
    # number of times the character changes, plus the first character.
    # Effectively, we are counting the number of contiguous blocks of 
    # identical characters.
    
    count = 1
    n = len(s)
    
    for i in range(1, n):
        # If the current character is different from the previous one,
        # it marks the start of a new group that can be included in the subsequence.
        if s[i] != s[i - 1]:
            count += 1
            
    return count
