METADATA = {
    "id": 1704,
    "name": "Determine if String Halves Are Alike",
    "slug": "determine_if_string_halves_are_alike",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check whether the two halves of a string contain the same number of vowels.",
}


def solve() -> None:
    """Determine if the two halves of a string are alike.

    The function reads a single line from standard input representing the string
    `s`. It prints ``True`` if the number of vowels in the first half of `s`
    equals the number of vowels in the second half, otherwise it prints ``False``.

    Args:
        None (input is read from ``stdin``).

    Returns:
        None (the result is printed to ``stdout``).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO("book")
        >>> solve()
        True
        >>> sys.stdin = io.StringIO("text")
        >>> solve()
        False
    """
    import sys

    input_line: str = sys.stdin.readline().strip()
    if not input_line:
        return

    s: str = input_line
    length: int = len(s)
    half: int = length // 2
    vowels: set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    first_half_vowel_count: int = 0
    second_half_vowel_count: int = 0

    # Iterate over both halves simultaneously
    for index in range(half):
        if s[index] in vowels:
            first_half_vowel_count += 1
        if s[index + half] in vowels:
            second_half_vowel_count += 1

    result: bool = first_half_vowel_count == second_half_vowel_count
    print(result)