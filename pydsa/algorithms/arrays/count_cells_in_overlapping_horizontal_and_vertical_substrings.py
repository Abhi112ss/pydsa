METADATA = {
    "id": 3529,
    "name": "Count Cells in Overlapping Horizontal and Vertical Substrings",
    "slug": "count-cells-in-overlapping-horizontal-and-vertical-substrings",
    "category": "Array",
    "aliases": [],
    "tags": ["2d_array", "prefix_sum", "string_matching"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of cells that are part of both a horizontal and a vertical substring matching a specific pattern.",
}

def solve(grid: list[list[str]], horizontal_pattern: str, vertical_pattern: str) -> int:
    """
    Counts the number of cells (i, j) that belong to at least one occurrence 
    of horizontal_pattern in row i AND at least one occurrence of 
    vertical_pattern in column j.

    Args:
        grid: A 2D list of characters.
        horizontal_pattern: The string pattern to search for horizontally.
        vertical_pattern: The string pattern to search for vertically.

    Returns:
        The total count of cells satisfying both conditions.

    Examples:
        >>> grid = [["a", "b", "a", "b"], ["b", "a", "b", "a"]]
        >>> solve(grid, "ab", "ba")
        4
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    h_len = len(horizontal_pattern)
    v_len = len(vertical_pattern)

    # is_h_part[i][j] is True if grid[i][j] is part of a horizontal match
    is_h_part = [[False for _ in range(cols)] for _ in range(rows)]
    # is_v_part[i][j] is True if grid[i][j] is part of a vertical match
    is_v_part = [[False for _ in range(cols)] for _ in range(rows)]

    # 1. Identify horizontal matches
    for r in range(rows):
        # Use a sliding window or simple string matching for each row
        # Since we need to mark all cells in the match, we find the start indices
        row_str = "".join(grid[r])
        start = 0
        while True:
            idx = row_str.find(horizontal_pattern, start)
            if idx == -1:
                break
            # Mark all cells in this specific match
            for c in range(idx, idx + h_len):
                is_h_part[r][c] = True
            start = idx + 1

    # 2. Identify vertical matches
    for c in range(cols):
        # Construct the column string
        col_str = "".join(grid[r][c] for r in range(rows))
        start = 0
        while True:
            idx = col_str.find(vertical_pattern, start)
            if idx == -1:
                break
            # Mark all cells in this specific match
            for r in range(idx, idx + v_len):
                is_v_part[r][c] = True
            start = idx + 1

    # 3. Count cells that satisfy both conditions
    count = 0
    for r in range(rows):
        for c in range(cols):
            if is_h_part[r][c] and is_v_part[r][c]:
                count += 1

    return count
