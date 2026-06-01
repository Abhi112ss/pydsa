METADATA = {
    "id": 1507,
    "name": "Reformat Date",
    "slug": "reformat-date",
    "category": "String",
    "aliases": [],
    "tags": ["string", "parsing"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Reformat a date string from 'yyyy-mm-dd' format to 'd-m-yyyy' format.",
}

def solve(date: str) -> str:
    """
    Reformats a date string from 'yyyy-mm-dd' to 'd-m-yyyy'.

    Args:
        date: A string representing a date in 'yyyy-mm-dd' format.

    Returns:
        A string representing the reformatted date in 'd-m-yyyy' format.

    Examples:
        >>> solve("2002-12-08")
        '8-12-2002'
        >>> solve("2019-01-01")
        '1-1-2019'
    """
    # Split the input string by the hyphen delimiter to extract year, month, and day
    year, month, day = date.split("-")

    # Convert month and day to integers to remove leading zeros
    # Then convert back to strings to reconstruct the new format
    formatted_month = str(int(month))
    formatted_day = str(int(day))

    # Reconstruct the string using the template 'd-m-yyyy'
    return f"{formatted_day}-{formatted_month}-{year}"
