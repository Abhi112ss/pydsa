METADATA = {
    "id": 2213,
    "name": "Longest Substring of One Repeating Character",
    "slug": "longest_substring_of_one_repeating_character",
    "category": "string",
    "aliases": [],
    "tags": ["sliding_window", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a substring consisting of the same character after deleting at most one character.",
}


def solve() -> None:
    """Compute the longest substring of a single repeating character after at most one deletion.

    Args:
        None (input is read from standard input).

    Returns:
        None (the result is printed to standard output).

    Example:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('aaabaaa')
        >>> solve()
        7
    """
    import sys

    input_data: str = sys.stdin.readline().strip()
    if not input_data:
        print(0)
        return

    # Initialize tracking variables for the previous block and the current block.
    previous_char: str = ''
    previous_len: int = 0
    current_char: str = input_data[0]
    current_len: int = 1
    max_length: int = 1

    for index in range(1, len(input_data)):
        char: str = input_data[index]
        if char == current_char:
            # Extend the current block of identical characters.
            current_len += 1
        else:
            # End of the current block; update the maximum length without deletion.
            if current_len > max_length:
                max_length = current_len
            # If the previous block character matches the new character, we can merge
            # the previous block with the current block by deleting the single differing character.
            if previous_char == char:
                merged_len: int = previous_len + current_len
                if merged_len > max_length:
                    max_length = merged_len
            # Shift the current block to become the previous block.
            previous_char = current_char
            previous_len = current_len
            # Start a new current block.
            current_char = char
            current_len = 1

    # Account for the final block after the loop.
    if current_len > max_length:
        max_length = current_len
    # In case the last block can merge with the previous block (handled during the loop),
    # no additional work is needed.

    print(max_length)