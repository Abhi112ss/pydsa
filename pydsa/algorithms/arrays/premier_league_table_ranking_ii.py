METADATA = {
    "id": 3252,
    "name": "Premier League Table Ranking II",
    "slug": "premier-league-table-ranking-ii",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rank football teams based on points, goal difference, and goals scored using a multi-level sorting criteria.",
}

def solve(teams: list[dict[str, int]]) -> list[str]:
    """
    Ranks football teams based on specific Premier League criteria.
    
    The ranking criteria are applied in the following order of priority:
    1. Total Points (descending)
    2. Goal Difference (descending)
    3. Goals Scored (descending)
    4. Alphabetical order of team name (ascending)

    Args:
        teams: A list of dictionaries where each dictionary contains:
            - 'name': str (the team name)
            - 'points': int (total points earned)
            - 'goal_difference': int (goals scored minus goals conceded)
            - 'goals_scored': int (total goals scored)

    Returns:
        A list of team names sorted according to the ranking criteria.

    Examples:
        >>> teams = [
        ...     {"name": "Arsenal", "points": 3, "goal_difference": 1, "goals_scored": 2},
        ...     {"name": "Chelsea", "points": 3, "goal_difference": 1, "goals_scored": 3},
        ...     {"name": "Liverpool", "points": 3, "goal_difference": 2, "goals_scored": 2}
        ... ]
        >>> solve(teams)
        ['Liverpool', 'Chelsea', 'Arsenal']
    """
    
    def ranking_key(team: dict[str, int]) -> tuple[int, int, int, str]:
        """
        Generates a sort key for the team.
        
        To handle descending order for integers within a single sort call, 
        we negate the numeric values. For the name (string), we keep it 
        as is for ascending order.
        """
        # We negate points, goal_difference, and goals_scored to achieve 
        # descending order while using Python's default ascending sort.
        # The name is kept positive for ascending alphabetical order.
        return (
            -team["points"],
            -team["goal_difference"],
            -team["goals_scored"],
            team["name"]
        )

    # Sort the list of dictionaries using the custom key.
    # Python's Timsort is stable and highly efficient for this O(n log n) operation.
    sorted_teams = sorted(teams, key=ranking_key)

    # Extract and return only the names of the sorted teams.
    return [team["name"] for team in sorted_teams]
