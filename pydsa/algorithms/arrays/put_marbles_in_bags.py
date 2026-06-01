METADATA = {
    "id": 2551,
    "name": "Put Marbles in Bags",
    "slug": "put-marbles-in-bags",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum difference between the largest and smallest marble in any k consecutive bags after sorting.",
}

def solve(marbles: list[int], k: int) -> int:
    """
    Finds the minimum difference between the largest and smallest marble 
    in any k consecutive bags after sorting the marbles.

    Args:
        marbles: A list of integers representing the number of marbles in each bag.
        k: The number of consecutive bags to consider.

    Returns:
        The minimum difference between the maximum and minimum marble count 
        in any window of size k.

    Examples:
        >>> solve([1, 10, 5], 2)
        4
        >>> solve([10, 1, 2, 7, 12], 3)
        5
    """
    # Sorting allows us to ensure that for any window of size k, 
    # the minimum is at the start and the maximum is at the end.
    marbles.sort()
    
    # Initialize min_diff with a very large value.
    # The window size is k, so the difference is between index i and i + k - 1.
    min_diff = float('inf')
    n = len(marbles)
    
    # Iterate through all possible windows of size k.
    # The window starts at index i and ends at index i + k - 1.
    for i in range(n - k + 1):
        current_diff = marbles[i + k - 1] - marbles[i]
        if current_diff < min_diff:
            min_diff = current_diff
            
    return int(min_diff)
