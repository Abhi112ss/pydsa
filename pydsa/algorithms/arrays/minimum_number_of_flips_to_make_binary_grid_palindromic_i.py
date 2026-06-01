METADATA = {
    "id": 3239,
    "name": "Minimum Number of Flips to Make Binary Grid Palindromic I",
    "slug": "minimum-number-of-flips-to-make-binary-grid-palindromic-i",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of flips required to make a binary grid palindromic by comparing symmetric elements.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum number of flips to make a binary grid palindromic.
    
    A grid is palindromic if grid[i][j] == grid[m-1-i][n-1-j] for all i, j.
    The problem asks for the minimum flips to satisfy this condition.
    
    Args:
        grid: A 2D list of integers (0 or 1) representing the binary grid.
        
    Returns:
        The minimum number of flips required.
        
    Examples:
        >>> solve([[0, 1], [1, 0]])
        0
        >>> solve([[1, 1], [1, 0]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])
    flips = 0
    
    # We only need to iterate through half of the total elements to avoid double counting.
    # The total number of elements is rows * cols.
    total_elements = rows * cols
    
    # Iterate through the first half of the flattened grid indices.
    # For each element at index k, its symmetric counterpart is at (total_elements - 1 - k).
    for k in range(total_elements // 2):
        # Convert flat index k back to 2D coordinates (r1, c1)
        r1, c1 = divmod(k, cols)
        
        # Convert symmetric flat index back to 2D coordinates (r2, c2)
        # The symmetric element is at (rows - 1 - r1, cols - 1 - c1)
        r2, c2 = rows - 1 - r1, cols - 1 - c1
        
        # If the symmetric elements are not equal, one flip is required to make them match.
        if grid[r1][c1] != grid[r2][c2]:
            flips += 1
            
    return flips
