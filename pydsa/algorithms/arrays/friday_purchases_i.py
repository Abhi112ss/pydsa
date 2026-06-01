METADATA = {
    "id": 2993,
    "name": "Friday Purchases I",
    "slug": "friday-purchases-i",
    "category": "Array",
    "aliases": [],
    "tags": ["filtering", "counting", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of transactions that occurred on a Friday given a list of transaction dates.",
}

from datetime import datetime

def solve(transactions: list[int]) -> int:
    """
    Counts how many transaction dates fall on a Friday.

    The input is a list of integers representing dates in the format YYYYMMDD.
    A date is considered a Friday if its day of the week is Friday.

    Args:
        transactions: A list of integers where each integer is a date in YYYYMMDD format.

    Returns:
        The total count of transactions that occurred on a Friday.

    Examples:
        >>> solve([20230512, 20230513, 20230519])
        2
        >>> solve([20230101, 20230102])
        0
    """
    friday_count = 0
    
    for date_int in transactions:
        # Convert integer YYYYMMDD to string to parse it
        date_str = str(date_int)
        
        # Parse the string into a datetime object
        # datetime.strptime is efficient for this scale
        current_date = datetime.strptime(date_str, "%Y%m%d")
        
        # weekday() returns 0 for Monday, ..., 4 for Friday, ..., 6 for Sunday
        if current_date.weekday() == 4:
            friday_count += 1
            
    return friday_count
