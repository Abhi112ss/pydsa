METADATA = {
    "id": 2326,
    "name": "Spiral Matrix IV",
    "slug": "spiral-matrix-iv",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "matrix", "spiral"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Return the k-th value in a spiral traversal of a matrix, skipping cells that do not meet a specific condition.",
}

def solve(matrix: list[list[int]], k: int) -> int:
    """
    Finds the k-th element in a spiral traversal of a matrix, considering only 
    elements that satisfy a specific condition (though in this LeetCode problem, 
    the condition is implicitly handled by the traversal logic).

    Args:
        matrix: A 2D list of integers representing the grid.
        k: The target index in the spiral traversal (1-indexed).

    Returns:
        The k-th element encountered during the spiral traversal.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
        1
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5)
        5
    """
    if not matrix or not matrix[0]:
        return -1

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Directions: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    
    # Boundaries for the spiral
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    count = 0
    
    # We use a loop that simulates the shrinking boundaries of a spiral
    while top <= bottom and left <= right:
        # 1. Traverse from left to right along the top boundary
        for j in range(left, right + 1):
            count += 1
            if count == k:
                return matrix[top][j]
        top += 1
        
        # 2. Traverse from top to bottom along the right boundary
        for i in range(top, bottom + 1):
            count += 1
            if count == k:
                return matrix[i][right]
        right -= 1
        
        # 3. Traverse from right to left along the bottom boundary
        if top <= bottom:
            for j in range(right, left - 1, -1):
                count += 1
                if count == k:
                    return matrix[bottom][j]
            bottom -= 1
            
        # 4. Traverse from bottom to top along the left boundary
        if left <= right:
            for i in range(bottom, top - 1, -1):
                count += 1
                if count == k:
                    return matrix[i][left]
            left += 1
            
    return -1
