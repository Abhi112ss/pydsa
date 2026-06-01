METADATA = {
    "id": 1901,
    "name": "Find a Peak Element II",
    "slug": "find-a-peak-element-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m log n)",
    "space_complexity": "O(1)",
    "description": "Find a peak element in a 2D matrix where a peak is an element strictly greater than its adjacent neighbors.",
}

def solve(mat: list[list[int]]) -> int:
    """
    Finds the coordinates of a peak element in a 2D matrix.
    
    A peak element is an element that is strictly greater than its 
    immediate neighbors (up, down, left, right).
    
    The algorithm uses binary search on columns to achieve O(m log n) time complexity,
    where m is the number of rows and n is the number of columns.

    Args:
        mat: A 2D list of integers representing the matrix.

    Returns:
        A list of two integers [row, col] representing the coordinates of a peak.

    Examples:
        >>> solve([[1,4],[3,2]])
        [0, 1]
        >>> solve([[10,20,15],[21,30,14],[7,16,32]])
        [1, 1]
    """
    rows = len(mat)
    cols = len(mat[0])
    
    low_col = 0
    high_col = cols - 1
    
    while low_col <= high_col:
        mid_col = (low_col + high_col) // 2
        
        # Find the row index of the maximum element in the current middle column.
        # This ensures that the element is greater than its top and bottom neighbors.
        max_row_idx = 0
        for row_idx in range(rows):
            if mat[row_idx][mid_col] > mat[max_row_idx][mid_col]:
                max_row_idx = row_idx
        
        # Check left and right neighbors to determine the search direction.
        # We treat out-of-bounds as negative infinity.
        left_val = mat[max_row_idx][mid_col - 1] if mid_col > 0 else -1
        right_val = mat[max_row_idx][mid_col + 1] if mid_col < cols - 1 else -1
        
        current_val = mat[max_row_idx][mid_col]
        
        if current_val > left_val and current_val > right_val:
            # Found a peak: it's greater than top/bottom (by max selection)
            # and greater than left/right (by this check).
            return [max_row_idx, mid_col]
        elif left_val > current_val:
            # If the left neighbor is larger, a peak must exist in the left half.
            high_col = mid_col - 1
        else:
            # If the right neighbor is larger, a peak must exist in the right half.
            low_col = mid_col + 1
            
    return [-1, -1]
