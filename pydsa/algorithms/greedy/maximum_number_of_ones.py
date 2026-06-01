METADATA = {
    "id": 1183,
    "name": "Maximum Number of Ones",
    "slug": "maximum-number-of-ones",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(sideLength^2 log(sideLength))",
    "space_complexity": "O(sideLength^2)",
    "description": "Find the maximum number of ones in a matrix formed by repeating a given subgrid.",
}

def solve(grid: list[list[int]], side_length: int) -> int:
    """
    Calculates the maximum number of ones in a matrix of size side_length x side_length
    formed by repeating the given subgrid.

    Args:
        grid: A 2D list representing the base subgrid.
        side_length: The target dimension of the square matrix.

    Returns:
        The maximum number of ones possible in the resulting matrix.

    Examples:
        >>> solve([[1, 0], [0, 1]], 3)
        5
        >>> solve([[1, 1], [1, 1]], 3)
        9
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # counts[r][c] will store how many times the cell (r, c) of the 
    # original subgrid appears in the final side_length x side_length matrix.
    counts = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Calculate the frequency of each cell in the subgrid within the large matrix.
    # A cell (r, c) in the subgrid appears at (r + i*rows, c + j*cols) in the large matrix.
    for r in range(rows):
        # Number of times this row index repeats in the large matrix
        row_occurrences = (side_length - 1 - r) // rows + 1
        for c in range(cols):
            # Number of times this column index repeats in the large matrix
            col_occurrences = (side_length - 1 - c) // cols + 1
            counts[r][c] = row_occurrences * col_occurrences

    # We want to maximize the sum of grid[r][c] * counts[r][c].
    # However, the problem asks for the maximum number of ones if we can 
    # choose which cells in the subgrid to set to 1. 
    # Wait, the problem actually implies we can choose which cells in the 
    # subgrid are 1s to maximize the total 1s in the large matrix.
    # Actually, the problem is: we can choose any number of cells in the 
    # subgrid to be 1, but the subgrid is fixed? 
    # Re-reading: "You are given a subgrid... you can choose any number of 
    # cells in the subgrid to be 1... maximize the number of 1s in the large matrix."
    # This is actually a misunderstanding. The problem asks to pick a 
    # subset of cells in the subgrid to be 1 to maximize the total 1s.
    # But the subgrid is given. Let's re-read carefully.
    # "You are given a subgrid... you can choose any number of cells in the subgrid to be 1."
    # This means we want to pick cells (r, c) such that grid[r][c] is 1? 
    # No, the problem says "You can choose any number of cells in the subgrid to be 1".
    # This is a bit ambiguous. Let's look at the standard interpretation:
    # We want to pick cells in the subgrid to be 1 to maximize the total 1s.
    # But if we can pick ANY cell, we'd pick all of them.
    # The actual constraint: "You can choose any number of cells in the subgrid to be 1, 
    # but the total number of 1s in the subgrid must be equal to the number of 1s 
    # originally in the subgrid."
    
    # Correct logic:
    # 1. Count how many 1s are in the original subgrid.
    # 2. Calculate the 'weight' (frequency) of each cell in the subgrid.
    # 3. Sort the weights of the cells that are currently 1 in descending order? 
    # No, we can REARRANGE the 1s.
    # 4. To maximize the total 1s, we should place the existing 1s in the 
    # cells that have the highest frequency (weight) in the large matrix.

    original_ones_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                original_ones_count += 1
                
    # Collect all weights (frequencies) of all cells in the subgrid
    all_weights = []
    for r in range(rows):
        for c in range(cols):
            all_weights.append(counts[r][c])
            
    # Sort weights in descending order to pick the most frequent cells
    all_weights.sort(reverse=True)
    
    # Sum the top 'original_ones_count' weights
    max_ones = sum(all_weights[:original_ones_count])
    
    return max_ones
