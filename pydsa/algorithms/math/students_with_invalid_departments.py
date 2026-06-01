METADATA = {
    "id": 1350,
    "name": "Students With Invalid Departments",
    "slug": "students-with-invalid-departments",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "join", "filtering"],
    "difficulty": "easy",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(M)",
    "description": "Identify students whose department ID does not exist in the departments table.",
}

from typing import List, Dict, Any


def solve(students: List[Dict[str, Any]], departments: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Identifies students who are assigned to a department ID that does not exist 
    in the departments table.

    Args:
        students: A list of dictionaries where each dictionary represents a student 
            with keys 'student_id', 'name', and 'department_id'.
        departments: A list of dictionaries where each dictionary represents a 
            department with keys 'department_id' and 'department_name'.

    Returns:
        A list of dictionaries containing the 'student_id' and 'name' of students 
        with invalid department IDs, sorted by student_id in ascending order.

    Examples:
        >>> students = [
        ...     {"student_id": 1, "name": "Alice", "department_id": 10},
        ...     {"student_id": 2, "name": "Bob", "department_id": 20},
        ...     {"student_id": 3, "name": "Charlie", "department_id": 30}
        ... ]
        >>> departments = [
        ...     {"department_id": 10, "department_name": "CS"},
        ...     {"department_id": 20, "department_name": "Math"}
        ... ]
        >>> solve(students, departments)
        [{'student_id': 3, 'name': 'Charlie'}]
    """
    # Create a set of all valid department IDs for O(1) average lookup time
    valid_department_ids = {dept["department_id"] for dept in departments}

    invalid_students = []

    # Iterate through students to find those whose department_id is not in the valid set
    for student in students:
        if student["department_id"] not in valid_department_ids:
            # Append only the required fields
            invalid_students.append({
                "student_id": student["student_id"],
                "name": student["name"]
            })

    # Sort the resulting list by student_id in ascending order as per standard SQL requirements
    invalid_students.sort(key=lambda x: x["student_id"])

    return invalid_students
