METADATA = {
    "id": 1891,
    "name": "Cutting Ribbons",
    "slug": "cutting_ribbons",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_len))",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of ribbons such that we can cut at least k ribbons from the given pieces.",
}

def solve(ribbons: list[int], k: int) -> int:
    """
    Finds the maximum possible length of ribbons such that we can obtain at least k pieces.

    Args:
        ribbons: A list of integers representing the lengths of available ribbon pieces.
        k: The required number of ribbon pieces of equal length.

    Returns:
        The maximum length of the ribbons. Returns 0 if it is impossible to get k pieces.

    Examples:
        >>> solve([4, 3, 2, 6], 4)
        2
        >>> solve([1, 1, 1], 4)
        0
        >>> solve([10, 10, 10], 3)
        10
    """
    if not ribbons or k <= 0:
        return 0

    # The minimum possible length is 1 (if we can't even get k pieces of length 1, return 0)
    # The maximum possible length is the maximum value in the input array
    low = 1
    high = max(ribbons)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        # Greedy check: Count how many pieces of length 'mid' we can get
        count = 0
        for length in ribbons:
            count += length // mid
        
        # If we can get at least k pieces, this length is a candidate
        # Try to see if a larger length is possible
        if count >= k:
            result = mid
            low = mid + 1
        else:
            # If we can't get k pieces, the length is too large
            high = mid - 1
            
    return result
