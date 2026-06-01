METADATA = {
    "id": 1727,
    "name": "Largest Submatrix With Rearrangements",
    "slug": "largest-submatrix-with-rearrangements",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(m * n log n)",
    "space_complexity": "O(m * n)",
    "description": "Find the largest submatrix area possible by rearranging columns for each row.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Calculates the area of the largest submatrix possible by rearranging columns.

    The algorithm processes each row by calculating the number of consecutive 
    ones ending at each column (treating it like a histogram height). 
    For each row, we sort these heights in descending order to maximize 
    the potential area of a rectangle starting at that row.

    Args:
        matrix: A 2D list of integers (0s and 1s).

    Returns:
        The area of the largest submatrix.

    Examples:
        >>> solve([[0,0,0,1,0],[0,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0]])
        3
        >>> solve([[1,0,1],[1,1,0],[1,1,0]])
        4
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0

    # heights[r][c] will store the number of consecutive 1s 
    # ending at matrix[r][c] looking upwards.
    heights = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                # If current cell is 1, increment height from the cell above
                if r == 0:
                    heights[r][c] = 1
                else:
                    heights[r][c] = heights[r - 1][c] + 1
            else:
                heights[r][c] = 0

    for r in range(rows):
        # Create a copy of the current row's heights to sort independently
        # Sorting allows us to rearrange columns to form the largest possible rectangle
        current_row_heights = sorted(heights[r], reverse=True)
        
        for i in range(cols):
            # The width of the rectangle is (i + 1)
            # The height is the smallest height in the sorted sequence up to index i
            # Since it's sorted descending, current_row_heights[i] is the minimum height
            current_area = current_row_heights[i] * (i + 1)
            if current_area > max_area:
                max_area = current_area

    return max_area
