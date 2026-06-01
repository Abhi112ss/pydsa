METADATA = {
    "id": 1197,
    "name": "Minimum Knight Moves",
    "slug": "minimum-knight-moves",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "math", "shortest-path"],
    "difficulty": "hard",
    "time_complexity": "O(|x * y|)",
    "space_complexity": "O(|x * y|)",
    "description": "Find the minimum number of moves a knight requires to reach a target square (x, y) from (0, 0) on an infinite chessboard.",
}

from collections import deque

def solve(target_x: int, target_y: int) -> int:
    """
    Calculates the minimum number of moves for a knight to reach (target_x, target_y) from (0, 0).

    The problem is solved using Breadth-First Search (BFS) with symmetry optimization.
    Since the chessboard is infinite and symmetric, we can transform the target 
    coordinates to their absolute values to reduce the search space to the first quadrant.

    Args:
        target_x: The x-coordinate of the target square.
        target_y: The y-coordinate of the target square.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve(2, 1)
        1
        >>> solve(5, 5)
        4
    """
    # Use symmetry: (x, y), (-x, y), (x, -y), (-x, -y) are all equivalent.
    # We map everything to the first quadrant to minimize the state space.
    target_x, target_y = abs(target_x), abs(target_y)

    # Possible knight moves
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    # Queue stores (current_x, current_y, current_distance)
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        curr_x, curr_y, dist = queue.popleft()

        if curr_x == target_x and curr_y == target_y:
            return dist

        for dx, dy in directions:
            next_x, next_y = curr_x + dx, curr_y + dy

            # Optimization: Because we are targeting the first quadrant, 
            # we can allow the BFS to explore slightly into negative territory 
            # (specifically down to -2) to account for paths that "swing" around 
            # the origin to reach targets near (0,0) efficiently.
            if (next_x, next_y) not in visited and next_x >= -2 and next_y >= -2:
                visited.add((next_x, next_y))
                queue.append((next_x, next_y, dist + 1))

    return -1  # Should never be reached on an infinite board