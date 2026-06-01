METADATA = {
    "id": 1664,
    "name": "Ways to Make a Fair Array",
    "slug": "ways_to_make_a_fair_array",
    "category": "array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count indices whose removal makes the array fair (equal even/odd sums).",
}

import sys

def solve() -> None:
    """Count the number of indices whose removal makes the array fair.

    The function reads a single line from standard input containing space‑separated
    integers representing the array `nums`. It prints the count of indices `i` such that
    after removing `nums[i]` the sum of elements at even positions equals the sum of
    elements at odd positions in the resulting array.

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Example:
        >>> # input
        >>> 2 1 6 4
        >>> # output
        >>> 1
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = [int(x) for x in data]

    total_even_sum = 0
    total_odd_sum = 0
    for index, value in enumerate(nums):
        if index % 2 == 0:
            total_even_sum += value
        else:
            total_odd_sum += value

    prefix_even_sum = 0
    prefix_odd_sum = 0
    fair_count = 0

    for index, value in enumerate(nums):
        # Suffix sums exclude the current element
        if index % 2 == 0:
            suffix_even_sum = total_even_sum - prefix_even_sum - value
            suffix_odd_sum = total_odd_sum - prefix_odd_sum
        else:
            suffix_even_sum = total_even_sum - prefix_even_sum
            suffix_odd_sum = total_odd_sum - prefix_odd_sum - value

        # After removal, elements after index shift parity:
        #   original odd positions become even, original even become odd
        new_even_sum = prefix_even_sum + suffix_odd_sum
        new_odd_sum = prefix_odd_sum + suffix_even_sum

        if new_even_sum == new_odd_sum:
            fair_count += 1

        # Update prefix sums for next iteration
        if index % 2 == 0:
            prefix_even_sum += value
        else:
            prefix_odd_sum += value

    print(fair_count)
