METADATA = {
    "id": 2486,
    "name": "Append Characters to String to Make Subsequence",
    "slug": "append_characters_to_string_to_make_subsequence",
    "category": "string",
    "aliases": [],
    "tags": ["two_pointer", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum number of characters to append to make t a subsequence of s.",
}


def solve() -> None:
    """Read two strings and output the minimum number of characters to append.

    Args:
        None (reads from standard input):
            The first line contains the source string `s`.
            The second line contains the target string `t`.

    Returns:
        None (prints the result):
            An integer representing the minimum number of characters that need to be
            appended to `s` so that `t` becomes a subsequence of the resulting string.

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("coaching\\ncoding\\n")
        >>> solve()
        4
        >>> sys.stdin = io.StringIO("abc\\nabc\\n")
        >>> solve()
        0
    """
    import sys

    data = sys.stdin.read().splitlines()
    if len(data) < 2:
        return
    source_string = data[0].rstrip("\n")
    target_string = data[1].rstrip("\n")

    # Two-pointer scan: advance target pointer when characters match.
    target_index = 0
    for source_char in source_string:
        if target_index < len(target_string) and source_char == target_string[target_index]:
            target_index += 1

    # Characters not matched in target need to be appended.
    characters_to_append = len(target_string) - target_index
    print(characters_to_append)