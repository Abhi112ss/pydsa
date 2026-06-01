METADATA = {
    "id": 2443,
    "name": "Sum of Number and Its Reverse",
    "slug": "sum_of_number_and_its_reverse",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Return the sum of a number and its digit-reversed counterpart.",
}


def solve() -> None:
    """Read an integer, compute the sum of the number and its reverse, and print it.

    Args:
        None (input is read from standard input).

    Returns:
        None (the result is printed to standard output).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('123')
        >>> solve()
        444
        >>> sys.stdin = io.StringIO('120')
        >>> solve()
        141
    """
    import sys

    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    number = int(input_data)

    # Compute the reversed number using digit extraction.
    reversed_number = 0
    temp = number
    while temp > 0:
        digit = temp % 10               # extract the least‑significant digit
        reversed_number = reversed_number * 10 + digit  # build the reversed number
        temp //= 10                     # remove the processed digit

    result = number + reversed_number
    print(result)