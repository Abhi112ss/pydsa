METADATA = {
    "id": 178,
    "name": "Rank Scores",
    "slug": "rank_scores",
    "category": "logic",
    "aliases": ["Dense Rank"],
    "tags": ["logic", "sorting", "hash-map"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the dense rank of scores where identical scores receive the same rank and the next rank is the next consecutive integer.",
}


def solve(scores: list[float]) -> list[int]:
    """Calculates the dense rank for a list of scores.

    Args:
        scores: A list of numerical scores to be ranked.

    Returns:
        A list of integers representing the dense rank of each score in the input list.

    Examples:
        >>> solve([3.50, 3.65, 4.00, 3.85, 4.00, 3.65])
        [4, 3, 1, 2, 1, 3]
    """
    if not scores:
        return []

    # Step 1: Identify unique scores and sort them in descending order.
    # Sorting unique values takes O(U log U) where U is the number of unique scores.
    unique_scores_sorted = sorted(list(set(scores)), reverse=True)

    # Step 2: Create a mapping from score to its dense rank.
    # Rank is determined by the position in the sorted unique list (1-indexed).
    rank_mapping = {score: index + 1 for index, score in enumerate(unique_scores_sorted)}

    # Step 3: Map each original score to its corresponding rank.
    # This maintains the original order of the input list.
    result_ranks = [rank_mapping[score] for score in scores]

    return result_ranks