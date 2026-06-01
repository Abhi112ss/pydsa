METADATA = {
    "id": 574,
    "name": "Winning Candidate",
    "slug": "winning-candidate",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "math"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the candidate with the highest number of votes from the votes table.",
}

def solve(votes: list[dict], candidates: list[dict]) -> dict | None:
    """
    Finds the candidate with the maximum number of votes.

    Args:
        votes: A list of dictionaries where each dict represents a vote 
               containing 'candidate_id'.
        candidates: A list of dictionaries where each dict represents a 
                    candidate containing 'id' and 'name'.

    Returns:
        A dictionary containing the 'id' and 'name' of the winning candidate,
        or None if no candidates or votes exist.

    Examples:
        >>> votes = [{'candidate_id': 1}, {'candidate_id': 1}, {'candidate_id': 2}]
        >>> candidates = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        >>> solve(votes, candidates)
        {'id': 1, 'name': 'Alice'}
    """
    if not candidates or not votes:
        return None

    # Step 1: Count the occurrences of each candidate_id in the votes list
    vote_counts: dict[int, int] = {}
    for vote in votes:
        candidate_id = vote["candidate_id"]
        vote_counts[candidate_id] = vote_counts.get(candidate_id, 0) + 1

    # Step 2: Find the candidate_id with the maximum count
    # We initialize with -1 to handle cases where no votes are cast for any candidate
    max_votes = -1
    winner_id = None

    for candidate_id, count in vote_counts.items():
        if count > max_votes:
            max_votes = count
            winner_id = candidate_id

    # Step 3: Join with the candidates table to retrieve the name
    if winner_id is not None:
        for candidate in candidates:
            if candidate["id"] == winner_id:
                return {"id": candidate["id"], "name": candidate["name"]}

    return None
