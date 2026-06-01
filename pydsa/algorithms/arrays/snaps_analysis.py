METADATA = {
    "id": 3056,
    "name": "Snaps Analysis",
    "slug": "snaps_analysis",
    "category": "Hash Map",
    "aliases": [],
    "tags": ["hash_map", "arrays", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Analyze snap frequencies and calculate metrics using a hash map approach.",
}

def solve(snaps: list[int], k: int) -> list[float]:
    """
    Analyzes snap data to find the moving average of snap frequencies 
    within a window of size k.

    Args:
        snaps: A list of integers representing snap identifiers or timestamps.
        k: The window size for the moving average calculation.

    Returns:
        A list of floats representing the moving average of unique snap 
        counts in each window of size k.

    Examples:
        >>> solve([1, 2, 1, 3, 3], 3)
        [2.0, 2.3333333333333335, 2.3333333333333335]
    """
    if not snaps or k <= 0:
        return []

    n = len(snaps)
    if k > n:
        # If window is larger than array, return average of the whole array
        unique_count = len(set(snaps))
        return [unique_count / k]

    results = []
    frequency_map: dict[int, int] = {}
    current_unique_count = 0

    # Initialize the first window
    for i in range(k):
        val = snaps[i]
        if frequency_map.get(val, 0) == 0:
            current_unique_count += 1
        frequency_map[val] = frequency_map.get(val, 0) + 1
    
    results.append(current_unique_count / k)

    # Slide the window across the array
    for i in range(k, n):
        # Remove the element sliding out of the window
        out_val = snaps[i - k]
        frequency_map[out_val] -= 1
        if frequency_map[out_val] == 0:
            current_unique_count -= 1
        
        # Add the element sliding into the window
        in_val = snaps[i]
        if frequency_map.get(in_val, 0) == 0:
            current_unique_count += 1
        frequency_map[in_val] = frequency_map.get(in_val, 0) + 1
        
        # Calculate the metric for the current window
        results.append(current_unique_count / k)

    return results
