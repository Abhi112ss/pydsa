METADATA = {
    "id": 3154,
    "name": "Find Number of Ways to Reach the K-th Stair",
    "slug": "find-number-of-ways-to-reach-the-k-th-stair",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(k)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of ways to reach the k-th stair using steps of size 1 or 2, starting from a given stair and direction.",
}

def solve(k: int, start_stair: int, direction: int) -> int:
    """
    Calculates the number of ways to reach the k-th stair using steps of size 1 or 2.

    The problem is a variation of the Fibonacci sequence. If we are moving 
    upwards, the number of ways to reach stair 'i' is the sum of ways to 
    reach 'i-1' and 'i-2'. If moving downwards, the logic is mirrored.

    Args:
        k: The target stair index.
        start_stair: The starting stair index.
        direction: The direction of movement (1 for up, -1 for down).

    Returns:
        The number of ways to reach the k-th stair.

    Examples:
        >>> solve(4, 1, 1)
        3
        >>> solve(4, 5, -1)
        3
        >>> solve(4, 4, 1)
        1
    """
    # If we are already at the target, there is exactly 1 way (doing nothing)
    if start_stair == k:
        return 1

    # If the target is unreachable due to direction
    if (direction == 1 and start_stair > k) or (direction == -1 and start_stair < k):
        return 0

    # Normalize the problem: always treat it as moving from 0 to a target distance 'n'
    # This allows us to use a standard Fibonacci-based DP approach.
    n = abs(k - start_stair)

    # We need to find the (n+1)-th Fibonacci number where F(0)=1, F(1)=1, F(2)=2...
    # dp_prev2 represents ways to reach (i-2), dp_prev1 represents ways to reach (i-1)
    dp_prev2 = 1  # Ways to reach distance 0
    dp_prev1 = 1  # Ways to reach distance 1

    if n == 0:
        return 1
    if n == 1:
        return 1

    # Iteratively calculate ways to reach distance 'n'
    for _ in range(2, n + 1):
        current_ways = dp_prev1 + dp_prev2
        dp_prev2 = dp_prev1
        dp_prev1 = current_ways

    return dp_prev1
