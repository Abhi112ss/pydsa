METADATA = {
    "id": 739,
    "name": "Daily Temperatures",
    "slug": "daily-temperatures",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find how many days you have to wait until a warmer temperature occurs.",
}

def solve(temperatures: list[int]) -> list[int]:
    """
    Calculates the number of days to wait for a warmer temperature for each day.

    Args:
        temperatures: A list of integers representing daily temperatures.

    Returns:
        A list of integers where the i-th element is the number of days to wait 
        until a warmer temperature, or 0 if no such day exists.

    Examples:
        >>> solve([73, 74, 75, 71, 69, 72, 76, 73])
        [1, 1, 4, 2, 1, 1, 0, 0]
        >>> solve([30, 40, 50, 60])
        [1, 1, 1, 0]
        >>> solve([30, 30, 30])
        [0, 0, 0]
    """
    n = len(temperatures)
    answer = [0] * n
    # The stack will store indices of temperatures in a monotonic decreasing order.
    # This allows us to find the next greater element efficiently.
    stack: list[int] = []

    for current_day in range(n):
        current_temp = temperatures[current_day]
        
        # While the current temperature is warmer than the temperature at the 
        # index stored at the top of the stack, we have found the next warmer day.
        while stack and current_temp > temperatures[stack[-1]]:
            previous_day = stack.pop()
            # The difference in indices represents the number of days to wait.
            answer[previous_day] = current_day - previous_day
            
        # Push the current day's index onto the stack to find its next warmer day later.
        stack.append(current_day)

    return answer
