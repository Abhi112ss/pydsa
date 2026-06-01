METADATA = {
    "id": 762,
    "name": "Prime Number of Set Bits in Binary Representation",
    "slug": "prime_number_of_set_bits_in_binary_representation",
    "category": "math",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(R - L)",
    "space_complexity": "O(1)",
    "description": "Count numbers in a range whose binary representation contains a prime number of set bits.",
}


def solve(left: int, right: int) -> int:
    """Count integers in the inclusive range [left, right] whose binary representation
    contains a prime number of set bits.

    Args:
        left: The lower bound of the range (inclusive).
        right: The upper bound of the range (inclusive).

    Returns:
        The count of numbers whose number of 1‑bits is a prime.

    Examples:
        >>> solve(6, 10)
        4
        >>> solve(10, 15)
        5
    """
    # Prime numbers that can appear as a count of set bits for 32‑bit integers.
    prime_set_bits = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
    qualifying_count = 0

    for number in range(left, right + 1):
        # Use the built‑in bit_count method for fast popcount.
        if number.bit_count() in prime_set_bits:
            qualifying_count += 1

    return qualifying_count