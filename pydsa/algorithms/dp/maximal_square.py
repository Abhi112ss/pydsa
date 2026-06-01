METADATA = {
    "id": 221,
    "name": "Maximal Square",
    "slug": "maximal-square",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the largest square containing only 1's in a binary matrix and return its area.",
}

def solve(matrix: list[list[str]]) -> int:
    """
    Args:
        matrix: A 2D list of strings representing a binary matrix.

    Returns:
        The area of the largest square containing only 1's.
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if matrix[r - 1][c - 1] == "1":
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                if dp[r][c] > max_side:
                    max_side = dp[r][c]

    return max_side * max_side