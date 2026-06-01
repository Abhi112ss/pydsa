METADATA = {
    "id": 91,
    "name": "Decode Ways",
    "slug": "decode-ways",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a string containing only digits, determine the total number of ways to decode it into letters.",
}

def solve(s: str) -> int:
    """
    Calculates the number of ways to decode a string of digits into letters (A-Z).

    Args:
        s: A string containing only digits.

    Returns:
        The total number of ways to decode the string.

    Examples:
        >>> solve("12")
        2
        >>> solve("226")
        3
        >>> solve("06")
        0
    """
    if not s or s[0] == '0':
        return 0

    n = len(s)
    # dp[i] represents the number of ways to decode the prefix s[0...i-1]
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # An empty string has one way to be decoded (doing nothing)
    dp[1] = 1  # We already checked s[0] != '0', so there's 1 way for the first char

    for i in range(2, n + 1):
        # Check single digit decoding (s[i-1])
        # If the current digit is not '0', it can form a valid letter (1-9)
        one_digit = int(s[i - 1])
        if one_digit != 0:
            dp[i] += dp[i - 1]

        # Check two digit decoding (s[i-2...i-1])
        # If the two digits form a number between 10 and 26, it's a valid letter
        two_digits = int(s[i - 2 : i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]
