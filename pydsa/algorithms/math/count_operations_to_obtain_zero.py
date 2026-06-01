METADATA = {
    "id": 2169,
    "name": "Count Operations to Obtain Zero",
    "slug": "count_operations_to_obtain_zero",
    "category": "math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Return the number of operations required to reduce either of two integers to zero by repeatedly subtracting the smaller from the larger.",
}


def _count_operations(num1: int, num2: int) -> int:
    """Calculate the number of subtraction operations until one number becomes zero.

    The naive approach subtracts the smaller number from the larger one repeatedly,
    which can be accelerated by using integer division to count multiple subtractions
    at once (the Euclidean algorithm).

    Args:
        num1: First non‑negative integer.
        num2: Second non‑negative integer.

    Returns:
        The total count of subtraction operations required to make either integer zero.

    Examples:
        >>> _count_operations(2, 3)
        3
        >>> _count_operations(10, 10)
        1
    """
    operation_count = 0
    a, b = num1, num2

    # Continue until one of the numbers becomes zero.
    while a != 0 and b != 0:
        if a >= b:
            # a can be reduced by b multiple times; each subtraction counts as an operation.
            operation_count += a // b
            a %= b
        else:
            operation_count += b // a
            b %= a

    return operation_count


def solve() -> None:
    """Read two integers from standard input, compute and print the operation count.

    Input format:
        Two space‑separated integers on a single line.

    Output format:
        A single integer representing the number of operations.

    Example:
        Input: 2 3
        Output: 3
    """
    import sys

    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    num1, num2 = map(int, data[:2])
    result = _count_operations(num1, num2)
    sys.stdout.write(str(result))