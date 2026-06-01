METADATA = {
    "id": 2645,
    "name": "Minimum Additions to Make Valid String",
    "slug": "minimum_additions_to_make_valid_string",
    "category": "greedy",
    "aliases": [],
    "tags": ["greedy", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of insertions needed so that no two adjacent characters in the string are equal.",
}


def solve() -> None:
    """Read a string from standard input and output the minimum number of insertions
    required to make it valid (no two adjacent characters are the same).

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("aab")
        >>> solve()
        1
        >>> sys.stdin = io.StringIO("ababa")
        >>> solve()
        0
    """
    import sys

    input_data = sys.stdin.read().splitlines()
    if not input_data:
        print(0)
        return

    s = input_data[0].strip()
    if not s:
        print(0)
        return

    additions_needed = 0
    previous_char = s[0]

    # Iterate over the string, counting each occurrence where the current character
    # equals the previous one. Each such case requires one insertion to break the
    # adjacency, which is optimal because inserting any character other than the
    # opposite would not reduce future conflicts.
    for current_char in s[1:]:
        if current_char == previous_char:
            additions_needed += 1
        previous_char = current_char

    print(additions_needed)