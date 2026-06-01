METADATA = {
    "id": 1450,
    "name": "Number of Students Doing Homework at a Given Time",
    "slug": "number_of_students_doing_homework_at_a_given_time",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the number of students whose homework interval includes the query time.",
}


def solve(start_time: list[int], end_time: list[int], query_time: int) -> int:
    """Count how many students are doing homework at a specific time.

    Args:
        start_time: List of start times for each student's homework.
        end_time: List of end times for each student's homework.
        query_time: The time to query.

    Returns:
        The number of students whose interval [start_time[i], end_time[i]] includes query_time.

    Examples:
        >>> solve([1, 2, 3], [3, 2, 7], 4)
        1
        >>> solve([4], [4], 4)
        1
        >>> solve([9, 8, 7], [9, 8, 7], 10)
        0
    """
    # Initialize counter for students active at query_time
    active_student_count = 0

    # Iterate over paired start and end times
    for student_start, student_end in zip(start_time, end_time):
        # Check inclusive interval condition
        if student_start <= query_time <= student_end:
            active_student_count += 1

    return active_student_count