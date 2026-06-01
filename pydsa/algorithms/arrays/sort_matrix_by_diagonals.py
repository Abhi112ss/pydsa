METADATA = {
    "id": 3446,
    "name": "Sort Matrix by Diagonals",
    "slug": "sort-matrix-by-diagonals",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "arrays", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 log n)",
    "space_complexity": "O(n^2)",
    "description": "Sort elements in the bottom-left diagonals in descending order and top-right diagonals in ascending order.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Sorts the diagonals of a square matrix based on their position.
    
    Bottom-left diagonals (where row index >= col index) are sorted in descending order.
    Top-right diagonals (where row index < col index) are sorted in ascending order.

    Args:
        grid: A square 2D list of integers.

    Returns:
        The modified grid with sorted diagonals.

    Examples:
        >>> solve([[1, 7, 3], [9, 8, 2], [4, 5, 6]])
        [[1, 2, 3], [4, 8, 7], [9, 5, 6]]
    """
    n = len(grid)
    # Dictionary to group elements by their diagonal identifier (row - col)
    # Elements on the same diagonal share the same (i - j) value.
    diagonals: dict[int, list[int]] = {}

    for r in range(n):
        for c in range(n):
            diff = r - c
            if diff not in diagonals:
                diagonals[diff] = []
            diagonals[diff].append(grid[r][c])

    # Sort each diagonal group according to the problem rules
    for diff in diagonals:
        if diff >= 0:
            # Bottom-left diagonals (including main diagonal) -> Descending
            diagonals[diff].sort(reverse=True)
        else:
            # Top-right diagonals -> Ascending
            diagonals[diff].sort()

    # Reconstruct the grid using the sorted values
    # We use a pointer/index tracker for each diagonal to pop elements efficiently
    # or simply use a dictionary of iterators.
    diagonal_iterators = {diff: iter(vals) for diff, vals in diagonals.items()}

    for r in range(n):
        for c in range(n):
            diff = r - c
            grid[r][c] = next(diagonal_iterators[diff])

    return grid
