METADATA = {
    "id": 87,
    "name": "Scramble String",
    "slug": "scramble-string",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "recursion"],
    "difficulty": "hard",
    "time_complexity": "O(n^4)",
    "space_complexity": "O(n^3)",
    "description": "Determine if one string is a scrambled version of another based on a recursive binary tree splitting process.",
}

def solve(s1: str, s2: str) -> bool:
    """
    Determines if s2 is a scrambled string of s1 using memoized recursion.

    Args:
        s1: The first input string.
        s2: The second input string.

    Returns:
        True if s2 is a scrambled version of s1, False otherwise.

    Examples:
        >>> solve("great", "rgeat")
        True
        >>> solve("abcde", "caebd")
        False
    """
    memo: dict[tuple[str, str], bool] = {}

    def is_scramble(str1: str, str2: str) -> bool:
        # Base case: identical strings
        if str1 == str2:
            return True
        
        # Base case: different character counts or lengths
        if len(str1) != len(str2) or sorted(str1) != sorted(str2):
            return False
        
        state = (str1, str2)
        if state in memo:
            return memo[state]

        n = len(str1)
        # Try splitting the string at every possible index i
        for i in range(1, n):
            # Case 1: No swap at this level
            # Left part of s1 matches left part of s2 AND right part of s1 matches right part of s2
            if (is_scramble(str1[:i], str2[:i]) and 
                is_scramble(str1[i:], str2[i:])):
                memo[state] = True
                return True

            # Case 2: Swap occurred at this level
            # Left part of s1 matches right part of s2 AND right part of s1 matches left part of s2
            if (is_scramble(str1[:i], str2[n-i:]) and 
                is_scramble(str1[i:], str2[:n-i])):
                memo[state] = True
                return True

        memo[state] = False
        return False

    return is_scramble(s1, s2)
