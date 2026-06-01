METADATA = {
    "id": 1631,
    "name": "Path With Minimum Effort",
    "slug": "path_with_minimum_effort",
    "category": "graph",
    "aliases": [],
    "tags": ["dijkstra", "binary_search", "graphs"],
    "difficulty": "hard",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V)",
    "description": "Find the minimum effort required to travel from top-left to bottom-right in a grid.",
}


def solve(heights: list[list[int]]) -> int:
    """Find the minimum effort required to travel from the top‑left corner to the
    bottom‑right corner of a grid.

    The effort of a path is defined as the maximum absolute difference in heights
    between two consecutive cells along the path. The goal is to minimise this
    maximum difference.

    Args:
        heights: A 2‑D list of non‑negative integers representing the height of each
            cell in the grid.

    Returns:
        The minimum possible effort (an integer) of any path from (0, 0) to the
        bottom‑right cell.

    Examples:
        >>> solve([[1,2,2],[3,8,2],[5,3,5]])
        2
        >>> solve([[1,2,3],[3,8,4],[5,3,5]])
        1
        >>> solve([[1,2,1],[1,2,1],[1,2,1]])
        0
    """
    import heapq

    if not heights or not heights[0]:
        return 0

    row_count: int = len(heights)
    col_count: int = len(heights[0])
    # distance matrix stores the best (minimum) effort found so far for each cell
    effort_to: list[list[int]] = [[float('inf')] * col_count for _ in range(row_count)]
    effort_to[0][0] = 0

    # priority queue stores (current_effort, row, col)
    priority_queue: list[tuple[int, int, int]] = [(0, 0, 0)]

    # directions for the four adjacent neighbours
    neighbour_offsets: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while priority_queue:
        current_effort, row, col = heapq.heappop(priority_queue)

        # If we have reached the target cell, its effort is optimal
        if row == row_count - 1 and col == col_count - 1:
            return current_effort

        # Skip processing if a better effort was already recorded
        if current_effort > effort_to[row][col]:
            continue

        for d_row, d_col in neighbour_offsets:
            next_row: int = row + d_row
            next_col: int = col + d_col

            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                edge_effort: int = abs(heights[next_row][next_col] - heights[row][col])
                # The effort to reach the neighbour is the maximum of the current path effort
                # and the edge we are about to traverse.
                next_effort: int = max(current_effort, edge_effort)

                if next_effort < effort_to[next_row][next_col]:
                    effort_to[next_row][next_col] = next_effort
                    heapq.heappush(priority_queue, (next_effort, next_row, next_col))

    # The loop always returns upon reaching the target; this line is unreachable.
    return effort_to[row_count - 1][col_count - 1]