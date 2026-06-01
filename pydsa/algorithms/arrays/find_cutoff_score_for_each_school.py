METADATA = {
    "id": 1988,
    "name": "Find Cutoff Score for Each School",
    "slug": "find-cutoff-score-for-each-school",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n)",
    "description": "Calculate the floor of the average of passing scores for each school.",
}

def solve(passingScores: list[list[int]], threshold: int) -> list[int]:
    """
    Calculates the cutoff score for each school based on the average of passing scores.

    A score is considered passing if it is greater than or equal to the threshold.
    The cutoff score for a school is the floor of the average of its passing scores.
    If a school has no passing scores, the cutoff score is 0.

    Args:
        passingScores: A 2D list where passingScores[i] contains the scores of students in school i.
        threshold: The minimum score required to be considered a passing score.

    Returns:
        A list of integers representing the cutoff score for each school.

    Examples:
        >>> solve([[10, 20, 30], [5, 15, 25]], 15)
        [20, 20]
        >>> solve([[1, 2, 3], [4, 5, 6]], 10)
        [0, 0]
        >>> solve([[10, 20, 30], [1, 2, 3]], 15)
        [20, 0]
    """
    cutoff_scores = []

    for school_scores in passingScores:
        passing_sum = 0
        passing_count = 0

        # Iterate through scores to find those meeting the threshold
        for score in school_scores:
            if score >= threshold:
                passing_sum += score
                passing_count += 1

        # If no students passed, the cutoff is 0
        if passing_count == 0:
            cutoff_scores.append(0)
        else:
            # Calculate floor of the average using integer division
            cutoff_scores.append(passing_sum // passing_count)

    return cutoff_scores
