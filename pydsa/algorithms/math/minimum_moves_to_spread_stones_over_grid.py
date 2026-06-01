METADATA = {
    "id": 2850,
    "name": "Minimum Moves to Spread Stones Over Grid",
    "slug": "minimum-moves-to-spread-stones-over-grid",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum moves to spread stones such that every cell in an n x n grid has exactly one stone.",
}

def solve(n: int, stones: list[list[int]]) -> int:
    """
    Calculates the minimum moves to spread stones such that every cell in an n x n grid 
    has exactly one stone. A move consists of moving a stone to an adjacent cell.

    The problem is equivalent to finding the minimum Manhattan distance sum to 
    transform the current distribution into a uniform distribution. Since we 
    must end with exactly one stone per cell, the problem is a minimum weight 
    perfect matching in a bipartite graph, which for Manhattan distance on a 
    grid can be solved by calculating the sum of distances for rows and columns 
    independently.

    Args:
        n: The dimension of the n x n grid.
        stones: A list of [r, c] coordinates representing the initial positions of stones.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve(2, [[0, 0], [1, 1]])
        2
        >>> solve(3, [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
        0
    """
    # The problem asks for the minimum cost to move stones to a target configuration.
    # The target configuration is one stone at every (r, c) where 0 <= r, c < n.
    # This is a minimum weight matching problem in a bipartite graph.
    # For Manhattan distance, the total cost is the sum of costs to satisfy 
    # row requirements and column requirements independently.
    
    # However, since we are given exactly n*n stones and must fill an n*n grid,
    # we can treat this as a minimum cost flow problem. 
    # For a grid, the minimum cost to move items to specific slots is 
    # equivalent to the sum of |current_pos - target_pos| for a sorted sequence.
    
    # Because we can pair any stone with any target cell, the optimal strategy 
    # is to match the i-th smallest row coordinate with the i-th smallest 
    # target row coordinate, and similarly for columns.
    
    rows = sorted([s[0] for s in stones])
    cols = sorted([s[1] for s in stones])
    
    # The target row coordinates are [0, 0, ..., 1, 1, ..., n-1, n-1, ...]
    # specifically, each row index i appears n times.
    target_rows = []
    target_cols = []
    for i in range(n):
        for _ in range(n):
            target_rows.append(i)
            target_cols.append(i)
            
    # The total Manhattan distance is the sum of absolute differences 
    # of sorted coordinates.
    total_moves = 0
    for r_curr, r_target in zip(rows, target_rows):
        total_moves += abs(r_curr - r_target)
        
    for c_curr, c_target in zip(cols, target_cols):
        total_moves += abs(c_curr - c_target)
        
    return total_moves
