METADATA = {
    "id": 191,
    "name": "Number of 1 Bits",
    "slug": "number_of_1_bits",
    "category": "Bit Manipulation",
    "aliases": ["Hamming Weight"],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).",
}


def solve(n: int) -> int:
    """
    Calculates the number of set bits (1s) in an integer using Brian Kernighan's algorithm.

    Args:
        n: An unsigned integer.

    Returns:
        The number of '1' bits in the binary representation of n.

    Examples:
        >>> solve(11)
        3
        >>> solve(128)
        1
    """
    set_bits_count = 0
    
    # Brian Kernighan's algorithm: n & (n - 1) clears the least significant set bit.
    # This is more efficient than checking every bit if the number is sparse.
    while n > 0:
        # Clear the lowest set bit
        n &= (n - 1)
        set_bits_count += 1
        
    return set_bits_count

# Note: In Python 3.10+, one could also use n.bit_count() for the same result.