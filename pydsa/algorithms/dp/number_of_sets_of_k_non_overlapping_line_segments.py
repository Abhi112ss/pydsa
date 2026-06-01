METADATA = {
    "id": 1621,
    "name": "Number of Sets of K Non-Overlapping Line Segments",
    "slug": "number_of_sets_of_k_non_overlapping_line_segments",
    "category": "algorithms",
    "aliases": [],
    "tags": ["dynamic_programming", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n*k)",
    "space_complexity": "O(n*k)",
    "description": "Count the ways to choose k non‑overlapping segments from a given list of intervals.",
}


import sys
from bisect import bisect_right
from typing import List, Tuple

MOD = 10**9 + 7


def solve() -> None:
    """
    Reads input, computes the number of ways to select k non‑overlapping line segments,
    and prints the result modulo 1_000_000_007.

    Input format (space‑separated integers):
        n k m
        start_1 end_1
        start_2 end_2
        ...
        start_m end_m

    where:
        n – maximum coordinate value (unused in the algorithm),
        k – required number of non‑overlapping segments,
        m – number of given intervals,
        start_i, end_i – inclusive bounds of the i‑th interval.

    Returns:
        None (the answer is printed to stdout).

    Example:
        Input:
            10 2 3
            1 2
            2 3
            4 5
        Output:
            2
    """
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return

    n, k, m = data[0], data[1], data[2]
    intervals: List[Tuple[int, int]] = [
        (data[3 + 2 * i], data[3 + 2 * i + 1]) for i in range(m)
    ]

    # Sort intervals by their ending coordinate to enable binary search on non‑overlap.
    intervals.sort(key=lambda x: x[1])

    # Extract ends for binary search.
    ends = [end for _, end in intervals]

    # prev_index[i] = largest index j (< i) such that intervals[j].end < intervals[i].start
    prev_index: List[int] = []
    for start, _ in intervals:
        # bisect_right returns the insertion point; subtract 1 gives the last end <= start-1.
        j = bisect_right(ends, start - 1) - 1
        prev_index.append(j)

    # dp[i][j] = number of ways to pick j segments from first i intervals (1‑based indexing).
    dp: List[List[int]] = [[0] * (k + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1  # One way to choose zero segments.

    for i in range(1, m + 1):
        for seg_count in range(1, k + 1):
            # Exclude current interval.
            exclude = dp[i - 1][seg_count]
            # Include current interval if a compatible previous interval exists.
            include = 0
            prev = prev_index[i - 1]
            if prev != -1:
                include = dp[prev + 1][seg_count - 1]
            else:
                # No previous interval, can only start a new set if seg_count == 1.
                if seg_count == 1:
                    include = 1
            dp[i][seg_count] = (exclude + include) % MOD

    print(dp[m][k] % MOD)
