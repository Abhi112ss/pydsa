METADATA = {
    "id": 1189,
    "name": "Maximum Number of Balloons",
    "slug": "maximum_number_of_balloons",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the maximum number of instances of the word 'balloon' that can be formed from the characters of a given string.",
}

import sys
from collections import Counter

def solve() -> None:
    """Read a string from standard input and print the maximum number of
    instances of the word ``balloon`` that can be constructed from its characters.

    Args:
        None (input is read from ``stdin``).

    Returns:
        None (the result is printed to ``stdout``).

    Examples:
        >>> import sys, io
        >>> sys.stdin = io.StringIO('nlaebolko')
        >>> solve()
        1
        >>> sys.stdin = io.StringIO('loonbalxballpoon')
        >>> solve()
        2
    """
    input_text = sys.stdin.readline().strip()
    # Count frequency of each character in the input string
    character_frequencies: Counter = Counter(input_text)

    # Required frequencies for each character in the word "balloon"
    required_frequencies = {
        'b': 1,
        'a': 1,
        'l': 2,
        'o': 2,
        'n': 1,
    }

    # Determine the limiting character by taking the floor division of available
    # counts by required counts; the smallest quotient is the answer.
    possible_counts = []
    for char, required in required_frequencies.items():
        available = character_frequencies.get(char, 0)
        possible_counts.append(available // required)
    max_balloons = min(possible_counts)

    print(max_balloons)