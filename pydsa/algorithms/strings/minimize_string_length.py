METADATA = {
    "id": 2716,
    "name": "Minimize String Length",
    "slug": "minimize_string_length",
    "category": "algorithms",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimal possible length after repeatedly deleting any two adjacent different characters.",
}


def solve() -> None:
    """Read a string from standard input and print the minimal possible length.

    The operation allowed is to delete any two adjacent characters that are
    different. Repeating this operation optimally reduces the string to a form
    where all remaining characters are identical.

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Example:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('aabbbc')
        >>> solve()
        1
    """
    import sys

    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    # Count frequency of each character (only lowercase letters are possible)
    frequency = [0] * 26  # fixed size for O(1) extra space
    for ch in input_data:
        frequency[ord(ch) - ord('a')] += 1

    total_length = len(input_data)
    max_freq = max(frequency)

    # After cancelling pairs of different characters, the remaining length is
    # the excess of the most frequent character over all others.
    minimal_length = max(0, 2 * max_freq - total_length)

    print(minimal_length)
