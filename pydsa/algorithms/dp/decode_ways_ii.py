METADATA = {
    "id": 639,
    "name": "Decode Ways II",
    "slug": "decode-ways-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of ways to decode a string containing digits and '*' where '*' can represent any digit from 1 to 9.",
}

def solve(s: str) -> int:
    """
    Calculates the number of ways to decode a string containing digits and '*'.
    '*' can be any digit from '1' to '9'.
    
    Args:
        s: The encoded string containing digits '0'-'9' and '*'.
        
    Returns:
        The total number of ways to decode the string modulo 10^9 + 7.
        
    Examples:
        >>> solve("1*")
        9
        >>> solve("*0")
        1
        >>> solve("06")
        0
    """
    MOD = 10**9 + 7
    n = len(s)
    if n == 0:
        return 0

    # dp_prev2 represents ways to decode up to i-2
    # dp_prev1 represents ways to decode up to i-1
    dp_prev2 = 1
    dp_prev1 = 0

    # Base case: handle the first character
    if s[0] == '*':
        dp_prev1 = 9
    elif s[0] != '0':
        dp_prev1 = 1
    else:
        return 0

    for i in range(1, n):
        current_ways = 0
        char = s[i]
        prev_char = s[i-1]

        # Case 1: Single digit decoding (s[i])
        if char == '*':
            current_ways = (current_ways + 9 * dp_prev1) % MOD
        elif char != '0':
            current_ways = (current_ways + dp_prev1) % MOD

        # Case 2: Two digit decoding (s[i-1]s[i])
        # Subcase A: Both are digits
        if prev_char != '*' and char != '*':
            val = int(prev_char + char)
            if 10 <= val <= 26:
                current_ways = (current_ways + dp_prev2) % MOD
        
        # Subcase B: First is '*', second is digit
        elif prev_char == '*' and char != '*':
            # If char is '0'-'6', '*' can be '1' or '2' (2 ways)
            # If char is '7'-'9', '*' can only be '1' (1 way)
            if '0' <= char <= '6':
                current_ways = (current_ways + 2 * dp_prev2) % MOD
            else:
                current_ways = (current_ways + dp_prev2) % MOD
        
        # Subcase C: First is digit, second is '*'
        elif prev_char != '*' and char == '*':
            # If prev is '1', '*' can be '1'-'9' (9 ways)
            # If prev is '2', '*' can be '1'-'6' (6 ways)
            if prev_char == '1':
                current_ways = (current_ways + 9 * dp_prev2) % MOD
            elif prev_char == '2':
                current_ways = (current_ways + 6 * dp_prev2) % MOD
        
        # Subcase D: Both are '*'
        else:
            # Combinations: 11-19 (9) + 21-26 (6) = 15 ways
            current_ways = (current_ways + 15 * dp_prev2) % MOD

        # Shift DP states for next iteration
        dp_prev2 = dp_prev1
        dp_prev1 = current_ways
        
        # If no ways to decode current prefix, we can stop early
        if dp_prev1 == 0 and dp_prev2 == 0:
            return 0

    return dp_prev1
