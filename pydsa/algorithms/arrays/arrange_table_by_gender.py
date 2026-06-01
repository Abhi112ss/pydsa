METADATA = {
    "id": 2308,
    "name": "Arrange Table by Gender",
    "slug": "arrange_table_by_gender",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Return the rows sorted so that females appear before males.",
}

def solve(table: list[dict[str, str]]) -> list[dict[str, str]]:
    """Sort a list of gender records so that females appear before males.

    Args:
        table: A list of dictionaries, each containing the keys:
            - "name": the person's name (string)
            - "sex": the gender character, either "f" for female or "m" for male

    Returns:
        A new list of dictionaries sorted by gender, with all rows where
        "sex" == "f" appearing before rows where "sex" == "m". The relative
        order within each gender group is preserved (stable sort).

    Examples:
        >>> records = [{"name": "Alice", "sex": "f"}, {"name": "Bob", "sex": "m"}]
        >>> solve(records)
        [{'name': 'Alice', 'sex': 'f'}, {'name': 'Bob', 'sex': 'm'}]

        >>> records = [{"name": "Tom", "sex": "m"}, {"name": "Jane", "sex": "f"}]
        >>> solve(records)
        [{'name': 'Jane', 'sex': 'f'}, {'name': 'Tom', 'sex': 'm'}]
    """
    # Use a key that maps 'f' to 0 and 'm' to 1; this ensures females come first.
    # The built‑in sorted function is stable, preserving original order within groups.
    sorted_table = sorted(table, key=lambda row: 0 if row.get("sex") == "f" else 1)
    return sorted_table