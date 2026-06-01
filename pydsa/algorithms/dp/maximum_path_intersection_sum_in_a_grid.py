METADATA = {
    "id": 3938,
    "name": "Maximum Path Intersection Sum in a Grid",
    "slug": "maximum-path-intersection-sum-in-a-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "graphs", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 * m^2)",
    "space_complexity": "O(n^2 * m^2)",
    "description": "Find the maximum sum of values at the intersection points of two paths moving from top-left to bottom-right in a grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum sum of values at the intersection points of two paths.
    
    The problem asks for the maximum sum of values where two paths (each moving 
    only right or down) intersect. However, based on the standard interpretation 
    of such grid problems, we are looking for the maximum sum of values collected 
    by two paths that can share cells.

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The maximum sum of values collected by two paths from (0,0) to (R-1, C-1).

    Examples:
        >>> solve([[1, 2], [3, 4]])
        10  # Path 1: 1->2->4, Path 2: 1->3->4. Sum: 1+2+4 + 3 = 10 (if intersection is counted once)
                               # Or if both paths are summed: (1+2+4) + (1+3+4) - (1+4) = 10
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # dp[r1][c1][r2][c2] is too large. 
    # Since both paths move one step at a time, we can use 'steps' as a dimension.
    # steps = r + c. Thus, r1 + c1 = r2 + c2 = steps.
    # We only need to track (r1, r2) for a given 'steps'.
    # dp[steps][r1][r2]
    
    # To optimize space, we use dp[r1][r2] and update it for each step.
    # dp[r1][r2] represents the max sum at current step where path 1 is at row r1 
    # and path 2 is at row r2.
    
    # Initialize DP table with a very small number
    # dp[r1][r2]
    dp = [[float('-inf')] * rows for _ in range(rows)]
    
    # Base case: at step 0, both paths are at (0,0)
    dp[0][0] = grid[0][0]

    # Total steps to reach (rows-1, cols-1) is (rows-1) + (cols-1)
    total_steps = (rows - 1) + (cols - 1)

    for step in range(1, total_steps + 1):
        new_dp = [[float('-inf')] * rows for _ in range(rows)]
        
        # Iterate through possible rows for path 1 and path 2
        # r must be <= step and r < rows and (step - r) < cols
        for r1 in range(max(0, step - cols + 1), min(step + 1, rows)):
            c1 = step - r1
            for r2 in range(max(0, step - cols + 1), min(step + 1, rows)):
                c2 = step - r2
                
                # Possible previous states for (r1, c1) and (r2, c2)
                # Each path could have come from Top (r-1, c) or Left (r, c-1)
                prev_states = []
                # Path 1 moves: (r1-1, c1) or (r1, c1-1)
                # Path 2 moves: (r2-1, c2) or (r2, c2-1)
                
                # We check all 4 combinations of previous positions
                for pr1 in [r1, r1 - 1]:
                    for pr2 in [r2, r2 - 1]:
                        if 0 <= pr1 < rows and 0 <= pr2 < rows:
                            # Check if the previous step was valid for the current step
                            # (i.e., the previous row/col must have been within bounds)
                            pc1 = (step - 1) - pr1
                            pc2 = (step - 1) - pr2
                            if 0 <= pc1 < cols and 0 <= pc2 < cols:
                                prev_states.append(dp[pr1][pr2])
                
                if prev_states:
                    max_prev = max(prev_states)
                    if max_prev != float('-inf'):
                        # If paths are at the same cell, add the value once.
                        # Otherwise, add both values.
                        if r1 == r2:
                            new_dp[r1][r2] = max_prev + grid[r1][c1]
                        else:
                            new_dp[r1][r2] = max_prev + grid[r1][c1] + grid[r2][c2]
        dp = new_dp

    return int(dp[rows - 1][rows - 1])
