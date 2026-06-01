METADATA = {
    "id": 1690,
    "name": "Stone Game VII",
    "slug": "stone-game-vii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "interval_dp"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Calculate the maximum score difference Alice can achieve over Bob in a game where players pick stones from either end of a subarray.",
}

def solve(stones: list[int]) -> int:
    """
    Calculates the maximum score difference Alice can achieve over Bob.

    The game is played by two players. In each turn, a player chooses a subarray 
    by removing a stone from either the left or right end. The player's score 
    increases by the sum of the remaining stones. Both players play optimally.

    Args:
        stones: A list of integers representing the number of stones in each pile.

    Returns:
        The maximum score difference (Alice's score - Bob's score).

    Examples:
        >>> solve([5, 3, 4, 5])
        1
        >>> solve([1, 2, 3, 4])
        2
    """
    n = len(stones)
    
    # Precompute prefix sums to calculate subarray sums in O(1)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + stones[i]

    def get_sum(left: int, right: int) -> int:
        """Returns the sum of stones from index left to right inclusive."""
        return prefix_sums[right + 1] - prefix_sums[left]

    # dp[i][j] represents the maximum score difference the current player 
    # can achieve using the subarray stones[i...j].
    dp = [[0] * n for _ in range(n)]

    # Iterate over the length of the subarray from 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Option 1: Player picks the leftmost stone (index i)
            # Score gained: sum(stones[i+1...j])
            # Remaining game: dp[i+1][j] (which is the opponent's max difference)
            # Current player's net gain: sum(i+1...j) - dp[i+1][j]
            pick_left = get_sum(i + 1, j) - dp[i + 1][j]
            
            # Option 2: Player picks the rightmost stone (index j)
            # Score gained: sum(stones[i...j-1])
            # Remaining game: dp[i][j-1]
            # Current player's net gain: sum(i...j-1) - dp[i][j-1]
            pick_right = get_sum(i, j - 1) - dp[i][j - 1]
            
            # The player chooses the maximum of the two options
            dp[i][j] = max(pick_left, pick_right)

    return dp[0][n - 1]
