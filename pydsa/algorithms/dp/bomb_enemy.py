METADATA = {
    "id": 361,
    "name": "Bomb Enemy",
    "slug": "bomb-enemy",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m+n)",
    "description": "Calculate the number of enemies killed by a bomb placed at each cell in a grid, considering walls and enemy visibility.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Calculates the number of enemies killed by a bomb placed at each cell.
    
    A bomb kills enemies in the same row and column until it hits a wall ('#') 
    or the edge of the grid.

    Args:
        grid: A 2D list of strings where 'E' is enemy, '#' is wall, and '.' is empty.

    Returns:
        A 2D list of integers representing the number of enemies killed at each cell.

    Examples:
        >>> grid = [["E", ".", "#", "E"], [".", ".", ".", "."], ["E", ".", ".", "E"]]
        >>> solve(grid)
        [[1, 1, 0, 1], [1, 1, 0, 1], [2, 2, 0, 2]]
    """
    if not grid or not grid[0]:
        return []

    rows = len(grid)
    cols = len(grid[0])

    # row_enemies[r][c] stores how many enemies are visible from (r, c) in its row
    # col_enemies[r][c] stores how many enemies are visible from (r, c) in its column
    row_enemies = [[0] * cols for _ in range(rows)]
    col_enemies = [[0] * cols for _ in range(rows)]

    # Precompute row-wise visibility
    for r in range(rows):
        # Left to right pass
        count = 0
        for c in range(cols):
            if grid[r][c] == "#":
                count = 0
            elif grid[r][c] == "E":
                count += 1
            row_enemies[r][c] = count
            
        # Right to left pass
        count = 0
        for c in range(cols - 1, -1, -1):
            if grid[r][c] == "#":
                count = 0
            elif grid[r][c] == "E":
                count += 1
            # Total enemies in row segment is (enemies to left) + (enemies to right)
            # But we must avoid double counting the current cell if it's an enemy
            # We use a trick: row_enemies[r][c] currently holds left-side count.
            # We'll update it to be the sum of left and right.
            # To avoid double counting, we subtract the current cell if it's an enemy.
            # However, a cleaner way is to store left and right separately or 
            # just calculate the total segment sum.
            # Let's use a temporary variable for right-side count.
            pass # Logic handled below in a cleaner way

    # Re-implementing precomputation more robustly
    # Row pass
    for r in range(rows):
        # Left to right
        left_count = 0
        left_arr = [0] * cols
        for c in range(cols):
            if grid[r][c] == "#":
                left_count = 0
            elif grid[r][c] == "E":
                left_count += 1
            left_arr[c] = left_count
            
        # Right to left
        right_count = 0
        right_arr = [0] * cols
        for c in range(cols - 1, -1, -1):
            if grid[r][c] == "#":
                right_count = 0
            elif grid[r][c] == "E":
                right_count += 1
            right_arr[c] = right_count
            
        # Combine: total enemies in row segment = left + right - (1 if current is E else 0)
        for c in range(cols):
            if grid[r][c] == "#":
                row_enemies[r][c] = 0
            else:
                current_is_enemy = 1 if grid[r][c] == "E" else 0
                row_enemies[r][c] = left_arr[c] + right_arr[c] - current_is_enemy

    # Column pass
    for c in range(cols):
        # Top to bottom
        top_count = 0
        top_arr = [0] * rows
        for r in range(rows):
            if grid[r][c] == "#":
                top_count = 0
            elif grid[r][c] == "E":
                top_count += 1
            top_arr[r] = top_count
            
        # Bottom to top
        bottom_count = 0
        bottom_arr = [0] * rows
        for r in range(rows - 1, -1, -1):
            if grid[r][c] == "#":
                bottom_count = 0
            elif grid[r][c] == "E":
                bottom_count += 1
            bottom_arr[r] = bottom_count
            
        # Combine
        for r in range(rows):
            if grid[r][c] == "#":
                col_enemies[r][c] = 0
            else:
                current_is_enemy = 1 if grid[r][c] == "E" else 0
                col_enemies[r][c] = top_arr[r] + bottom_arr[r] - current_is_enemy

    # Final result construction
    result = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                result[r][c] = 0
            else:
                # Total killed = enemies in row + enemies in col - (1 if current is E else 0)
                # We subtract the current cell once because it's counted in both row and col
                current_is_enemy = 1 if grid[r][c] == "E" else 0
                result[r][c] = row_enemies[r][c] + col_enemies[r][c] - current_is_enemy

    return result
