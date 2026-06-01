METADATA = {
    "id": 569,
    "name": "Median Employee Salary",
    "slug": "median-employee-salary",
    "category": "SQL/Algorithm",
    "aliases": [],
    "tags": ["sorting", "ranking", "median"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the median salary for each department by ranking salaries and selecting the middle elements.",
}

from typing import List, Dict


def solve(employee_data: List[Dict], department_data: List[Dict]) -> List[Dict]:
    """
    Calculates the median salary for each department.

    The median is defined as the middle value if the count is odd, 
    or the average of the two middle values if the count is even.
    However, in many SQL-style problems (like LeetCode 569), 
    the 'median' is often requested as the specific middle value(s) 
    based on rank. This implementation follows the standard mathematical 
    median definition.

    Args:
        employee_data: A list of dictionaries where each dict contains 
                       'id', 'name', 'salary', and 'departmentId'.
        department_data: A list of dictionaries where each dict contains 
                         'id' and 'name'.

    Returns:
        A list of dictionaries containing 'Department' and 'Median_Salary'.

    Examples:
        >>> employees = [
        ...     {"id": 1, "name": "Joe", "salary": 70000, "departmentId": 1},
        ...     {"id": 2, "name": "Jim", "salary": 80000, "departmentId": 1},
        ...     {"id": 3, "name": "Henry", "salary": 90000, "departmentId": 1},
        ...     {"id": 4, "name": "Sam", "salary": 60000, "departmentId": 2}
        ... ]
        >>> departments = [
        ...     {"id": 1, "name": "IT"},
        ...     {"id": 2, "name": "Sales"}
        ... ]
        >>> solve(employees, departments)
        [{'Department': 'IT', 'Median_Salary': 80000.0}, {'Department': 'Sales', 'Median_Salary': 60000.0}]
    """
    # Map department IDs to names for quick lookup
    dept_map = {dept["id"]: dept["name"] for dept in department_data}
    
    # Group salaries by department ID
    dept_salaries: Dict[int, List[float]] = {}
    for emp in employee_data:
        dept_id = emp["departmentId"]
        if dept_id not in dept_salaries:
            dept_salaries[dept_id] = []
        dept_salaries[dept_id].append(float(emp["salary"]))

    results = []

    # Calculate median for each department
    for dept_id, salaries in dept_salaries.items():
        # Sort salaries to find the middle elements
        salaries.sort()
        n = len(salaries)
        
        if n % 2 == 1:
            # Odd number of elements: pick the middle one
            median = salaries[n // 2]
        else:
            # Even number of elements: average of the two middle ones
            mid_right = n // 2
            mid_left = mid_right - 1
            median = (salaries[mid_left] + salaries[mid_right]) / 2.0

        results.append({
            "Department": dept_map.get(dept_id, "Unknown"),
            "Median_Salary": median
        })

    # Sort results by Department name as is standard in reporting
    results.sort(key=lambda x: x["Department"])
    return results
