METADATA = {
    "id": 2604,
    "name": "Minimum Time to Eat All Grains",
    "slug": "minimum-time-to-eat-all-grains",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log(max_time))",
    "space_complexity": "O(1)",
    "description": "Find the minimum time required to eat all grains given specific consumption constraints using binary search.",
}

def solve(grains: list[int], capacity: int) -> int:
    """
    Calculates the minimum time required to eat all grains.

    Args:
        grains: A list of integers representing the amount of grains in each pile.
        capacity: The maximum amount of grains that can be eaten in one unit of time.

    Returns:
        The minimum time required to eat all grains.

    Examples:
        >>> solve([3, 2, 4], 2)
        5
        >>> solve([1, 1, 1], 1)
        3
    """
    
    def can_eat_all(time_limit: int) -> bool:
        """
        Checks if it is possible to eat all grains within the given time limit.
        
        Args:
            time_limit: The maximum allowed time.
            
        Returns:
            True if possible, False otherwise.
        """
        total_time_needed = 0
        for grain_pile in grains:
            # Calculate time needed for the current pile: ceil(grain_pile / capacity)
            # Using (a + b - 1) // b for integer ceiling division
            time_for_pile = (grain_pile + capacity - 1) // capacity
            total_time_needed += time_for_pile
            
            # Early exit if we exceed the time limit
            if total_time_needed > time_limit:
                return False
        return total_time_needed <= time_limit

    # The minimum possible time is the sum of grains divided by capacity (rounded up)
    # or simply 1 if grains are empty. However, a safer lower bound is 1.
    # The maximum possible time is the sum of all grains (if capacity is 1).
    low = 1
    high = sum(grains)
    ans = high

    # Binary search on the answer space [low, high]
    while low <= high:
        mid = (low + high) // 2
        if can_eat_all(mid):
            # If mid is a valid time, try to find a smaller valid time
            ans = mid
            high = mid - 1
        else:
            # If mid is not enough time, we must increase the time limit
            low = mid + 1
            
    return ans
