METADATA = {
    "id": 190,
    "name": "Reverse Bits",
    "slug": "reverse_bits",
    "category": "bit_manipulation",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Reverse bits of a given 32 bits unsigned integer.",
}


def solve(n: int) -> int:
    """
    Reverses the bits of a 32-bit unsigned integer.

    Args:
        n: A 32-bit unsigned integer.

    Returns:
        The integer formed by reversing the bits of n.

    Examples:
        >>> solve(43261596)
        964176192
        >>> solve(0b00000010100101000001111010011100)
        964176192
    """
    reversed_num = 0
    
    # Iterate through all 32 bits of the input integer
    for _ in range(32):
        # Shift the result to the left to make space for the next bit
        reversed_num <<= 1
        
        # Extract the least significant bit of n and add it to the result
        reversed_num |= (n & 1)
        
        # Shift n to the right to process the next bit in the next iteration
        n >>= 1
        
    return reversed_num
