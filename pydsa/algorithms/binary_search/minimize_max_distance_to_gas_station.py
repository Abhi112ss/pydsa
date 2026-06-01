METADATA = {
    "id": 774,
    "name": "Minimize Max Distance to Gas Station",
    "slug": "minimize-max-distance-to-gas-station",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(N * log(Max_Dist / Precision))",
    "space_complexity": "O(1)",
    "description": "Find the minimum possible maximum distance between adjacent gas stations after adding K new stations.",
}

def solve(gas_station: list[int], k: int) -> float:
    """
    Finds the minimum possible maximum distance between adjacent gas stations 
    after adding at most k new stations.

    Args:
        gas_station: A list of integers representing the positions of existing gas stations.
        k: The number of additional gas stations that can be added.

    Returns:
        The minimum possible maximum distance between any two adjacent gas stations.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)
        1.0
        >>> solve([1, 10], 1)
        4.5
    """
    
    def can_achieve_max_dist(max_dist: float) -> bool:
        """
        Checks if it is possible to have a maximum distance between stations 
        no greater than 'max_dist' by adding at most k stations.
        """
        added_stations = 0
        for i in range(len(gas_station) - 1):
            current_gap = gas_station[i + 1] - gas_station[i]
            # Calculate how many stations are needed to split this gap 
            # such that every sub-gap is <= max_dist.
            # We use (gap / max_dist) and take the ceiling, then subtract 1.
            # Using a small epsilon to handle floating point precision issues.
            needed = int(current_gap / max_dist - 1e-9)
            added_stations += needed
            
            if added_stations > k:
                return False
        return True

    # Binary search range: 
    # Lower bound is 0 (or a very small positive number).
    # Upper bound is the largest existing gap.
    low = 0.0
    high = float(gas_station[-1] - gas_station[0])
    
    # Perform binary search for a fixed number of iterations to ensure 
    # high precision (approx 100 iterations provides ~10^-30 precision).
    for _ in range(100):
        mid = (low + high) / 2
        if can_achieve_max_dist(mid):
            # If we can achieve this distance, try a smaller distance.
            high = mid
        else:
            # If we cannot, we need a larger distance.
            low = mid
            
    return high
