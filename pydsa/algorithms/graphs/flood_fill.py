METADATA = {
    "id": 733,
    "name": "Flood Fill",
    "slug": "flood-fill",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Change the color of a starting pixel and all its connected pixels of the same color to a new color.",
}

def solve(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """
    Args:
        image: A 2D grid representing pixel colors.
        sr: The starting row index.
        sc: The starting column index.
        color: The new color to apply.

    Returns:
        The modified image after the flood fill operation.
    """
    rows_count = len(image)
    cols_count = len(image[0])
    original_color = image[sr][sc]

    if original_color == color:
        return image

    def perform_dfs(row: int, col: int) -> None:
        if row < 0 or row >= rows_count or col < 0 or col >= cols_count:
            return
        if image[row][col] != original_color:
            return

        image[row][col] = color

        perform_dfs(row + 1, col)
        perform_dfs(row - 1, col)
        perform_dfs(row, col + 1)
        perform_dfs(row, col - 1)

    perform_dfs(sr, sc)
    return image