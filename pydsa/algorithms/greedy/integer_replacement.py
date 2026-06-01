METADATA = {
    "id": 397,
    "name": "Integer Replacement",
    "slug": "integer-replacement",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to transform an integer n to 1 using specific increment/decrement rules.",
}

def solve(n: int) -> int:
    """
    Calculates the minimum number of operations to reduce n to 1.
    
    Operations allowed:
    1. If n is even, replace n with n / 2.
    2. If n is odd, replace n with either n + 1 or n - 1.

    Args:
        n: The starting integer.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve(7)
        4
        >>> solve(8)
        3
    """
    operations = 0
    current_n = n

    while current_n > 1:
        if current_n % 2 == 0:
            # If even, the only optimal move is division
            current_n //= 2
        else:
            # If odd, we decide whether to add 1 or subtract 1.
            # The goal is to make the next number divisible by 4 to maximize 
            # the number of subsequent divisions by 2.
            
            # Special case: 3 is better handled by subtracting 1 (3 -> 2 -> 1)
            # rather than adding 1 (3 -> 4 -> 2 -> 1), even though 4 is divisible by 4.
            if current_n == 3:
                current_n -= 1
            # Check if (n + 1) results in a number divisible by 4 using bitwise logic
            elif (current_n + 1) % 4 == 0:
                current_n += 1
            else:
                current_n -= 1
        
        operations += 1

    return operations
