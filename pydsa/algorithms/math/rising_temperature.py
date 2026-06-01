METADATA = {
    "id": 197,
    "name": "Rising Temperature",
    "slug": "rising_temperature",
    "category": "Database",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all dates with higher temperature than the previous day using a self-join on date difference.",
}


def solve(weather_rows: list[dict]) -> list[int]:
    """
    Given a list of weather records, return the IDs of dates where the temperature
    is higher than the previous day's temperature.

    Args:
        weather_rows: A list of dicts, each with keys 'id', 'recordDate', and 'temperature'.
                      'recordDate' is a string in 'YYYY-MM-DD' format.

    Returns:
        A list of integer IDs where the temperature rose compared to the previous day.

    Examples:
        >>> rows = [
        ...     {"id": 1, "recordDate": "2015-01-01", "temperature": 10},
        ...     {"id": 2, "recordDate": "2015-01-02", "temperature": 25},
        ...     {"id": 3, "recordDate": "2015-01-03", "temperature": 20},
        ...     {"id": 4, "recordDate": "2015-01-04", "temperature": 30},
        ... ]
        >>> solve(rows)
        [2, 4]
    """
    from datetime import datetime, timedelta

    # Build a lookup from date string to (id, temperature) for O(1) access
    date_to_info: dict[str, tuple[int, int]] = {}
    for row in weather_rows:
        date_to_info[row["recordDate"]] = (row["id"], row["temperature"])

    result: list[int] = []

    # For each row, check if the previous day exists and has a lower temperature
    for row in weather_rows:
        current_date = datetime.strptime(row["recordDate"], "%Y-%m-%d")
        previous_date = current_date - timedelta(days=1)
        previous_date_str = previous_date.strftime("%Y-%m-%d")

        if previous_date_str in date_to_info:
            previous_temp = date_to_info[previous_date_str][1]
            if row["temperature"] > previous_temp:
                result.append(row["id"])

    return result