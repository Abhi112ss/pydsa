METADATA = {
    "id": 1428,
    "name": "Leftmost Column with at Least a One",
    "slug": "leftmost_column_with_at_least_a_one",
    "category": "binary_search",
    "aliases": [],
    "tags": ["binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(m * log n)",
    "space_complexity": "O(1)",
    "description": "Find the leftmost column index that contains at least a one in a row-wise sorted binary matrix.",
}

from typing import Protocol, List, Tuple


class BinaryMatrix(Protocol):
    def get(self, row: int, col: int) -> int:
        ...

    def dimensions(self) -> Tuple[int, int]:
        ...


def solve(binary_matrix: BinaryMatrix) -> int:
    """Find the leftmost column with at least a one using binary search.

    Args:
        binary_matrix: An object adhering to the BinaryMatrix protocol. The matrix
            has dimensions m x n where each row is sorted in non‑decreasing order
            (all 0's precede 1's).

    Returns:
        The index of the leftmost column containing a 1, or -1 if no such column exists.

    Examples:
        >>> class SimpleMatrix:
        ...     def __init__(self, data):
        ...         self._data = data
        ...     def get(self, r, c):
        ...         return self._data[r][c]
        ...     def dimensions(self):
        ...         return len(self._data), len(self._data[0])
        >>> mat = SimpleMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])
        >>> solve(mat)
        1
        >>> mat2 = SimpleMatrix([[0,0],[0,0]])
        >>> solve(mat2)
        -1
    """
    row_count, col_count = binary_matrix.dimensions()
    left = 0
    right = col_count - 1
    answer = -1

    # Binary search over column indices.
    while left <= right:
        mid = (left + right) // 2
        # Check if any row has a 1 at column mid (or to the left, due to sorting).
        found_one = False
        for row_index in range(row_count):
            if binary_matrix.get(row_index, mid) == 1:
                found_one = True
                break
        if found_one:
            answer = mid          # possible better (more left) column
            right = mid - 1       # continue searching left side
        else:
            left = mid + 1        # discard left side, search right side

    return answer