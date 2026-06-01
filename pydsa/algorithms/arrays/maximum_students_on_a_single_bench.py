METADATA = {
    "id": 3450,
    "name": "Maximum Students on a Single Bench",
    "slug": "maximum-students-on-a-single-bench",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays", "sliding window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of students that can sit on a single bench given specific seating constraints.",
}

def solve(students: list[int]) -> int:
    """
    Calculates the maximum number of students that can be seated on a single bench.
    
    The problem implies finding the longest contiguous segment of students 
    that satisfies the seating constraints (represented by the input array).
    Based on the problem description, we look for the maximum length of 
    consecutive elements that meet the criteria.

    Args:
        students: A list of integers representing student presence or constraints.

    Returns:
        The maximum number of students on a single bench.

    Examples:
        >>> solve([1, 1, 0, 1, 1, 1])
        3
        >>> solve([0, 0, 0])
        0
        >>> solve([1, 0, 1, 0, 1])
        1
    """
    if not students:
        return 0

    max_students = 0
    current_streak = 0

    for student in students:
        # If the current element satisfies the condition (e.g., student is present)
        if student == 1:
            current_streak += 1
            # Update the global maximum if the current streak is longer
            if current_streak > max_students:
                max_students = current_streak
        else:
            # Reset the streak when the condition is broken
            current_streak = 0

    return max_students
