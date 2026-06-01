METADATA = {
    "id": 3802,
    "name": "Number of Ways to Paint Sheets",
    "slug": "number_of_ways_to_paint_sheets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of ways to paint sheets given specific constraints using dynamic programming.",
}

def solve(n: int, k: int, m: int) -> int:
    """
    Args:
        n: The total number of sheets to paint.
        k: The number of available colors.
        m: The constraint parameter for adjacent sheets.

    Returns:
        The total number of ways to paint the sheets modulo 10^9 + 7.
    """
    MODULO = 10**9 + 7

    if n == 0:
        return 0
    if n == 1:
        return k % MODULO

    dp = [0] * (n + 1)
    dp[1] = k % MODULO

    if n >= 2:
        dp[2] = (k * (k - 1)) % MODULO

    for i in range(3, n + 1):
        term1 = (dp[i - 1] * (k - 1)) % MODULO
        term2 = (dp[i - 2] * (k - 2)) % MODULO
        
        if m > 1:
            term2 = (dp[i - 2] * (k - 1)) % MODULO
            
        dp[i] = (term1 + term2) % MODULO

    return dp[n]