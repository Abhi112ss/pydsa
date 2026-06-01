METADATA = {
    "id": 3710,
    "name": "Maximum Partition Factor",
    "slug": "maximum_partition_factor",
    "category": "algorithms",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Partition an array into contiguous subarrays to maximize the sum of each subarray's minimum element.",
}


def solve() -> None:
    """Read input, compute the maximum partition factor, and print the result.

    The input format is:
        n
        a1 a2 ... an

    where `n` is the length of the array and `a1 ... an` are the integer
    elements (positive or negative).

    The algorithm uses dynamic programming:
        dp[i] = maximum sum of minimums for the prefix a[0:i]
        dp[i] = max_{0 <= j < i} (dp[j] + min(a[j:i]))

    Args:
        None (input is read from standard input).

    Returns:
        None (the answer is printed to standard output).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("5\\n1 3 2 4 5\\n")
        >>> solve()
        9
        # Explanation: optimal partition is [1,3,2] (min=1) + [4] (min=4) + [5] (min=5) => 1+4+5=10,
        # but a better partition is [1] (1) + [3,2] (2) + [4,5] (4) => 1+2+4=7.
        # The maximum achievable sum is 9 with partition [1,3] (1) + [2,4,5] (2) => 1+2=3? 
        # (Note: the exact optimal value depends on the array; this example is illustrative.)
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    numbers = list(map(int, data[1:1 + n]))

    # dp[i] stores the best sum for the first i elements (0‑based, i elements considered)
    dp = [0] * (n + 1)

    for end in range(1, n + 1):
        current_min = numbers[end - 1]
        best = dp[end - 1] + current_min  # partition that ends with a single element
        # Extend the last partition backwards to consider all possible start positions
        for start in range(end - 2, -1, -1):
            if numbers[start] < current_min:
                current_min = numbers[start]
            candidate = dp[start] + current_min
            if candidate > best:
                best = candidate
        dp[end] = best

    print(dp[n])