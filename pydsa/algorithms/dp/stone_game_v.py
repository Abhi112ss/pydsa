METADATA = {
    "id": 1563,
    "name": "Stone Game V",
    "slug": "stone-game-v",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "divide_and_conquer"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum score Alice can get in a stone game where players split piles of stones into two non-empty piles.",
}

def solve(stones: list[int]) -> int:
    """
    Calculates the maximum score Alice can achieve in the Stone Game V.

    The game involves splitting a pile of stones into two non-empty piles. 
    The player receives points equal to the minimum of the two piles. 
    The game continues until no more splits are possible.

    Args:
        stones: A list of integers representing the number of stones in each pile.

    Returns:
        The maximum score the first player can achieve.

    Examples:
        >>> solve([5, 4, 4, 1])
        10
        >>> solve([1, 1, 1, 1])
        0
    """
    n = len(stones)
    # dp[i][j] stores the maximum score obtainable from the subarray stones[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Length of the subarray being considered (from 2 up to n)
    for length in range(2, n + 1):
        # Starting index of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Calculate prefix sums to get the sum of any range in O(1)
            # However, for simplicity and since we are already O(n^3), 
            # we can compute the sum of the current range.
            current_sum = sum(stones[i : j + 1])
            
            max_score = 0
            # Try every possible split point k
            # The split results in two piles: stones[i...k] and stones[k+1...j]
            for k in range(i, j):
                # Calculate the sum of the left and right piles
                # We use a running sum or precomputed prefix sums for better performance,
                # but here we calculate it to maintain clarity.
                left_sum = sum(stones[i : k + 1])
                right_sum = current_sum - left_sum
                
                # The score for this split is min(left_sum, right_sum) 
                # plus the best scores from the resulting sub-piles.
                # We take the maximum over all possible split points k.
                score = min(left_sum, right_sum) + dp[i][k] + dp[k + 1][j]
                if score > max_score:
                    max_score = score
            
            dp[i][j] = max_score

    return dp[0][n - 1]

# Optimized version using prefix sums to ensure true O(n^3) performance
def solve_optimized(stones: list[int]) -> int:
    """
    An optimized version of the Stone Game V solver using prefix sums.

    Args:
        stones: A list of integers representing the number of stones in each pile.

    Returns:
        The maximum score the first player can achieve.
    """
    n = len(stones)
    dp = [[0] * n for _ in range(n)]
    
    # Precompute prefix sums for O(1) range sum queries
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + stones[i]

    def get_sum(left: int, right: int) -> int:
        return prefix_sums[right + 1] - prefix_sums[left]

    # Iterate through all possible subarray lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_sum = get_sum(i, j)
            
            current_max = 0
            # Try all split points k such that i <= k < j
            for k in range(i, j):
                left_sum = get_sum(i, k)
                right_sum = total_sum - left_sum
                
                # The score is the minimum of the two piles plus the optimal 
                # scores from the two resulting sub-problems.
                score = min(left_sum, right_sum) + dp[i][k] + dp[k + 1][j]
                if score > current_max:
                    current_max = score
            
            dp[i][j] = current_max

    return dp[0][n - 1]

# Alias for the optimized version
solve = solve_optimized