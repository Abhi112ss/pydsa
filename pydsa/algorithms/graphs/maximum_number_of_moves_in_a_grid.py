METADATA = {
    "id": 2684,
    "name": "Maximum Number of Moves in a Grid",
    "slug": "maximum-number-of-moves-in-a-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "dynamic_programming", "memoization"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum number of moves possible in a grid starting from (0, 0) following specific movement rules.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum number of moves possible in a grid starting from (0, 0).
    
    A move is valid if the next cell is in one of the 8 directions and its value 
    is strictly greater than the current cell's value.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The maximum number of moves possible.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        8
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        0
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # memo[r][c] stores the max moves possible starting from cell (r, c)
    memo: list[list[int]] = [[-1 for _ in range(cols)] for _ in range(rows)]

    def dfs(r: int, c: int) -> int:
        # If we have already computed the result for this cell, return it
        if memo[r][c] != -1:
            return memo[r][c]

        max_moves = 0
        current_val = grid[r][c]

        # Explore all 8 directions: horizontal, vertical, and diagonal
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                nr, nc = r + dr, c + dc

                # Check boundaries and the strictly increasing condition
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > current_val:
                    # The moves from current cell is 1 + moves from the next cell
                    max_moves = max(max_moves, 1 + dfs(nr, nc))

        memo[r][c] = max_moves
        return max_moves

    return dfs(0, 0)
