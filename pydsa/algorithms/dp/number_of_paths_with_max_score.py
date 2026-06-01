METADATA = {
    "id": 1301,
    "name": "Number of Paths with Max Score",
    "slug": "number-of-paths-with-max-score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the number of paths from the bottom-right to the top-left that yield the maximum possible score.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the number of paths from the bottom-right corner to the top-left corner
    that yield the maximum possible score.

    The score is defined as the sum of values in the cells visited, excluding the 
    starting and ending cells. The path can move up, left, or diagonally up-left.

    Args:
        grid: An n x n matrix of integers.

    Returns:
        The number of paths with the maximum score, modulo 10^9 + 7.

    Examples:
        >>> solve([[0,0,0],[0,0,0],[0,0,0]])
        1
        >>> solve([[5,0,0],[0,0,0],[0,0,5]])
        1
    """
    MOD = 1_000_000_007
    n = len(grid)

    # dp_score[r][c] stores the maximum score achievable reaching cell (r, c)
    # dp_count[r][c] stores the number of ways to achieve that maximum score
    dp_score = [[0.0] * n for _ in range(n)]
    dp_count = [[0] * n for _ in range(n)]

    # Base case: The starting cell (bottom-right)
    # We don't include the value of the start or end cell in the score calculation.
    # However, to make the DP transition uniform, we treat the start as having 0 score.
    dp_count[n - 1][n - 1] = 1

    # Iterate through the grid from bottom-right to top-left
    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            # Skip the starting cell as it's already initialized
            if r == n - 1 and c == n - 1:
                continue

            max_prev_score = -1.0
            ways = 0

            # Check three possible previous cells: (r+1, c), (r, c+1), (r+1, c+1)
            # These are the cells from which we could have moved to (r, c)
            for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                prev_r, prev_c = r + dr, c + dc

                if 0 <= prev_r < n and 0 <= prev_c < n:
                    # If the previous cell was reachable
                    if dp_count[prev_r][prev_c] > 0:
                        # We calculate the score contribution. 
                        # Note: grid[r][c] is added to the path score, 
                        # but the problem says exclude start and end.
                        # We handle this by only adding grid[r][c] if it's not the top-left.
                        # Actually, a cleaner way: add grid[r][c] to the score of the path 
                        # coming from a neighbor, but don't add grid[0][0] at the very end.
                        
                        # To simplify: we add grid[r][c] to the score of the path 
                        # as we move into (r, c). We will subtract grid[0][0] at the end 
                        # or simply not add it.
                        
                        # Correct logic: The score of a path is sum(grid[i][j]) for all 
                        # (i, j) in path except start and end.
                        # Let's define dp_score[r][c] as the max score of a path from 
                        # (n-1, n-1) to (r, c) including grid[r][c] but excluding grid[n-1][n-1].
                        
                        current_path_score = dp_score[prev_r][prev_c] + grid[r][c]
                        
                        if current_path_score > max_prev_score:
                            max_prev_score = current_path_score
                            ways = dp_count[prev_r][prev_c]
                        elif current_path_score == max_prev_score:
                            ways = (ways + dp_count[prev_r][prev_c]) % MOD

            if max_prev_score != -1.0:
                dp_score[r][c] = max_prev_score
                dp_count[r][c] = ways

    # The score at (0, 0) includes grid[0][0], but the problem says exclude it.
    # However, the 'ways' (dp_count) is what we need.
    # Since we added grid[r][c] for every cell including (0,0), 
    # the max_score logic is correct, but we must ensure the path count 
    # is returned for the top-left cell.
    
    # One edge case: if the max score is 0, we still need to return the count.
    # The way we built it, dp_count[0][0] will contain the number of paths 
    # that reached (0,0) with the maximum score.
    
    # Because we added grid[0][0] to the score in the last step of the loop,
    # we need to adjust the score logic to strictly follow "exclude start and end".
    # Let's refine: The score of a path is sum of grid[i][j] for all cells 
    # except (n-1, n-1) and (0, 0).
    
    # Re-calculating logic:
    # Let dp_score[r][c] be the max score from (n-1, n-1) to (r, c) 
    # including grid[r][c] but NOT including grid[n-1][n-1].
    # Then the final score at (0,0) will be (sum of path) - grid[0][0].
    # This is exactly what the loop does.
    
    # Final adjustment: The loop adds grid[r][c] to the score.
    # When r=0, c=0, it adds grid[0][0]. 
    # To exclude grid[0][0], we can just subtract it from the score, 
    # but the count remains the same.
    
    # Wait, if grid[0][0] is very large, it might change which path is "max".
    # But grid[0][0] is added to ALL paths reaching (0,0). 
    # So it doesn't change the relative order of path scores.
    
    # Let's re-verify:
    # Path: (n-1, n-1) -> ... -> (0, 0)
    # Score = grid[r1][c1] + ... + grid[rk][ck] where (r1, c1) and (rk, ck) 
    # are neighbors of start and end.
    # Our DP: dp_score[r][c] = max(dp_score[prev] + grid[r][c])
    # For (0,0), dp_score[0][0] = max(dp_score[neighbor] + grid[0][0])
    # This is (sum of all cells in path including start and end) - grid[n-1][n-1].
    # To get the actual score: actual = dp_score[0][0] - grid[0][0].
    # Since grid[0][0] is constant for all paths, the path with max dp_score[0][0]
    # is the same as the path with max actual score.

    return dp_count[0][0]
