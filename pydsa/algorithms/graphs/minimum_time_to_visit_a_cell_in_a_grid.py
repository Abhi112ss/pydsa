METADATA = {
    "id": 2577,
    "name": "Minimum Time to Visit a Cell In a Grid",
    "slug": "minimum-time-to-visit-a-cell-in-a-grid",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "priority_queue", "graphs", "dijkstra"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * log(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum time to reach the bottom-right cell from the top-left cell in a grid where movement is restricted by cell values.",
}

import heapq

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum time to reach the bottom-right cell from the top-left cell.
    
    The time taken to move to an adjacent cell is determined by the value in the 
    target cell. If the current time is less than the cell's value, we must wait 
    until the time reaches the cell's value + 1.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The minimum time to reach the bottom-right cell, or -1 if unreachable.

    Examples:
        >>> solve([[0, 1, 1], [1, 1, 1], [1, 1, 0]])
        4
        >>> solve([[0, 2, 2], [2, 2, 2], [2, 2, 0]])
        -1
    """
    rows = len(grid)
    cols = len(grid[0])

    # If the neighbors of the starting cell are all blocked (value > 1), 
    # we can never move from (0, 0).
    if (rows > 1 or cols > 1) and grid[0][1] > 1 and grid[1][0] > 1:
        return -1

    # Min-priority queue for Dijkstra's: (current_time, row, col)
    priority_queue: list[tuple[int, int, int]] = [(0, 0, 0)]
    
    # Distance table to keep track of the minimum time to reach each cell
    min_time_to_cell: list[list[int]] = [[float('inf')] * cols for _ in range(rows)]
    min_time_to_cell[0][0] = 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while priority_queue:
        current_time, r, c = heapq.heappop(priority_queue)

        # If we reached the destination, return the time
        if r == rows - 1 and c == cols - 1:
            return current_time

        # If we found a better path to this cell already, skip
        if current_time > min_time_to_cell[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                # The cell value represents the minimum time required to enter it.
                # If current_time is already >= grid[nr][nc], we move in 1 step.
                # Otherwise, we must wait until time = grid[nr][nc], then move (total time = grid[nr][nc] + 1).
                # This can be simplified to: max(current_time + 1, grid[nr][nc] + 1)
                wait_time = max(current_time + 1, grid[nr][nc] + 1)

                if wait_time < min_time_to_cell[nr][nc]:
                    min_time_to_cell[nr][nc] = wait_time
                    heapq.heappush(priority_queue, (wait_time, nr, nc))

    return -1
