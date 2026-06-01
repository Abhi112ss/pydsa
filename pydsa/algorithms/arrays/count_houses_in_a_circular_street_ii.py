METADATA = {
    "id": 2753,
    "name": "Count Houses in a Circular Street II",
    "slug": "count-houses-in-a-circular-street-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays", "circular_array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of houses that can be selected in a circular street such that no two selected houses are adjacent.",
}

def solve(houses: list[int]) -> int:
    """
    Calculates the maximum number of houses that can be selected in a circular 
    street such that no two selected houses are adjacent.

    Args:
        houses: A list of integers where houses[i] represents the value of the i-th house.

    Returns:
        The maximum sum of values of non-adjacent houses in a circular arrangement.

    Examples:
        >>> solve([1, 2, 3, 1])
        4
        >>> solve([1, 2, 3])
        3
        >>> solve([5, 1, 1, 5])
        6
    """
    n = len(houses)
    
    # Base cases for small arrays
    if n == 0:
        return 0
    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0], houses[1])

    def solve_linear(arr: list[int]) -> int:
        """Standard House Robber I logic for a linear arrangement."""
        prev_max = 0
        curr_max = 0
        for val in arr:
            # Standard DP: max(include current + two steps back, exclude current)
            temp = curr_max
            curr_max = max(prev_max + val, curr_max)
            prev_max = temp
        return curr_max

    # In a circular street, you cannot pick both the first and the last house.
    # Therefore, the answer is the maximum of two scenarios:
    # 1. Exclude the last house (consider houses from index 0 to n-2)
    # 2. Exclude the first house (consider houses from index 1 to n-1)
    
    case_exclude_last = solve_linear(houses[:-1])
    case_exclude_first = solve_linear(houses[1:])

    return max(case_exclude_last, case_exclude_first)
