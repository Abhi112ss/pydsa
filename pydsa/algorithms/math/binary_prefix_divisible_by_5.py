METADATA = {
    "id": 1018,
    "name": "Binary Prefix Divisible By 5",
    "slug": "binary_prefix_divisible_by_5",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return a list indicating whether each binary prefix of the input array is divisible by 5.",
}


def solve(arr: list[int]) -> list[bool]:
    """Determine divisibility of binary prefixes by 5.

    Args:
        arr: A list of integers containing only 0s and 1s representing a binary number.

    Returns:
        A list of booleans where the i‑th element is True if the binary number formed by
        the first i+1 bits of `arr` is divisible by 5, otherwise False.

    Examples:
        >>> solve([0,1,1])
        [True, False, False]
        >>> solve([1,1,1,0,1])
        [False, False, False, False, True]
    """
    result: list[bool] = []
    current_mod: int = 0

    for bit in arr:
        # Update the remainder of the current prefix modulo 5.
        current_mod = (current_mod * 2 + bit) % 5
        # The prefix is divisible by 5 iff the remainder is zero.
        result.append(current_mod == 0)

    return result