METADATA = {
    "id": 3858,
    "name": "Minimum Bitwise OR From Grid",
    "slug": "minimum_bitwise_or_from_grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "grid", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(m * n * log(max_val))",
    "space_complexity": "O(m * n * log(max_val))",
    "description": "Find the minimum bitwise OR value achievable by traversing from the top-left to the bottom-right of a grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum bitwise OR value achievable by traversing from (0,0) to (m-1, n-1).
    
    The path can only move right or down. We use dynamic programming where each cell 
    stores a set of all possible bitwise OR values reachable at that cell.

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The minimum bitwise OR value possible at the bottom-right cell.

    Examples:
        >>> solve([[1, 2], [4, 8]])
        3
        >>> solve([[1, 1], [1, 1]])
        1
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # dp[r][c] stores a set of all unique bitwise OR values possible at cell (r, c)
    # Using a set is efficient because the number of unique OR values is bounded 
    # by the number of bits (e.g., 30 bits -> max 30-31 unique values per cell).
    dp: list[list[set[int]]] = [[set() for _ in range(cols)] for _ in range(rows)]

    # Initialize starting cell
    dp[0][0].add(grid[0][0])

    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue
            
            current_val = grid[r][c]
            
            # Check cell above
            if r > 0:
                for prev_or in dp[r - 1][c]:
                    dp[r][c].add(prev_or | current_val)
            
            # Check cell to the left
            if c > 0:
                for prev_or in dp[r][c - 1]:
                    dp[r][c].add(prev_or | current_val)
            
            # Optimization: The number of unique OR values in a path is logarithmic 
            # relative to the maximum value in the grid because each new OR 
            # either stays the same or adds at least one bit.

    # The answer is the minimum value in the set at the target cell
    return min(dp[rows - 1][cols - 1])
