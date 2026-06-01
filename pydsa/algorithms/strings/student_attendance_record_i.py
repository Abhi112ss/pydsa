METADATA = {
    "id": 551,
    "name": "Student Attendance Record I",
    "slug": "student_attendance_record_i",
    "category": "string",
    "aliases": ["check_record"],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check if a student's attendance record is eligible for an award based on absence and late criteria.",
}

def solve(s: str) -> bool:
    """
    Determine if a student's attendance record is eligible for an award.

    A student is eligible if:
    - The student was absent ('A') for strictly fewer than 2 days total.
    - The student was never late ('L') for 3 or more consecutive days.

    Args:
        s (str): The attendance record string containing only 'A', 'L', and 'P'.

    Returns:
        bool: True if the student is eligible for an award, False otherwise.

    Examples:
        >>> solve("PPALLP")
        True
        >>> solve("PPALLL")
        False
        >>> solve("AA")
        False
    """
    # Check if the count of 'A' is less than 2 and 'LLL' is not in the string
    return s.count('A') < 2 and 'LLL' not in s