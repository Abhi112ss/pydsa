METADATA = {
    "id": 1652,
    "name": "Defuse the Bomb",
    "slug": "defuse_the_bomb",
    "category": "array",
    "aliases": [],
    "tags": ["sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of bombs to defuse so that the sum of remaining bombs does not exceed the given power.",
}


def solve() -> None:
    """Read input, compute and print the minimum number of bombs to defuse.

    Args:
        Input is read from standard input.
        The first line contains an integer `power`.
        The second line contains space‑separated integers representing `bombs`.

    Returns:
        Prints a single integer – the minimum number of bombs that must be
        defused.

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("10\\n2 3 5 7")
        >>> solve()
        2
        >>> sys.stdin = io.StringIO("100\\n1 2 3")
        >>> solve()
        0
    """
    import sys

    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    power = int(data[0].strip())
    bombs = list(map(int, data[1].strip().split())) if len(data) > 1 else []

    n = len(bombs)
    if n == 0:
        print(0)
        return

    total_sum = sum(bombs)
    # If the whole array already satisfies the power constraint, no bomb needs to be defused.
    if total_sum <= power:
        print(0)
        return

    max_keep_len = 0
    current_sum = 0
    left = 0

    # Iterate over a virtual doubled array to handle circular subarrays.
    for right in range(2 * n):
        current_sum += bombs[right % n]

        # Shrink window from the left while the sum exceeds the allowed power.
        while current_sum > power and left <= right:
            current_sum -= bombs[left % n]
            left += 1

        window_len = right - left + 1
        # Only consider windows up to length n (cannot keep more than all bombs).
        if window_len > max_keep_len and window_len <= n:
            max_keep_len = window_len

    # Minimum bombs to defuse = total bombs - maximum keepable contiguous segment.
    result = n - max_keep_len
    print(result)