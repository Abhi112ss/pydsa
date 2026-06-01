METADATA = {
    "id": 2614,
    "name": "Prime In Diagonal",
    "slug": "prime_in_diagonal",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(max_val))",
    "space_complexity": "O(1)",
    "description": "Find the maximum prime number located on the diagonals of a square matrix.",
}

def is_prime(n: int) -> bool:
    """Checks if a number is prime.

    Args:
        n: The integer to check.

    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisors up to sqrt(n) using 6k +/- 1 optimization
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solve(grid: list[list[int]]) -> int:
    """Finds the maximum prime number on the diagonals of a square matrix.

    The diagonals include the main diagonal (top-left to bottom-right) 
    and the anti-diagonal (top-right to bottom-left).

    Args:
        grid: A square 2D list of integers.

    Returns:
        The maximum prime number found on the diagonals, or -1 if no prime exists.

    Examples:
        >>> solve([[4, 2, 3], [1, 5, 6], [7, 8, 9]])
        7
        >>> solve([[8, 3, 1], [4, 5, 6], [7, 8, 9]])
        5
        >>> solve([[4, 8, 4], [8, 4, 8], [4, 8, 4]])
        -1
    """
    n = len(grid)
    max_prime = -1

    for i in range(n):
        # The main diagonal element is at grid[i][i]
        # The anti-diagonal element is at grid[i][n - 1 - i]
        
        # Check main diagonal
        main_val = grid[i][i]
        if main_val > max_prime and is_prime(main_val):
            max_prime = main_val
            
        # Check anti-diagonal
        anti_val = grid[i][n - 1 - i]
        if anti_val > max_prime and is_prime(anti_val):
            max_prime = anti_val

    return max_prime
