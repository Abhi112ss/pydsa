METADATA = {
    "id": 2339,
    "name": "All the Matches of the League",
    "slug": "all-the-matches-of-the-league",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of matches in a league given the number of teams and matches played per team.",
}

def solve(teams: int, matches_per_team: int) -> int:
    """
    Calculates the total number of matches played in a league.

    In a league where every match involves exactly two teams, the sum of 
    matches played by all teams counts each match twice (once for each participant).
    Therefore, the total matches is (teams * matches_per_team) / 2.

    Args:
        teams: The total number of teams in the league.
        matches_per_team: The number of matches each team plays.

    Returns:
        The total number of matches played in the league.

    Examples:
        >>> solve(3, 2)
        3
        >>> solve(4, 3)
        6
    """
    # Each match is shared by 2 teams. 
    # Summing matches_per_team for all teams counts every match twice.
    total_match_occurrences = teams * matches_per_team
    
    # Divide by 2 to get the unique number of matches.
    return total_match_occurrences // 2
