METADATA = {
    "id": 1736,
    "name": "Latest Time by Replacing Hidden Digits",
    "slug": "latest_time_by_replacing_hidden_digits",
    "category": "string",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Replace '?' in a time string to form the latest valid 24‑hour time.",
}


def solve() -> None:
    """Replace hidden digits in a 24‑hour time string with the largest possible digits.

    Args:
        None (reads a single line from standard input).

    Returns:
        None (prints the resulting time string).

    Example:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("2?:?0\\n")
        >>> solve()
        23:50
    """
    import sys

    time_str: str = sys.stdin.readline().strip()
    # Convert to a mutable list of characters for in‑place updates.
    time_chars: list[str] = list(time_str)

    # Position 0: hour tens.
    if time_chars[0] == "?":
        # If hour ones is unknown or can be at most 3, we can set tens to '2'.
        if time_chars[1] == "?" or time_chars[1] <= "3":
            time_chars[0] = "2"
        else:
            time_chars[0] = "1"

    # Position 1: hour ones.
    if time_chars[1] == "?":
        if time_chars[0] == "2":
            time_chars[1] = "3"  # Max hour when tens is 2.
        else:
            time_chars[1] = "9"

    # Position 3: minute tens.
    if time_chars[3] == "?":
        time_chars[3] = "5"  # Minutes tens can be at most 5.

    # Position 4: minute ones.
    if time_chars[4] == "?":
        time_chars[4] = "9"

    result_time: str = "".join(time_chars)
    sys.stdout.write(result_time)