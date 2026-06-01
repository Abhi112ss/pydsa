METADATA = {
    "id": 580,
    "name": "Count Students in Each Department",
    "slug": "count-students-in-each-department",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "math"],
    "difficulty": "easy",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Count the number of students in each department using a left join to include departments with zero students.",
}

from typing import List, Dict, Any


def solve(department: List[Dict[str, Any]], student: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Counts the number of students in each department.

    This function simulates a SQL LEFT JOIN between the Department table 
    and the Student table, grouping by department name to count occurrences.

    Args:
        department: A list of dictionaries representing the Department table.
            Each dict contains 'id' and 'name'.
        student: A list of dictionaries representing the Student table.
            Each dict contains 'id', 'name', and 'departmentId'.

    Returns:
        A list of dictionaries containing 'name' (department name) and 
        'student_count' (number of students in that department).

    Examples:
        >>> dept = [{"id": 1, "name": "IT"}, {"id": 2, "name": "HR"}]
        >>> stud = [{"id": 1, "name": "Alice", "departmentId": 1}]
        >>> solve(dept, stud)
        [{'name': 'IT', 'student_count': 1}, {'name': 'HR', 'student_count': 0}]
    """
    # Step 1: Create a mapping of department IDs to their names for O(1) lookup
    # This simulates the index on the Department table
    dept_id_to_name: Dict[int, str] = {d["id"]: d["name"] for d in department}

    # Step 2: Count students per department ID using a hash map
    # This simulates the aggregation (GROUP BY) part of the SQL query
    student_counts: Dict[int, int] = {}
    for s in student:
        dept_id = s["departmentId"]
        student_counts[dept_id] = student_counts.get(dept_id, 0) + 1

    # Step 3: Perform the "Left Join" logic
    # Iterate through all departments to ensure those with 0 students are included
    result: List[Dict[str, Any]] = []
    for d in department:
        dept_id = d["id"]
        dept_name = d["name"]
        
        # If the dept_id is not in our student_counts, the count is 0
        count = student_counts.get(dept_id, 0)
        
        result.append({
            "name": dept_name,
            "student_count": count
        })

    return result
