METADATA = {
    "id": 172,
    "name": "Factorial Trailing Zeroes",
    "slug": "factorial-trailing-zeroes",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Given an integer n, return the number of trailing zeroes in n!.",
}

def solve(n: int) -> int:
    """
    Counts the number of trailing zeros in n! by counting factors of 5.
    
    Args:
        n: The integer to compute factorial trailing zeroes for.
        
    Returns:
        The number of trailing zeroes in n!.
        
    Examples:
        >>> solve(3)
        0
        >>> solve(5)
        1
        >>> solve(25)
        6
    """
    count = 0
    divisor = 5
    
    # Count multiples of 5, 25, 125, etc. until divisor exceeds n
    while divisor <= n:
        count += n // divisor
        divisor *= 5  # Move to next power of 5
    
    return count