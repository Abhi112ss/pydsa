METADATA = {
    "id": 1240,
    "name": "Tiling a Rectangle with the Fewest Squares",
    "slug": "tiling-a-rectangle-with-the-fewest-squares",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "dynamic_programming", "recursion"],
    "difficulty": "hard",
    "time_complexity": "O(exponential)",
    "space_complexity": "O(n * m)",
    "description": "Find the minimum number of squares needed to tile an n x m rectangle.",
}

def solve(n: int, m: int) -> int:
    """
    Finds the minimum number of squares needed to tile an n x m rectangle.

    Args:
        n: The height of the rectangle.
        m: The width of the rectangle.

    Returns:
        The minimum number of squares required to tile the rectangle.

    Examples:
        >>> solve(2, 3)
        3
        >>> solve(5, 8)
        5
    """
    # Ensure n is the smaller dimension to reduce search space slightly
    if n > m:
        n, m = m, n

    # grid[r][c] tracks if a cell is occupied
    grid = [[False for _ in range(m)] for _ in range(n)]
    
    # Initialize result with the worst case: n * m (all 1x1 squares)
    # Or more accurately, the area, but we use a large number for pruning.
    self_min_squares = n * m

    def backtrack(count: int) -> None:
        nonlocal self_min_squares

        # Pruning: if current count is already worse than best found, stop
        if count >= self_min_squares:
            return

        # Find the first empty cell (top-to-bottom, left-to-right)
        row_idx, col_idx = -1, -1
        found = False
        for r in range(n):
            for c in range(m):
                if not grid[r][c]:
                    row_idx, col_idx = r, c
                    found = True
                    break
            if found:
                break

        # If no empty cell is found, we have tiled the whole rectangle
        if not found:
            self_min_squares = min(self_min_squares, count)
            return

        # Determine the maximum possible square size that can fit at (row_idx, col_idx)
        # It must not exceed the rectangle boundaries or overlap existing squares
        max_size = 1
        while (row_idx + max_size < n and 
               col_idx + max_size < m and 
               all(not grid[row_idx + i][col_idx + j] 
                   for i in range(max_size + 1) 
                   for j in range(max_size + 1))):
            # The check above is slightly inefficient; let's refine the logic:
            # We check if the new square of size (max_size + 1) is valid.
            is_valid = True
            new_size = max_size + 1
            if row_idx + new_size <= n and col_idx + new_size <= m:
                for r in range(row_idx, row_idx + new_size):
                    for c in range(col_idx, col_idx + new_size):
                        if grid[r][c]:
                            is_valid = False
                            break
                    if not is_valid:
                        break
                if is_valid:
                    max_size = new_size
                else:
                    break
            else:
                break

        # Try placing squares of all possible sizes from largest to smallest
        # Trying larger squares first helps find a good upper bound quickly for pruning
        for size in range(max_size, 0, -1):
            # Mark the square as filled
            for r in range(row_idx, row_idx + size):
                for c in range(col_idx, col_idx + size):
                    grid[r][c] = True
            
            backtrack(count + 1)

            # Backtrack: unmark the square
            for r in range(row_idx, row_idx + size):
                for c in range(col_idx, col_idx + size):
                    grid[r][c] = False

    backtrack(0)
    return self_min_squares
