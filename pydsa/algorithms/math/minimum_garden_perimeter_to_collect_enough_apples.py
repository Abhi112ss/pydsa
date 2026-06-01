METADATA = {
    "id": 1954,
    "name": "Minimum Garden Perimeter to Collect Enough Apples",
    "slug": "minimum-garden-perimeter-to-collect-enough-apples",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the minimum perimeter of a square garden centered at (0,0) that contains at least a given number of apples.",
}

def solve(grid: list[list[int]], neededApples: int) -> int:
    """
    Calculates the minimum perimeter of a square garden to collect enough apples.

    The garden is a square centered at (0,0). A square with side length 2*k 
    (extending from -k to k in both dimensions) contains a specific number 
    of apples. The total apples in a square of radius k can be calculated 
    using the sum of apples in all cells (i, j) where |i| <= k and |j| <= k.

    Args:
        grid: A 2D list of integers representing the number of apples in each cell.
        neededApples: The target number of apples to collect.

    Returns:
        The minimum perimeter of the square garden.

    Examples:
        >>> grid = [[1,1,1],[1,1,1],[1,1,1]]
        >>> neededApples = 1
        >>> solve(grid, neededApples)
        4
        >>> grid = [[0,2,0],[2,0,2],[0,2,0]]
        >>> neededApples = 10
        >>> solve(grid, neededApples)
        16
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Precompute 2D prefix sums to allow O(1) range sum queries.
    # prefix_sum[i][j] stores the sum of grid[0...i-1][0...j-1]
    prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix_sum[r + 1][c + 1] = (
                grid[r][c] + 
                prefix_sum[r][c + 1] + 
                prefix_sum[r + 1][c] - 
                prefix_sum[r][c]
            )

    def get_sum(r1: int, c1: int, r2: int, c2: int) -> int:
        """Returns the sum of apples in the rectangle from (r1, c1) to (r2, c2) inclusive."""
        # Adjust indices for 1-based prefix_sum array
        # Ensure indices are within grid boundaries
        r1, c1 = max(0, r1), max(0, c1)
        r2, c2 = min(rows - 1, r2), min(cols - 1, c2)
        
        if r1 > r2 or c1 > c2:
            return 0
            
        return (
            prefix_sum[r2 + 1][c2 + 1] - 
            prefix_sum[r1][c2 + 1] - 
            prefix_sum[r2 + 1][c1] + 
            prefix_sum[r1][c1]
        )

    # The center of the grid is (rows // 2, cols // 2).
    # We expand the square radius 'k' until the sum of apples is >= neededApples.
    center_r, center_c = rows // 2, cols // 2
    
    # The maximum possible radius is the distance to the furthest corner.
    max_radius = max(center_r, center_c, rows - 1 - center_r, cols - 1 - center_c)
    
    # Binary search for the minimum radius k.
    # A square with radius k covers rows [center_r - k, center_r + k] 
    # and columns [center_c - k, center_c + k].
    low = 0
    high = max_radius
    ans_radius = max_radius

    while low <= high:
        mid = (low + high) // 2
        
        # Calculate sum of apples in the square with radius 'mid'
        current_apples = get_sum(
            center_r - mid, center_c - mid, 
            center_r + mid, center_c + mid
        )
        
        if current_apples >= neededApples:
            ans_radius = mid
            high = mid - 1
        else:
            low = mid + 1

    # The perimeter of a square with radius k is 8 * k.
    # A square with radius 0 is just the center cell (perimeter 0 if we consider side length 0, 
    # but the problem implies side length 2k, so perimeter is 4 * (2k) = 8k).
    # If k=0, perimeter is 0. If k=1, side is 2, perimeter is 8.
    return 8 * ans_radius