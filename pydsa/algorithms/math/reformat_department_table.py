METADATA = {
    "id": 1179,
    "name": "Reformat Department Table",
    "slug": "reformat_department_table",
    "category": "database",
    "aliases": [],
    "tags": ["pivot", "group_by"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Pivot the Department table to have separate month columns.",
}


def solve(department: list[list[object]]) -> list[list[object]]:
    """Pivot department data so each department has separate month columns.

    Args:
        department: A list of rows, each row is [id, name, month, revenue].

    Returns:
        A list of rows, each row is [id, name, Jan, Feb, Mar] where missing
        month revenues are represented by None. Rows are ordered by ascending id.

    Examples:
        >>> solve([[1, "A", "Jan", 100], [1, "A", "Feb", 200], [2, "B", "Mar", 300]])
        [[1, "A", 100, 200, None], [2, "B", None, None, 300]]
    """
    # Mapping from (id, name) to a dict of month -> revenue
    pivot: dict[tuple[int, str], dict[str, int]] = {}

    for row in department:
        dept_id, dept_name, month, revenue = row  # unpack row
        key = (dept_id, dept_name)
        if key not in pivot:
            pivot[key] = {}
        pivot[key][month] = revenue  # aggregate revenue per month

    # Build the result list, ordering by department id
    result: list[list[object]] = []
    for (dept_id, dept_name), month_map in sorted(pivot.items(), key=lambda item: item[0][0]):
        jan_rev = month_map.get("Jan")
        feb_rev = month_map.get("Feb")
        mar_rev = month_map.get("Mar")
        result.append([dept_id, dept_name, jan_rev, feb_rev, mar_rev])

    return result