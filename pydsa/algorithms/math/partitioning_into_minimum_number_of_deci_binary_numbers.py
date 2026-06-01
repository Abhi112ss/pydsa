METADATA = {
    "id": 1689,
    "name": "Partitioning Into Minimum Number Of Deci-Binary Numbers",
    "slug": "partitioning_into_minimum_number_of_deci_binary_numbers",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of deci-binary numbers required to sum to the given integer.",
}


def solve() -> None:
    """Read an integer and output the minimum number of deci-binary numbers needed.

    Args:
        None (reads from standard input).

    Returns:
        None (writes the result to standard output).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('32')
        >>> solve()
        3
        >>> sys.stdin = io.StringIO('82734')
        >>> solve()
        8
    """
    import sys

    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    number_str = input_data
    # The answer equals the largest digit in the decimal representation.
    max_digit = 0
    for character in number_str:
        digit = ord(character) - ord('0')  # convert char to int without int()
        if digit > max_digit:
            max_digit = digit
            # early exit if we reach 9, the highest possible digit
            if max_digit == 9:
                break

    sys.stdout.write(str(max_digit))