METADATA = {
    "id": 476,
    "name": "Number Complement",
    "slug": "number_complement",
    "category": "bit_manipulation",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the complement of an integer's binary representation."
}

def _find_complement(number: int) -> int:
    """Return the bitwise complement of ``number`` within its bit-length.

    Args:
        number: A non‑negative integer.

    Returns:
        The integer representing the complement of ``number``'s binary form.

    Examples:
        >>> _find_complement(5)
        2
        >>> _find_complement(1)
        0
    """
    if number == 0:
        # Edge case: binary representation is "0", complement should be "1"
        return 1
    # Create a mask with all bits set to 1 that matches the length of ``number``.
    mask = (1 << number.bit_length()) - 1
    # XOR with the mask flips all bits, yielding the complement.
    return mask ^ number

def solve() -> None:
    """Read an integer from standard input, print its complement.

    The function follows the optimal O(1) time and O(1) space algorithm
    by constructing a bitmask of the same length as the input number
    and applying XOR.

    Example:
        Input: 5
        Output: 2
    """
    import sys
    data = sys.stdin.read().strip()
    if not data:
        return
    try:
        input_number = int(data)
    except ValueError:
        # If the input cannot be parsed as an integer, do nothing.
        return
    result = _find_complement(input_number)
    sys.stdout.write(str(result))
