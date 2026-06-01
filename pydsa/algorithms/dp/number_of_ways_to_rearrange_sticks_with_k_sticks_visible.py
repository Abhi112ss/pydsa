METADATA = {
    "id": 1866,
    "name": "Number of Ways to Rearrange Sticks With K Sticks Visible",
    "slug": "number-of-ways-to-rearrange-sticks-with-k-sticks-visible",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "combinatorics", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Find the number of ways to rearrange n sticks such that exactly k sticks are visible from the front.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of ways to rearrange n sticks such that exactly k sticks are visible.
    
    A stick is visible if it is taller than all sticks in front of it.
    The problem is equivalent to finding the Unsigned Stirling Numbers of the First Kind.
    
    Args:
        n: The total number of sticks.
        k: The number of sticks that must be visible.
        
    Returns:
        The number of ways to rearrange the sticks modulo 10^9 + 7.
        
    Examples:
        >>> solve(3, 2)
        3
        >>> solve(4, 2)
        11
    """
    MOD = 1_000_000_007

    # Base cases:
    # If k is 0, it's impossible to have 0 visible sticks unless n is 0.
    # If k > n, it's impossible.
    if k == 0 or k > n:
        return 0
    if n == 0:
        return 1 if k == 0 else 0

    # dp[i][j] represents the number of ways to arrange i sticks such that j are visible.
    # We use a 2D array for clarity, though it can be optimized to 1D.
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 0 sticks, 0 visible is 1 way (empty set).
    dp[0][0] = 1

    for i in range(1, n + 1):
        # A stick can only be visible if j <= i.
        # We only care up to k visible sticks.
        for j in range(1, min(i, k) + 1):
            # There are two scenarios for the i-th (tallest) stick:
            # 1. The i-th stick is placed at the very front. 
            #    It becomes visible, so we need j-1 visible sticks from the previous i-1 sticks.
            #    Ways: dp[i-1][j-1]
            # 2. The i-th stick is placed in any of the (i-1) positions behind existing sticks.
            #    It will not be visible because it's the tallest and placed behind others.
            #    Ways: dp[i-1][j] * (i - 1)
            
            dp[i][j] = (dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]) % MOD

    return dp[n][k]
