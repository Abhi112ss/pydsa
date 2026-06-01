METADATA = {
    "id": 887,
    "name": "Super Egg Drop",
    "slug": "super-egg-drop",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["binary_search", "math", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(k * log n)",
    "space_complexity": "O(k)",
    "description": "Find the minimum number of moves required to determine the highest floor from which an egg can be dropped without breaking, given k eggs and n floors.",
}

def solve(k: int, n: int) -> int:
    """
    Calculates the minimum number of moves required to find the critical floor.
    
    The approach uses dynamic programming where dp[m][e] represents the maximum 
    number of floors we can check with 'm' moves and 'e' eggs.
    The transition is: dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1.
    - dp[m-1][e-1]: floors covered if the egg breaks (we have one less egg and one less move).
    - dp[m-1][e]: floors covered if the egg doesn't break (we have the same eggs and one less move).
    - 1: the current floor being tested.

    Args:
        k: The number of eggs available.
        n: The number of floors to test.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve(1, 2)
        2
        >>> solve(2, 6)
        3
        >>> solve(3, 14)
        4
    """
    # dp[e] will store the maximum floors reachable with 'e' eggs for the current number of moves.
    # We use a 1D array to optimize space from O(k * moves) to O(k).
    dp = [0] * (k + 1)
    moves = 0

    # We continue increasing the number of moves until the maximum reachable floor 
    # with k eggs is greater than or equal to the target n floors.
    while dp[k] < n:
        moves += 1
        # We iterate backwards to ensure we use the dp values from the previous 'moves' iteration.
        # This is similar to the space optimization used in the 0/1 Knapsack problem.
        for eggs in range(k, 0, -1):
            # dp[eggs] (new) = dp[eggs-1] (old) + dp[eggs] (old) + 1
            # This represents: (floors if egg breaks) + (floors if egg survives) + current floor
            dp[eggs] = dp[eggs - 1] + dp[eggs] + 1
            
    return moves
