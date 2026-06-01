METADATA = {
    "id": 2965,
    "name": "Find Missing and Repeated Values",
    "slug": "find-missing-and-repeated-values",
    "category": "Math",
    "aliases": [],
    "tags": ["arrays", "math", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the single repeated number and the single missing number in an n x n grid containing numbers from 1 to n^2.",
}

def solve(grid: list[list[int]]) -> list[int]:
    """
    Finds the repeated and missing numbers in an n x n grid using mathematical formulas.

    The problem provides an n x n grid containing numbers from 1 to n^2. 
    One number appears twice (a), and one number is missing (b).
    We use the sum of first k integers and the sum of squares of first k integers
    to create a system of two equations to solve for a and b.

    Args:
        grid: A 2D list of integers representing the n x n grid.

    Returns:
        A list of two integers [a, b], where 'a' is the repeated number 
        and 'b' is the missing number.

    Examples:
        >>> solve([[1, 3], [2, 2]])
        [2, 4]
        >>> solve([[1, 1], [2, 2]])
        [1, 3] # Note: This specific example depends on grid content, 
               # but follows the logic of finding the duplicate and missing.
    """
    n = len(grid)
    total_elements = n * n
    
    # Expected sum of numbers from 1 to N (where N = n^2)
    # Formula: N * (N + 1) / 2
    expected_sum = total_elements * (total_elements + 1) // 2
    
    # Expected sum of squares of numbers from 1 to N
    # Formula: N * (N + 1) * (2N + 1) / 6
    expected_sum_sq = total_elements * (total_elements + 1) * (2 * total_elements + 1) // 6
    
    actual_sum = 0
    actual_sum_sq = 0
    
    # Calculate actual sum and actual sum of squares from the grid
    for row in grid:
        for val in row:
            actual_sum += val
            actual_sum_sq += val * val
            
    # Let 'a' be the repeated number and 'b' be the missing number.
    # actual_sum - expected_sum = a - b  => (Eq 1)
    # actual_sum_sq - expected_sum_sq = a^2 - b^2 => (Eq 2)
    
    diff_sum = actual_sum - expected_sum  # a - b
    diff_sum_sq = actual_sum_sq - expected_sum_sq  # a^2 - b^2
    
    # Since a^2 - b^2 = (a - b)(a + b), then:
    # (a + b) = (a^2 - b^2) / (a - b)
    sum_ab = diff_sum_sq // diff_sum  # a + b
    
    # Now we have:
    # 1) a - b = diff_sum
    # 2) a + b = sum_ab
    # Adding them: 2a = diff_sum + sum_ab => a = (diff_sum + sum_ab) / 2
    repeated = (diff_sum + sum_ab) // 2
    missing = sum_ab - repeated
    
    return [repeated, missing]
