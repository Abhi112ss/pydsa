METADATA = {
    "id": 506,
    "name": "Relative Ranks",
    "slug": "relative_ranks",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "heap", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Assign relative ranks to athletes based on their scores, with the top three receiving 'Gold Medal', 'Silver Medal', and 'Bronze Medal'.",
}


def solve(score: list[int]) -> list[str]:
    """Assign relative ranks to athletes based on their scores.

    Athletes are ranked from highest to lowest score. The top three athletes
    receive "Gold Medal", "Silver Medal", and "Bronze Medal" respectively.
    All other athletes receive their rank as a string number.

    Args:
        score: A list of unique integers representing athlete scores.

    Returns:
        A list of strings where each element is the rank corresponding to
        the athlete at that index in the input list.

    Examples:
        >>> solve([5, 4, 3, 2, 1])
        ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        >>> solve([10, 3, 8, 9, 4])
        ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']
    """
    n = len(score)

    # Create list of (score, original_index) pairs and sort by score descending
    indexed_scores = sorted(
        enumerate(score),
        key=lambda pair: pair[1],
        reverse=True
    )

    # Initialize result array to store rank strings at original indices
    result = [""] * n

    # Assign rank strings based on sorted position
    for rank_position, (_, original_index) in enumerate(indexed_scores):
        if rank_position == 0:
            result[original_index] = "Gold Medal"
        elif rank_position == 1:
            result[original_index] = "Silver Medal"
        elif rank_position == 2:
            result[original_index] = "Bronze Medal"
        else:
            result[original_index] = str(rank_position + 1)

    return result