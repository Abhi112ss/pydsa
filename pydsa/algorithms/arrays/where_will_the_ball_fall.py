METADATA = {
    "id": 1706,
    "name": "Where Will the Ball Fall",
    "slug": "where_will_the_ball_fall",
    "category": "array",
    "aliases": [],
    "tags": ["simulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Simulate balls rolling through a diagonal grid to determine their exit columns.",
}


def solve(grid: list[list[int]]) -> list[int]:
    """Simulate each ball's path through a diagonal grid.

    Args:
        grid: A 2‑D list of integers where each element is either 1 (down‑right slope)
              or -1 (down‑left slope). The grid has m rows and n columns.

    Returns:
        A list of length n where the i‑th element is the column index where the ball
        dropped from column i exits the bottom of the grid, or -1 if the ball gets
        stuck.

    Examples:
        >>> solve([[1,1,-1,-1],[1,1,-1,-1],[-1,-1,1,1],[-1,-1,1,1]])
        [1, -1, -1, 0]
        >>> solve([[1,1],[-1,-1]])
        [-1, -1]
    """
    row_count: int = len(grid)
    col_count: int = len(grid[0]) if row_count > 0 else 0
    exit_columns: list[int] = [-1] * col_count

    for start_col in range(col_count):
        current_col: int = start_col
        for row in range(row_count):
            direction: int = grid[row][current_col]
            next_col: int = current_col + direction

            # Ball hits the side wall → stuck
            if next_col < 0 or next_col >= col_count:
                current_col = -1
                break

            # Ball encounters a V‑shaped obstacle → stuck
            if grid[row][next_col] != direction:
                current_col = -1
                break

            # Move ball to the next cell
            current_col = next_col

        if current_col != -1:
            exit_columns[start_col] = current_col

    return exit_columns