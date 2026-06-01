METADATA = {
    "id": 338,
    "name": "Counting Bits",
    "slug": "counting_bits",
    "category": "Algorithms",
    "aliases": ["count bits", "counting bits"],
    "tags": ["dynamic_programming", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an integer n, return an array of length n + 1 where each element at index i is the number of 1's in the binary representation of i.",
}

def solve(n: int) -> list[int]:
    """Return an array where ans[i] is the number of 1-bits in the binary representation of i, for 0 <= i <= n.

    Uses the DP relation: bits[i] = bits[i >> 1] + (i & 1).
    The number of set bits in i equals the number of set bits in i // 2 (right-shifted by 1),
    plus 1 if the least significant bit is set.

    Args:
        n: A non-negative integer representing the upper bound of the range [0, n].

    Returns:
        A list of length n + 1 where each element is the popcount of its index.

    Examples:
        >>> solve(2)
        [0, 1, 1]
        >>> solve(5)
        [0, 1, 1, 2, 1, 2]
        >>> solve(0)
        [0]
    """
    bits = [0] * (n + 1)

    for i in range(1, n + 1):
        # bits[i >> 1] is already computed since i >> 1 < i; add 1 if the lowest bit is set
        bits[i] = bits[i >> 1] + (i & 1)

    return bits