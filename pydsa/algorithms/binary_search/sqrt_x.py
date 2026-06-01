METADATA = {
    "id": 69,
    "name": "Sqrt(x)",
    "slug": "sqrtx",
    "category": "math",
    "aliases": [],
    "tags": ["binary_search", "math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Compute the integer square root of a non-negative integer.",
}

def solve(x: int) -> int:
    """
    Compute the integer square root of a non-negative integer x.
    
    Args:
        x: Non-negative integer for which to compute the integer square root.
    
    Returns:
        The largest integer k such that k*k <= x.
    
    Examples:
        >>> solve(4)
        2
        >>> solve(8)
        2
        >>> solve(9)
        3
    """
    # Handle edge case where x is 0
    if x == 0:
        return 0
    
    # Initialize binary search bounds
    low, high = 0, x
    
    # Perform binary search to find the largest integer k where k*k <= x
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        
        # If we found exact square, return immediately
        if square == x:
            return mid
        # If square is too small, search upper half
        elif square < x:
            low = mid + 1
        # If square is too large, search lower half
        else:
            high = mid - 1
    
    # After loop, high is the largest integer satisfying the condition
    return high