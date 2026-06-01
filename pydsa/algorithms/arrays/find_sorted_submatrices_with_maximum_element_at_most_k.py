METADATA = {
    "id": 3359,
    "name": "Find Sorted Submatrices With Maximum Element at Most K",
    "slug": "find_sorted_submatrices_with_maximum_element_at_most_k",
    "category": "array",
    "aliases": [],
    "tags": ["two_pointer", "prefix_sum", "2d_array"],
    "difficulty": "medium",
    "time_complexity": "O(m^2 * n)",
    "space_complexity": "O(m * n)",
    "description": "Count submatrices whose maximum element does not exceed K in a row‑ and column‑sorted matrix.",
}


import sys
from typing import List


def solve() -> None:
    """Read a matrix and integer K, then print the number of submatrices whose
    maximum element is at most K.

    The input format is:
        m n K
        a_11 a_12 ... a_1n
        ...
        a_m1 a_m2 ... a_mn

    Args:
        None (reads from standard input).

    Returns:
        None (writes the answer to standard output).

    Example:
        >>> # input
        >>> # 3 3 5
        >>> # 1 2 3
        >>> # 2 3 4
        >>> # 3 4 5
        >>> # output
        >>> # 18
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    rows = int(next(it))
    cols = int(next(it))
    k = int(next(it))

    # Build binary matrix where 1 indicates value <= K
    binary: List[List[int]] = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            value = int(next(it))
            binary[i][j] = 1 if value <= k else 0

    # Prefix sums per column to allow O(1) query of number of valid cells
    # between any two rows for a fixed column.
    prefix: List[List[int]] = [[0] * cols for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix[r + 1][c] = prefix[r][c] + binary[r][c]

    total_submatrices = 0
    # Iterate over all pairs of top and bottom rows.
    for top in range(rows):
        for bottom in range(top, rows):
            height = bottom - top + 1
            consecutive_valid = 0
            # Scan columns, using sliding window to count contiguous
            # segments where every cell in the current row range is <= K.
            for c in range(cols):
                valid_in_column = prefix[bottom + 1][c] - prefix[top][c] == height
                if valid_in_column:
                    consecutive_valid += 1
                    total_submatrices += consecutive_valid
                else:
                    consecutive_valid = 0

    print(total_submatrices)
