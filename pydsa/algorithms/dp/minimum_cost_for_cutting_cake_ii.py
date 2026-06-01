METADATA = {
    "id": 3219,
    "name": "Minimum Cost for Cutting Cake II",
    "slug": "minimum-cost-for-cutting-cake-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "interval_dp"],
    "difficulty": "hard",
    "time_complexity": "O(N^3 * M^3)",
    "space_complexity": "O(N^2 * M^2)",
    "description": "Find the minimum cost to cut a rectangular cake into unit squares using given horizontal and vertical cuts.",
}

def solve(m: int, n: int, h_cuts: list[int], v_cuts: list[int]) -> int:
    """
    Calculates the minimum cost to cut a cake of size m x n into 1x1 pieces.

    Args:
        m: The height of the cake.
        n: The width of the cake.
        h_cuts: A list of integers representing the indices of horizontal cuts.
        v_cuts: A list of integers representing the indices of vertical cuts.

    Returns:
        The minimum cost to perform all cuts.

    Examples:
        >>> solve(3, 3, [1, 2], [1, 2])
        12
    """
    # Sort cuts to define intervals clearly
    h_cuts.sort()
    v_cuts.sort()

    # Add boundaries to the cuts to simplify interval logic
    # h_points: [0, cut1, cut2, ..., m]
    # v_points: [0, cut1, cut2, ..., n]
    h_points = [0] + h_cuts + [m]
    v_points = [0] + v_cuts + [n]

    num_h = len(h_points)
    num_v = len(v_points)

    # dp[i][j][k][l] represents the min cost to cut the rectangle 
    # bounded by h_points[i], h_points[j], v_points[k], v_points[l]
    # Using a 4D array for interval DP
    dp = [[[[0] * num_v for _ in range(num_v)] for _ in range(num_h)] for _ in range(num_h)]

    # Iterate over the size of the intervals (number of segments covered)
    for dh in range(2, num_h):  # height interval size (in terms of segments)
        for dk in range(2, num_v):  # width interval size
            for i in range(num_h - dh):
                j = i + dh
                for k in range(num_v - dk):
                    l = k + dk
                    
                    # Current rectangle dimensions
                    height = h_points[j] - h_points[i]
                    width = v_points[l] - v_points[k]
                    
                    min_cost = float('inf')

                    # Try all possible horizontal cuts within the current interval [i, j]
                    for cut_idx in range(i + 1, j):
                        # Cost = (cost of current cut) + (cost of left part) + (cost of right part)
                        # The cost of a cut is the perimeter of the current rectangle
                        current_cut_cost = 2 * (height + width)
                        res = current_cut_cost + dp[i][cut_idx][k][l] + dp[cut_idx][j][k][l]
                        if res < min_cost:
                            min_cost = res

                    # Try all possible vertical cuts within the current interval [k, l]
                    for cut_idx in range(k + 1, l):
                        current_cut_cost = 2 * (height + width)
                        res = current_cut_cost + dp[i][j][k][cut_idx] + dp[i][j][cut_idx][l]
                        if res < min_cost:
                            min_cost = res
                    
                    dp[i][j][k][l] = min_cost if min_cost != float('inf') else 0

    # The answer is the cost for the full rectangle from index 0 to end
    return dp[0][num_h - 1][0][num_v - 1]
