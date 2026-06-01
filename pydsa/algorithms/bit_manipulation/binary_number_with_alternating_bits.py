METADATA = {
    "id": 693,
    "name": "Binary Number with Alternating Bits",
    "slug": "binary_number_with_alternating_bits",
    "category": "Bit Manipulation",
    "aliases": ["has_alternating_bits", "alternating_bits"],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits always have different values.",
}


def solve(n: int) -> bool:
    """Determine if a positive integer has alternating bits in its binary representation.

    A number has alternating bits if no two adjacent bits in its binary
    representation are the same (e.g., 1010 or 101).

    Algorithm: XOR n with n >> 1. If bits alternate, the XOR result is all 1s.
    Then check that result + 1 is a power of 2 (single bit set).

    Args:
        n: A positive integer to check.

    Returns:
        True if n has alternating bits, False otherwise.

    Examples:
        >>> solve(5)
        True
        >>> solve(7)
        False
        >>> solve(10)
        True
        >>> solve(11)
        False
    """
    # XOR n with itself shifted right by 1: alternating bits produce all 1s
    xor_result = n ^ (n >> 1)

    # A number that is all 1s in binary has the property that
    # adding 1 produces a power of 2 (single bit), so AND with itself is 0
    return (xor_result & (xor_result + 1)) == 0