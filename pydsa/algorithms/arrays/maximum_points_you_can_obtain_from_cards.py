METADATA = {
    "id": 1423,
    "name": "Maximum Points You Can Obtain from Cards",
    "slug": "maximum-points-you-can-obtain-from-cards",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum points you can obtain by picking k cards from either the beginning or the end of the array.",
}

def solve(card_points: list[int], k: int) -> int:
    """
    Calculates the maximum points obtainable by picking k cards from the ends.

    The problem is equivalent to finding a contiguous subarray of size (n - k) 
    with the minimum sum. The maximum points will be the total sum of all 
    cards minus this minimum subarray sum.

    Args:
        card_points: A list of integers representing the points on each card.
        k: The number of cards to pick.

    Returns:
        The maximum points possible.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 1], 3)
        12
        >>> solve([2, 2, 2], 2)
        4
        >>> solve([9, 7, 7, 9, 7, 7, 9], 7)
        50
    """
    n = len(card_points)
    window_size = n - k
    
    # If we pick all cards, return the total sum immediately
    if window_size == 0:
        return sum(card_points)

    # Calculate the sum of the initial window of size (n - k)
    current_window_sum = 0
    for i in range(window_size):
        current_window_sum += card_points[i]
    
    min_window_sum = current_window_sum
    total_sum = current_window_sum
    
    # Slide the window across the array to find the minimum sum
    # We start from the end of the first window and move to the end of the array
    for i in range(window_size, n):
        total_sum += card_points[i]
        # Add the new element entering the window and remove the one leaving
        current_window_sum += card_points[i] - card_points[i - window_size]
        if current_window_sum < min_window_sum:
            min_window_sum = current_window_sum
            
    # The maximum points is the total sum minus the smallest sum of unpicked cards
    return total_sum - min_window_sum
