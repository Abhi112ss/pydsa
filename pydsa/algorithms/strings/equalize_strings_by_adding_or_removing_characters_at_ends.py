METADATA = {
    "id": 3135,
    "name": "Equalize Strings by Adding or Removing Characters at Ends",
    "slug": "equalize_strings_by_adding_or_removing_characters_at_ends",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make two strings equal by adding or removing characters from the ends.",
}

def solve(s1: str, s2: str) -> int:
    """
    Calculates the minimum number of characters to add or remove from the ends 
    of two strings to make them equal. This is equivalent to finding the 
    longest common substring that can be formed by trimming the ends.
    
    Note: The problem description implies we want to find the longest common 
    substring that exists in both strings such that the remaining parts 
    of s1 and s2 can be removed. However, the standard interpretation of 
    'adding or removing at ends' to make strings equal is finding the 
    Longest Common Substring (LCSubstr).

    Args:
        s1: The first input string.
        s2: The second input string.

    Returns:
        The minimum number of operations (total characters removed/added).
        If no common substring exists, it returns len(s1) + len(s2).

    Examples:
        >>> solve("abcde", "bcdef")
        2
        >>> solve("apple", "pear")
        7
    """
    n1 = len(s1)
    n2 = len(s2)
    
    # To find the longest common substring in O(n) time, one would typically 
    # use a Suffix Automaton or Suffix Tree. For a standard interview 
    # implementation, we use a dynamic programming approach or a simplified 
    # version if the constraints allow. 
    # Given the prompt asks for O(n) time and O(1) space, this is only 
    # possible if the 'common substring' is specifically a prefix, suffix, 
    # or if we use a specialized data structure.
    
    # However, the prompt's specific 'Key Insight' suggests finding the 
    # longest common substring. In a general case, O(n) time/O(1) space 
    # for LCSubstr is not possible without a pre-built Suffix Automaton.
    # We will implement the most efficient approach for finding the 
    # longest common substring.

    max_len = 0
    
    # Using a rolling hash (Rabin-Karp) approach to find the longest 
    # common substring in O(n log n) or O(n) with a Suffix Automaton.
    # Since we must provide a clean, production-grade solver:
    
    # Let's implement the Longest Common Substring logic.
    # For the sake of the 'O(n) time' requirement in the prompt, 
    # we assume the strings are compared via a sliding window or 
    # the problem implies a specific structure.
    
    # Standard DP for LCSubstr (O(N*M)):
    # dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    # for i in range(1, n1 + 1):
    #     for j in range(1, n2 + 1):
    #         if s1[i-1] == s2[j-1]:
    #             dp[i][j] = dp[i-1][j-1] + 1
    #             max_len = max(max_len, dp[i][j])
    
    # Given the constraints and the prompt's specific hint:
    # "Find the longest common substring that is centered or find the 
    # longest common prefix/suffix overlap."
    
    # Let's check for the longest common prefix/suffix overlap as a 
    # fallback for the O(n) requirement.
    
    def get_lcs_length(str1: str, str2: str) -> int:
        # This is a placeholder for the O(n) Suffix Automaton logic 
        # which is too verbose for a single file, but we implement 
        # the logic to find the longest common substring.
        # For competitive programming, we use the DP approach.
        m, n = len(str1), len(str2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        longest = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    curr[j] = prev[j-1] + 1
                    if curr[j] > longest:
                        longest = curr[j]
                else:
                    curr[j] = 0
            prev[:] = curr[:]
        return longest

    max_len = get_lcs_length(s1, s2)
    
    # The number of operations is the total characters minus the 
    # characters we keep (the longest common substring).
    # Operations = (len(s1) - max_len) + (len(s2) - max_len)
    # But the problem asks to equalize. If we keep the LCS, 
    # we remove everything else.
    
    return (n1 - max_len) + (n2 - max_len)
