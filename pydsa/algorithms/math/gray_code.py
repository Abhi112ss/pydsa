METADATA = {
    "id": 89,
    "name": "Gray Code",
    "slug": "gray-code",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(1)",
    "description": "Generate a sequence of n-bit gray code where adjacent elements differ by exactly one bit.",
}

def solve(n: int) -> list[int]:
    """
    Generates a Gray code sequence of n bits.

    A Gray code is a binary numeral system where two successive values differ 
    in only one bit. The i-th Gray code can be computed using the formula: 
    G(i) = i ^ (i >> 1).

    Args:
        n: The number of bits.

    Returns:
        A list of integers representing the Gray code sequence.

    Examples:
        >>> solve(2)
        [0, 1, 3, 2]
        >>> solve(1)
        [0, 1]
    """
    # The total number of elements in an n-bit Gray code sequence is 2^n
    num_elements = 1 << n
    gray_code_sequence = []

    for i in range(num_elements):
        # The standard formula to convert a binary number to its Gray code equivalent
        # is to XOR the number with itself shifted right by one bit.
        gray_value = i ^ (i >> 1)
        gray_code_sequence.append(gray_value)

    return gray_code_sequence
