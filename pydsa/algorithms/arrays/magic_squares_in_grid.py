METADATA = {
    "id": 840,
    "name": "Magic Squares In Grid",
    "slug": "magic-squares-in-grid",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(1)",
    "description": "Count the number of 3x3 magic squares in a given grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of 3x3 magic squares in the provided grid.
    
    A 3x3 magic square must contain all digits from 1 to 9 exactly once,
    and all rows, columns, and both diagonals must sum to 15.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The total count of 3x3 magic squares found in the grid.

    Examples:
        >>> solve([[0,0,0,0,0],[0,4,9,5,0],[0,3,5,7,0],[0,8,1,6,0],[0,0,0,0,0]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])
    magic_count = 0

    # Pre-defined set of all digits required for a 3x3 magic square
    required_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # Iterate through every possible top-left corner (r, c) of a 3x3 square
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Extract the 3x3 subgrid elements
            subgrid = [
                grid[r][c], grid[r][c+1], grid[r][c+2],
                grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
            ]

            # Step 1: Check if the subgrid contains exactly the digits 1-9
            if set(subgrid) != required_digits:
                continue

            # Step 2: Verify all row sums equal 15
            if (subgrid[0] + subgrid[1] + subgrid[2] != 15 or
                subgrid[3] + subgrid[4] + subgrid[5] != 15 or
                subgrid[6] + subgrid[7] + subgrid[8] != 15):
                continue

            # Step 3: Verify all column sums equal 15
            if (subgrid[0] + subgrid[3] + subgrid[6] != 15 or
                subgrid[1] + subgrid[4] + subgrid[7] != 15 or
                subgrid[2] + subgrid[5] + subgrid[8] != 15):
                continue

            # Step 4: Verify both diagonal sums equal 15
            if (subgrid[0] + subgrid[4] + subgrid[8] != 15 or
                subgrid[2] + subgrid[4] + subgrid[6] != 15):
                continue

            # If all checks pass, it is a magic square
            magic_count += 1

    return magic_count