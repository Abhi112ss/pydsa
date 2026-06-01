METADATA = {
    "id": 3276,
    "name": "Select Cells in Grid With Maximum Score",
    "slug": "select-cells-in-grid-with-maximum-score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Select cells in a grid such that no two selected cells are in the same row or column, maximizing the sum of values.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the maximum score by selecting cells such that no two cells share a row or column.
    
    This is a variation of the assignment problem, but since we can choose any number 
    of cells (not necessarily all rows/cols), and the constraints/structure allow, 
    we observe that we want to pick the best available values. However, the standard 
    assignment problem is usually solved via Min-Cost Max-Flow or the Hungarian Algorithm.
    Given the problem constraints and the nature of 'selecting cells', this is 
    equivalent to finding the maximum weight matching in a bipartite graph.
    
    Args:
        grid: A 2D list of integers representing the grid values.
        
    Returns:
        The maximum possible sum of selected cells.
        
    Examples:
        >>> solve([[1, 2], [3, 4]])
        5
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        3
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # The problem is equivalent to finding the Maximum Weight Bipartite Matching.
    # Since we want to maximize the sum and can pick any number of cells, 
    # we only pick cells with positive values.
    # For a general grid, the Hungarian algorithm or Min-Cost Max-Flow is required.
    # However, for the specific constraints of LeetCode problems of this type,
    # we implement a version of the augmenting path algorithm (Kuhn's or similar)
    # adapted for weights (Successive Shortest Path algorithm).

    # We use a simplified version of the Successive Shortest Path algorithm 
    # using Bellman-Ford or SPFA to handle potential negative weights (though here weights are positive).
    # Since we want to maximize, we can negate weights and find min cost.
    
    # To keep the implementation clean and within O(m*n) or O(m*n*k) expectations:
    # We use a greedy approach with augmenting paths.
    
    match_col = [-1] * cols
    match_row = [-1] * rows
    
    # We use a standard Max Weight Bipartite Matching approach.
    # Because the grid can be large, we use the augmenting path method.
    # Note: For a general dense bipartite graph, the complexity is O(V * E).
    # Here V = rows + cols, E = rows * cols.
    
    # Since we want to maximize the sum, we can use the property that 
    # we only add an augmenting path if it increases the total weight.
    
    # For the sake of a production-grade implementation that fits the "optimal" 
    # requirement for this specific problem type:
    
    # We'll use a greedy approach to find an initial matching, then improve it.
    # But the most robust way is the Hungarian Algorithm (O(N^3)).
    
    # Given the prompt asks for O(m*n) and mentions DP/Greedy, 
    # it implies a specific structure or a misunderstanding of the general problem.
    # If the grid has specific properties (like only certain cells can be picked), 
    # the complexity changes. Assuming general grid:
    
    # Let's implement the augmenting path algorithm for Max Weight Matching.
    # We use the fact that we can pick any number of cells.
    
    # For small/medium grids, we can use the following:
    # We iteratively find the best augmenting path.
    
    total_score = 0
    
    # We use a simplified version of the primal-dual algorithm for max weight matching.
    # labels for rows and columns (dual variables)
    u = [0] * rows
    v = [0] * cols
    p = [0] * (cols + 1)
    way = [0] * (cols + 1)
    
    # We transform the problem to a min-cost problem by using (MAX_VAL - grid[i][j])
    # But since we can pick any number of cells, we only care about positive contributions.
    # A simpler way: The problem is equivalent to finding the max weight matching 
    # in a bipartite graph where edges are grid[i][j] if grid[i][j] > 0.
    
    # Let's use the standard Hungarian algorithm implementation (O(N^3)).
    # We pad the grid to be square.
    n = max(rows, cols)
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                matrix[r + 1][c + 1] = grid[r][c]

    # p[j] is the row matched with column j
    p = [0] * (n + 1)
    # way[j] stores the path for augmenting
    way = [0] * (n + 1)
    # u and v are dual variables
    u = [0] * (n + 1)
    v = [0] * (n + 1)

    for i in range(1, n + 1):
        p[0] = i
        j_cur = 0
        min_v = [float('inf')] * (n + 1)
        used = [False] * (n + 1)
        
        while True:
            used[j_cur] = True
            i_cur = p[j_cur]
            delta = float('inf')
            j_next = 0
            
            for j in range(1, n + 1):
                if not used[j]:
                    # We want to maximize, so we use -matrix[i_cur][j] for min-cost
                    # But we can also use the dual update logic directly.
                    # To find max weight matching, we use the cost as -grid[i][j]
                    cur = -matrix[i_cur][j] - u[i_cur] - v[j]
                    if cur < min_v[j]:
                        min_v[j] = cur
                        way[j] = j_cur
                    if min_v[j] < delta:
                        delta = min_v[j]
                        j_next = j
            
            # Update dual variables
            for j in range(0, n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    min_v[j] -= delta
            
            j_cur = j_next
            if p[j_cur] == 0:
                break
        
        # Augment path
        while True:
            j_prev = way[j_cur]
            p[j_cur] = p[j_prev]
            j_cur = j_prev
            if j_cur == 0:
                break

    # The total weight is the sum of matrix[p[j]][j] for all matched j
    # where matrix[p[j]][j] > 0.
    # However, the Hungarian algorithm finds a perfect matching.
    # Since we can pick any number of cells, we only sum positive values.
    # The dual variables u and v actually help us find the max weight.
    # The max weight is -v[0].
    
    # Let's calculate the sum directly from the matching.
    ans = 0
    for j in range(1, n + 1):
        if p[j] > 0:
            val = matrix[p[j]][j]
            if val > 0:
                ans += val
                
    # Wait, the Hungarian algorithm finds a perfect matching in a square matrix.
    # If we use 0 for non-existent edges, it finds the max weight perfect matching.
    # Since we can choose NOT to pick a cell, we only care about positive values.
    # The standard Hungarian on the matrix with 0s for non-positive values 
    # will find the max weight matching.
    
    # Re-calculating ans correctly:
    # The Hungarian algorithm as implemented above finds the min cost perfect matching.
    # By using -matrix[i][j], it finds the max weight perfect matching.
    # Because we padded with 0s, it will pick 0s if they are part of the "best" perfect matching.
    # This is exactly what we want.
    
    final_sum = 0
    for j in range(1, n + 1):
        row_idx = p[j]
        if row_idx > 0:
            val = matrix[row_idx][j]
            if val > 0:
                final_sum += val
                
    return final_sum
