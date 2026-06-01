METADATA = {
    "id": 1351,
    "name": "Count Negative Numbers in a Sorted Matrix",
    "slug": "count_negative_numbers_in_a_sorted_matrix",
    "category": "array",
    "aliases": [],
    "tags": ["binary_search", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
    "description": "Count the number of negative numbers in a row- and column-wise sorted matrix.",
}


def solve(matrix: list[list[int]]) -> int:
    """Count negative numbers in a matrix sorted in non‑increasing order both row‑wise and column‑wise.

    Args:
        matrix: A list of lists of integers where each row and each column is sorted
                in non‑increasing order (i.e., from largest to smallest).

    Returns:
        The total count of negative integers present in the matrix.

    Examples:
        >>> solve([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
        8
        >>> solve([[3,2],[1,0]])
        0
        >>> solve([[-1]])
        1
    """
    if not matrix or not matrix[0]:
        return 0

    row_count: int = len(matrix)
    col_count: int = len(matrix[0])
    row_index: int = 0
    col_index: int = col_count - 1
    negative_total: int = 0

    # Traverse from the top‑right corner moving only left or down.
    while row_index < row_count and col_index >= 0:
        if matrix[row_index][col_index] < 0:
            # All elements below this cell in the current column are also negative.
            negative_total += row_count - row_index
            col_index -= 1  # Move left to check the next column.
        else:
            row_index += 1  # Move down to find the first negative in this column.

    return negative_total