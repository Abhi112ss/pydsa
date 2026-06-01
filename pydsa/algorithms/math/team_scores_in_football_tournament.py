METADATA = {
    "id": 1212,
    "name": "Team Scores in Football Tournament",
    "slug": "team-scores-in-football-tournament",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total points for each team in a football tournament based on match results.",
}

def solve(matches: list[list[int]]) -> list[int]:
    """
    Calculates the total points for each team in a football tournament.
    
    Points are awarded as follows:
    - Win: 3 points
    - Draw: 1 point
    - Loss: 0 points

    Args:
        matches: A list of lists where each sublist contains [homeTeam, awayTeam, homeScore, awayScore].

    Returns:
        A list of integers representing the total points for each team, 
        where the index corresponds to the team ID.

    Examples:
        >>> solve([[1, 2, 3, 1], [2, 3, 0, 0], [1, 3, 2, 1]])
        [0, 6, 4, 1]
        >>> solve([[1, 2, 1, 1], [1, 2, 1, 1]])
        [0, 2, 2]
    """
    # Determine the number of teams by finding the maximum team ID present in matches
    # Since team IDs are 1-indexed, we need max_id + 1 slots
    max_team_id = 0
    for match in matches:
        max_team_id = max(max_team_id, match[0], match[1])
    
    # Initialize points array with zeros
    # Index 0 will remain unused as team IDs start from 1
    team_points = [0] * (max_team_id + 1)

    for home_team, away_team, home_score, away_score in matches:
        if home_score > away_score:
            # Home team wins
            team_points[home_team] += 3
            team_points[away_team] += 0
        elif home_score < away_score:
            # Away team wins
            team_points[home_team] += 0
            team_points[away_team] += 3
        else:
            # It's a draw
            team_points[home_team] += 1
            team_points[away_team] += 1

    # Return the points list excluding the 0-th index
    return team_points[1:]
