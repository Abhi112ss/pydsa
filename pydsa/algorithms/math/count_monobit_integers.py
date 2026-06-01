METADATA = {
    "id": 3827,
    "name": "Count Monobit Integers",
    "slug": "count-monobit-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Count how many integers from 1 to n are monobit integers (integers whose binary representation contains exactly one '1').",
}

def solve(n: int) -> int:
    """
    Counts the number of monobit integers in the range [1, n].
    
    A monobit integer is defined as an integer whose binary representation 
    contains exactly one '1'. These are exactly the powers of 2 (1, 2, 4, 8, ...).

    Args:
        n: The upper bound of the range (inclusive).

    Returns:
        The count of monobit integers between 1 and n.

    Examples:
        >>> solve(1)
        1
        >>> solve(3)
        2
        >>> solve(10)
        4
    """
    if n <= 0:
        return 0

    count = 0
    current_power_of_two = 1
    
    # Iterate through powers of 2: 1, 2, 4, 8...
    # As long as the power of 2 is less than or equal to n, it is a monobit integer.
    while current_power_of_two <= n:
        count += 1
        # Bitwise shift left is equivalent to multiplying by 2
        current_power_of_two <<= 1
        
    return count
