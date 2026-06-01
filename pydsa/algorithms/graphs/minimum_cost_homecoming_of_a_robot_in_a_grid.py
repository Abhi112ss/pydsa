METADATA = {
    "id": 2087,
    "name": "Minimum Cost Homecoming of a Robot in a Grid",
    "slug": "minimum-cost-homecoming-of-a-robot-in-a-grid",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to return a robot to (0, 0) by summing the costs of moving up and left.",
}

def solve(rows: int, cols: int, top: list[int], bottom: list[int], left: list[int], right: list[int]) -> int:
    """
    Calculates the minimum cost to move a robot from (rows-1, cols-1) to (0, 0).

    Since all costs are non-negative, the optimal strategy is to move directly 
    towards the origin (up and left) without any unnecessary lateral movements.
    The total cost is the sum of all costs in the 'top' array and 'left' array.

    Args:
        rows: The number of rows in the grid.
        cols: The number of columns in the grid.
        top: A list of costs to move from row i to row i-1.
        bottom: A list of costs to move from row i to row i+1.
        left: A list of costs to move from col j to col j-1.
        right: A list of costs to move from col j to col j+1.

    Returns:
        The minimum cost to reach (0, 0).

    Examples:
        >>> solve(3, 3, [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1])
        4
        >>> solve(2, 2, [1, 1], [1, 1], [1, 1], [1, 1])
        2
    """
    # To reach (0, 0) from (rows-1, cols-1), the robot must traverse 
    # every row transition in the 'top' array and every column transition 
    # in the 'left' array exactly once.
    
    # Sum of costs to move up through all rows
    total_up_cost = sum(top)
    
    # Sum of costs to move left through all columns
    total_left_cost = sum(left)
    
    return total_up_cost + total_left_cost
