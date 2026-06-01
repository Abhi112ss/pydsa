METADATA = {
    "id": 1922,
    "name": "Count Good Numbers",
    "slug": "count-good-numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "modular_arithmetic", "binary_exponentiation"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of good digit strings of length n where even indices have 5 choices and odd indices have 4 choices, modulo 10^9 + 7.",
}

def solve(n: int) -> int:
    """
    Calculates the number of good digit strings of length n.
    
    A digit string is good if even indices (0, 2, ...) contain even digits (0, 2, 4, 6, 8)
    and odd indices (1, 3, ...) contain prime digits (2, 3, 5, 7).
    There are 5 even digits and 4 prime digits.
    
    Args:
        n: The length of the digit string.
        
    Returns:
        The total number of good digit strings modulo 10^9 + 7.
        
    Examples:
        >>> solve(1)
        5
        >>> solve(4)
        400
    """
    MODULO = 1_000_000_007

    # Number of even indices (0, 2, 4...) in a string of length n
    # If n=1, even_indices=1 (index 0). If n=4, even_indices=2 (indices 0, 2).
    even_indices_count = (n + 1) // 2
    
    # Number of odd indices (1, 3, 5...) in a string of length n
    # If n=1, odd_indices=0. If n=4, odd_indices=2 (indices 1, 3).
    odd_indices_count = n // 2

    def power(base: int, exponent: int) -> int:
        """Performs modular exponentiation using the binary exponentiation algorithm."""
        result = 1
        base %= MODULO
        while exponent > 0:
            # If exponent is odd, multiply result by current base
            if exponent % 2 == 1:
                result = (result * base) % MODULO
            # Square the base and halve the exponent
            base = (base * base) % MODULO
            exponent //= 2
        return result

    # The total count is (5^even_indices) * (4^odd_indices) % MODULO
    # We use modular exponentiation to keep the time complexity O(log n)
    even_part = power(5, even_indices_count)
    odd_part = power(4, odd_indices_count)

    return (even_part * odd_part) % MODULO
