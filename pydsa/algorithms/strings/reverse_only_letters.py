METADATA = {
    "id": 917,
    "name": "Reverse Only Letters",
    "slug": "reverse_only_letters",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse only the letters in a string while keeping non‑letter characters in place.",
}

import sys

def reverse_only_letters(s: str) -> str:
    """Reverse only the letters in the given string.

    Args:
        s: Input string containing letters and other characters.

    Returns:
        A new string where all letters are reversed and all non‑letter characters
        remain at their original indices.

    Examples:
        >>> reverse_only_letters("ab-cd")
        'dc-ba'
        >>> reverse_only_letters("a-bC-dEf-ghIj")
        'j-Ih-gfE-dCba'
    """
    characters = list(s)  # mutable sequence
    left_index = 0
    right_index = len(characters) - 1

    while left_index < right_index:
        # Move left_index forward until it points to a letter
        if not characters[left_index].isalpha():
            left_index += 1
            continue
        # Move right_index backward until it points to a letter
        if not characters[right_index].isalpha():
            right_index -= 1
            continue
        # Swap the two letters
        characters[left_index], characters[right_index] = (
            characters[right_index],
            characters[left_index],
        )
        left_index += 1
        right_index -= 1

    return "".join(characters)


def solve() -> None:
    """Read a string from standard input, reverse only its letters, and print the result."""
    input_line = sys.stdin.readline()
    if not input_line:
        return
    s = input_line.rstrip("\n")
    result = reverse_only_letters(s)
    print(result)
