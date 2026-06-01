METADATA = {
    "id": 1051,
    "name": "Height Checker",
    "slug": "height_checker",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array_comparison"],
    "difficulty": "Easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count how many students are not in the correct position compared to the sorted order.",
}


def solve() -> None:
    """Read a list of integers representing heights from standard input and print the number of indices where the height differs from the sorted order.

    Args:
        None (input is read from stdin).

    Returns:
        None. The result is printed to stdout.

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('1 1 4 2 1 3')
        >>> solve()
        3
    """
    import sys

    # Read all integers from stdin; if no input, exit early.
    raw_tokens = sys.stdin.read().strip().split()
    if not raw_tokens:
        return

    # Convert tokens to a list of heights.
    heights: list[int] = list(map(int, raw_tokens))

    # Obtain the sorted order of heights.
    sorted_heights: list[int] = sorted(heights)

    # Count positions where the original height differs from the sorted height.
    mismatch_count: int = sum(
        1 for original, sorted_val in zip(heights, sorted_heights) if original != sorted_val
    )

    # Output the result.
    print(mismatch_count)