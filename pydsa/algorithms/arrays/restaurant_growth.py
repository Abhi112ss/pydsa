METADATA = {
    "id": 1321,
    "name": "Restaurant Growth",
    "slug": "restaurant-growth",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total amount for each day considering the current day and the previous six days.",
}

def solve(amounts: list[int]) -> list[int]:
    """
    Calculates the total amount for each day, including the current day and the 
    previous six days (a 7-day window).

    Args:
        amounts: A list of integers representing the daily amounts.

    Returns:
        A list of integers where each element is the sum of the current day 
        and the previous six days.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9])
        [1, 3, 6, 10, 15, 21, 28, 35, 42]
        >>> solve([10, 20, 30])
        [10, 30, 60]
    """
    n = len(amounts)
    result = [0] * n
    current_window_sum = 0

    for i in range(n):
        # Add the current day's amount to the window
        current_window_sum += amounts[i]
        
        # If the window exceeds 7 days, subtract the element that is no longer in the window
        if i >= 7:
            current_window_sum -= amounts[i - 7]
            
        result[i] = current_window_sum

    return result
