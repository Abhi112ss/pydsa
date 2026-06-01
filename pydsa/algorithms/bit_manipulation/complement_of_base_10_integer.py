METADATA = {
    "id": 1009,
    "name": "Complement of Base 10 Integer",
    "slug": "complement_of_base_10_integer",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Return the bitwise complement of a positive integer.",
}


def solve() -> None:
    """Read an integer from standard input and output its bitwise complement.

    The complement is obtained by flipping all bits of the binary representation
    of the number, excluding any leading zeros.

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Examples:
        >>> # Input: 5
        >>> # Output: 2
        >>> # Explanation: 5 in binary is 101, its complement is 010 which is 2.
        >>> # Input: 1
        >>> # Output: 0
        >>> # Explanation: 1 in binary is 1, complement is 0.
    """
    import sys

    raw_input = sys.stdin.read().strip()
    if not raw_input:
        return

    number = int(raw_input)

    # Edge case: complement of 0 is defined as 1 (binary "0" -> "1")
    if number == 0:
        print(1)
        return

    # Determine the length of the binary representation (without leading zeros)
    bit_length = number.bit_length()

    # Create a mask consisting of all 1s with the same bit length
    mask = (1 << bit_length) - 1

    # XOR with the mask flips all bits, yielding the complement
    complement = mask ^ number

    print(complement)