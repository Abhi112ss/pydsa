METADATA = {
    "id": 3459,
    "name": "Length of Longest V-Shaped Diagonal Segment",
    "slug": "length_of_longest_v_shaped_diagonal_segment",
    "category": "array",
    "aliases": [],
    "tags": ["dfs", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(n*m)",
    "description": "Find the maximum length of a V‑shaped diagonal segment consisting only of 1's in a binary matrix.",
}


import sys
from typing import List


def solve() -> None:
    """
    Reads a binary matrix from standard input and prints the length of the longest
    V‑shaped diagonal segment formed entirely of 1's.

    The input format:
    - The first line contains two integers n and m (the number of rows and columns).
    - The next n lines each contain m integers (0 or 1) separated by spaces.

    Returns:
        None. The result is printed to standard output.

    Example:
        Input:
            4 5
            1 0 1 1 1
            1 1 0 1 0
            1 1 1 0 1
            0 1 1 1 1
        Output:
            5
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    rows = int(next(it))
    cols = int(next(it))
    matrix: List[List[int]] = [[int(next(it)) for _ in range(cols)] for _ in range(rows)]

    # dl[i][j] = length of consecutive 1's on the down‑left diagonal starting at (i, j)
    # dr[i][j] = length of consecutive 1's on the down‑right diagonal starting at (i, j)
    dl: List[List[int]] = [[0] * cols for _ in range(rows)]
    dr: List[List[int]] = [[0] * cols for _ in range(rows)]

    # Fill dl and dr from bottom to top so that we can use previously computed values
    for i in range(rows - 1, -1, -1):
        for j in range(cols):
            if matrix[i][j] == 1:
                # down‑left: move to (i+1, j-1) if inside bounds
                if i + 1 < rows and j - 1 >= 0:
                    dl[i][j] = 1 + dl[i + 1][j - 1]
                else:
                    dl[i][j] = 1
                # down‑right: move to (i+1, j+1) if inside bounds
                if i + 1 < rows and j + 1 < cols:
                    dr[i][j] = 1 + dr[i + 1][j + 1]
                else:
                    dr[i][j] = 1
            else:
                dl[i][j] = 0
                dr[i][j] = 0

    max_length = 0
    for i in range(rows):
        for j in range(cols):
            arm_len = min(dl[i][j], dr[i][j])
            if arm_len > 0:
                # V length = 2 * arm_len - 1 (apex counted once)
                candidate = 2 * arm_len - 1
                if candidate > max_length:
                    max_length = candidate

    print(max_length)
