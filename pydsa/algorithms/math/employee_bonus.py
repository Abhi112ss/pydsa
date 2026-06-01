METADATA = {
    "id": 577,
    "name": "Employee Bonus",
    "slug": "employee_bonus",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find employees whose bonus is less than 1000 or who have no bonus record.",
}


def solve(employees: list[dict], bonuses: list[dict]) -> list[dict]:
    """
    Find employees whose bonus is less than 1000 or who have no bonus record.

    This simulates a SQL LEFT JOIN between Employee and Bonus tables,
    filtering for bonus < 1000 or NULL bonus.

    Args:
        employees: List of dicts with keys 'empId', 'name', 'supervisor', 'salary'.
        bonuses: List of dicts with keys 'empId', 'bonus'.

    Returns:
        List of dicts with keys 'name' and 'bonus' for qualifying employees.

    Examples:
        >>> employees = [
        ...     {"empId": 3, "name": "Brad", "supervisor": None, "salary": 4000},
        ...     {"empId": 1, "name": "John", "supervisor": 3, "salary": 1000},
        ...     {"empId": 2, "name": "Dan", "supervisor": 3, "salary": 2000},
        ...     {"empId": 4, "name": "Thomas", "supervisor": 3, "salary": 4000},
        ... ]
        >>> bonuses = [
        ...     {"empId": 2, "bonus": 500},
        ...     {"empId": 4, "bonus": 2000},
        ... ]
        >>> solve(employees, bonuses)
        [{'name': 'Brad', 'bonus': None}, {'name': 'John', 'bonus': None}, {'name': 'Dan', 'bonus': 500}]
    """
    # Build a lookup dict from empId to bonus for O(1) access
    bonus_lookup: dict[int, int] = {}
    for bonus_record in bonuses:
        bonus_lookup[bonus_record["empId"]] = bonus_record["bonus"]

    # Iterate all employees, performing a left join and filtering
    result: list[dict] = []
    for employee in employees:
        emp_id = employee["empId"]
        bonus_value = bonus_lookup.get(emp_id)  # None if no bonus record (simulates LEFT JOIN NULL)

        # Keep employees with bonus < 1000 or no bonus at all
        if bonus_value is None or bonus_value < 1000:
            result.append({"name": employee["name"], "bonus": bonus_value})

    return result