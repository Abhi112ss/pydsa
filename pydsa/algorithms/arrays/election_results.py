METADATA = {
    "id": 2820,
    "name": "Election Results",
    "slug": "election-results",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the candidate with the maximum number of votes from a given list of votes.",
}

def solve(votes: list[int]) -> int:
    """
    Finds the candidate who received the maximum number of votes.

    Args:
        votes: A list of integers where each integer represents a vote for a candidate ID.

    Returns:
        The candidate ID with the highest number of votes. If multiple candidates 
        have the same maximum votes, the problem context usually implies returning 
        any or the first encountered, but standard implementation returns the max.

    Examples:
        >>> solve([1, 2, 3, 1, 2, 1])
        1
        >>> solve([5, 5, 2, 2, 2])
        2
    """
    if not votes:
        return -1

    # Dictionary to store the frequency of each candidate's votes
    vote_counts: dict[int, int] = {}

    for candidate in votes:
        # Increment the count for the candidate in the hash map
        vote_counts[candidate] = vote_counts.get(candidate, 0) + 1

    max_votes = -1
    winner = -1

    # Iterate through the hash map to find the candidate with the highest count
    for candidate, count in vote_counts.items():
        if count > max_votes:
            max_votes = count
            winner = candidate
            
    return winner
