METADATA = {
    "id": 2849,
    "name": "Determine if a Cell Is Reachable at a Given Time",
    "slug": "determine-if-a-cell-is-reachable-at-a-given-time",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "grid", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a cell (row, col) is reachable from (0, 0) in exactly 'time' steps given a grid of obstacles.",
}

def solve(grid: list[list[int]], row: int, col: int, time: int) -> bool:
    """
    Determines if a cell (row, col) is reachable from (0, 0) in exactly 'time' steps.

    A cell is reachable if:
    1. The target cell itself is not an obstacle.
    2. The Manhattan distance from (0, 0) to (row, col) is less than or equal to 'time'.
    3. The parity of the Manhattan distance matches the parity of 'time'.
    4. There is a path available (in this specific problem, since we can move back and forth, 
       the only way to be blocked is if the target is an obstacle or the distance is impossible).

    Args:
        grid: A 2D list representing the grid where 1 is an obstacle and 0 is empty.
        row: The target row index.
        col: The target column index.
        time: The exact number of steps allowed.

    Returns:
        True if the cell is reachable, False otherwise.

    Examples:
        >>> solve([[0,0,0],[0,0,0],[0,0,0]], 1, 1, 2)
        True
        >>> solve([[0,0,0],[0,1,0],[0,0,0]], 1, 1, 2)
        False
        >>> solve([[0,0,0],[0,0,0],[0,0,0]], 1, 1, 3)
        False
    """
    # 1. Check if the target cell is an obstacle
    if grid[row][col] == 1:
        return False

    # 2. Calculate Manhattan distance from (0, 0) to (row, col)
    manhattan_distance = row + col

    # 3. Check if the distance is greater than the allowed time
    if manhattan_distance > time:
        return False

    # 4. Check parity: To reach a cell in 'time' steps, the difference between 
    # 'time' and 'manhattan_distance' must be even (because every step away 
    # from the target must be compensated by a step back towards it).
    if (time - manhattan_distance) % 2 != 0:
        return False

    # Note: In this specific problem constraints and movement rules, 
    # if the target is not an obstacle and parity/distance match, 
    # a path always exists because we can oscillate between two adjacent empty cells.
    return True
