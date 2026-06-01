METADATA = {
    "id": 1715,
    "name": "Count Apples and Oranges",
    "slug": "count-apples-and-oranges",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of apples and oranges that pass through a given range [left, right] using the quadratic formula.",
}

import math

def solve(left: int, right: int, startApple: int, endApple: int, startOrange: int, endOrange: int) -> list[int]:
    """
    Calculates the number of apples and oranges that pass through the range [left, right].

    The position of a fruit at time t is given by: position = start + direction * t^2.
    We need to find the number of integer time steps t >= 0 such that:
    left <= start + direction * t^2 <= right.

    Args:
        left: The left boundary of the range.
        right: The right boundary of the range.
        startApple: The starting position of the apple.
        endApple: The direction of the apple (1 or -1).
        startOrange: The starting position of the orange.
        endOrange: The direction of the orange (1 or -1).
        startOrange: The starting position of the orange.
        endOrange: The direction of the orange (1 or -1).

    Returns:
        A list of two integers [apple_count, orange_count].

    Examples:
        >>> solve(5, 8, 1, 1, 10, -1)
        [2, 3]
    """

    def count_fruits_in_range(start: int, direction: int, left: int, right: int) -> int:
        """
        Helper to find the number of integer t >= 0 satisfying the range condition.
        
        The inequality is: left <= start + direction * t^2 <= right
        
        If direction == 1:
            left <= start + t^2  =>  t^2 >= left - start
            start + t^2 <= right =>  t^2 <= right - start
            So: max(0, left - start) <= t^2 <= right - start
            
        If direction == -1:
            left <= start - t^2  =>  t^2 <= start - left
            start - t^2 <= right =>  t^2 >= start - right
            So: max(0, start - right) <= t^2 <= start - left
        """
        
        # Define the bounds for t^2 based on the direction
        if direction == 1:
            lower_t_sq = max(0, left - start)
            upper_t_sq = right - start
        else:
            lower_t_sq = max(0, start - right)
            upper_t_sq = start - left

        # If the upper bound for t^2 is negative, no fruit ever enters the range
        if upper_t_sq < 0 or lower_t_sq > upper_t_sq:
            return 0

        # Find the range of integer t values.
        # t_min is the smallest integer such that t^2 >= lower_t_sq
        # t_max is the largest integer such that t^2 <= upper_t_sq
        t_min = math.ceil(math.sqrt(lower_t_sq))
        t_max = math.floor(math.sqrt(upper_t_sq))

        # If t_min > t_max, no integer t exists in the interval
        if t_min > t_max:
            return 0
        
        return t_max - t_min + 1

    apple_count = count_fruits_in_range(startApple, endApple, left, right)
    orange_count = count_fruits_in_range(startOrange, endOrange, left, right)

    return [apple_count, orange_count]
