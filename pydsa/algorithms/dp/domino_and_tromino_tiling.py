METADATA = {
    "id": 790,
    "name": "Domino and Tromino Tiling",
    "slug": "domino-and-tromino-tiling",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "math-logic"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of ways to tile a 2 x n board using 2x1 dominoes and L-shaped trominoes.",
}

def solve(n: int) -> int:
    """
    Calculates the number of ways to tile a 2 x n board using dominoes and trominoes.

    The problem can be solved using dynamic programming. Let dp[i] be the number of 
    ways to tile a 2 x i board.
    The recurrence relation is: dp[i] = 2 * dp[i-1] + dp[i-3].
    Alternatively, derived from state transitions:
    dp[i] = dp[i-1] + dp[i-2] + 2 * (dp[i-3] + dp[i-4] + ... + dp[0])
    Which simplifies to: dp[i] = 2 * dp[i-1] + dp[i-3].

    Args:
        n: The width of the 2 x n board.

    Returns:
        The number of ways to tile the board modulo 10^9 + 7.

    Examples:
        >>> solve(1)
        1
        >>> solve(3)
        5
        >>> solve(4)
        11
    """
    MOD = 1_000_000_007

    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5

    # We only need the last three states to compute the next state:
    # dp[i] = 2 * dp[i-1] + dp[i-3]
    # Initial values for n=1, n=2, n=3
    prev_3 = 1  # dp[1]
    prev_2 = 2  # dp[2]
    prev_1 = 5  # dp[3]
    
    current_val = 0
    for _ in range(4, n + 1):
        # Apply the recurrence relation: dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
        current_val = (2 * prev_1 + prev_3) % MOD
        
        # Shift states forward for the next iteration
        prev_3 = prev_2
        prev_2 = prev_1
        prev_1 = current_val
        
    return prev_1
