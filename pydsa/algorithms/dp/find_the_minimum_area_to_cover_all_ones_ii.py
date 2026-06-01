METADATA = {
    "id": 3197,
    "name": "Find the Minimum Area to Cover All Ones II",
    "slug": "find-the-minimum-area-to-cover-all-ones-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "prefix_sum", "matrix", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(m^2 * n^2)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum total area of three non-overlapping rectangles that cover all ones in a binary matrix.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum total area of three non-overlapping rectangles that cover all ones.

    The strategy involves partitioning the grid into three rectangles using 
    horizontal and vertical cuts. There are 6 possible configurations for 
    partitioning a rectangle into three non-overlapping sub-rectangles:
    1. Two horizontal cuts (3 rows).
    2. Two vertical cuts (3 columns).
    3. One horizontal cut, then the bottom part is split vertically.
    4. One horizontal cut, then the top part is split vertically.
    5. One vertical cut, then the right part is split horizontally.
    6. One vertical cut, then the left part is split horizontally.

    Args:
        grid: A 2D list of integers representing the binary matrix.

    Returns:
        The minimum total area required to cover all ones.

    Examples:
        >>> solve([[0,1,0],[1,0,1]])
        6
    """
    rows = len(grid)
    cols = len(grid[0])

    def get_min_area(r1: int, r2: int, c1: int, c2: int) -> int:
        """Calculates the minimum area of a single rectangle covering all ones in a subgrid."""
        min_r, max_r = float('inf'), float('-inf')
        min_c, max_c = float('inf'), float('-inf')
        found = False
        
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 1:
                    found = True
                    if r < min_r: min_r = r
                    if r > max_r: max_r = r
                    if c < min_c: min_c = c
                    if c > max_c: max_c = c
        
        if not found:
            return 10**9  # Return a large value if no ones are found
        return (max_r - min_r + 1) * (max_c - min_c + 1)

    ans = float('inf')

    # Case 1: Two horizontal cuts (3 horizontal strips)
    for i in range(rows - 2):
        for j in range(i + 1, rows - 1):
            area = (get_min_area(0, i, 0, cols - 1) + 
                    get_min_area(i + 1, j, 0, cols - 1) + 
                    get_min_area(j + 1, rows - 1, 0, cols - 1))
            ans = min(ans, area)

    # Case 2: Two vertical cuts (3 vertical strips)
    for i in range(cols - 2):
        for j in range(i + 1, cols - 1):
            area = (get_min_area(0, rows - 1, 0, i) + 
                    get_min_area(0, rows - 1, i + 1, j) + 
                    get_min_area(0, rows - 1, j + 1, cols - 1))
            ans = min(ans, area)

    # Case 3: Horizontal cut, then bottom part split vertically
    for i in range(rows - 1):
        top_area = get_min_area(0, i, 0, cols - 1)
        for j in range(cols - 1):
            bottom_left = get_min_area(i + 1, rows - 1, 0, j)
            bottom_right = get_min_area(i + 1, rows - 1, j + 1, cols - 1)
            ans = min(ans, top_area + bottom_left + bottom_right)

    # Case 4: Horizontal cut, then top part split vertically
    for i in range(rows - 1):
        bottom_area = get_min_area(i + 1, rows - 1, 0, cols - 1)
        for j in range(cols - 1):
            top_left = get_min_area(0, i, 0, j)
            top_right = get_min_area(0, i, j + 1, cols - 1)
            ans = min(ans, bottom_area + top_left + top_right)

    # Case 5: Vertical cut, then right part split horizontally
    for j in range(cols - 1):
        left_area = get_min_area(0, rows - 1, 0, j)
        for i in range(rows - 1):
            right_top = get_min_area(0, i, j + 1, cols - 1)
            right_bottom = get_min_area(i + 1, rows - 1, j + 1, cols - 1)
            ans = min(ans, left_area + right_top + right_bottom)

    # Case 6: Vertical cut, then left part split horizontally
    for j in range(cols - 1):
        right_area = get_min_area(0, rows - 1, j + 1, cols - 1)
        for i in range(rows - 1):
            left_top = get_min_area(0, i, 0, j)
            left_bottom = get_min_area(i + 1, rows - 1, 0, j)
            ans = min(ans, right_area + left_top + left_bottom)

    return int(ans)
