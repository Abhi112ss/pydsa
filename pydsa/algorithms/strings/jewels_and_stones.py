METADATA = {
    "id": 771,
    "name": "Jewels and Stones",
    "slug": "jewels_and_stones",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Count how many stones are also jewels.",
}


def solve(jewels: str, stones: str) -> int:
    """Count the number of stones that are also jewels.

    Args:
        jewels: A string containing distinct characters representing jewel types.
        stones: A string containing characters representing stones you have.

    Returns:
        The count of characters in `stones` that also appear in `jewels`.

    Examples:
        >>> solve("aA", "aAAbbbb")
        3
        >>> solve("z", "ZZ")
        0
    """
    # Create a hash set of jewel characters for O(1) membership checks.
    jewel_set = set(jewels)

    # Iterate over each stone and increment count when it is a jewel.
    jewel_count = 0
    for stone in stones:
        if stone in jewel_set:
            jewel_count += 1

    return jewel_count