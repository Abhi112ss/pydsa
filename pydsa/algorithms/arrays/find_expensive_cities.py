METADATA = {
    "id": 2987,
    "name": "Find Expensive Cities",
    "slug": "find-expensive-cities",
    "category": "Array",
    "aliases": [],
    "tags": ["filtering", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find all cities where the distance to any other city is greater than a given threshold.",
}

def solve(cities: list[list[int]], distance_threshold: int) -> list[int]:
    """
    Finds all cities that are 'expensive' based on the distance threshold.
    A city is expensive if the distance to every other city is greater than the threshold.

    Args:
        cities: A list of lists where cities[i] = [x_i, y_i, population_i].
        distance_threshold: The maximum distance allowed for a city to not be expensive.

    Returns:
        A list of indices of the expensive cities, sorted in ascending order.

    Examples:
        >>> solve([[1, 2, 1], [3, 4, 1]], 1)
        [0, 1]
        >>> solve([[1, 1, 1], [2, 2, 1], [3, 3, 1]], 1)
        [0, 2]
    """
    expensive_cities = []
    n = len(cities)

    for i in range(n):
        is_expensive = True
        x_i, y_i, _ = cities[i]
        
        # Check distance from city i to every other city j
        for j in range(n):
            if i == j:
                continue
            
            x_j, y_j, _ = cities[j]
            # Calculate squared Euclidean distance to avoid expensive sqrt operation
            # The condition dist > threshold is equivalent to dist^2 > threshold^2
            squared_dist = (x_i - x_j) ** 2 + (y_i - y_j) ** 2
            
            if squared_dist <= distance_threshold ** 2:
                # If any city is within the threshold, city i is not expensive
                is_expensive = False
                break
        
        if is_expensive:
            expensive_cities.append(i)

    return expensive_cities
