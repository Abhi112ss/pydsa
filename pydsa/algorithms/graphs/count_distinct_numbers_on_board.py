METADATA = {
    "id": 2549,
    "name": "Count Distinct Numbers on Board",
    "slug": "count-distinct-numbers-on-board",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "hash_set", "matrix", "traversal"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the number of distinct values reachable from a starting cell in a grid using DFS.",
}

def solve(board: list[list[int]], start_row: int, start_col: int) -> int:
    """
    Finds the number of distinct values reachable from a starting cell in a grid.

    Args:
        board: A 2D list of integers representing the grid.
        start_row: The starting row index.
        start_col: The starting column index.

    Returns:
        The count of unique integers encountered during the traversal.

    Examples:
        >>> board = [[1, 2], [3, 4]]
        >>> solve(board, 0, 0)
        4
        >>> board = [[1, 1], [1, 2]]
        >>> solve(board, 0, 0)
        2
    """
    rows_count = len(board)
    cols_count = len(board[0])
    
    # Set to keep track of visited cells to avoid infinite loops and redundant work
    visited = set()
    # Set to store the unique values encountered during traversal
    distinct_values = set()
    
    # Stack for iterative DFS to avoid recursion depth issues in large grids
    stack = [(start_row, start_col)]
    visited.add((start_row, start_col))
    
    while stack:
        current_row, current_col = stack.pop()
        
        # Add the value of the current cell to our collection of unique values
        distinct_values.add(board[current_row][current_col])
        
        # Explore all 4 adjacent directions (Up, Down, Left, Right)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_row = current_row + dr
            neighbor_col = current_col + dc
            
            # Check boundaries and if the cell has already been visited
            if (0 <= neighbor_row < rows_count and 
                0 <= neighbor_col < cols_count and 
                (neighbor_row, neighbor_col) not in visited):
                
                visited.add((neighbor_row, neighbor_col))
                stack.append((neighbor_row, neighbor_col))
                
    return len(distinct_values)
