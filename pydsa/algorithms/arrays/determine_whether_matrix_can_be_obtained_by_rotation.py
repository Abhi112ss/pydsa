METADATA = {
    "id": 1886,
    "name": "Determine Whether Matrix Can Be Obtained By Rotation",
    "slug": "determine_whether_matrix_can_be_obtained_by_rotation",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["arrays", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Check if a target matrix can be obtained by rotating the given matrix 0, 90, 180, or 270 degrees clockwise.",
}


def solve(matrix: list[list[int]], target: list[list[int]]) -> bool:
    """Determine whether the target matrix can be obtained by rotating the input matrix.

    Args:
        matrix: A 2‑D list representing the original matrix.
        target: A 2‑D list representing the matrix to compare against.

    Returns:
        True if the target matrix equals the original matrix after 0, 1, 2, or 3 clockwise
        90° rotations; otherwise False.

    Examples:
        >>> solve([[1,2],[3,4]], [[3,1],[4,2]])
        True
        >>> solve([[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]])
        True
        >>> solve([[1,2],[3,4]], [[1,4],[2,3]])
        False
    """
    def rotate_clockwise(mat: list[list[int]]) -> list[list[int]]:
        """Return a new matrix rotated 90 degrees clockwise."""
        rows, cols = len(mat), len(mat[0])
        # New matrix has dimensions cols x rows
        return [
            [mat[rows - 1 - row][col] for row in range(rows)]
            for col in range(cols)
        ]

    current = matrix
    for _ in range(4):
        if current == target:
            return True
        # Rotate for the next iteration
        current = rotate_clockwise(current)
    return False