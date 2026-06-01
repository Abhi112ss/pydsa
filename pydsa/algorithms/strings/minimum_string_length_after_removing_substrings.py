METADATA = {
    "id": 2696,
    "name": "Minimum String Length After Removing Substrings",
    "slug": "minimum-string-length-after-removing-substrings",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum length of a string after repeatedly removing all occurrences of 'ab' and 'pq'.",
}

def solve(s: str, pattern1: str, pattern2: str) -> int:
    """
    Calculates the minimum length of the string after removing all occurrences 
    of pattern1 and pattern2.

    Args:
        s: The input string.
        pattern1: The first substring to remove.
        pattern2: The second substring to remove.

    Returns:
        The length of the resulting string after all possible removals.

    Examples:
        >>> solve("aabbaa", "ab", "pq")
        2
        >>> solve("leetcode", "ee", "t")
        4
    """
    stack: list[str] = []
    
    # Pre-calculate pattern lengths for efficiency
    len1 = len(pattern1)
    len2 = len(pattern2)

    for char in s:
        stack.append(char)
        
        # Check if the end of the stack matches pattern1
        if len(stack) >= len1:
            # Using slicing on a list is O(k) where k is pattern length
            # Since pattern length is constant (2), this is O(1)
            if stack[-len1:] == list(pattern1):
                for _ in range(len1):
                    stack.pop()
                    
        # Check if the end of the stack matches pattern2
        # We check both patterns because removing one might create the other
        if len(stack) >= len2:
            if stack[-len2:] == list(pattern2):
                for _ in range(len2):
                    stack.pop()

    return len(stack)
