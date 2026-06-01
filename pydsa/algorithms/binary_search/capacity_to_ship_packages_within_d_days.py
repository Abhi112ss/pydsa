METADATA = {
    "id": 1011,
    "name": "Capacity To Ship Packages Within D Days",
    "slug": "capacity-to-ship-packages-within-d-days",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search_on_answer", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(sum(weights) - max(weights)))",
    "space_complexity": "O(1)",
    "description": "Find the minimum weight capacity of a ship that will allow all packages to be shipped within D days.",
}

def solve(weights: list[int], days: int) -> int:
    """
    Finds the minimum capacity required to ship all weights within the given days.

    Args:
        weights: A list of integers representing the weight of each package.
        days: The maximum number of days allowed to ship all packages.

    Returns:
        The minimum integer capacity of the ship.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
        15
        >>> solve([3, 2, 2, 4, 1, 4], 3)
        6
    """

    def can_ship_with_capacity(capacity: int) -> bool:
        """
        Checks if it is possible to ship all packages within 'days' using the given capacity.

        Args:
            capacity: The current capacity being tested.

        Returns:
            True if possible, False otherwise.
        """
        days_needed = 1
        current_load = 0
        
        for weight in weights:
            # If adding this weight exceeds capacity, start a new day
            if current_load + weight > capacity:
                days_needed += 1
                current_load = weight
            else:
                current_load += weight
                
        return days_needed <= days

    # The minimum possible capacity must be at least the heaviest package
    # The maximum possible capacity is the sum of all weights (shipping everything in 1 day)
    low = max(weights)
    high = sum(weights)
    result = high

    # Binary search over the range of possible capacities
    while low <= high:
        mid_capacity = (low + high) // 2
        
        if can_ship_with_capacity(mid_capacity):
            # If this capacity works, try to find a smaller one
            result = mid_capacity
            high = mid_capacity - 1
        else:
            # If this capacity is too small, increase the lower bound
            low = mid_capacity + 1
            
    return result
