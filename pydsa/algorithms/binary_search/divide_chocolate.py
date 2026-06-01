METADATA = {
    "id": 1231,
    "name": "Divide Chocolate",
    "slug": "divide_chocolate",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(sum(sweetness)))",
    "space_complexity": "O(1)",
    "description": "Find the maximum minimum sweetness value possible when dividing a chocolate bar into k+1 pieces.",
}

def solve(sweetness: list[int], k: int) -> int:
    """
    Finds the maximum possible minimum sweetness value among k+1 pieces.

    Args:
        sweetness: A list of integers representing the sweetness of each chocolate piece.
        k: The number of additional pieces to create (total pieces = k + 1).

    Returns:
        The maximum possible minimum sweetness value.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        5
        >>> solve([8, 1, 3, 2, 1, 4, 5, 9], 3)
        4
    """
    
    def can_divide(min_sweetness_threshold: int) -> bool:
        """
        Checks if it is possible to divide the chocolate into at least k+1 pieces
        where each piece has at least min_sweetness_threshold sweetness.
        """
        pieces_count = 0
        current_sum = 0
        
        for s in sweetness:
            current_sum += s
            # If current accumulated sweetness meets the threshold, "cut" the piece
            if current_sum >= min_sweetness_threshold:
                pieces_count += 1
                current_sum = 0
        
        # We need at least k + 1 pieces
        return pieces_count >= k + 1

    # The range for binary search:
    # Low: The smallest possible sweetness (at least 1)
    # High: The total sum of all sweetness (the maximum possible single piece)
    low = 1
    high = sum(sweetness)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        # If we can achieve a minimum sweetness of 'mid', try a larger value
        if can_divide(mid):
            result = mid
            low = mid + 1
        else:
            # If 'mid' is too high, we must search in the lower half
            high = mid - 1
            
    return result
