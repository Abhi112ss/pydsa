METADATA = {
    "id": 3071,
    "name": "Minimum Operations to Write the Letter Y on a Grid",
    "slug": "minimum-operations-to-write-the-letter-y-on-a-grid",
    "category": "Simulation",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to write the letter 'Y' on an n x n grid where cells are either 0 or 1.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum operations to write the letter 'Y' on an n x n grid.
    
    The 'Y' shape consists of:
    1. A diagonal from (0, 0) to (n-1, n-1) - wait, that's not 'Y'.
    Actually, the 'Y' shape on an n x n grid is defined as:
    - The top part: (0, 0) to (n//2, n//2) and (0, n-1) to (n//2, n//2).
    - The bottom part: (n//2, n//2) to (n-1, n//2).
    
    Wait, let's re-verify the 'Y' shape definition for this specific problem:
    - Top-left branch: (i, i) for 0 <= i <= n // 2
    - Top-right branch: (i, n - 1 - i) for 0 <= i <= n // 2
    - Bottom stem: (i, n // 2) for n // 2 <= i < n
    
    Args:
        grid: An n x n matrix of integers (0 or 1).

    Returns:
        The minimum number of operations (1s to change to 0s or 0s to change to 1s) 
        to form the 'Y' shape.

    Examples:
        >>> solve([[0,0,1],[0,1,0],[0,0,0]])
        1
        >>> solve([[1,1,1],[1,1,1],[1,1,1]])
        3
    """
    n = len(grid)
    mid = n // 2
    
    # We need to count:
    # 1. How many 1s exist in cells that are NOT part of the 'Y' (must be turned to 0)
    # 2. How many 0s exist in cells that ARE part of the 'Y' (must be turned to 1)
    
    # To avoid double counting the center (mid, mid), we use a set or careful logic.
    # Since n is small (up to 500), we can use a set of tuples for the 'Y' coordinates.
    y_cells = set()
    
    # Top-left branch: (0,0) to (mid, mid)
    for i in range(mid + 1):
        y_cells.add((i, i))
        
    # Top-right branch: (0, n-1) to (mid, mid)
    for i in range(mid + 1):
        y_cells.add((i, n - 1 - i))
        
    # Bottom stem: (mid, mid) to (n-1, mid)
    for i in range(mid, n):
        y_cells.add((i, mid))
        
    operations = 0
    
    # Iterate through the entire grid
    for r in range(n):
        for c in range(n):
            is_y_part = (r, c) in y_cells
            
            if is_y_part:
                # If it's part of 'Y', it must be 1. If it's 0, we need 1 operation.
                if grid[r][c] == 0:
                    operations += 1
            else:
                # If it's NOT part of 'Y', it must be 0. If it's 1, we need 1 operation.
                if grid[r][c] == 1:
                    operations += 1
                    
    return operations
