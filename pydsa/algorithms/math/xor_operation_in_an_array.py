METADATA = {
    "id": 1486,
    "name": "XOR Operation in an Array",
    "slug": "xor_operation_in_an_array",
    "category": "Array",
    "aliases": [],
    "tags": ["bit_manipulation", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compute the cumulative XOR of an arithmetic progression with step 2.",
}


def solve(n: int, start: int) -> int:
    """Compute the XOR of an array defined by start and step 2.

    Args:
        n: The number of elements in the array.
        start: The first element of the array.

    Returns:
        The result of applying the bitwise XOR operation to all elements.

    Examples:
        >>> solve(5, 0)
        8
        >>> solve(4, 3)
        8
    """
    xor_result: int = 0
    for index in range(n):
        current_value: int = start + 2 * index  # generate the arithmetic progression element
        xor_result ^= current_value               # cumulative XOR
    return xor_result