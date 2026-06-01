METADATA = {
    "id": 1811,
    "name": "Find Interview Candidates",
    "slug": "find-interview-candidates",
    "category": "Sorting",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Filter candidates based on minimum score thresholds and return the top k candidates sorted by score descending.",
}

def solve(candidates: list[list[int]], thresholds: list[int], k: int) -> list[int]:
    """
    Filters candidates based on score thresholds and returns the top k candidate IDs.

    A candidate is valid if their score at every index i is greater than or equal 
    to the corresponding threshold[i]. Candidates are returned in descending 
    order of their scores. If scores are tied, the candidate with the higher ID 
    is preferred.

    Args:
        candidates: A list of lists where candidates[i] is the score list for candidate i.
        thresholds: A list of minimum required scores for each index.
        k: The number of top candidates to return.

    Returns:
        A list of k candidate IDs (indices) that meet the criteria, sorted by 
        score descending, then ID descending.

    Examples:
        >>> solve([[10, 20], [15, 25], [5, 30]], [10, 20], 2)
        [1, 0]
        >>> solve([[10, 10], [5, 5]], [10, 10], 1)
        []
    """
    valid_candidates = []

    for candidate_id, scores in enumerate(candidates):
        # Check if the candidate meets all threshold requirements
        is_eligible = True
        for score, threshold in zip(scores, thresholds):
            if score < threshold:
                is_eligible = False
                break
        
        if is_eligible:
            # We store (total_score, candidate_id) to facilitate sorting.
            # Since we want descending order for both, we can use the values directly
            # and sort with reverse=True.
            total_score = sum(scores)
            valid_candidates.append((total_score, candidate_id))

    # Sort candidates primarily by total score descending, 
    # and secondarily by candidate_id descending.
    valid_candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # Return only the top k IDs
    return [candidate_id for score, candidate_id in valid_candidates[:k]]
