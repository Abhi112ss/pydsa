METADATA = {
    "id": 1965,
    "name": "Employees With Missing Information",
    "slug": "employees_with_missing_information",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the IDs of employees that have any missing information.",
}


import sys
import ast
from typing import List, Any


def solve() -> None:
    """Read employee records from standard input and output the sorted list of employee IDs
    that contain at least one missing field.

    The input should be a single line representing a Python list of employee records,
    where each record is a list. Missing values can be represented by `null` (as in JSON)
    or by `None`. Example input:
        [[1, "John", 5000, "HR"], [2, null, 6000, "Finance"], [3, "Anna", null, "IT"]]

    The function prints a Python list of IDs sorted in ascending order.
    Example output for the above input:
        [2, 3]

    No arguments are taken; the function reads from `stdin` and writes to `stdout`.
    """
    raw_input: str = sys.stdin.read().strip()
    if not raw_input:
        print("[]")
        return

    # Convert JSON-like `null` to Python `None` before evaluation.
    normalized_input: str = raw_input.replace("null", "None")
    try:
        employee_records: List[List[Any]] = ast.literal_eval(normalized_input)
    except Exception:
        # If parsing fails, treat as empty list.
        print("[]")
        return

    missing_ids: List[int] = []
    for record in employee_records:
        # If any field in the record is None, the employee has missing information.
        if any(field is None for field in record):
            employee_id: int = record[0]  # first element is the employee ID
            missing_ids.append(employee_id)

    missing_ids.sort()
    print(missing_ids)