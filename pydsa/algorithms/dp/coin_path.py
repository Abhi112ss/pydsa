METADATA = {
    "id": 656,
    "name": "Coin Path",
    "slug": "coin-path",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n * b)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest path of coins from the first row to the last row.",
}

def solve(coins: list[list[int]]) -> list[int]:
    """
    Finds the lexicographically smallest path from the top row to the bottom row.
    
    A path is lexicographically smaller if at the first position where the paths 
    differ, the coin in the first path is smaller than the coin in the second path.

    Args:
        coins: A 2D list of integers representing the coins in each row.

    Returns:
        A list of integers representing the lexicographically smallest path.

    Examples:
        >>> solve([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
        [1, 1, 1]
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 4, 7]
    """
    if not coins or not coins[0]:
        return []

    num_rows = len(coins)
    num_cols = len(coins[0])

    # dp[j] will store the index of the best next coin in the row below
    # to ensure lexicographical smallest path.
    # We work backwards from the second-to-last row to the first row.
    # dp[i][j] = index k in row i+1 such that coins[i+1][k] is minimal 
    # and k is in {j-1, j, j+1}.
    
    # To save space, we only need the 'next indices' for the row we are currently processing.
    # next_indices[j] stores the column index in the row below that leads to the best path.
    next_indices = [0] * num_cols

    # Base case: For the last row, there are no "next" indices.
    # We start iterating from the second to last row.
    for row_idx in range(num_rows - 2, -1, -1):
        current_row = coins[row_idx]
        next_row = coins[row_idx + 1]
        new_next_indices = [0] * num_cols
        
        for col_idx in range(num_cols):
            # Possible moves from current cell (row_idx, col_idx)
            # are to (row_idx + 1, col_idx - 1), (row_idx + 1, col_idx), (row_idx + 1, col_idx + 1)
            best_next_col = -1
            
            # Check the three possible neighbors in the row below
            for neighbor_col in range(col_idx - 1, col_idx + 2):
                if 0 <= neighbor_col < num_cols:
                    if best_next_col == -1:
                        best_next_col = neighbor_col
                    else:
                        # Compare based on the value of the coin in the next row
                        val_current_neighbor = next_row[neighbor_col]
                        val_best_neighbor = next_row[best_next_col]
                        
                        if val_current_neighbor < val_best_neighbor:
                            best_next_col = neighbor_col
                        elif val_current_neighbor == val_best_neighbor:
                            # If coin values are equal, we must choose the neighbor 
                            # that leads to a lexicographically smaller path.
                            # Since we are moving backwards, the 'best' path is determined 
                            # by the index stored in our DP table for that neighbor.
                            # However, the problem asks for lexicographical smallest path.
                            # In a tie-break of coin values, the path is determined by 
                            # the subsequent coins. But wait, the rule is: 
                            # "the path is lexicographically smaller if at the first 
                            # position where the paths differ, the coin is smaller".
                            # Since we are at row i, and the coins at row i+1 are equal,
                            # we need to look at the path starting from row i+1.
                            # This is tricky. Actually, the greedy choice works if we 
                            # compare the paths. But we can't compare paths easily.
                            # Correct logic: If coins[i+1][c1] == coins[i+1][c2], 
                            # we need to know which one leads to a better path.
                            # We can't just use the index. We need to compare the 
                            # actual paths. But we can't store paths.
                            # Wait, the standard DP for this is: 
                            # dp[i][j] = min(coins[i+1][j-1], coins[i+1][j], coins[i+1][j+1])
                            # If there's a tie in the coin value, we need to pick the one 
                            # that is lexicographically smaller.
                            # This is solved by comparing the paths.
                            # To do this efficiently, we can use the fact that we are 
                            # building the path from bottom to top.
                            # Actually, the tie-breaking rule is: if coins[i+1][c1] == coins[i+1][c2],
                            # we pick the one that results in a lexicographically smaller path.
                            # This is equivalent to comparing the paths starting from those indices.
                            # Since we are going bottom-up, we can't easily compare.
                            # Let's re-evaluate: The problem is equivalent to finding the 
                            # shortest path in a DAG where edges have weights (coin_value, path_suffix).
                            # A simpler way: if values are equal, we need to compare the 
                            # sequences. We can use the indices to compare if we 
                            # pre-calculate the "rank" of paths.
                            # But for this specific problem, a simpler observation:
                            # We can use the DP to store the "best" path, but that's O(N^2).
                            # Let's use the property that we only care about the next coin.
                            # If coins[i+1][c1] == coins[i+1][c2], we need to pick the one 
                            # that is lexicographically smaller.
                            # We can compare these paths by looking at the next_indices.
                            # But that's still not quite right.
                            # Let's use the property: we can compare two paths in O(1) 
                            # if we use a technique like suffix arrays or hashing, 
                            # but that's overkill.
                            # Actually, the simplest way to handle ties is to realize 
                            # that if we are at row i, and we have two choices in row i+1 
                            # with the same coin value, we pick the one that is 
                            # lexicographically smaller.
                            # We can compare these by comparing the paths from row i+1 to the end.
                            # We can do this by storing the path or using a comparison function.
                            # Wait, the constraints are N=500. O(N^3) might pass.
                            # Let's try a different approach: 
                            # For each cell, store the best path. To avoid O(N^2) space, 
                            # we only store the next index and compare paths when needed.
                            pass

            # Re-thinking: The tie-breaking is the hard part.
            # Let's use the fact that we can compare two paths starting from row i+1 
            # by comparing their coin values at each subsequent row.
            # Since we are going bottom-up, we can't easily compare.
            # Let's go top-down? No, top-down is greedy and doesn't work.
            # Let's use the DP: dp[i][j] = the best path from (i, j) to the bottom.
            # To compare two paths efficiently:
            # We can use the fact that we only need to compare paths when coin values are equal.
            # Let's use the "next_indices" and a custom comparison.
            pass

    # Let's use a more robust approach for the tie-breaking.
    # We will store the best path from each cell to the bottom.
    # To keep it O(N^2), we can't store the whole path.
    # But we can compare two paths (i, j1) and (i, j2) by comparing 
    # coins[i+1][j1] vs coins[i+1][j2], then if equal, 
    # comparing the paths starting from (i+1, j1) and (i+1, j2).
    
    # We can use a "rank" system. rank[i][j] is the rank of the path 
    # starting from (i, j) among all paths starting from row i.
    
    num_rows = len(coins)
    num_cols = len(coins[0])
    
    # rank[j] will store the rank of the path starting from (current_row, j)
    # among all paths starting from current_row.
    # We'll use a list of tuples (coin_value, rank_of_next_path) to sort.
    
    # Base case: last row
    # The "path" from the last row is just the coin itself.
    # We rank the coins in the last row.
    last_row_ranks = []
    # To handle the rank, we sort the coins in the last row.
    # But wait, the rank should be based on the path.
    # For the last row, the path is just [coins[last_row][j]].
    # So we rank them based on their values.
    
    # To handle ties in the last row:
    # Sort indices based on coin value.
    sorted_indices = sorted(range(num_cols), key=lambda j: coins[num_rows-1][j])
    
    # Assign ranks. If values are equal, they get the same rank.
    # Actually, for the last row, if values are equal, the paths are 
    # [val] and [val], which are identical. So they get the same rank.
    ranks = [0] * num_cols
    current_rank = 0
    for i in range(num_cols):
        if i > 0 and coins[num_rows-1][sorted_indices[i]] > coins[num_rows-1][sorted_indices[i-1]]:
            current_rank += 1
        ranks[sorted_indices[i]] = current_rank
    
    # We also need to keep track of the best next index for the path reconstruction.
    # For the last row, there is no next index.
    best_next_idx = [0] * num_cols 

    for r in range(num_rows - 2, -1, -1):
        new_ranks = [0] * num_cols
        new_best_next = [0] * num_cols
        
        # For each cell in the current row, find the best neighbor in the next row.
        # A neighbor is better if:
        # 1. coins[r+1][neighbor] is smaller
        # 2. coins[r+1][neighbor] is equal, but rank[neighbor] is smaller
        
        # We can represent each neighbor as a tuple: (coins[r+1][neighbor], ranks[neighbor])
        # and pick the one that minimizes this tuple.
        
        for c in range(num_cols):
            best_neighbor = -1
            best_tuple = (float('inf'), float('inf'))
            
            for nc in range(c - 1, c + 2):
                if 0 <= nc < num_cols:
                    neighbor_tuple = (coins[r+1][nc], ranks[nc])
                    if neighbor_tuple < best_tuple:
                        best_tuple = neighbor_tuple
                        best_neighbor = nc
            
            new_best_next[c] = best_neighbor
            # Now we need to assign ranks to the current row.
            # The rank of cell (r, c) is determined by the tuple:
            # (coins[r][c], rank_of_path_starting_from_best_neighbor)
            # Wait, the rank of (r, c) is the rank of the path starting at (r, c).
            # The path is [coins[r][c], coins[r+1][best_neighbor], ...]
            # So the tuple for (r, c) is (coins[r][c], ranks[best_neighbor])
            # No, that's not quite right. The rank is for the whole path.
            # The path is (coins[r][c], path_from_best_neighbor).
            # So we sort cells (r, c) by (coins[r][c], ranks[best_neighbor]).
            
        # To assign ranks for the current row:
        # 1. Calculate the tuple for each cell: (coins[r][c], ranks[new_best_next[c]])
        # 2. Sort these tuples to assign new ranks.
        
        cell_tuples = []
        for c in range(num_cols):
            cell_tuples.append((coins[r][c], ranks[new_best_next[c]], c))
            
        # Sort by the tuple (coin_value, next_rank)
        cell_tuples.sort()
        
        current_rank = 0
        for i in range(num_cols):
            if i > 0 and (cell_tuples[i][0], cell_tuples[i][1]) > (cell_tuples[i-1][0], cell_tuples[i-1][1]):
                current_rank += 1
            new_ranks[cell_tuples[i][2]] = current_rank
            
        ranks = new_ranks
        best_next_idx = new_best_next

    # Reconstruction
    path = []
    curr_c = 0
    # The first row's best starting column is the one with the minimum (coins[0][c], ranks[best_next[c]])
    # But wait, the ranks we calculated are for the paths starting at (r, c).
    # So we just need to find the c in row 0 that has the minimum (coins[0][c], ranks[best_next[0][c]])
    # Actually, the ranks are already calculated for the first row.
    # The smallest rank in the first row corresponds to the lexicographically smallest path.
    
    min_rank = min(ranks)
    for c in range(num_cols):
        if ranks[c] == min_rank:
            curr_c = c
            break
            
    for r in range(num_rows):
        path.append(coins[r][curr_c])
        if r < num_rows - 1:
            curr_c = best_next_idx[curr_c]
            # Wait, best_next_idx needs to be updated per row.
            # Let's fix the loop.
            
    # Let's refine the reconstruction and the DP.
    return path

# The above logic is slightly flawed in the reconstruction. 
# Let's rewrite the solve function cleanly.

def solve(coins: list[list[int]]) -> list[int]:
    """
    Finds the lexicographically smallest path from the top row to the bottom row.
    """
    if not coins or not coins[0]:
        return []

    num_rows = len(coins)
    num_cols = len(coins[0])

    # next_col[r][c] stores the column in row r+1 that is part of the best path from (r, c)
    next_col = [[0] * num_cols for _ in range(num_rows)]
    # ranks[r][c] stores the rank of the path starting from (r, c)
    ranks = [[0] * num_cols for _ in range(num_rows)]

    # Base case: last row
    # Sort last row indices by coin value to assign ranks
    last_row_indices = sorted(range(num_cols), key=lambda c: coins[num_rows-1][c])
    current_rank = 0
    for i in range(num_cols):
        idx = last_row_indices[i]
        if i > 0 and coins[num_rows-1][idx] > coins[num_rows-1][last_row_indices[i-1]]:
            current_rank += 1
        ranks[num_rows-1][idx] = current_rank

    # DP: Bottom-up
    for r in range(num_rows - 2, -1, -1):
        # 1. For each cell, find the best neighbor in the next row
        for c in range(num_cols):
            best_nc = -1
            # A neighbor is better if (coins[r+1][nc], ranks[r+1][nc]) is smaller
            best_val = (float('inf'), float('inf'))
            
            for nc in range(c - 1, c + 2):
                if 0 <= nc < num_cols:
                    neighbor_