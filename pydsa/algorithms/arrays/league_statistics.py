METADATA = {
    "id": 1841,
    "name": "League Statistics",
    "slug": "league-statistics",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total points for each team in a league based on match results.",
}

def solve(teams: list[str], results: list[str]) -> list[str]:
    """
    Calculates the total points for each team in a league based on match results.
    
    A win gives 3 points, a draw gives 1 point, and a loss gives 0 points.
    The output should be a list of strings in the format "team_name: points",
    sorted by team name alphabetically.

    Args:
        teams: A list of team names.
        results: A list of strings representing match results in the format "team1 team2 outcome",
                 where outcome is 'W' (team1 wins), 'L' (team1 loses), or 'D' (draw).

    Returns:
        A list of strings formatted as "team: points", sorted alphabetically by team name.

    Examples:
        >>> solve(["TeamA", "TeamB", "TeamC"], ["TeamA TeamB W", "TeamB TeamC D"])
        ['TeamA: 3', 'TeamB: 1', 'TeamC: 1']
        >>> solve(["Lions", "Tigers", "Bears"], ["Lions Tigers L", "Tigers Bears W"])
        ['Bears: 0', 'Lions: 0', 'Tigers: 3']
    """
    # Initialize points dictionary with 0 for all teams
    points_map: dict[str, int] = {team: 0 for team in teams}

    for match in results:
        # Parse the match string into components
        parts = match.split()
        if len(parts) != 3:
            continue
            
        team_a, team_b, outcome = parts[0], parts[1], parts[2]

        # Update points based on the outcome
        if outcome == 'W':
            # Team A wins, Team B loses
            points_map[team_a] += 3
        elif outcome == 'L':
            # Team A loses, Team B wins
            points_map[team_b] += 3
        elif outcome == 'D':
            # Both teams get 1 point for a draw
            points_map[team_a] += 1
            points_map[team_b] += 1

    # Sort team names alphabetically and format the output strings
    sorted_teams = sorted(points_map.keys())
    return [f"{team}: {points_map[team]}" for team in sorted_teams]
