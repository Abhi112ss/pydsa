METADATA = {
    "id": 2466,
    "name": "Count Ways To Build Good Strings",
    "slug": "count-ways-to-build-good-strings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of ways to build a good string of length n using given allowed lengths, modulo 10^9 + 7.",
}

def solve(n: int, allowed_lengths: list[int]) -> int:
    """
    Calculates the number of ways to build a good string of length n.
    
    A string is 'good' if its length is n and it is constructed by 
    appending substrings with lengths present in the allowed_lengths list.

    Args:
        n: The target length of the string.
        allowed_lengths: A list of integers representing the allowed lengths 
            of substrings that can be appended.

    Returns:
        The total number of ways to build a good string of length n, 
        modulo 10^9 + 7.

    Examples:
        >>> solve(3, [1, 2])
        3
        >>> solve(5, [1, 2, 5])
        9
    """
    MODULO = 1_000_000_007
    
    # dp[i] stores the number of ways to construct a string of length i
    dp = [0] * (n + 1)
    
    # Base case: There is exactly one way to construct a string of length 0 (the empty string)
    dp[0] = 1
    
    # Iterate through every length from 1 to n to build up the DP table
    for current_length in range(1, n + 1):
        for length in allowed_lengths:
            # If the current length can be reached by adding a substring of 'length'
            # to a previously valid string of length (current_length - length)
            if current_length - length >= 0:
                dp[current_length] = (dp[current_length] + dp[current_length - length]) % MODULO
                
    return dp[n]
