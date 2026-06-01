METADATA = {
    "id": 371,
    "name": "Sum of Two Integers",
    "slug": "sum-of-two-integers",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "bitwise_operators"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of two integers without using the + or - operators.",
}

def solve(a: int, b: int) -> int:
    """
    Calculates the sum of two integers using bitwise operations.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.

    Examples:
        >>> solve(1, 2)
        3
        >>> solve(2, 3)
        5
        >>> solve(-1, 1)
        0
    """
    # Python integers have arbitrary precision, so we must simulate 
    # 32-bit signed integer behavior using a mask.
    mask = 0xFFFFFFFF
    
    while b & mask != 0:
        # XOR calculates the sum of bits where no carry is involved.
        sum_without_carry = a ^ b
        
        # AND followed by a left shift calculates the carry bits.
        carry = (a & b) << 1
        
        a = sum_without_carry
        b = carry

    # If 'a' is within the positive range of a 32-bit signed integer, return it.
    # Otherwise, convert the 32-bit unsigned representation back to a signed integer.
    # 0x7FFFFFFF is the maximum positive value for a 32-bit signed integer.
    return a & mask if b > 0 else a if a <= 0x7FFFFFFF else ~(a ^ mask)

# Note: The logic above handles Python's infinite bit length by masking to 32 bits.
# To correctly handle negative numbers in Python's bitwise logic:
def solve_refined(a: int, b: int) -> int:
    """
    Refined version to handle Python's arbitrary precision integers for 32-bit simulation.
    """
    mask = 0xFFFFFFFF
    
    while b != 0:
        # Calculate carry and sum using 32-bit mask to prevent infinite loops with negatives
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
        
    # If a is greater than the max signed 32-bit int, it represents a negative number
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

# Re-assigning solve to the refined version for production-grade correctness in Python
solve = solve_refined