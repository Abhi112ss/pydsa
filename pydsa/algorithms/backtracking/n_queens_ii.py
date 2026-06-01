METADATA = {
    "id": 52,
    "name": "N-Queens II",
    "slug": "n-queens-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(N!)",
    "space_complexity": "O(N)",
    "description": "Return the number of distinct ways to place n queens on an n x n chessboard such that no two queens attack each other.",
}

def solve(n: int) -> int:
    """
    Calculates the number of distinct solutions to the N-Queens problem.

    Args:
        n: The number of queens to place on an n x n board.

    Returns:
        The total number of distinct valid configurations.

    Examples:
        >>> solve(1)
        1
        >>> solve(4)
        2
        >>> solve(8)
        92
    """
    if n <= 0:
        return 0

    # We use bitmasks to track the availability of columns and diagonals.
    # cols: tracks which columns are occupied.
    # diag1: tracks diagonals from top-left to bottom-right (row - col is constant).
    # diag2: tracks diagonals from top-right to bottom-left (row + col is constant).
    # Using bitmasks allows O(1) checks and updates.
    
    count = 0

    def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
        nonlocal count
        
        # Base case: If all rows are filled, we found a valid configuration.
        if row == n:
            count += 1
            return

        # (1 << n) - 1 creates a bitmask of n ones.
        # ~(cols | diag1 | diag2) finds all positions that are NOT under attack.
        # We AND it with 'full_mask' to ignore bits beyond the n-th position.
        full_mask = (1 << n) - 1
        available_positions = full_mask & ~(cols | diag1 | diag2)

        while available_positions:
            # Extract the lowest set bit (the position to place the queen).
            position = available_positions & -available_positions
            
            # Remove this position from available positions.
            available_positions ^= position
            
            # Move to the next row.
            # diag1 is shifted right because as we move down, the diagonal influence moves right.
            # diag2 is shifted left because as we move down, the diagonal influence moves left.
            backtrack(
                row + 1,
                cols | position,
                (diag1 | position) >> 1,
                (diag2 | position) << 1
            )

    # Note: The bitmask approach for diagonals usually uses:
    # diag1 (left-to-right): (diag1 | position) << 1
    # diag2 (right-to-left): (diag2 | position) >> 1
    # However, the direction depends on how you define the bit shift relative to the row index.
    # Let's use a standard bitmasking approach for N-Queens.
    
    count = 0
    
    def backtrack_standard(row: int, cols: int, d1: int, d2: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return
        
        # All possible positions in this row (1s represent available spots)
        # A bit is 1 if the column is NOT attacked by cols, d1, or d2.
        possibilities = ((1 << n) - 1) & ~(cols | d1 | d2)
        
        while possibilities:
            # Get the rightmost set bit
            bit = possibilities & -possibilities
            # Mark this bit as used
            possibilities &= ~bit
            
            # Recurse to next row
            # d1: diagonal (row-col) shifts left
            # d2: diagonal (row+col) shifts right
            backtrack_standard(
                row + 1,
                cols | bit,
                (d1 | bit) << 1,
                (d2 | bit) >> 1
            )

    # Re-initializing with the standard bitmasking logic
    # We use d1 for the "left" diagonal and d2 for the "right" diagonal.
    # To ensure the bitmask stays within n bits, we mask d1 and d2.
    
    count = 0
    full_mask = (1 << n) - 1

    def solve_recursive(row: int, cols: int, d1: int, d2: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return
        
        # bits represents available columns in the current row
        bits = full_mask & ~(cols | d1 | d2)
        
        while bits:
            bit = bits & -bits
            bits ^= bit
            solve_recursive(
                row + 1,
                cols | bit,
                (d1 | bit) << 1 & full_mask,
                (d2 | bit) >> 1
            )

    solve_recursive(0, 0, 0, 0)
    return count
