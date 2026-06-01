METADATA = {
    "id": 2152,
    "name": "Minimum Number of Lines to Cover Points",
    "slug": "minimum-number-of-lines-to-cover-points",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["backtracking", "bit_manipulation", "bitmask", "geometry"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of lines required to cover all given points in a 2D plane.",
}

def solve(points: list[list[int]]) -> int:
    """
    Finds the minimum number of lines needed to cover all points.

    Args:
        points: A list of [x, y] coordinates.

    Returns:
        The minimum number of lines required to cover all points.

    Examples:
        >>> solve([[1,1],[2,2],[3,3],[4,4],[1,2],[2,3],[3,4],[4,5]])
        2
        >>> solve([[1,1],[2,2],[3,3]])
        1
    """
    n = len(points)
    if n <= 2:
        return 1 if n > 0 else 0

    # Precompute masks: for every pair of points (i, j), 
    # find all other points k that lie on the same line.
    # line_masks[i][j] is a bitmask representing points on the line through i and j.
    line_masks = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            mask = (1 << i) | (1 << j)
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Check all other points k to see if they are collinear with i and j
            # Using cross product to avoid floating point division:
            # (y2 - y1) / (x2 - x1) == (y3 - y1) / (x3 - x1)
            # => (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)
            for k in range(n):
                if k == i or k == j:
                    continue
                x3, y3 = points[k]
                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    mask |= (1 << k)
            
            line_masks[i][j] = mask
            line_masks[j][i] = mask

    # memoization for bitmask DP
    memo = {}

    def backtrack(remaining_mask: int) -> int:
        """
        Recursive function with memoization to find min lines for a set of points.
        """
        if remaining_mask == 0:
            return 0
        if remaining_mask in memo:
            return memo[remaining_mask]

        # Find the first point that is not yet covered
        first_point = 0
        while not (remaining_mask & (1 << first_point)):
            first_point += 1

        # Option 1: The line covers only this single point (edge case for single point lines)
        # However, in this problem, any line can cover at least 2 points if available.
        # To ensure we cover the first_point, we try all lines passing through it.
        
        # Try covering the first_point with every other available point
        res = n  # Initialize with worst case (one line per point)
        
        found_pair = False
        for j in range(n):
            if j != first_point and (remaining_mask & (1 << j)):
                found_pair = True
                # Use the precomputed mask for the line through first_point and j
                # We only care about points that are actually in our current remaining_mask
                current_line_mask = line_masks[first_point][j] & remaining_mask
                res = min(res, 1 + backtrack(remaining_mask & ~current_line_mask))
        
        # If no other point can be paired with first_point, it must be a single-point line
        if not found_pair:
            res = 1 + backtrack(remaining_mask & ~(1 << first_point))

        memo[remaining_mask] = res
        return res

    # The initial mask has all n bits set to 1
    return backtrack((1 << n) - 1)
