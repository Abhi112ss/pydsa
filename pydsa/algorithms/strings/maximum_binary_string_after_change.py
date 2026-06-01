METADATA = {
    "id": 1702,
    "name": "Maximum Binary String After Change",
    "slug": "maximum_binary_string_after_change",
    "category": "string",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Transform the binary string to its lexicographically maximum form using allowed operations.",
}

def maximum_binary_string(binary_string: str) -> str:
    """Return the lexicographically maximum binary string obtainable by applying the
    allowed operations any number of times.

    Args:
        binary_string: A string consisting only of characters '0' and '1'.

    Returns:
        The maximum possible binary string after performing the operations.

    Examples:
        >>> maximum_binary_string("000110")
        '011111'
        >>> maximum_binary_string("1111")
        '1111'
        >>> maximum_binary_string("010")
        '011'
    """
    # Count leading '1's before the first '0'
    leading_one_count = 0
    for character in binary_string:
        if character == '1':
            leading_one_count += 1
        else:
            break

    # If the string contains no '0', it is already maximal
    if leading_one_count == len(binary_string):
        return binary_string

    # The optimal result has exactly one '0' placed after the leading ones,
    # and all remaining positions are '1'.
    total_length = len(binary_string)
    suffix_one_count = total_length - leading_one_count - 1
    return '1' * leading_one_count + '0' + '1' * suffix_one_count

def solve() -> None:
    """Read a binary string from standard input, compute its maximum form,
    and print the result.

    The input consists of a single line containing the binary string.
    """
    import sys

    input_line = sys.stdin.readline()
    binary_string = input_line.strip()
    result_string = maximum_binary_string(binary_string)
    sys.stdout.write(result_string)
