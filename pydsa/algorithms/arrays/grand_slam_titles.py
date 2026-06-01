METADATA = {
    "id": 1783,
    "name": "Grand Slam Titles",
    "slug": "grand_slam_titles",
    "category": "Array",
    "aliases": [],
    "tags": ["array_manipulation", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many players have won a specific number of Grand Slam titles based on a list of winners.",
}

def solve(winners: list[str], target_count: int) -> int:
    """
    Counts how many players have won exactly the target number of Grand Slam titles.

    Args:
        winners: A list of strings where each string is the name of a player 
            who won a Grand Slam title.
        target_count: The specific number of titles to check for.

    Returns:
        The number of unique players who have won exactly target_count titles.

    Examples:
        >>> solve(["Federer", "Nadal", "Federer", "Djokovic", "Nadal", "Federer"], 3)
        1
        >>> solve(["A", "B", "A", "C", "B", "A"], 2)
        2
    """
    if not winners:
        return 0

    # Use a dictionary to store the frequency of each player's name
    # Since the number of players is bounded by the input size, 
    # this is O(n) time and O(n) space in the worst case of unique names.
    # However, the problem constraints often imply a limited set of players.
    title_counts: dict[str, int] = {}

    for player in winners:
        title_counts[player] = title_counts.get(player, 0) + 1

    # Count how many players reached the exact target_count
    players_with_target_titles = 0
    for count in title_counts.values():
        if count == target_count:
            players_with_target_titles += 1

    return players_with_target_titles
