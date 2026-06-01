METADATA = {
    "id": 1071,
    "name": "Greatest Common Divisor of Strings",
    "slug": "greatest_common_divisor_of_strings",
    "category": "String",
    "aliases": [],
    "tags": ["math", "strings", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Return the longest string that can be concatenated multiple times to form both input strings.",
}


import sys
import math
from typing import Tuple


def solve() -> None:
    """Read two strings from standard input and print their greatest common divisor string.

    Args:
        None (reads from stdin).

    Returns:
        None (writes result to stdout).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("ABCABC\\nABC")
        >>> solve()
        ABC
        >>> sys.stdin = io.StringIO("ABABAB\\nABAB")
        >>> solve()
        AB
        >>> sys.stdin = io.StringIO("LEET\\nCODE")
        >>> solve()
        <empty line>
    """
    data: Tuple[str, ...] = tuple(line.rstrip("\n") for line in sys.stdin.readlines())
    if len(data) < 2:
        return
    first_string: str = data[0]
    second_string: str = data[1]

    # If concatenations differ, no common divisor exists.
    if first_string + second_string != second_string + first_string:
        print("")
        return

    # Length of the GCD string is the greatest common divisor of the lengths.
    divisor_length: int = math.gcd(len(first_string), len(second_string))
    gcd_string: str = first_string[:divisor_length]
    print(gcd_string)