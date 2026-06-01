METADATA = {
    "id": 2595,
    "name": "Number of Even and Odd Bits",
    "slug": "number_of_even_and_odd_bits",
    "category": "bit_manipulation",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Return counts of set bits at even and odd positions for each number from 0 to n.",
}


def solve(n: int) -> list[list[int]]:
    """Compute the number of set bits at even and odd positions for each integer.

    Args:
        n: The inclusive upper bound of the range (0 <= i <= n).

    Returns:
        A list where the i‑th element is a list [even_count, odd_count] describing
        the number of set bits at even (0‑indexed) and odd positions in the binary
        representation of i.

    Examples:
        >>> solve(2)
        [[0, 0], [1, 0], [0, 1]]
        >>> solve(5)
        [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1], [0, 2]]
    """
    result: list[list[int]] = []
    for number in range(n + 1):
        even_count = 0
        odd_count = 0
        position = 0
        temp = number
        # Count set bits using bitwise operations; each iteration processes one bit.
        while temp:
            if temp & 1:
                if position % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            temp >>= 1
            position += 1
        result.append([even_count, odd_count])
    return result