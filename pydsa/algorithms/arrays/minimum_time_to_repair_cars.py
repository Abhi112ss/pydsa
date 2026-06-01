METADATA = {
    "id": 2594,
    "name": "Minimum Time to Repair Cars",
    "slug": "minimum-time-to-repair-cars",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(max_time))",
    "space_complexity": "O(1)",
    "description": "Find the minimum time required to repair all cars given a list of repair times for each mechanic.",
}

def solve(cars: list[int], mechanics: list[int]) -> int:
    """
    Calculates the minimum time required to repair all cars using the given mechanics.

    The problem is solved using binary search on the answer (the total time). 
    For a fixed time 'T', we check if the total number of cars that can be 
    repaired by all mechanics within 'T' is greater than or equal to the 
    total number of cars.

    Args:
        cars: A list of integers representing the number of cars to be repaired.
        mechanics: A list of integers representing the time taken by each mechanic to repair one car.

    Returns:
        The minimum time required to repair all cars.

    Examples:
        >>> solve([1, 2, 3], [1, 2])
        3
        >>> solve([10, 10, 10, 10], [1, 2, 3, 4])
        10
    """
    total_cars_needed = sum(cars)
    
    def can_repair_all(time_limit: int) -> bool:
        """Checks if all cars can be repaired within the given time limit."""
        repaired_count = 0
        for repair_rate in mechanics:
            # Each mechanic can repair (time_limit // repair_rate) cars
            repaired_count += time_limit // repair_rate
            if repaired_count >= total_cars_needed:
                return True
        return repaired_count >= total_cars_needed

    # Binary search range:
    # Low: 1 (minimum possible time)
    # High: The worst case is one mechanic (the slowest) repairing all cars.
    # To be safe and efficient, we use the fastest mechanic repairing all cars.
    low = 1
    high = min(mechanics) * total_cars_needed
    
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        # If the current time 'mid' is sufficient, try to find a smaller time
        if can_repair_all(mid):
            ans = mid
            high = mid - 1
        else:
            # If not sufficient, we need more time
            low = mid + 1
            
    return ans
