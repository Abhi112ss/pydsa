METADATA = {
    "id": 3921,
    "name": "Score Validator",
    "slug": "score-validator",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "validation", "linear-scan"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Verify if a sequence of scores follows a specific sequential constraint.",
}

def solve(scores: list[int]) -> bool:
    """
    Validates if the given sequence of scores satisfies the sequential constraint.
    
    The constraint requires that for every element at index i (where i > 0), 
    the score must be strictly greater than the score at index i-1.

    Args:
        scores: A list of integers representing the scores.

    Returns:
        True if the sequence is strictly increasing, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4])
        True
        >>> solve([1, 3, 2, 4])
        False
        >>> solve([5])
        True
        >>> solve([])
        True
    """
    # An empty list or a single element list is vacuously valid
    if len(scores) <= 1:
        return True

    # Iterate through the array starting from the second element
    for index in range(1, len(scores)):
        # Check if the current element violates the strictly increasing constraint
        if scores[index] <= scores[index - 1]:
            return False

    # If no violations were found, the sequence is valid
    return True
