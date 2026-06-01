METADATA = {
    "id": 2078,
    "name": "Two Furthest Houses With Different Colors",
    "slug": "two-furthest-houses-with-different-colors",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum distance between two houses that have different colors.",
}

def solve(colors: list[int]) -> int:
    """
    Finds the maximum distance between two houses with different colors.

    The algorithm identifies the first and last occurrence of each color.
    Since we want the maximum distance between *different* colors, we compare
    the distance between the first and last house of different colors.
    The maximum distance must involve either the very first house or the very last house.

    Args:
        colors: A list of integers representing the colors of the houses.

    Returns:
        The maximum distance between two houses with different colors.

    Examples:
        >>> solve([1, 1, 2, 2, 3, 3, 4, 4])
        6
        >>> solve([1, 2, 1, 2])
        3
        >>> solve([1, 1, 1])
        -1
    """
    n = len(colors)
    if n < 2:
        return -1

    # Find the first house that has a different color than the first house
    first_diff_from_start = -1
    for i in range(1, n):
        if colors[i] != colors[0]:
            first_diff_from_start = i
            break
    
    # If all houses have the same color, no two different colors exist
    if first_diff_from_start == -1:
        return -1

    # Find the last house that has a different color than the last house
    last_diff_from_end = -1
    for i in range(n - 2, -1, -1):
        if colors[i] != colors[n - 1]:
            last_diff_from_end = i
            break

    # The maximum distance must be one of two possibilities:
    # 1. The distance between the first house and the last house that isn't its color.
    # 2. The distance between the last house and the first house that isn't its color.
    # However, a more robust way to think about it:
    # The max distance is either (last_index_of_color_X - first_index_of_color_Y)
    # The optimal pair will always involve either index 0 or index n-1.
    
    # Option A: Distance from index 0 to the last house that doesn't match colors[0]
    # We already found the first diff, but we need the LAST diff from index 0.
    last_diff_from_start_idx = -1
    for i in range(n - 1, 0, -1):
        if colors[i] != colors[0]:
            last_diff_from_start_idx = i
            break
            
    # Option B: Distance from index n-1 to the first house that doesn't match colors[n-1]
    first_diff_from_end_idx = -1
    for i in range(0, n - 1):
        if colors[i] != colors[n - 1]:
            first_diff_from_end_idx = i
            break

    # Calculate distances and return the maximum
    dist1 = last_diff_from_start_idx if last_diff_from_start_idx != -1 else -1
    dist2 = (n - 1) - first_diff_from_end_idx if first_diff_from_end_idx != -1 else -1
    
    return max(dist1, dist2)
