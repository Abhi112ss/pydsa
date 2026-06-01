METADATA = {
    "id": 2180,
    "name": "Count Integers With Even Digit Sum",
    "slug": "count_integers_with_even_digit_sum",
    "category": "math",
    "aliases": [],
    "tags": ["math", "digit_dp"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Count numbers in [1, num] whose digit sum is even.",
}


def solve() -> None:
    """Count integers with an even digit sum.

    Args:
        None (reads from standard input).

    Returns:
        None (writes the answer to standard output).

    Example:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('30')
        >>> solve()
        15
    """
    import sys
    from functools import lru_cache

    data = sys.stdin.read().strip()
    if not data:
        return
    num: int = int(data)

    digits: list[int] = [int(ch) for ch in str(num)]

    @lru_cache(maxsize=None)
    def dfs(position: int, parity: int, tight: bool) -> int:
        """Return count of numbers for suffix starting at position with given parity.

        parity: 0 if current digit sum is even, 1 if odd.
        tight: True if prefix equals num's prefix so far.
        """
        if position == len(digits):
            # reached the end; count this number if digit sum is even
            return 1 if parity == 0 else 0

        limit: int = digits[position] if tight else 9
        total: int = 0
        for digit in range(0, limit + 1):
            new_parity: int = (parity + digit) & 1  # update parity modulo 2
            total += dfs(position + 1, new_parity, tight and digit == limit)
        return total

    # Count numbers in [0, num] with even digit sum, then exclude 0
    count_even_up_to_num: int = dfs(0, 0, True) - 1
    sys.stdout.write(str(count_even_up_to_num))
