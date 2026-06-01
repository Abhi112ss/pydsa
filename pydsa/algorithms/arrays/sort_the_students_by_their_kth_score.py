METADATA = {
    "id": 2545,
    "name": "Sort the Students by Their Kth Score",
    "slug": "sort-the-students-by-their-kth-score",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort students based on their k-th highest score in descending order, using student ID as a tie-breaker.",
}

def solve(scores: list[list[int]], k: int) -> list[int]:
    """
    Sorts students based on their k-th highest score in descending order.
    If two students have the same k-th score, the student with the smaller ID comes first.

    Args:
        scores: A 2D list where scores[i] contains the scores of the i-th student.
               The index i represents the student's ID.
        k: The rank of the score to use for sorting (1-indexed).

    Returns:
        A list of student IDs sorted according to the specified criteria.

    Examples:
        >>> solve([[10, 20, 30], [5, 15, 25]], 2)
        [0, 1]
        >>> solve([[10, 20, 30], [30, 20, 10]], 2)
        [0, 1]
    """
    # Create a list of tuples: (kth_score, student_id)
    # We use -student_id for the tie-breaker if we were sorting everything descending,
    # but since we want ID ascending and score descending, we handle it in the key.
    student_data = []
    
    for student_id, student_scores in enumerate(scores):
        # Sort individual student scores in descending order to find the k-th highest
        sorted_scores = sorted(student_scores, reverse=True)
        # k is 1-indexed, so we access index k-1
        kth_score = sorted_scores[k - 1]
        student_data.append((kth_score, student_id))

    # Sort the students:
    # Primary key: kth_score (descending -> use negative for ascending sort logic)
    # Secondary key: student_id (ascending)
    # Python's sort is stable, but we can do it in one pass with a custom key.
    student_data.sort(key=lambda x: (-x[0], x[1]))

    # Extract and return only the student IDs
    return [student_id for _, student_id in student_data]
