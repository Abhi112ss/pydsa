METADATA = {
    "id": 120,
    "name": "Triangle",
    "slug": "triangle",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["arrays", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum path sum from top to bottom of a triangle where you can only move to adjacent numbers in the row below.",
}

def solve(triangle: list[list[int]]) -> int:
    """
    Calculates the minimum path sum from the top of the triangle to the bottom.

    The algorithm uses a bottom-up dynamic programming approach. Instead of 
    starting from the top and managing multiple paths, we start from the 
    second-to-last row and move upwards. For each element, we add the 
    minimum of its two direct children from the row below.

    Args:
        triangle: A list of lists representing the triangle.

    Returns:
        The minimum path sum.

    Examples:
        >>> solve([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
        11
        >>> solve([[2], [1, 1], [3, 1, 1], [1, 1, 1, 1]])
        5
    """
    if not triangle:
        return 0

    # We use a 1D array to store the minimum path sums of the row below.
    # Initializing it with the last row of the triangle.
    # This allows us to achieve O(n) space complexity.
    n = len(triangle)
    dp = list(triangle[-1])

    # Iterate from the second-to-last row up to the top row.
    for row_index in range(n - 2, -1, -1):
        current_row = triangle[row_index]
        for col_index in range(len(current_row)):
            # The minimum path sum at the current position is the current value
            # plus the minimum of the two adjacent values in the row below.
            dp[col_index] = current_row[col_index] + min(dp[col_index], dp[col_index + 1])

    # After reaching the top, the first element contains the total minimum path sum.
    return dp[0]
