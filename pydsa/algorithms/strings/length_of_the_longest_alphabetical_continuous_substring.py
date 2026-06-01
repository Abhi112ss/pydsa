METADATA = {
    "id": 2414,
    "name": "Length of the Longest Alphabetical Continuous Substring",
    "slug": "length_of_the_longest_alphabetical_continuous_substring",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the length of the longest substring where each character follows the previous one alphabetically.",
}


def solve() -> None:
    """Read a lowercase string from standard input and print the length of the longest
    alphabetical continuous substring.

    Args:
        None (input is read from stdin).

    Returns:
        None (the result is printed to stdout).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('abczab')
        >>> solve()
        3
        >>> sys.stdin = io.StringIO('abc')
        >>> solve()
        3
    """
    import sys

    input_data = sys.stdin.read().strip()
    if not input_data:
        print(0)
        return

    max_length = 1
    current_length = 1

    # Iterate through the string, comparing each character with its predecessor.
    for index in range(1, len(input_data)):
        if ord(input_data[index]) - ord(input_data[index - 1]) == 1:
            # Characters are consecutive in the alphabet; extend the current window.
            current_length += 1
        else:
            # Break in continuity; start a new window from the current character.
            current_length = 1
        # Update the maximum length found so far.
        if current_length > max_length:
            max_length = current_length

    print(max_length)