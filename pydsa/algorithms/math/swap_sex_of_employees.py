METADATA = {
    "id": 627,
    "name": "Swap Sex of Employees",
    "slug": "swap_sex_of_employees",
    "category": "Database",
    "aliases": [],
    "tags": ["logic", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Swap the sex values in an employees table using a conditional expression or XOR-like logic to flip between two discrete values without temporary storage.",
}

def solve(employees: list[dict]) -> list[dict]:
    """Swap the sex of each employee using XOR-like logic to flip between 'M' and 'F'.

    Args:
        employees: A list of employee dictionaries, each containing at least a 'sex' key with value 'M' or 'F'.

    Returns:
        The same list with each employee's 'sex' value swapped ('M' becomes 'F', 'F' becomes 'M').

    Examples:
        >>> solve([{'name': 'Alice', 'sex': 'F'}, {'name': 'Bob', 'sex': 'M'}])
        [{'name': 'Alice', 'sex': 'M'}, {'name': 'Bob', 'sex': 'F'}]
        >>> solve([{'name': 'Charlie', 'sex': 'M'}])
        [{'name': 'Charlie', 'sex': 'F'}]
    """
    # Use XOR-like logic: map 'M' -> 'F' and 'F' -> 'M' via a simple conditional swap
    for employee in employees:
        # Flip the sex value using a conditional expression (no temporary variable needed)
        employee['sex'] = 'F' if employee['sex'] == 'M' else 'M'
    
    return employees