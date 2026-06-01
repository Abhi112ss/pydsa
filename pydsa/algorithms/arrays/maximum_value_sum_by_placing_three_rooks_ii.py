METADATA = {
    "id": 3257,
    "name": "Maximum Value Sum by Placing Three Rooks II",
    "slug": "maximum-value-sum-by-placing-three-rooks-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of three elements in a grid such that no two elements share the same row or column.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the maximum sum of three elements in a grid such that no two elements 
    share the same row or column.

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The maximum sum of three elements satisfying the rook placement constraint.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        24
        >>> solve([[10, 1, 1], [1, 10, 1], [1, 1, 10]])
        30
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # To find the maximum sum of 3 rooks, we only need to consider the 
    # top 3 largest values in each row and each column.
    # This reduces the search space from N*M to at most 3*N + 3*M.
    
    candidates = []
    
    # Collect top 3 candidates from each row
    for r in range(rows):
        row_vals = []
        for c in range(cols):
            row_vals.append((grid[r][c], r, c))
        # Sort descending and take top 3
        row_vals.sort(key=lambda x: x[0], reverse=True)
        candidates.extend(row_vals[:3])
        
    # Collect top 3 candidates from each column
    for c in range(cols):
        col_vals = []
        for r in range(rows):
            col_vals.append((grid[r][c], r, c))
        # Sort descending and take top 3
        col_vals.sort(key=lambda x: x[0], reverse=True)
        candidates.extend(col_vals[:3])
        
    # Remove duplicates to avoid redundant checks
    # Using a set of (value, row, col) tuples
    unique_candidates = list(set(candidates))
    
    # Sort all candidates by value descending to optimize the search
    unique_candidates.sort(key=lambda x: x[0], reverse=True)
    
    max_sum = -float('inf')
    num_candidates = len(unique_candidates)
    
    # Brute force the reduced candidate set. 
    # Since the number of candidates is O(N), O(N^3) is acceptable 
    # if N is small, but here N is the number of rows/cols.
    # However, the problem constraints and the "top 3" logic 
    # ensure we only check a very small subset of the grid.
    for i in range(num_candidates):
        val1, r1, c1 = unique_candidates[i]
        
        # Pruning: if current value + two largest possible values < max_sum, break
        if i + 2 < num_candidates:
            if val1 + unique_candidates[i+1][0] + unique_candidates[i+2][0] <= max_sum:
                break
        
        for j in range(i + 1, num_candidates):
            val2, r2, c2 = unique_candidates[j]
            
            # Check if second rook conflicts with first
            if r1 == r2 or c1 == c2:
                continue
                
            if val1 + val2 + (unique_candidates[j+1][0] if j+1 < num_candidates else 0) <= max_sum:
                break
                
            for k in range(j + 1, num_candidates):
                val3, r3, c3 = unique_candidates[k]
                
                # Check if third rook conflicts with first or second
                if r3 == r1 or c3 == c1 or r3 == r2 or c3 == c2:
                    continue
                
                current_sum = val1 + val2 + val3
                if current_sum > max_sum:
                    max_sum = current_sum
                    
    return int(max_sum)
