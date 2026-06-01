METADATA = {
    "id": 2428,
    "name": "Maximum Sum of an Hourglass",
    "slug": "maximum-sum-of-an-hourglass",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "matrix", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of an hourglass shape within a 2D grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum sum of an hourglass pattern in a 2D grid.
    
    An hourglass pattern in a 2D array is a subset of values shaped like:
    a b c
      d
    e f g

    Args:
        grid: A 2D list of integers representing the matrix.

    Returns:
        The maximum sum found among all possible hourglasses in the grid.

    Examples:
        >>> solve([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,0]])
        9
        >>> solve([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        70
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # An hourglass requires at least a 3x3 area.
    # If the grid is smaller than 3x3, no hourglass can be formed.
    if rows < 3 or cols < 3:
        return 0

    max_sum = float('-inf')

    # Iterate through all possible top-left corners (r, c) of a 3x3 hourglass.
    # The range is limited to (rows - 2) and (cols - 2) to prevent index out of bounds.
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Calculate the sum of the 7 elements forming the hourglass:
            # Top row: (r, c), (r, c+1), (r, c+2)
            # Middle: (r+1, c+1)
            # Bottom row: (r+2, c), (r+2, c+1), (r+2, c+2)
            current_hourglass_sum = (
                grid[r][c] + grid[r][c + 1] + grid[r][c + 2] +
                grid[r + 1][c + 1] +
                grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]
            )
            
            # Update the global maximum sum found so far.
            if current_hourglass_sum > max_sum:
                max_sum = current_hourglass_sum

    return int(max_sum)
