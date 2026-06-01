METADATA = {
    "id": 3226,
    "name": "Number of Bit Changes to Make Two Integers Equal",
    "slug": "number-of-bit-changes-to-make-two-integers-equal",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "xor"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of bits that need to be flipped to transform one integer into another.",
}

def solve(num1: int, num2: int) -> int:
    """
    Calculates the number of bit changes required to make num1 equal to num2.

    The number of bit changes is equivalent to the number of set bits (1s) 
    in the result of the bitwise XOR operation between the two numbers.

    Args:
        num1: The first integer.
        num2: The second integer.

    Returns:
        The count of differing bits between num1 and num2.

    Examples:
        >>> solve(10, 7)
        3
        # 10 is 1010, 7 is 0111. XOR is 1101 (3 bits set)
        >>> solve(3, 3)
        0
    """
    # The XOR operation results in a 1 at every position where the bits differ
    xor_result = num1 ^ num2
    
    # Count the number of set bits (1s) in the XOR result
    # Using the built-in bit_count() method available in Python 3.10+
    # This is highly optimized and runs in O(1) for fixed-width integers
    return xor_result.bit_count()
