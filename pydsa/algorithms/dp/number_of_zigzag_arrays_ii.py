METADATA = {
    "id": 3700,
    "name": "Number of ZigZag Arrays II",
    "slug": "number_of_zigzag_arrays_ii",
    "category": "dynamic_programming",
    "aliases": [],
    "tags": ["dp", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(m)",
    "description": "Counts length‑n arrays with values 1..m that alternate between increasing and decreasing.",
}

def solve() -> None:
    """Counts the number of zigzag arrays of length ``n`` with values in ``[1, m]``.

    A zigzag array satisfies:
        a1 < a2 > a3 < a4 > a5 < ...

    Args:
        n (int): length of the array.
        m (int): maximum value (minimum is 1).

    Returns:
        None: prints the count modulo 10**9+7.

    Example:
        >>> # input: 2 3
        >>> # possible arrays: [1,2], [1,3], [2,3]
        >>> # output: 3
        >>> # run:
        >>> # echo "2 3" | python solution.py
        3
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    MOD = 10**9 + 7

    # dp_up[v]  – number of arrays of current length ending with value v
    #             where the last relation is "up" (previous < v).
    # dp_down[v] – similar, but last relation is "down" (previous > v).
    dp_up = [1] * (m + 1)   # length 1, treat as both up and down
    dp_down = [1] * (m + 1)

    for length in range(2, n + 1):
        if length % 2 == 0:  # need an "up" relation at the end
            # prefix sums of dp_down allow O(1) range sum for k < v
            prefix = [0] * (m + 2)
            for value in range(1, m + 1):
                prefix[value] = (prefix[value - 1] + dp_down[value]) % MOD
            new_up = [0] * (m + 1)
            for value in range(1, m + 1):
                new_up[value] = prefix[value - 1]  # sum_{k < value} dp_down[k]
            dp_up = new_up
            # dp_down remains unchanged; it will be used when the next length needs a "down"
        else:  # need a "down" relation at the end
            # suffix sums of dp_up allow O(1) range sum for k > v
            suffix = [0] * (m + 2)
            for value in range(m, 0, -1):
                suffix[value] = (suffix[value + 1] + dp_up[value]) % MOD
            new_down = [0] * (m + 1)
            for value in range(1, m + 1):
                new_down[value] = suffix[value + 1]  # sum_{k > value} dp_up[k]
            dp_down = new_down
            # dp_up stays unchanged for the next iteration

    if n % 2 == 0:
        answer = sum(dp_up[1:]) % MOD
    else:
        answer = sum(dp_down[1:]) % MOD

    print(answer)
