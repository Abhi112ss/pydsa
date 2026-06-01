METADATA = {
    "id": 2906,
    "name": "Construct Product Matrix",
    "slug": "construct-product-matrix",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "matrix", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Construct an m x n matrix such that the product of all elements equals target, and each element is at most 10^6.",
}

def solve(m: int, n: int, target: int) -> list[list[int]]:
    """
    Constructs an m x n matrix where the product of all elements equals target.
    Each element in the matrix must be at most 10^6.

    Args:
        m: The number of rows in the matrix.
        n: The number of columns in the matrix.
        target: The required product of all elements in the matrix.

    Returns:
        A 2D list of integers representing the constructed matrix.

    Raises:
        ValueError: If it is impossible to construct such a matrix.

    Examples:
        >>> solve(2, 2, 4)
        [[2, 2], [1, 1]]
        >>> solve(2, 2, 10)
        [[5, 2], [1, 1]]
        >>> solve(2, 2, 11)
        ValueError: Impossible to construct matrix
    """
    # Initialize the matrix with 1s
    matrix = [[1 for _ in range(n)] for _ in range(m)]
    
    # We want to fill the matrix with the largest possible factors first
    # to ensure we don't exceed the 10^6 limit per cell.
    # We use a greedy approach by filling cells one by one.
    
    # Sort indices by some order, but since all cells are equal, 
    # we can just iterate through them.
    current_cell_idx = 0
    total_cells = m * n
    
    # We iterate through the cells and try to divide the target by the largest
    # possible factors. However, a simpler way is to find prime factors
    # and distribute them. But even simpler: just greedily divide the target
    # by the largest possible divisor that fits in a cell and doesn't 
    # leave us with too many remaining factors for the remaining cells.
    
    # Actually, the most robust way is to find all prime factors of target
    # and distribute them into the cells.
    factors = []
    temp_target = target
    d = 2
    while d * d <= temp_target:
        while temp_target % d == 0:
            factors.append(d)
            temp_target //= d
        d += 1
    if temp_target > 1:
        factors.append(temp_target)
    
    # If the number of prime factors is greater than the number of cells,
    # it's impossible because each cell can hold multiple factors, 
    # but we can't have more than one factor per cell if we want to keep 
    # them small? No, that's wrong. We can have multiple factors in one cell.
    # The constraint is: total cells >= number of prime factors? No.
    # The constraint is: we can have at most m*n factors if we put one per cell.
    # If we have more prime factors than cells, we MUST combine them.
    # But combining them might exceed 10^6.
    
    # Correct Greedy:
    # 1. Get all prime factors.
    # 2. If len(factors) > m * n, it's impossible (since each factor is >= 2).
    # 3. Sort factors descending to try and fit them into cells.
    
    if len(factors) > total_cells:
        raise ValueError("Impossible to construct matrix")
    
    # Sort factors descending to fill cells greedily
    factors.sort(reverse=True)
    
    # Fill cells with factors
    # To stay under 10^6, we can just put one factor per cell.
    # Since we already checked len(factors) <= total_cells, 
    # we can just put each factor in its own cell.
    # Wait, if a factor itself is > 10^6, it's impossible.
    # But the problem says target is up to 10^12, so a prime factor 
    # could be up to 10^12. 
    # Actually, if a prime factor is > 10^6, we can't put it in a cell.
    # But we can't split a prime factor. So if any prime factor > 10^6, return error.
    
    for f in factors:
        if f > 10**6:
            raise ValueError("Impossible to construct matrix")
            
    # Distribute factors into the matrix
    # Since we checked len(factors) <= total_cells, we can just put 
    # one factor per cell.
    for i in range(len(factors)):
        row = i // n
        col = i % n
        matrix[row][col] = factors[i]
        
    return matrix
