METADATA = {
    "id": 1366,
    "name": "Rank Teams by Votes",
    "slug": "rank-teams-by-votes",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(m * n log n)",
    "space_complexity": "O(m * n)",
    "description": "Rank teams based on the frequency of votes at each rank position, using team names as tie-breakers.",
}

def solve(votes: str, teams: list[str]) -> list[str]:
    """
    Ranks teams based on the frequency of votes at each rank position.

    The ranking criteria are:
    1. The number of votes at the first position.
    2. If tied, the number of votes at the second position, and so on.
    3. If still tied, the team name in alphabetical order.

    Args:
        votes: A string representing the sequence of votes.
        teams: A list of strings representing the names of the teams.

    Returns:
        A list of strings representing the ranked teams.

    Examples:
        >>> solve("FFFAA", ["B", "A", "C"])
        ['A', 'B', 'C']
        >>> solve("ZXY", ["X", "Y", "Z"])
        ['Z', 'X', 'Y']
    """
    if not votes or not teams:
        return []

    num_ranks = len(votes)
    # Initialize a frequency map where each team maps to a list of counts 
    # for each rank position (0 to num_ranks - 1).
    # Using a dictionary for O(1) lookup of team name to its vote profile.
    team_vote_counts: dict[str, list[int]] = {team: [0] * num_ranks for team in teams}

    # Populate the vote counts for each team at each rank position.
    for vote_sequence in votes:
        for rank_index, team_name in enumerate(vote_sequence):
            team_vote_counts[team_name][rank_index] += 1

    # Sort the teams using a custom key.
    # The key is a tuple: (count_at_rank_0, count_at_rank_1, ..., -alphabetical_order)
    # We use negative team name in the tuple logic or handle it in the sort key 
    # to ensure descending order for counts and ascending order for names.
    # Since Python's sort is stable, we can sort by name first, then by counts.
    
    # Step 1: Sort alphabetically (ascending) to handle the tie-breaker.
    sorted_teams = sorted(teams)

    # Step 2: Sort by the vote counts in descending order.
    # Because we sort by counts descending, and the sort is stable, 
    # teams with identical counts will maintain their alphabetical order.
    sorted_teams.sort(key=lambda team: team_vote_counts[team], reverse=True)

    return sorted_teams
