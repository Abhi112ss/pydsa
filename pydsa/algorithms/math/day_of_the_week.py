METADATA = {
    "id": 1185,
    "name": "Day of the Week",
    "slug": "day-of-the-week",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Given a date, return the day of the week it falls on.",
}

def solve(year: int, month: int, day: int) -> str:
    """
    Calculates the day of the week for a given date using Zeller's congruence or 
    a reference date calculation.

    Args:
        year: The year of the date.
        month: The month of the date (1-12).
        day: The day of the month.

    Returns:
        The name of the day of the week (e.g., "Monday").

    Examples:
        >>> solve(2019, 1, 1)
        'Tuesday'
        >>> solve(2014, 3, 15)
        'Saturday'
    """
    days_of_week = [
        "Sunday", "Monday", "Tuesday", "Wednesday", 
        "Thursday", "Friday", "Saturday"
    ]

    # We use a reference date: January 1, 1971 was a Friday.
    # However, a more robust way for any date is to use the formula for 
    # total days passed since a fixed epoch.
    
    # Adjust month and year for Zeller's congruence or similar algorithms:
    # In many algorithms, January and February are treated as months 13 and 14 
    # of the previous year.
    if month < 3:
        month += 12
        year -= 1

    # Zeller's congruence formula for the day of the week:
    # h = (q + floor(13(m+1)/5) + K + floor(K/4) + floor(J/4) - 2J) mod 7
    # where q is day, m is month, K is year of century, J is zero-based century.
    # However, a simpler approach for LeetCode constraints is calculating 
    # total days from a known epoch.
    
    # Let's use the standard Gregorian calendar math:
    # Total days = days from years + days from months + day
    
    def is_leap(y: int) -> bool:
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    # Calculate total days from year 1 to year-1
    # We use a simplified version of the formula for total days passed
    # to avoid O(N) loops.
    
    # Total days passed since year 1, month 1, day 1
    # This is a standard mathematical approach for Gregorian calendar.
    
    # Using the formula for day of week:
    # d = day
    # m = month
    # y = year
    # We adjust m and y for Jan/Feb
    if month <= 2:
        month += 12
        year -= 1
        
    # K = year % 100, J = year // 100
    k = year % 100
    j = year // 100
    
    # Zeller's congruence (modified for Gregorian)
    # h is the day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
    h = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    
    # Map Zeller's result to our days_of_week list
    # Zeller: 0:Sat, 1:Sun, 2:Mon, 3:Tue, 4:Wed, 5:Thu, 6:Fri
    zeller_to_standard = [6, 0, 1, 2, 3, 4, 5] # Index 0 is Sunday
    
    # Alternatively, map directly from Zeller's h:
    mapping = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }
    
    return mapping[h]
