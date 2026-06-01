METADATA = {
    "id": 3616,
    "name": "Number of Student Replacements",
    "slug": "number-of-student-replacements",
    "category": "math",
    "aliases": [],
    "tags": ["math", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of replacements needed to satisfy a specific sequence constraint.",
}

def solve(scores: list[int], k: int) -> int:
    """
    Calculates the minimum number of replacements needed to ensure that 
    every element in the list is at least k greater than its predecessor.

    Args:
        scores: A list of integers representing student scores.
        k: The minimum required difference between consecutive scores.

    Returns:
        The total number of replacements performed.

    Examples:
        >>> solve([1, 5, 2, 10], 3)
        1
        >>> solve([1, 2, 3], 2)
        2
    """
    replacements = 0
    current_score = scores[0]

    # Iterate through the scores starting from the second element
    for i in range(1, len(scores)):
        # Check if the current score violates the constraint relative to the previous valid score
        if scores[i] < current_score + k:
            # If it violates, we must replace it. 
            # To minimize future replacements, we greedily set it to the smallest possible valid value.
            current_score = current_score + k
            replacements += 1
        else:
            # If it satisfies the constraint, we update our reference score to the current score
            current_score = scores[i]

    return replacements
