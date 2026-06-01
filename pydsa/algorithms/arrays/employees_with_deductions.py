METADATA = {
    "id": 2394,
    "name": "Employees With Deductions",
    "slug": "employees_with_deductions",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "group_by"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return each employee's total deduction, including employees with no deductions using a left join.",
}


def solve() -> str:
    """
    Generates the SQL query for LeetCode problem 2394: Employees With Deductions.

    Returns:
        str: The SQL statement that computes each employee's total deduction,
             using a LEFT JOIN to include employees without any deductions.

    Example:
        >>> query = solve()
        >>> isinstance(query, str)
        True
        >>> "LEFT JOIN" in query
        True
    """
    # Build the query:
    # 1. LEFT JOIN Employee with Deduction on employee_id.
    # 2. Aggregate deductions per employee; COALESCE replaces NULL with 0 for employees without deductions.
    # 3. Group by employee attributes and order by employee_id.
    query: str = (
        "SELECT e.employee_id, e.name, e.salary, COALESCE(SUM(d.deduction), 0) AS total_deduction "
        "FROM Employee e "
        "LEFT JOIN Deduction d ON e.employee_id = d.employee_id "
        "GROUP BY e.employee_id, e.name, e.salary "
        "ORDER BY e.employee_id"
    )
    return query