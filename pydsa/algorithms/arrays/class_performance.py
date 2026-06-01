METADATA = {
    "id": 2989,
    "name": "Class Performance",
    "slug": "class-performance",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate class performance metrics based on student scores.",
}

def solve(scores: list[int], threshold: int) -> dict[str, float]:
    """
    Calculates the percentage of students who scored above a certain threshold.

    Args:
        scores: A list of integers representing student scores.
        threshold: The score threshold to evaluate performance against.

    Returns:
        A dictionary containing the 'above_threshold_percentage' and 
        'average_score'.

    Examples:
        >>> solve([85, 90, 70, 60, 95], 80)
        {'above_threshold_percentage': 60.0, 'average_score': 80.0}
        >>> solve([10, 20, 30], 25)
        {'above_threshold_percentage': 33.33333333333333, 'average_score': 20.0}
    """
    if not scores:
        return {
            "above_threshold_percentage": 0.0,
            "average_score": 0.0
        }

    total_sum = 0
    count_above_threshold = 0
    total_students = len(scores)

    # Single pass to calculate sum and count students meeting the threshold
    for score in scores:
        total_sum += score
        if score > threshold:
            count_above_threshold += 1

    # Calculate metrics using the aggregated values
    average_score = total_sum / total_students
    above_threshold_percentage = (count_above_threshold / total_students) * 100

    return {
        "above_threshold_percentage": above_threshold_percentage,
        "average_score": average_score
    }
