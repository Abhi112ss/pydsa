METADATA = {
    "id": 3246,
    "name": "Premier League Table Ranking",
    "slug": "premier-league-table-ranking",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rank football teams based on a hierarchical set of criteria including points, goal difference, and goals scored.",
}

def solve(teams: list[list[int]]) -> list[int]:
    """
    Args:
        teams: A list of lists where each sub-list contains [team_id, points, goal_difference, goals_scored].

    Returns:
        A list of team IDs sorted according to the Premier League ranking rules.
    """
    def ranking_key(team_data: list[int]) -> tuple[int, int, int, int]:
        team_id = team_data[0]
        points = team_data[1]
        goal_difference = team_data[2]
        goals_scored = team_data[3]
        return (-points, -goal_difference, -goals_scored, team_id)

    sorted_teams = sorted(teams, key=ranking_key)
    
    return [team[0] for team in sorted_teams]