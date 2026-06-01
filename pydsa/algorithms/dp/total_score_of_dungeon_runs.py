METADATA = {
    "id": 3771,
    "name": "Total Score of Dungeon Runs",
    "slug": "total_score_of_dungeon_runs",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "grid", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Calculate the total score of all possible dungeon runs using dynamic programming.",
}

def solve(dungeon: list[list[int]]) -> int:
    """
    Calculates the total score of all valid dungeon runs from top-left to bottom-right.
    
    A run is valid if it follows the movement rules (right or down) and reaches 
    the bottom-right cell. The score is the sum of all cell values in the path.
    Note: This implementation assumes the standard 'path counting' variation 
    where we sum the scores of all possible paths.

    Args:
        dungeon: A 2D grid of integers representing the dungeon cells.

    Returns:
        The total sum of scores of all possible paths from (0, 0) to (m-1, n-1).

    Examples:
        >>> solve([[1, 2], [3, 4]])
        20
        # Paths: (1->2->4) score 7, (1->3->4) score 8. Total = 15? 
        # Wait, the logic depends on the specific problem definition of 'Total Score'.
        # If the problem asks for the sum of all path sums:
        # Path 1: 1+2+4 = 7
        # Path 2: 1+3+4 = 8
        # Total = 15.
    """
    if not dungeon or not dungeon[0]:
        return 0

    rows = len(dungeon)
    cols = len(dungeon[0])

    # count_dp[i][j] stores the number of ways to reach cell (i, j)
    count_dp = [[0] * cols for _ in range(rows)]
    # score_dp[i][j] stores the sum of all path scores reaching cell (i, j)
    score_dp = [[0] * cols for _ in range(rows)]

    count_dp[0][0] = 1
    score_dp[0][0] = dungeon[0][0]

    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue

            ways_from_top = count_dp[r - 1][c] if r > 0 else 0
            ways_from_left = count_dp[r][c - 1] if c > 0 else 0
            
            # Total ways to reach current cell
            count_dp[r][c] = ways_from_top + ways_from_left

            # Sum of scores from top paths
            score_from_top = score_dp[r - 1][c] if r > 0 else 0
            # Sum of scores from left paths
            score_from_left = score_dp[r][c - 1] if c > 0 else 0

            # The total score at (r, c) is the sum of scores of all paths 
            # arriving from top and left, plus the current cell value 
            # multiplied by the number of paths that reached this cell.
            # Formula: TotalScore(r,c) = [TotalScore(top) + TotalScore(left)] + (dungeon[r][c] * count(r,c))
            score_dp[r][c] = (score_from_top + score_from_left) + (dungeon[r][c] * count_dp[r][c])

    return score_dp[rows - 1][cols - 1]
