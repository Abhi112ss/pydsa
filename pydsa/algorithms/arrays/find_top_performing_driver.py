METADATA = {
    "id": 3308,
    "name": "Find Top Performing Driver",
    "slug": "find_top_performing_driver",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the driver with the highest total performance score, using driver ID as a tie-breaker.",
}

def solve(driver_ids: list[int], scores: list[int]) -> int:
    """
    Finds the driver ID with the highest total performance score.
    In case of a tie in scores, the driver with the smallest ID is chosen.

    Args:
        driver_ids: A list of integers representing the driver IDs.
        scores: A list of integers representing the performance scores for each driver.

    Returns:
        The driver ID of the top performing driver.

    Examples:
        >>> solve([1, 2, 1, 3, 2], [10, 20, 5, 30, 10])
        3
        >>> solve([1, 2, 3], [10, 10, 10])
        1
    """
    if not driver_ids:
        return -1

    # Aggregate total scores per driver using a hash map
    performance_map: dict[int, int] = {}
    for driver_id, score in zip(driver_ids, scores):
        performance_map[driver_id] = performance_map.get(driver_id, 0) + score

    # We need to find the max score. 
    # If scores are equal, we need the minimum driver_id.
    # We can achieve this by transforming the data into tuples: (score, -driver_id)
    # and finding the max, or by sorting.
    
    # Convert map to a list of tuples: (total_score, negative_driver_id)
    # Using negative driver_id allows us to use a standard max() function 
    # to pick the largest score and then the "largest" negative ID (which is the smallest actual ID).
    candidates: list[tuple[int, int]] = []
    for driver_id, total_score in performance_map.items():
        candidates.append((total_score, -driver_id))

    # Find the tuple with the maximum score and maximum negative ID
    best_performance = max(candidates)

    # Return the original driver ID (negate the negative ID back)
    return -best_performance[1]
