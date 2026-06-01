METADATA = {
    "id": 3195,
    "name": "Find the Minimum Area to Cover All Ones I",
    "slug": "find-the-minimum-area-to-cover-all-ones-i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum area of a rectangle that contains all the 1s in a binary grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum area of a rectangle that covers all 1s in a binary grid.

    The minimum area is determined by the bounding box of all cells containing 1.
    We find the minimum and maximum row indices and the minimum and maximum 
    column indices where a 1 is present.

    Args:
        grid: A 2D list of integers where 1 represents a target cell and 0 represents empty.

    Returns:
        The area of the smallest rectangle covering all 1s.

    Examples:
        >>> solve([[0, 1, 0], [1, 0, 1]])
        6
        >>> solve([[0, 0], [0, 0]]) # Note: Problem constraints usually guarantee at least one 1
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Initialize boundaries to extreme values
    min_row, max_row = rows, -1
    min_col, max_col = cols, -1
    found_one = False

    # Iterate through the entire grid to find the bounding box of 1s
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                found_one = True
                # Update the bounding box boundaries
                if r < min_row:
                    min_row = r
                if r > max_row:
                    max_row = r
                if c < min_col:
                    min_col = c
                if c > max_col:
                    max_col = c

    # If no 1s were found, the area is 0
    if not found_one:
        return 0

    # The area is the product of the height and width of the bounding box
    height = max_row - min_row + 1
    width = max_col - min_col + 1

    return height * width
