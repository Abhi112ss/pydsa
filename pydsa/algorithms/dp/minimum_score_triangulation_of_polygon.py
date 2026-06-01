METADATA = {
    "id": 1039,
    "name": "Minimum Score Triangulation of Polygon",
    "slug": "minimum-score-triangulation-of-polygon",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "interval_dp"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum score to triangulate a polygon where the score is the sum of products of vertices of each triangle.",
}

def solve(values: list[int]) -> int:
    """
    Calculates the minimum score to triangulate a polygon using interval DP.

    The problem is solved by considering a sub-polygon defined by vertices from 
    index i to index j. For any edge (i, j), we pick a third vertex k (where i < k < j)
    to form a triangle (i, k, j). This splits the polygon into two smaller 
    sub-polygons: (i to k) and (k to j).

    Args:
        values: A list of integers representing the values of the vertices of the polygon.

    Returns:
        The minimum score required to triangulate the polygon.

    Examples:
        >>> solve([1, 2, 3])
        6
        >>> solve([3, 7, 4, 5])
        141
    """
    n = len(values)
    
    # dp[i][j] represents the minimum score to triangulate the polygon 
    # formed by vertices from index i to index j inclusive.
    dp = [[0] * n for _ in range(n)]

    # The length of the sub-polygon segment (number of vertices involved)
    # A triangle requires at least 3 vertices.
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            # Initialize with a very large value
            dp[i][j] = float('inf')
            
            # Try every possible vertex k between i and j to form triangle (i, k, j)
            for k in range(i + 1, j):
                # The score is the product of the current triangle + 
                # the optimal scores of the two resulting sub-polygons.
                current_triangle_score = values[i] * values[k] * values[j]
                total_score = current_triangle_score + dp[i][k] + dp[k][j]
                
                if total_score < dp[i][j]:
                    dp[i][j] = int(total_score)

    # The answer is the minimum score for the full polygon from vertex 0 to n-1
    return dp[0][n - 1]
