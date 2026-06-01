METADATA = {
    "id": 940,
    "name": "Distinct Subsequences II",
    "slug": "distinct-subsequences-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of non-empty distinct subsequences of a string modulo 10^9 + 7.",
}

def solve(s: str) -> int:
    """
    Calculates the number of distinct non-empty subsequences of a given string.

    The algorithm uses dynamic programming. Let dp[i] be the number of distinct 
    subsequences using the first i characters. When adding a new character 'c', 
    the number of subsequences doubles (we either include 'c' or we don't), 
    but we must subtract the subsequences that were already counted when 'c' 
    last appeared to avoid duplicates.

    Args:
        s: The input string.

    Returns:
        The total number of distinct non-empty subsequences modulo 10^9 + 7.

    Examples:
        >>> solve("abc")
        7
        >>> solve("aba")
        5
    """
    MOD = 1_000_000_007
    
    # total_subsequences tracks the number of distinct subsequences 
    # (including the empty subsequence) found so far.
    total_subsequences = 1
    
    # last_added_count stores how many new subsequences were added 
    # the last time a specific character was encountered.
    # This allows us to subtract duplicates efficiently.
    last_added_count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for char in s:
        # The number of new subsequences we can form by appending 'char' 
        # to all existing subsequences is equal to the current total.
        new_subsequences = total_subsequences
        
        # To avoid duplicates, we subtract the number of subsequences 
        # that were added the last time this specific character was used.
        # This is because appending 'char' to those old subsequences 
        # would result in the same strings we are currently generating.
        current_added = (new_subsequences - last_added_count[char]) % MOD
        
        # Update the total count: current total + new unique subsequences.
        total_subsequences = (total_subsequences + current_added) % MOD
        
        # Update the record for this character to reflect the amount 
        # it contributed to the total count in this step.
        last_added_count[char] = (last_added_count[char] + current_added) % MOD

    # Subtract 1 to exclude the empty subsequence from the final count.
    return (total_subsequences - 1 + MOD) % MOD
