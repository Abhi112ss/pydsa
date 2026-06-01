METADATA = {
    "id": 1406,
    "name": "Stone Game III",
    "slug": "stone-game-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine the maximum score difference Alice can achieve over Bob in a game of picking stones.",
}

def solve(stones: list[int]) -> int:
    """
    Calculates the maximum score difference Alice can achieve over Bob.

    The game is played by two players who can take 1, 2, or 3 stones from the front.
    Alice goes first. We use dynamic programming to find the maximum relative 
    score (current player's score minus opponent's score) from any index i.

    Args:
        stones: A list of integers representing the number of stones in each pile.

    Returns:
        The maximum score difference (Alice's score - Bob's score).

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6])
        1
        >>> solve([1, 1, 1, 1, 1, 1])
        0
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8])
        1
    """
    n = len(stones)
    # dp[i] represents the maximum relative score the current player can get 
    # starting from index i to the end of the array.
    dp = [0] * (n + 1)

    # Iterate backwards from the end of the stones array to the beginning.
    for i in range(n - 1, -1, -1):
        # Option 1: Take 1 stone
        # Current player gets stones[i] and the opponent gets dp[i+1]
        res = stones[i] - dp[i + 1]

        # Option 2: Take 2 stones (if available)
        if i + 2 <= n:
            res = max(res, stones[i] + stones[i + 1] - dp[i + 2])

        # Option 3: Take 3 stones (if available)
        if i + 3 <= n:
            res = max(res, stones[i] + stones[i + 1] + stones[i + 2] - dp[i + 3])

        # Store the best relative score for the current position
        dp[i] = res

    return dp[0]
