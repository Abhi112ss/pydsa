METADATA = {
    "id": 618,
    "name": "Students Report By Geography",
    "slug": "students_report_by_geography",
    "category": "Database/Algorithm Simulation",
    "aliases": [],
    "tags": ["pivot", "window_function", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Pivot student data to report them by continent, ordered by their appearance within each continent.",
}

from typing import List, Dict, Any


def solve(students: List[Dict[str, Any]], continents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Pivots student data to report them by continent. Each continent becomes a column,
    and the values are the student names.

    Args:
        students: A list of dictionaries where each dict contains 'name' and 'continent_id'.
        continents: A list of dictionaries where each dict contains 'id' and 'name'.

    Returns:
        A list of dictionaries where each dictionary represents a row of student names
        mapped to continent names.

    Examples:
        >>> students = [{'name': 'Alice', 'continent_id': 1}, {'name': 'Bob', 'continent_id': 2}]
        >>> continents = [{'id': 1, 'name': 'Asia'}, {'id': 2, 'name': 'Europe'}]
        >>> solve(students, continents)
        [{'Asia': 'Alice', 'Europe': 'Bob'}]
    """
    # Map continent IDs to their names for quick lookup
    continent_map = {c['id']: c['name'] for c in continents}
    continent_names = [c['name'] for c in continents]

    # Group students by continent_id
    # We use a dictionary where key is continent_id and value is a list of names
    grouped_students: Dict[int, List[str]] = {}
    for student in students:
        cid = student['continent_id']
        if cid not in grouped_students:
            grouped_students[cid] = []
        grouped_students[cid].append(student['name'])

    # To simulate the "row number" logic, we find the maximum number of students 
    # any single continent has to determine how many rows the output will have.
    max_rows = 0
    for names in grouped_students.values():
        max_rows = max(max_rows, len(names))

    result: List[Dict[str, Any]] = []

    # Iterate through row indices (0 to max_rows - 1)
    for row_idx in range(max_rows):
        row_data: Dict[str, Any] = {}
        
        # For each continent, pick the student at the current row index
        for cont_id, name in continent_map.items():
            # Check if the current continent has a student at this row index
            if cont_id in grouped_students and row_idx < len(grouped_students[cont_id]):
                row_data[name] = grouped_students[cont_id][row_idx]
            else:
                # If no student exists for this continent at this row, set to None or omit
                # Based on standard pivot behavior, we omit or set to null. 
                # Here we follow the requirement of mapping names to continent columns.
                row_data[name] = None
        
        # Clean up None values if the problem implies sparse rows (optional depending on spec)
        # For this implementation, we keep them to maintain consistent column structure
        result.append(row_data)

    # Filter out rows that are entirely None (if any)
    final_result = [r for r in result if any(v is not None for v in r.values())]

    return final_result
