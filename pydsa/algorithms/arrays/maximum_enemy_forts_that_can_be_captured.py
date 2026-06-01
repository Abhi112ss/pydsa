METADATA = {
    "id": 2511,
    "name": "Maximum Enemy Forts That Can Be Captured",
    "slug": "maximum-enemy-forts-that-can-be-captured",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of enemy forts that can be captured given a maximum distance constraint between the first and last fort.",
}

def solve(forts: list[int], maxDistance: int) -> int:
    """
    Finds the maximum number of forts that can be captured such that the 
    distance between the first and last captured fort is at most maxDistance.

    Args:
        forts: A list of integers representing the positions of enemy forts.
        maxDistance: The maximum allowed distance between the first and last fort.

    Returns:
        The maximum number of forts that can be captured.

    Examples:
        >>> solve([1, 3, 3, 3, 5], 3)
        4
        >>> solve([1, 1, 1, 1], 0)
        4
        >>> solve([1, 5, 10], 2)
        1
    """
    max_forts = 0
    left_pointer = 0
    n = len(forts)

    # Use a sliding window approach with two pointers
    for right_pointer in range(n):
        # If the current window exceeds the maxDistance, shrink it from the left
        while forts[right_pointer] - forts[left_pointer] > maxDistance:
            left_pointer += 1
        
        # Calculate the number of forts in the current valid window
        current_window_size = right_pointer - left_pointer + 1
        
        # Update the global maximum
        if current_window_size > max_forts:
            max_forts = current_window_size

    return max_forts
