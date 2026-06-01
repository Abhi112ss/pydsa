METADATA = {
    "id": 1904,
    "name": "The Number of Full Rounds You Have Played",
    "slug": "the_number_of_full_rounds_you_have_played",
    "category": "math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the number of complete 15‑minute rounds between two timestamps.",
}


def solve(start_time: int, end_time: int) -> int:
    """Calculate the number of full 15‑minute rounds played.

    Args:
        start_time: The minute when the gaming session started (inclusive).
        end_time: The minute when the gaming session ended (exclusive).

    Returns:
        The count of complete rounds that both start and end within the interval.

    Examples:
        >>> solve(12, 53)
        2
        >>> solve(30, 75)
        2
        >>> solve(0, 14)
        0
    """
    # Compute the first round start that is a multiple of 15 and not earlier than start_time.
    first_round_start = ((start_time + 14) // 15) * 15

    # Compute the last round start that is a multiple of 15 and not later than end_time.
    last_round_start = (end_time // 15) * 15

    # If the first possible round start exceeds the last possible start, no full rounds exist.
    if first_round_start > last_round_start:
        return 0

    # Number of full rounds is the distance between the two starts divided by the round length, plus one.
    return (last_round_start - first_round_start) // 15 + 1