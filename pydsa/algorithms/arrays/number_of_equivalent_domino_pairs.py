METADATA = {
    "id": 1128,
    "name": "Number of Equivalent Domino Pairs",
    "slug": "number_of_equivalent_domino_pairs",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count pairs of dominoes that become identical after sorting each domino's two numbers.",
}


def solve(dominoes: list[list[int]]) -> int:
    """Count the number of equivalent domino pairs.

    An equivalent pair consists of two dominoes [a, b] and [c, d] such that
    after sorting each domino's numbers, they become identical.
    For each domino we sort its two values, encode it as a single integer,
    and use a frequency map to count how many previous dominoes have the same
    encoding.

    Args:
        dominoes: A list of dominoes, each represented by a list of two integers
                  where 1 <= value <= 9.

    Returns:
        The total number of equivalent domino pairs.

    Examples:
        >>> solve([[1,2],[1,2],[1,1],[1,2],[2,2]])
        4
        >>> solve([[1,2],[2,1],[3,4],[5,6]])
        1
    """
    # Frequency map: key is encoded sorted domino, value is occurrence count.
    frequency: dict[int, int] = {}
    pair_count: int = 0

    for domino in dominoes:
        first, second = domino[0], domino[1]
        # Ensure the smaller value comes first to normalize the domino.
        if first > second:
            first, second = second, first
        # Encode as a two‑digit number (since values are 1‑9).
        encoded = first * 10 + second
        # Existing occurrences form pairs with the current domino.
        existing = frequency.get(encoded, 0)
        pair_count += existing
        # Record this domino for future pairings.
        frequency[encoded] = existing + 1

    return pair_count