METADATA = {
    "id": 1086,
    "name": "High Five",
    "slug": "high-five",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "group_by", "order_by"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the average of the top five scores for each student.",
}

from collections import defaultdict

def solve(student_id: list[int], score: list[int]) -> list[list[int]]:
    """
    Calculates the average of the top five scores for each student.

    Args:
        student_id: A list of student IDs corresponding to each score.
        score: A list of scores corresponding to each student ID.

    Returns:
        A list of lists where each inner list contains [student_id, average_top_five_score],
        sorted by student_id in ascending order. The average is rounded down to the nearest integer.

    Examples:
        >>> solve([1, 1, 1, 1, 1, 2, 2, 2, 2, 2], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        [[1, 8], [2, 3]]
    """
    # Map student IDs to a list of their scores
    student_scores_map = defaultdict(list)
    for s_id, s_score in zip(student_id, score):
        student_scores_map[s_id].append(s_score)

    result = []
    
    # Sort student IDs to ensure the output is in ascending order
    sorted_student_ids = sorted(student_scores_map.keys())

    for s_id in sorted_student_ids:
        # Sort scores in descending order to easily pick the top 5
        current_scores = student_scores_map[s_id]
        current_scores.sort(reverse=True)
        
        # Take the top 5 scores (or fewer if the student has less than 5)
        top_five = current_scores[:5]
        
        # Calculate the average and round down to the nearest integer
        # Using integer division // for floor behavior as per SQL requirements
        average_score = sum(top_five) // len(top_five)
        
        result.append([s_id, average_score])

    return result
