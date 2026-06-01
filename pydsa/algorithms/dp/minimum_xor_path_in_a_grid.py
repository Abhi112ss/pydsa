METADATA = {
    "id": 3882,
    "name": "Minimum XOR Path in a Grid",
    "slug": "minimum_xor_path_in_a_grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bit_manipulation", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(n * m * 1024)",
    "space_complexity": "O(n * m * 1024)",
    "description": "Find the minimum XOR sum of a path from the top-left to the bottom-right of a grid, moving only right or down.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum XOR sum of a path from (0, 0) to (rows-1, cols-1).
    
    The path can only move down or right. We use dynamic programming where 
    dp[i][j] is a set of all possible XOR sums reachable at cell (i, j).

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The minimum XOR sum possible for a path from top-left to bottom-right.

    Examples:
        >>> solve([[1, 2], [3, 4]])
        # Path 1->2->4: 1^2^4 = 7
        # Path 1->3->4: 1^3^4 = 6
        # Returns 6
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    # The maximum possible XOR value depends on the constraints. 
    # Assuming grid values are up to 1023, max XOR is 1023.
    # We use a 3D DP table where dp[i][j] is a bitset (represented by an integer)
    # or a set of possible XOR values. For efficiency in Python, 
    # we use a list of sets or a boolean array.
    
    # dp[i][j] stores a set of all possible XOR sums at cell (i, j)
    dp: list[list[set[int]]] = [[set() for _ in range(cols)] for _ in range(rows)]

    # Initialize starting cell
    dp[0][0].add(grid[0][0])

    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue
            
            current_val = grid[r][c]
            
            # Check cell above
            if r > 0:
                for prev_xor in dp[r-1][c]:
                    dp[r][c].add(prev_xor ^ current_val)
            
            # Check cell to the left
            if c > 0:
                for prev_xor in dp[r][c-1]:
                    dp[r][c].add(prev_xor ^ current_val)

    # The answer is the minimum value in the set at the bottom-right cell
    return min(dp[rows-1][cols-1])
