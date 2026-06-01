METADATA = {
    "id": 2517,
    "name": "Maximum Tastiness of Candy Basket",
    "slug": "maximum-tastiness-of-candy-basket",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible minimum difference between any two candies in a subset of a given size.",
}

def solve(candy: list[int], num_candies: int) -> int:
    """
    Finds the maximum possible minimum difference between any two candies in a subset.

    Args:
        candy: A list of integers representing the tastiness of each candy.
        num_candies: The number of candies to select for the subset.

    Returns:
        The maximum possible minimum difference between any two candies in the subset.

    Examples:
        >>> solve([1, 5, 8, 10], 3)
        3
        >>> solve([1, 2, 3, 4, 5], 2)
        4
    """
    # Sort the candies to allow for a greedy check and binary search on the range
    candy.sort()
    
    def can_achieve_min_diff(min_diff: int) -> bool:
        """
        Checks if it is possible to select 'num_candies' such that 
        the difference between any two is at least 'min_diff'.
        """
        count = 1  # Select the first candy
        last_selected_value = candy[0]
        
        for i in range(1, len(candy)):
            # If the current candy satisfies the minimum difference requirement
            if candy[i] - last_selected_value >= min_diff:
                count += 1
                last_selected_value = candy[i]
                # If we have selected enough candies, return True early
                if count >= num_candies:
                    return True
        return False

    # Binary search range: 
    # Low is 0 (minimum possible difference)
    # High is the difference between the largest and smallest candy
    low = 0
    high = candy[-1] - candy[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        # If it's possible to have a minimum difference of 'mid', 
        # try to see if a larger difference is possible.
        if can_achieve_min_diff(mid):
            result = mid
            low = mid + 1
        else:
            # Otherwise, the difference is too large, search in the lower half.
            high = mid - 1
            
    return result
