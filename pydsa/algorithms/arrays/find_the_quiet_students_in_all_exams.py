METADATA = {
    "id": 1412,
    "name": "Find the Quiet Students in All Exams",
    "slug": "find-the-quiet-students-in-all-exams",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N)",
    "description": "Identify students who achieved the minimum score in every single exam they participated in.",
}

def solve(student_scores: list[list[int]]) -> list[int]:
    """
    Finds students who were 'quiet' in all exams they took.
    A student is quiet in an exam if their score is the minimum score in that exam.
    A student is considered quiet overall if they were quiet in every exam they attended.

    Args:
        student_scores: A 2D list where student_scores[i] is a list of scores 
                        for student i. A score of -1 means the student did not 
                        take that exam.

    Returns:
        A list of student indices who were quiet in all their exams, 
        sorted in ascending order.

    Examples:
        >>> solve([[1, 1], [2, 1], [1, 2]])
        [0]
        >>> solve([[1, 1], [2, 1], [1, 2], [1, 1]])
        [0, 3]
    """
    if not student_scores:
        return []

    num_students = len(student_scores)
    num_exams = len(student_scores[0])

    # Step 1: Find the minimum score for each exam.
    # Initialize with infinity to handle comparison.
    min_scores_per_exam = [float('inf')] * num_exams
    for exam_idx in range(num_exams):
        for student_idx in range(num_students):
            score = student_scores[student_idx][exam_idx]
            if score != -1:
                if score < min_scores_per_exam[exam_idx]:
                    min_scores_per_exam[exam_idx] = score

    # Step 2: Check if each student was quiet in all exams they attended.
    quiet_students = []
    for student_idx in range(num_students):
        is_quiet_everywhere = True
        
        for exam_idx in range(num_exams):
            score = student_scores[student_idx][exam_idx]
            
            # If the student attended the exam, check if their score matches the minimum.
            if score != -1:
                if score != min_scores_per_exam[exam_idx]:
                    is_quiet_everywhere = False
                    break
        
        if is_quiet_everywhere:
            quiet_students.append(student_idx)

    return quiet_students
