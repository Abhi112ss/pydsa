METADATA = {
    "id": 3322,
    "name": "Premier League Table Ranking III",
    "slug": "premier-league-table-ranking-iii",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "custom_comparator"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rank teams based on a hierarchical set of criteria: points, goal difference, goals scored, and alphabetical order.",
}

from functools import cmp_to_key

def solve(teams: list[dict[str, int | str]]) -> list[str]:
    """
    Ranks football teams based on hierarchical criteria.
    
    The ranking criteria are applied in the following order of priority:
    1. Points (Descending)
    2. Goal Difference (Descending)
    3. Goals Scored (Descending)
    4. Team Name (Ascending/Alphabetical)

    Args:
        teams: A list of dictionaries where each dictionary contains:
            - 'name' (str): The name of the team.
            - 'points' (int): Total points earned.
            - 'goals_for' (int): Goals scored.
            - 'goals_against' (int): Goals conceded.

    Returns:
        A list of team names sorted according to the ranking criteria.

    Examples:
        >>> teams = [
        ...     {"name": "Arsenal", "points": 3, "goals_for": 2, "goals_against": 1},
        ...     {"name": "Chelsea", "points": 3, "goals_for": 2, "goals_against": 1},
        ...     {"name": "Liverpool", "points": 4, "goals_for": 3, "goals_against": 1}
        ... ]
        >>> solve(teams)
        ['Liverpool', 'Arsenal', 'Chelsea']
    """

    def compare_teams(team_a: dict[str, int | str], team_b: dict[str, int | str]) -> int:
        """
        Comparator function to implement hierarchical sorting.
        Returns -1 if team_a should come before team_b, 1 if after, and 0 if equal.
        """
        # 1. Compare Points (Descending)
        if team_a["points"] != team_b["points"]:
            return 1 if team_b["points"] > team_a["points"] else -1

        # Calculate Goal Difference: Goals For - Goals Against
        gd_a = team_a["goals_for"] - team_a["goals_against"]
        gd_b = team_b["goals_for"] - team_b["goals_against"]

        # 2. Compare Goal Difference (Descending)
        if gd_a != gd_b:
            return 1 if gd_b > gd_a else -1

        # 3. Compare Goals Scored (Descending)
        if team_a["goals_for"] != team_b["goals_for"]:
            return 1 if team_b["goals_for"] > team_a["goals_for"] else -1

        # 4. Compare Name (Ascending/Alphabetical)
        name_a = str(team_a["name"])
        name_b = str(team_b["name"])
        if name_a < name_b:
            return -1
        elif name_a > name_b:
            return 1
        
        return 0

    # Sort the list using the custom comparator
    # We use cmp_to_key to convert our comparison logic into a key function for Timsort
    sorted_teams = sorted(teams, key=cmp_to_key(compare_teams))

    # Extract and return only the names
    return [team["name"] for team in sorted_teams]
