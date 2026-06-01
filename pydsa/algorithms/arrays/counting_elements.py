METADATA = {
    "id": 1426,
    "name": "Counting Elements",
    "slug": "counting_elements",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count elements that have a strictly greater element in the array.",
}


def solve() -> None:
    """Read an integer array from standard input and print the count of elements
    that have a strictly greater element elsewhere in the array.

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Examples:
        >>> # Input: 1 2 3
        >>> # Output: 2
        >>> # Explanation: 1 and 2 each have a greater element (2 and 3).
        >>> import sys, io
        >>> sys.stdin = io.StringIO("1 2 3")
        >>> solve()
        2
    """
    import sys

    # Read all integers from stdin; an empty line yields an empty list.
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        print(0)
        return
    nums = list(map(int, raw_input.split()))

    # Build a hash set for O(1) membership checks.
    unique_values = set(nums)

    # Count each element that has a value exactly one greater present.
    # This condition is sufficient because any strictly greater element
    # implies the existence of some element equal to x + 1 in the set.
    count = sum(1 for value in nums if (value + 1) in unique_values)

    print(count)