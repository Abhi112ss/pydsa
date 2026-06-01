METADATA = {
    "id": 2679,
    "name": "Sum in a Matrix",
    "slug": "sum_in_a_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "array"],
    "difficulty": "Easy",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(1)",
    "description": "Return the sum of all elements in the given matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """Calculate the total sum of all integers in a 2D matrix.

    Args:
        matrix: A list of lists where each inner list represents a row of integers.

    Returns:
        The sum of every integer present in the matrix.

    Examples:
        >>> solve([[1,2,3],[4,5,6]])
        21
        >>> solve([[0]])
        0
    """
    total_sum = 0
    for row in matrix:
        for value in row:
            total_sum += value  # accumulate each element
    return total_sum