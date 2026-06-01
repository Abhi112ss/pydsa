METADATA = {
    "id": 2285,
    "name": "Maximum Total Importance of Roads",
    "slug": "maximum-total-importance-of-roads",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "hash_map", "array", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum total importance of roads by summing the product of each road's frequency and the importance of the cities it connects.",
}

def solve(roads: list[list[int]], cities: list[int]) -> int:
    """
    Calculates the maximum total importance of roads.

    The total importance is the sum of (importance of city u + importance of city v)
    for every road (u, v) in the roads list.

    Args:
        roads: A list of roads where each road is represented as [city1, city2].
        cities: A list where cities[i] is the importance of city i + 1.

    Returns:
        The maximum total importance of all roads.

    Examples:
        >>> solve([[1, 2], [1, 2], [1, 3], [1, 4], [1, 5], [4, 5]], [5, 4, 3, 2, 1])
        30
        >>> solve([[1, 2], [1, 2], [1, 3], [1, 4], [1, 5], [4, 5]], [1, 1, 1, 1, 1])
        12
    """
    # Use a dictionary to count the frequency of each unique road.
    # We sort the pair (u, v) to ensure that [1, 2] and [2, 1] are treated as the same road.
    road_counts: dict[tuple[int, int], int] = {}
    
    for u, v in roads:
        # Normalize the road representation by sorting the city indices
        road = (u, v) if u < v else (v, u)
        road_counts[road] = road_counts.get(road, 0) + 1
        
    total_importance = 0
    
    # Iterate through the unique roads and their frequencies.
    # For each road, the contribution to the total importance is:
    # frequency * (importance of city u + importance of city v)
    for (u, v), count in road_counts.items():
        # cities list is 0-indexed, so city i is at cities[i-1]
        importance_u = cities[u - 1]
        importance_v = cities[v - 1]
        total_importance += count * (importance_u + importance_v)
        
    return total_importance
