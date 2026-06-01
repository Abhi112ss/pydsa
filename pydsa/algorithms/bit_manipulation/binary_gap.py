METADATA = {
    "id": 868,
    "name": "Binary Gap",
    "slug": "binary_gap",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the longest distance between two consecutive 1's in the binary representation of n.",
}


def solve(n: int) -> int:
    """Return the length of the longest binary gap of a positive integer.

    Args:
        n: A positive integer whose binary representation will be examined.

    Returns:
        The maximum number of bits between two consecutive 1's in the binary
        representation of ``n``. If there is no such pair, returns ``0``.

    Examples:
        >>> solve(22)  # binary: 10110
        2
        >>> solve(8)   # binary: 1000
        0
        >>> solve(5)   # binary: 101
        1
    """
    # Position of the current bit (starting from 0 for the least‑significant bit)
    bit_position: int = 0
    # Position of the most recent encountered 1; -1 indicates none seen yet
    last_one_position: int = -1
    # Maximum gap found so far
    max_gap: int = 0

    while n > 0:
        if n & 1:  # Current bit is 1
            if last_one_position != -1:
                current_gap = bit_position - last_one_position
                if current_gap > max_gap:
                    max_gap = current_gap
            last_one_position = bit_position
        # Move to the next higher bit
        n >>= 1
        bit_position += 1

    return max_gap