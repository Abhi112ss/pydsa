METADATA = {
    "id": 2174,
    "name": "Remove All Ones With Row and Column Flips II",
    "slug": "remove-all-ones-with-row-and-column-flips-ii",
    "category": "Matrix",
    "aliases": [],
    "tags": ["greedy", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Determine if it is possible to make all elements in a binary matrix zero by flipping rows and columns.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a binary matrix can be transformed into all zeros using row and column flips.

    The core logic relies on the fact that the first row's state dictates which columns 
    must be flipped to clear the first row. Once the columns are fixed, the remaining 
    rows must be flipped if their first element is 1 to attempt to clear the row. 
    Finally, we verify if the entire matrix is zero.

    Args:
        grid: A 2D list of integers (0 or 1) representing the matrix.

    Returns:
        True if the matrix can be cleared, False otherwise.

    Examples:
        >>> solve([[0, 1], [1, 0]])
        True
        >>> solve([[1, 1], [1, 1]])
        True
        >>> solve([[0, 1], [1, 1]])
        False
    """
    rows = len(grid)
    cols = len(grid[0])

    # Step 1: Determine which columns must be flipped.
    # A column must be flipped if the element in the first row is 1.
    # We use a boolean array to track column flip states to keep space O(cols) 
    # or we can conceptually treat it as O(1) extra space relative to the input if we 
    # were allowed to modify the grid, but here we use a small auxiliary list.
    col_flips = [False] * cols
    for j in range(cols):
        if grid[0][j] == 1:
            col_flips[j] = True

    # Step 2: Determine which rows must be flipped.
    # After deciding column flips, a row must be flipped if its first element 
    # (after accounting for the column flip) is 1.
    row_flips = [False] * rows
    for i in range(rows):
        # Check the first element of the row after applying the column flip
        # If grid[i][0] is 1 and col_flips[0] is True, it becomes 0.
        # If grid[i][0] is 1 and col_flips[0] is False, it stays 1.
        # Effectively: current_val = grid[i][0] ^ col_flips[0]
        current_val = grid[i][0]
        if col_flips[0]:
            current_val = 1 - current_val
        
        if current_val == 1:
            row_flips[i] = True

    # Step 3: Verify if the entire matrix becomes zero under these flips.
    # For every cell (i, j), the final value is:
    # grid[i][j] XOR row_flip[i] XOR col_flip[j]
    # We want this to be 0 for all i, j.
    for i in range(rows):
        for j in range(cols):
            # Calculate the state of the cell after applying row and column flips
            val = grid[i][j]
            if row_flips[i]:
                val = 1 - val
            if col_flips[j]:
                val = 1 - val
            
            if val != 0:
                return False

    return True
