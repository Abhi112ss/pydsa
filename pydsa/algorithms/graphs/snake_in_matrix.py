METADATA = {
    "id": 3248,
    "name": "Snake in Matrix",
    "slug": "snake_in_matrix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "matrix", "backtracking", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the length of the longest snake-like path in a matrix following specific directional constraints.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Args:
        grid: A 2D list of integers representing the matrix.

    Returns:
        The length of the longest snake-like path.
    """
    rows = len(grid)
    cols = len(grid[0])
    memo = {}

    def get_max_path(row: int, col: int, direction: int) -> int:
        state = (row, col, direction)
        if state in memo:
            return memo[state]

        max_len = 1
        
        if direction == 0:
            next_directions = [1, 2]
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        elif direction == 1:
            next_directions = [2, 3]
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        elif direction == 2:
            next_directions = [3, 0]
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        else:
            next_directions = [0, 1]
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dr, dc = moves[direction]
        nr, nc = row + dr, col + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[row][col]:
            for next_dir in next_directions:
                max_len = max(max_len, 1 + get_max_path(nr, nc, next_dir))

        memo[state] = max_len
        return max_len

    overall_max = 0
    for r in range(rows):
        for c in range(cols):
            for d in range(4):
                overall_max = max(overall_max, get_max_path(r, c, d))

    return overall_max