METADATA = {
    "id": 3580,
    "name": "Find Consistently Improving Employees",
    "slug": "find_consistently_improving_employees",
    "category": "Arrays",
    "aliases": [],
    "tags": ["two_pointer", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of contiguous subarrays where each element is strictly greater than the previous one.",
}

def solve(performance_scores: list[int]) -> int:
    """
    Calculates the total number of contiguous subarrays where performance scores 
    are strictly increasing.

    Args:
        performance_scores: A list of integers representing employee performance scores.

    Returns:
        The total count of strictly increasing contiguous subarrays.

    Examples:
        >>> solve([1, 2, 3])
        6
        # Subarrays: [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]
        
        >>> solve([3, 2, 1])
        3
        # Subarrays: [3], [2], [1]
        
        >>> solve([1, 3, 2, 4])
        5
        # Subarrays: [1], [3], [2], [4], [1, 3], [2, 4]
    """
    if not performance_scores:
        return 0

    total_increasing_subarrays = 0
    current_streak_length = 0

    for i in range(len(performance_scores)):
        # If it's the first element or it's greater than the previous element,
        # increment the current streak of increasing numbers.
        if i > 0 and performance_scores[i] > performance_scores[i - 1]:
            current_streak_length += 1
        else:
            # Otherwise, reset the streak to 1 (the current element itself).
            current_streak_length = 1
        
        # A streak of length 'k' ending at index 'i' contributes 'k' new 
        # increasing subarrays ending at 'i' (e.g., if streak is [1, 2, 3], 
        # new subarrays are [3], [2, 3], [1, 2, 3]).
        total_increasing_subarrays += current_streak_length

    return total_increasing_subarrays
