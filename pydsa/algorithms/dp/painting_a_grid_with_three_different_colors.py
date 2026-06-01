METADATA = {
    "id": 1931,
    "name": "Painting a Grid With Three Different Colors",
    "slug": "painting-a-grid-with-three-different-colors",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * 3^m)",
    "space_complexity": "O(3^m)",
    "description": "Find the number of ways to paint an n x m grid with three colors such that no two adjacent cells have the same color.",
}

def solve(n: int, m: int) -> int:
    """
    Calculates the number of ways to paint an n x m grid with three colors 
    such that no two adjacent cells (horizontally or vertically) have the same color.

    Args:
        n: The number of rows in the grid.
        m: The number of columns in the grid.

    Returns:
        The total number of valid colorings modulo 10^9 + 7.

    Examples:
        >>> solve(1, 1)
        3
        >>> solve(2, 2)
        18
    """
    MOD = 1_000_000_007

    # To optimize, we ensure m is the smaller dimension to minimize the state space.
    # The complexity is O(n * 3^m).
    if m > n:
        n, m = m, n

    # Pre-calculate all valid colorings for a single row of length m.
    # A row is valid if no two adjacent cells have the same color.
    # We represent a row as a base-3 number (0, 1, 2).
    valid_rows = []
    num_states = 3**m

    for i in range(num_states):
        row_pattern = []
        temp = i
        is_valid = True
        for _ in range(m):
            color = temp % 3
            # Check horizontal adjacency constraint
            if row_pattern and row_pattern[-1] == color:
                is_valid = False
                break
            row_pattern.append(color)
            temp //= 3
        
        if is_valid:
            valid_rows.append(row_pattern)

    # dp[i] stores the number of ways to color the current row with pattern i.
    # We use a dictionary or list to map the pattern (as a tuple) to its count.
    # Using a list of tuples for valid_rows makes it easier to iterate.
    
    # Initial state: first row
    # dp maps the tuple representation of a valid row to the number of ways to form it.
    dp = {}
    for row in valid_rows:
        dp[tuple(row)] = 1

    # Iterate through rows from 2 to n
    for _ in range(1, n):
        new_dp = {}
        for current_row in valid_rows:
            current_tuple = tuple(current_row)
            ways_to_reach_current = 0
            
            # Check compatibility with all valid patterns from the previous row
            for prev_row_tuple, count in dp.items():
                # Check vertical adjacency constraint
                is_compatible = True
                for col in range(m):
                    if current_row[col] == prev_row_tuple[col]:
                        is_compatible = False
                        break
                
                if is_compatible:
                    ways_to_reach_current = (ways_to_reach_current + count) % MOD
            
            if ways_to_reach_current > 0:
                new_dp[current_tuple] = ways_to_reach_current
        
        dp = new_dp

    return sum(dp.values()) % MOD
