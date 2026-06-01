METADATA = {
    "id": 3017,
    "name": "Count the Number of Houses at a Certain Distance II",
    "slug": "count-the-number-of-houses-at-a-certain-distance-ii",
    "category": "math",
    "aliases": [],
    "tags": ["math", "prefix_sum", "coordinate_transformation"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs of houses with a Manhattan distance exactly equal to k using coordinate transformation.",
}

def solve(houses: list[list[int]], k: int) -> int:
    """
    Args:
        houses: A list of [x, y] coordinates representing house locations.
        k: The target Manhattan distance.

    Returns:
        The number of pairs of houses with Manhattan distance exactly k.
    """
    transformed_points = []
    for x, y in houses:
        transformed_points.append((x + y, x - y))

    point_counts = {}
    for u, v in transformed_points:
        point_counts[(u, v)] = point_counts.get((u, v), 0) + 1

    total_pairs = 0
    
    for (u, v), count in point_counts.items():
        target_u_plus_v = u + v + k
        target_u_minus_v = u - v + k
        
        if target_u_plus_v % 2 == 0 and target_u_minus_v % 2 == 0:
            target_u = (target_u_plus_v + target_u_minus_v) // 2
            target_v = (target_u_plus_v - target_u_minus_v) // 2
            if (target_u, target_v) in point_counts:
                total_pairs += count * point_counts[(target_u, target_v)]

        target_u_plus_v_alt = u + v + k
        target_u_minus_v_alt = u - v - k
        if target_u_plus_v_alt % 2 == 0 and target_u_minus_v_alt % 2 == 0:
            target_u = (target_u_plus_v_alt + target_u_minus_v_alt) // 2
            target_v = (target_u_plus_v_alt - target_u_minus_v_alt) // 2
            if (target_u, target_v) in point_counts:
                total_pairs += count * point_counts[(target_u, target_v)]

        target_u_plus_v_alt2 = u + v - k
        target_u_minus_v_alt2 = u - v + k
        if target_u_plus_v_alt2 % 2 == 0 and target_u_minus_v_alt2 % 2 == 0:
            target_u = (target_u_plus_v_alt2 + target_u_minus_v_alt2) // 2
            target_v = (target_u_plus_v_alt2 - target_u_minus_v_alt2) // 2
            if (target_u, target_v) in point_counts:
                total_pairs += count * point_counts[(target_u, target_v)]

        target_u_plus_v_alt3 = u + v - k
        target_u_minus_v_alt3 = u - v - k
        if target_u_plus_v_alt3 % 2 == 0 and target_u_minus_v_alt3 % 2 == 0:
            target_u = (target_u_plus_v_alt3 + target_u_minus_v_alt3) // 2
            target_v = (target_u_plus_v_alt3 - target_u_minus_v_alt3) // 2
            if (target_u, target_v) in point_counts:
                total_pairs += count * point_counts[(target_u, target_v)]

    if k == 0:
        ans = 0
        for count in point_counts.values():
            ans += (count * (count - 1)) // 2
        return ans

    return total_pairs // 2