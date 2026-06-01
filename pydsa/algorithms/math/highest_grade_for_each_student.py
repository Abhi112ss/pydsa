METADATA = {
    "id": 1112,
    "name": "Highest Grade For Each Student",
    "slug": "highest-grade-for-each-student",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the highest grade for each student, and if there's a tie, pick the one with the smallest course ID.",
}

def solve(student_grades: list[list[int]]) -> list[list[int]]:
    """
    Finds the highest grade for each student. In case of ties in grades, 
    the course with the smallest ID is selected.

    Args:
        student_grades: A list of lists where each sublist contains [student_id, course_id, grade].

    Returns:
        A list of lists where each sublist contains [student_id, highest_grade, smallest_course_id],
        sorted by student_id in ascending order.

    Examples:
        >>> solve([[1, 5, 2], [1, 6, 7], [2, 5, 4], [2, 6, 5]])
        [[1, 7, 6], [2, 5, 5]]
        >>> solve([[1, 5, 2], [1, 6, 2], [2, 5, 4], [2, 6, 5]])
        [[1, 2, 5], [2, 5, 5]]
    """
    # Map student_id -> (max_grade, min_course_id)
    # We use a dictionary to store the best result found so far for each student
    best_results: dict[int, tuple[int, int]] = {}

    for student_id, course_id, grade in student_grades:
        if student_id not in best_results:
            best_results[student_id] = (grade, course_id)
        else:
            current_max_grade, current_min_course = best_results[student_id]
            
            # Update if current grade is higher
            # OR if grade is equal but current course_id is smaller
            if grade > current_max_grade:
                best_results[student_id] = (grade, course_id)
            elif grade == current_max_grade and course_id < current_min_course:
                best_results[student_id] = (grade, course_id)

    # Convert the dictionary to the required list format
    # and sort by student_id as per problem requirements
    result: list[list[int]] = []
    for student_id in sorted(best_results.keys()):
        max_grade, min_course = best_results[student_id]
        result.append([student_id, max_grade, min_course])

    return result
