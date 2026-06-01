METADATA = {
    "id": 447,
    "name": "Number of Boomerangs",
    "slug": "number-of-boomerangs",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of triplets of points that form a boomerang.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the number of boomerangs in a given set of points.
    
    A boomerang is a tuple of points (i, j, k) such that the distance 
    between i and j is equal to the distance between i and k.

    Args:
        points: A list of coordinates where points[i] = [x_i, y_i].

    Returns:
        The total number of boomerangs.

    Examples:
        >>> solve([[0,0],[1,0],[2,0]])
        2
        >>> solve([[0,0]])
        0
    """
    total_boomerangs = 0

    for i in range(len(points)):
        # distance_counts stores the frequency of squared Euclidean distances 
        # from the current point points[i] to all other points.
        distance_counts: dict[int, int] = {}
        x1, y1 = points[i]

        for j in range(len(points)):
            if i == j:
                continue
            
            x2, y2 = points[j]
            # Use squared distance to avoid floating point precision issues with sqrt
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
            
            distance_counts[dist_sq] = distance_counts.get(dist_sq, 0) + 1

        # For a fixed center point i, if there are 'count' points at the same 
        # distance, we can choose 2 points out of 'count' to form a boomerang.
        # The number of permutations P(count, 2) = count * (count - 1).
        for count in distance_counts.values():
            if count > 1:
                total_boomerangs += count * (count - 1)

    return total_boomerangs
