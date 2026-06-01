METADATA = {
    "id": 914,
    "name": "X of a Kind in a Deck of Cards",
    "slug": "x_of_a_kind_in_a_deck_of_cards",
    "category": "Array",
    "aliases": [],
    "tags": ["math", "gcd", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n + log(max_val))",
    "space_complexity": "O(n)",
    "description": "Determine if the deck can be partitioned into groups of size X >= 2 where all cards in each group have the same value.",
}

from math import gcd
from functools import reduce


def solve(deck: list[int]) -> bool:
    """Determine if the deck can be partitioned into groups of size X >= 2
    where all cards in each group have the same value.

    The key insight is that we need the GCD of all card frequencies to be >= 2.
    If the GCD of all frequencies is g >= 2, then we can form groups of size g.

    Args:
        deck: List of integers representing card values.

    Returns:
        True if such a partition exists, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 4, 3, 2, 1])
        True
        >>> solve([1, 1, 1, 2, 2, 2, 3, 3])
        False
        >>> solve([1])
        False
        >>> solve([1, 1])
        True
        >>> solve([1, 1, 2, 2, 2, 2])
        True
    """
    if len(deck) < 2:
        return False

    # Count frequency of each card value using a dictionary
    freq_map: dict[int, int] = {}
    for card in deck:
        freq_map[card] = freq_map.get(card, 0) + 1

    frequencies = list(freq_map.values())

    # Compute the GCD of all frequencies
    # If the GCD >= 2, we can partition into groups of that size
    overall_gcd = reduce(gcd, frequencies)

    return overall_gcd >= 2