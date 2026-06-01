METADATA = {
    "id": 576,
    "name": "Out of Boundary Paths",
    "slug": "out-of-boundary-paths",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(max_moves * m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the number of paths of a given length that go out of the boundary of a grid.",
}

def solve(m: int, n: int, max_moves: int, obstacle: list[list[int]]) -> int:
    """
    Args:
        m: Number of rows in the grid.
        n: Number of columns in the grid.
        max_moves: Maximum number of moves allowed.
        obstacle: A list of [row, col] coordinates representing obstacles.

    Returns:
        The number of paths that go out of the boundary modulo 10^9 + 7.
    """
    MODULO = 1_000_000_007
    obstacle_set = set()
    for r, c in obstacle:
        obstacle_set.add((r, c))

    dp = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if (r, c) not in obstacle_set:
                dp[r][c] = 1

    total_out_of_bounds = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(max_moves):
        new_dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if dp[r][c] == 0:
                    continue
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in obstacle_set:
                            new_dp[nr][nc] = (new_dp[nr][nc] + dp[r][c]) % MODULO
                    else:
                        total_out_of_bounds = (total_out_of_bounds + dp[r][c]) % MODULO
        dp = new_dp

    return total_out_of_bounds