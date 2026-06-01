METADATA = {
    "id": 1460,
    "name": "Make Two Arrays Equal by Reversing Subarrays",
    "slug": "make_two_arrays_equal_by_reversing_subarrays",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if two arrays can be made equal by reversing any subarrays.",
}


import sys
from collections import Counter
from typing import List


def solve() -> None:
    """Read input, determine if two arrays can be made equal by subarray reversals, and print the result.

    Args:
        None (input is read from stdin):
            The first line contains an integer n, the length of the arrays.
            The second line contains n space‑separated integers representing the first array.
            The third line contains n space‑separated integers representing the second array.

    Returns:
        None. Prints "True" if the arrays can be made equal, otherwise "False".

    Examples:
        >>> # Input:
        >>> # 5
        >>> # 1 2 3 4 5
        >>> # 5 4 3 2 1
        >>> # Output:
        >>> # True
        >>> # Explanation: Reversing the whole array makes them equal.
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # First token is the length of the arrays
    n = int(data[0])
    # Next n tokens are the first array
    first_array: List[int] = list(map(int, data[1 : 1 + n]))
    # Remaining n tokens are the second array
    second_array: List[int] = list(map(int, data[1 + n : 1 + 2 * n]))

    # Count occurrences of each element in both arrays
    count_first = Counter(first_array)
    count_second = Counter(second_array)

    # Arrays can be made equal iff their element multisets match
    result = count_first == count_second
    print(result)