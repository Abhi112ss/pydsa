METADATA = {
    "id": 1329,
    "name": "Sort the Matrix Diagonally",
    "slug": "sort-the-matrix-diagonally",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "hash_map", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n * log(min(m, n)))",
    "space_complexity": "O(m * n)",
    "description": "Sort the elements of a matrix along each of its diagonals in ascending order.",
}

def solve(mat: list[list[int]]) -> list[list[int]]:
    """
    Args:
        mat: A 2D list of integers representing the matrix.

    Returns:
        A 2D list of integers where each diagonal is sorted in ascending order.
    """
    rows = len(mat)
    cols = len(mat[0])
    diagonals = {}

    for r in range(rows):
        for c in range(cols):
            diagonal_id = r - c
            if diagonal_id not in diagonals:
                diagonals[diagonal_id] = []
            diagonals[diagonal_id].append(mat[r][c])

    for diagonal_id in diagonals:
        diagonals[diagonal_id].sort()

    diagonal_indices = {diagonal_id: 0 for diagonal_id in diagonals}

    for r in range(rows):
        for c in range(cols):
            diagonal_id = r - c
            mat[r][c] = diagonals[diagonal_id][diagonal_indices[diagonal_id]]
            diagonal_indices[diagonal_id] += 1

    return mat