METADATA = {
    "id": 2128,
    "name": "Remove All Ones With Row and Column Flips",
    "slug": "remove-all-ones-with-row-and-column-flips",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "greedy", "bit manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Determine if a binary matrix can be transformed into a zero matrix by flipping all bits in selected rows and columns.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a binary matrix can be cleared (all zeros) using row and column flips.

    A matrix can be cleared if and only if every row is either identical to the 
    first row or is the bitwise complement of the first row.

    Args:
        grid: A 2D list of integers (0 or 1) representing the matrix.

    Returns:
        True if the matrix can be cleared, False otherwise.

    Examples:
        >>> solve([[0, 1], [1, 0]])
        True
        >>> solve([[0, 1], [1, 1]])
        False
    """
    if not grid or not grid[0]:
        return True

    rows = len(grid)
    cols = len(grid[0])
    
    # The first row defines the pattern. 
    # Every subsequent row must either match this pattern exactly 
    # or be the exact inverse (complement) of this pattern.
    first_row = grid[0]

    for r in range(1, rows):
        is_same = True
        is_complement = True
        
        for c in range(cols):
            # Check if current row matches the first row
            if grid[r][c] != first_row[c]:
                is_same = False
            
            # Check if current row is the bitwise complement of the first row
            # (i.e., if first_row[c] is 0, grid[r][c] must be 1, and vice versa)
            if grid[r][c] == first_row[c]:
                is_complement = False
                
            # Optimization: if it's neither, this row breaks the possibility
            if not is_same and not is_complement:
                return False
                
    return True
