METADATA = {
    "id": 741,
    "name": "Cherry Pickup",
    "slug": "cherry-pickup",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "memoization", "matrix", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum number of cherries collected by two people moving from (0,0) to (n-1,n-1) and back.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum number of cherries that can be collected.
    
    The problem can be modeled as two people starting at (0,0) and moving 
    simultaneously to (n-1, n-1). Since the return trip is symmetric to 
    the forward trip, we only need to track two paths moving forward.
    
    Args:
        grid: A 2D list of integers where 0 is empty, 1 is cherry, and -1 is obstacle.
        
    Returns:
        The maximum number of cherries collected, or -1 if impossible.
        
    Examples:
        >>> solve([[0,1,-1],[1,0,-1],[1,1,1]])
        5
        >>> solve([[0,1,1],[1,0,1],[1,1,0]])
        4
        >>> solve([[0,1,1],[1,1,0],[1,1,0]])
        4
    """
    n = len(grid)
    # memo[r1][c1][r2] stores max cherries for person 1 at (r1, c1) 
    # and person 2 at (r2, c2). Since r1 + c1 == r2 + c2 (steps taken),
    # c2 can be derived as: c2 = r1 + c1 - r2.
    memo: dict[tuple[int, int, int], int] = {}

    def dp(r1: int, c1: int, r2: int) -> int:
        c2 = r1 + c1 - r2
        
        # Base case: Out of bounds or hitting an obstacle
        if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or 
            grid[r1][c1] == -1 or grid[r2][c2] == -1):
            return float('-inf')
        
        # Base case: Reached the destination
        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        
        state = (r1, c1, r2)
        if state in memo:
            return memo[state]
        
        # Calculate cherries at current positions
        # If both people are on the same cell, only count the cherry once
        cherries = grid[r1][c1]
        if r1 != r2 or c1 != c2:
            cherries += grid[r2][c2]
            
        # Explore all 4 possible combinations of moves for the two people:
        # (Down, Down), (Down, Right), (Right, Down), (Right, Right)
        res = max(
            dp(r1 + 1, c1, r2 + 1),     # Both move Down
            dp(r1 + 1, c1, r2),         # P1 Down, P2 Right
            dp(r1, c1 + 1, r2 + 1),     # P1 Right, P2 Down
            dp(r1, c1 + 1, r2)          # Both move Right
        )
        
        # Store result in memo
        memo[state] = cherries + res
        return memo[state]

    result = dp(0, 0, 0)
    return int(result) if result > float('-inf') else -1
