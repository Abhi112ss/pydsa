METADATA = {
    "id": 1853,
    "name": "Convert Date Format",
    "slug": "convert_date_format",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Convert a date string from 'Day Month Year' format to 'YYYY-MM-DD' format.",
}


def solve(date: str) -> str:
    """Convert a date string from "Day Month Year" format to "YYYY-MM-DD".

    Args:
        date: A string representing a date, e.g., "20th Oct 2052".

    Returns:
        A string formatted as "YYYY-MM-DD", e.g., "2052-10-20".

    Examples:
        >>> solve("20th Oct 2052")
        '2052-10-20'
        >>> solve("6th Jun 1933")
        '1933-06-06'
    """
    # Mapping of month abbreviations to their two‑digit numeric representation.
    month_to_number = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    # Split the input into day, month, and year components.
    day_part, month_part, year_part = date.split(" ")

    # Remove the ordinal suffix ("st", "nd", "rd", "th") from the day.
    day_number = day_part[:-2]

    # Look up the numeric month string.
    month_number = month_to_number[month_part]

    # Ensure day is two digits.
    day_two_digits = day_number.zfill(2)

    # Assemble the final ISO‑8601 format.
    return f"{year_part}-{month_number}-{day_two_digits}"