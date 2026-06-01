METADATA = {
    "id": 2571,
    "name": "Minimum Operations to Reduce an Integer to 0",
    "slug": "minimum_operations_to_reduce_an_integer_to_0",
    "category": "math",
    "aliases": [],
    "tags": ["bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Compute the minimum number of operations to reduce an integer to zero using bit manipulation.",
}


def solve() -> None:
    """Read an integer from standard input and print the minimum number of operations
    required to reduce it to zero.

    The operation count equals the number of set bits in the binary representation of
    the integer.

    Args:
        None.

    Returns:
        None. The result is printed to standard output.

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('5')
        >>> solve()
        2
    """
    import sys

    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return

    number: int = int(input_data[0])

    # Count the number of 1s in the binary representation.
    # Use int.bit_count() when available for O(1) operation.
    if hasattr(int, "bit_count"):
        operation_count: int = number.bit_count()
    else:
        operation_count = bin(number).count('1')

    print(operation_count)