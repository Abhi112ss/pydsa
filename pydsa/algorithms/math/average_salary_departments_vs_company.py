METADATA = {
    "id": 615,
    "name": "Average Salary: Departments VS Company",
    "slug": "average-salary-departments-vs-company",
    "category": "Database",
    "aliases": [],
    "tags": ["window_function", "group_by"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Compare the average monthly salary of each department against the overall company average monthly salary.",
}

from typing import List, Dict


def solve(employee_table: List[Dict]) -> List[Dict]:
    """
    Calculates the average monthly salary for each department and compares it 
    to the company-wide average monthly salary.

    Args:
        employee_table: A list of dictionaries where each dictionary represents 
            an employee with keys 'id', 'name', 'department', and 'salary'.

    Returns:
        A list of dictionaries containing 'department', 'avg_dept_salary', 
        'avg_company_salary', and 'difference'.

    Examples:
        >>> employees = [
        ...     {"id": 1, "name": "Joe", "department": "IT", "salary": 70000},
        ...     {"id": 2, "name": "Jim", "department": "IT", "salary": 80000},
        ...     {"id": 3, "name": "Henry", "department": "Finance", "salary": 90000}
        ... ]
        >>> solve(employees)
        [{'department': 'IT', 'avg_dept_salary': 6250.0, 'avg_company_salary': 6250.0, 'difference': 0.0}, 
         {'department': 'Finance', 'avg_dept_salary': 7500.0, 'avg_company_salary': 6250.0, 'difference': 1250.0}]
    """
    if not employee_table:
        return []

    # Dictionary to store sum and count per department: {dept_name: [total_salary, count]}
    dept_stats: Dict[str, List[float]] = {}
    total_company_salary = 0.0
    total_employee_count = 0

    # Single pass to aggregate department data and company totals
    for emp in employee_table:
        salary = float(emp["salary"])
        dept = emp["department"]
        
        # Update company-wide metrics
        total_company_salary += salary
        total_employee_count += 1
        
        # Update department-specific metrics
        if dept not in dept_stats:
            dept_stats[dept] = [0.0, 0]
        dept_stats[dept][0] += salary
        dept_stats[dept][1] += 1

    # Calculate the company-wide monthly average
    # Note: In SQL context, salary is usually annual, so monthly is salary / 12
    avg_company_monthly = (total_company_salary / total_employee_count) / 12.0

    results = []
    # Iterate through departments to calculate local averages and differences
    for dept, stats in dept_stats.items():
        dept_total_salary, dept_count = stats
        avg_dept_monthly = (dept_total_salary / dept_count) / 12.0
        
        # Difference is (dept_avg - company_avg)
        # We round to 2 decimal places to match standard financial reporting expectations
        difference = round(avg_dept_monthly - avg_company_monthly, 2)
        
        results.append({
            "department": dept,
            "avg_dept_salary": round(avg_dept_monthly, 2),
            "avg_company_salary": round(avg_company_monthly, 2),
            "difference": difference
        })

    return results
