METADATA = {
    "id": 1225,
    "name": "Report Contiguous Dates",
    "slug": "report_contiguous_dates",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "logic", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify and group contiguous date sequences from a given list of dates.",
}

from datetime import date, timedelta

def solve(dates: list[date]) -> list[list[date]]:
    """
    Identifies contiguous blocks of dates from a provided list.

    Args:
        dates: A list of datetime.date objects.

    Returns:
        A list of lists, where each inner list contains a sequence of 
        consecutive dates.

    Examples:
        >>> from datetime import date
        >>> solve([date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 4)])
        [[date(2023, 1, 1), date(2023, 1, 2)], [date(2023, 1, 4)]]
    """
    if not dates:
        return []

    # Sort dates to ensure we can process them linearly
    sorted_dates = sorted(dates)
    
    result: list[list[date]] = []
    if not sorted_dates:
        return result

    # Initialize the first group with the first date
    current_group: list[date] = [sorted_dates[0]]

    for i in range(1, len(sorted_dates)):
        # Check if the current date is exactly one day after the previous date
        # This handles the logic of identifying contiguous sequences
        if sorted_dates[i] == sorted_dates[i - 1] + timedelta(days=1):
            current_group.append(sorted_dates[i])
        elif sorted_dates[i] == sorted_dates[i - 1]:
            # Handle duplicate dates by ignoring them (keeping the sequence intact)
            continue
        else:
            # If there is a gap, finalize the current group and start a new one
            result.append(current_group)
            current_group = [sorted_dates[i]]

    # Append the final group processed in the loop
    result.append(current_group)
    
    return result
