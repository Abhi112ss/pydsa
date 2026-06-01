METADATA = {
    "id": 1165,
    "name": "Single-Row Keyboard",
    "slug": "single_row_keyboard",
    "category": "string",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total time to type a word on a single-row keyboard.",
}

def solve() -> None:
    """Read a keyboard layout and a word from standard input and print the total typing time.

    Args:
        None (input is read from stdin):
            - First line: a string `keyboard` representing the layout of the single-row keyboard.
            - Second line: a string `word` to be typed.

    Returns:
        None (the result is printed to stdout).

    Example:
        >>> # input
        >>> abcdefghijklmnopqrstuvwxyz
        >>> cba
        >>> # output
        >>> 4
    """
    import sys

    data = sys.stdin.read().splitlines()
    if len(data) < 2:
        return
    keyboard: str = data[0].strip()
    word: str = data[1].strip()

    # Build an array mapping each character to its index on the keyboard.
    # Since the keyboard contains only lowercase letters, a fixed-size list of 26 elements suffices.
    char_positions: list[int] = [0] * 26
    for index, char in enumerate(keyboard):
        char_positions[ord(char) - ord('a')] = index

    total_time: int = 0
    previous_index: int = 0  # start at the first character of the keyboard (index 0)

    for char in word:
        current_index: int = char_positions[ord(char) - ord('a')]
        total_time += abs(current_index - previous_index)
        previous_index = current_index

    print(total_time)
