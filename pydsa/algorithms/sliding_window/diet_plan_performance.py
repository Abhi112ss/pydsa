METADATA = {
    "id": 1176,
    "name": "Diet Plan Performance",
    "slug": "diet-plan-performance",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the performance score based on a sliding window sum of calories over k days.",
}

def solve(calories: list[int], k: int) -> int:
    """
    Calculates the performance score based on the sum of calories over a k-day window.

    The performance score is calculated by subtracting the sum of calories 
    in each k-day window from the total sum of calories.

    Args:
        calories: A list of integers representing daily calorie intake.
        k: The size of the sliding window.

    Returns:
        The total performance score as an integer.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        11
        >>> solve([3, 2, 1], 3)
        3
    """
    total_calories_sum = sum(calories)
    n = len(calories)
    
    # Calculate the sum of the first window of size k
    current_window_sum = sum(calories[:k])
    
    # The performance score starts with the total sum minus the first window sum
    performance_score = total_calories_sum - current_window_sum
    
    # Slide the window across the array from index 1 to n-k
    for i in range(1, n - k + 1):
        # Update the window sum by removing the element that left the window 
        # and adding the element that entered the window
        current_window_sum = current_window_sum - calories[i - 1] + calories[i + k - 1]
        
        # Subtract the new window sum from the total score
        performance_score -= current_window_sum
        
    return performance_score
