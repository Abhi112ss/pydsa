METADATA = {
    "id": 1318,
    "name": "Minimum Flips to Make a OR b Equal to c",
    "slug": "minimum-flips-to-make-a-or-b-equal-to-c",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of bit flips required to make the bitwise OR of a and b equal to c.",
}

def solve(a: int, b: int, c: int) -> int:
    """
    Calculates the minimum number of bit flips needed to satisfy (a | b) == c.

    Args:
        a: The first integer.
        b: The second integer.
        c: The target integer resulting from (a | b).

    Returns:
        The minimum number of bit flips required.

    Examples:
        >>> solve(2, 6, 5)
        2
        >>> solve(2, 6, 7)
        1
    """
    flips = 0
    
    # We iterate through 31 bits as the problem constraints typically involve 
    # non-negative integers up to 10^9 (which fits in 30 bits).
    for i in range(31):
        # Extract the i-th bit of each number using bitwise AND with a mask
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1

        if bit_c == 0:
            # If target bit is 0, both a and b must be 0.
            # If a is 1, flip it. If b is 1, flip it.
            if bit_a == 1:
                flips += 1
            if bit_b == 1:
                flips += 1
        else:
            # If target bit is 1, at least one of a or b must be 1.
            # If both are 0, we must flip one of them to 1.
            if bit_a == 0 and bit_b == 0:
                flips += 1
                
    return flips
