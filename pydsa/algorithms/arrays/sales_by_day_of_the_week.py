METADATA = {
    "id": 1479,
    "name": "Sales by Day of the Week",
    "slug": "sales_by_day_of_the_week",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Aggregate daily sales amounts and return totals for each weekday in order.",
}


def solve(sales: list[str]) -> list[int]:
    """Aggregate sales amounts per weekday.

    Args:
        sales: A list of strings where each string is formatted as
            "<day> <amount>", e.g., "Mon 10". The day is one of
            "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" and amount
            is a non‑negative integer.

    Returns:
        A list of seven integers where the i‑th element represents the total
        sales for the i‑th day of the week (Monday through Sunday).

    Examples:
        >>> solve(["Mon 10", "Tue 20", "Mon 5"])
        [15, 20, 0, 0, 0, 0, 0]
        >>> solve(["Sun 7", "Sat 3", "Sun 2"])
        [0, 0, 0, 0, 0, 3, 9]
    """
    # Fixed mapping from day abbreviation to list index (Monday = 0)
    day_to_index = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6,
    }

    # Initialize totals for each day; constant size 7 → O(1) space
    weekly_totals = [0] * 7

    for entry in sales:
        # Split each entry into day and amount components
        day_part, amount_part = entry.split()
        day_index = day_to_index[day_part]          # map day to position
        weekly_totals[day_index] += int(amount_part)  # accumulate amount

    return weekly_totals