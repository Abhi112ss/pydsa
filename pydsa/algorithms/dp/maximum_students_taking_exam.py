METADATA = {
    "id": 1349,
    "name": "Maximum Students Taking Exam",
    "slug": "maximum-students-taking-exam",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["bitmask", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(m * 2^n * 2^n)",
    "space_complexity": "O(2^n)",
    "description": "Find the maximum number of students that can be seated in an m x n grid such that no two students are adjacent (horizontally, vertically, or diagonally).",
}

def solve(m: int, n: int) -> int:
    """
    Calculates the maximum number of students that can be seated in an m x n grid
    following the adjacency constraints.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The maximum number of students that can be seated.

    Examples:
        >>> solve(3, 3)
        5
        >>> solve(2, 2)
        2
    """
    # Precompute all valid bitmasks for a single row of width n.
    # A mask is valid if no two bits are adjacent (no two students side-by-side).
    valid_masks = []
    for mask in range(1 << n):
        if not (mask & (mask << 1)):
            valid_masks.append(mask)

    # dp[mask] stores the maximum students seated up to the current row,
    # where the current row's seating configuration is represented by 'mask'.
    dp = {mask: bin(mask).count('1') for mask in valid_masks}

    # Iterate through each row starting from the second row.
    for row in range(1, m):
        new_dp = {}
        for current_mask in valid_masks:
            current_count = bin(current_mask).count('1')
            max_prev_students = -1

            for prev_mask in valid_masks:
                # Check vertical and diagonal constraints:
                # 1. No student in current row is directly below a student in prev row.
                # 2. No student in current row is diagonally adjacent to a student in prev row.
                # These are covered by checking if (current_mask & prev_mask) is 0,
                # (current_mask & (prev_mask << 1)) is 0, and (current_mask & (prev_mask >> 1)) is 0.
                if not (current_mask & prev_mask) and \
                   not (current_mask & (prev_mask << 1)) and \
                   not (current_mask & (prev_mask >> 1)):
                    
                    if prev_mask in dp:
                        max_prev_students = max(max_prev_students, dp[prev_mask])

            # If a valid configuration for the previous row was found, update new_dp.
            if max_prev_students != -1:
                new_dp[current_mask] = max_prev_students + current_count
        
        # Move to the next row's DP state.
        dp = new_dp

    # The answer is the maximum value in the DP table after processing all rows.
    return max(dp.values()) if dp else 0
