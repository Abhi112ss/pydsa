METADATA = {
    "id": 1284,
    "name": "Minimum Number of Flips to Convert Binary Matrix to Zero Matrix",
    "slug": "minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "bitmask", "matrix", "backtracking"],
    "difficulty": "hard",
    "time_complexity": "O(2^(m*n) * m*n)",
    "space_complexity": "O(2^(m*n))",
    "description": "Find the minimum number of flips required to transform a binary matrix into a zero matrix using BFS.",
}

from collections import deque

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the minimum number of flips to convert a binary matrix to a zero matrix.
    
    Each flip operation toggles all elements in a specific row or column.
    This implementation uses BFS to find the shortest path in the state space.

    Args:
        matrix: A 2D list of integers representing the binary matrix.

    Returns:
        The minimum number of flips required, or -1 if it is impossible.

    Examples:
        >>> solve([[1, 0], [0, 1]])
        2
        >>> solve([[1, 1], [1, 1]])
        2
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Convert the 2D matrix into a single integer bitmask for efficient state tracking
    def matrix_to_mask(mat: list[list[int]]) -> int:
        mask = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    mask |= (1 << (r * cols + c))
        return mask

    target_mask = 0
    start_mask = matrix_to_mask(matrix)
    
    if start_mask == target_mask:
        return 0

    # Precompute masks for flipping each row and each column
    row_masks = []
    for r in range(rows):
        mask = 0
        for c in range(cols):
            mask |= (1 << (r * cols + c))
        row_masks.append(mask)
        
    col_masks = []
    for c in range(cols):
        mask = 0
        for r in range(rows):
            mask |= (1 << (r * cols + c))
        col_masks.append(mask)

    # BFS initialization
    queue = deque([(start_mask, 0)])
    visited = {start_mask}

    while queue:
        current_mask, dist = queue.popleft()

        # Try flipping every possible row
        for r_mask in row_masks:
            next_mask = current_mask ^ r_mask
            if next_mask == target_mask:
                return dist + 1
            if next_mask not in visited:
                visited.add(next_mask)
                queue.append((next_mask, dist + 1))

        # Try flipping every possible column
        for c_mask in col_masks:
            next_mask = current_mask ^ c_mask
            if next_mask == target_mask:
                return dist + 1
            if next_mask not in visited:
                visited.add(next_mask)
                queue.append((next_mask, dist + 1))

    return -1
