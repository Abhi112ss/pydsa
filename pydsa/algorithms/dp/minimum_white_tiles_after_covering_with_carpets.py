METADATA = {
    "id": 2209,
    "name": "Minimum White Tiles After Covering With Carpets",
    "slug": "minimum-white-tiles-after-covering-with-carpets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "hard",
    "time_complexity": "O(k * n^2)",
    "space_complexity": "O(k * n)",
    "description": "Find the minimum number of white tiles remaining after covering tiles with k carpets of given lengths.",
}

def solve(tiles: list[int], carpets: list[int]) -> int:
    """
    Calculates the minimum number of white tiles remaining after using all carpets.

    Args:
        tiles: A list of integers where 1 represents a black tile and 0 a white tile.
        carpets: A list of integers representing the lengths of available carpets.

    Returns:
        The minimum number of white tiles left uncovered.

    Examples:
        >>> solve([1, 1, 0, 1, 1], [1, 2])
        1
        >>> solve([1, 1, 1, 1, 1], [1, 1])
        3
    """
    n = len(tiles)
    k = len(carpets)
    total_black_tiles = sum(tiles)

    # dp[i][j] represents the maximum number of black tiles covered 
    # using the first i carpets considering tiles from index j to n-1.
    # We use (k + 1) x (n + 1) to handle base cases easily.
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # Precompute the number of black tiles covered if a carpet of length L 
    # starts at index i.
    # black_covered[carpet_idx][start_index]
    # To optimize, we can calculate this on the fly or pre-calculate.
    # Given the constraints and O(k * n^2), we calculate it inside the loop.

    for i in range(1, k + 1):
        carpet_len = carpets[i - 1]
        for j in range(n - 1, -1, -1):
            # Option 1: Don't use the current carpet starting at index j.
            # We move to the next tile index for the same carpet count.
            # However, the standard DP approach for this is:
            # dp[i][j] = max(dp[i][j+1], max_coverage_starting_at_j)
            
            # Option 1: Skip tile j for the current carpet i
            res = dp[i][j + 1]

            # Option 2: Place carpet i starting at index j
            # Calculate how many black tiles this carpet covers
            current_coverage = 0
            end_index = min(j + carpet_len, n)
            for idx in range(j, end_index):
                if tiles[idx] == 1:
                    current_coverage += 1
            
            # The total black tiles covered is current_coverage + 
            # the max black tiles covered by remaining i-1 carpets starting after this carpet.
            res = max(res, current_coverage + dp[i - 1][end_index])
            
            dp[i][j] = res

    # The answer is total black tiles minus the maximum black tiles we could cover.
    return total_black_tiles - dp[k][0]
