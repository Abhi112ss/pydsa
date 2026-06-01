METADATA = {
    "id": 1384,
    "name": "Total Sales Amount by Year",
    "slug": "total-sales-amount-by-year",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "logic", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total sales amount for each year in a given range by finding the intersection of sale periods and year periods.",
}

def solve(sales: list[list[int]], first_year: int, last_year: int) -> list[list[int]]:
    """
    Calculates the total sales amount for each year within a specified range.

    Args:
        sales: A list of sales records, where each record is [start_day, end_day, amount].
               The day is represented as (year - 1) * 365 + day_of_year.
        first_year: The starting year of the range.
        last_year: The ending year of the range.

    Returns:
        A list of lists where each sublist contains [year, total_amount] for that year.

    Examples:
        >>> sales = [[1, 365, 10], [366, 730, 20]]
        >>> first_year = 1
        >>> last_year = 2
        >>> solve(sales, first_year, last_year)
        [[1, 10], [2, 20]]
    """
    # Initialize results for each year in the range
    # Using a dictionary for O(1) access during accumulation
    results_map: dict[int, int] = {year: 0 for year in range(first_year, last_year + 1)}

    for start_day, end_day, amount in sales:
        # Determine the range of years this specific sale could potentially cover
        # A sale starting at day 1 is in year 1, a sale ending at 365 is in year 1
        # We calculate the year bounds to avoid iterating through all years for every sale
        start_year = (start_day - 1) // 365 + 1
        end_year = (end_day - 1) // 365 + 1

        # Only consider years within the requested [first_year, last_year] range
        actual_start_year = max(start_year, first_year)
        actual_end_year = min(end_year, last_year)

        for year in range(actual_start_year, actual_end_year + 1):
            # Calculate the boundaries of the current year in terms of absolute days
            year_start_day = (year - 1) * 365 + 1
            year_end_day = year * 365

            # Find the intersection of the sale period and the year period
            overlap_start = max(start_day, year_start_day)
            overlap_end = min(end_day, year_end_day)

            # If there is a valid overlap, calculate the amount for the overlapping days
            if overlap_start <= overlap_end:
                num_days = overlap_end - overlap_start + 1
                # amount is per day, so multiply by number of overlapping days
                results_map[year] += num_days * amount

    # Convert the dictionary to the required list of lists format, sorted by year
    return [[year, results_map[year]] for year in range(first_year, last_year + 1)]
