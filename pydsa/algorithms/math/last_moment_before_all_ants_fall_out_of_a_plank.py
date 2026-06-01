METADATA = {
    "id": 1503,
    "name": "Last Moment Before All Ants Fall Out of a Plank",
    "slug": "last-moment-before-all-ants-fall-out-of-a-plank",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the time until all ants fall off a plank, treating collisions as ants passing through each other.",
}

def solve(left_positions: list[int], right_positions: list[int], n: int) -> int:
    """
    Calculates the maximum time it takes for all ants to fall off the plank.
    
    The key insight is that when two ants collide and change directions, it is 
    mathematically equivalent to the ants simply passing through each other. 
    Therefore, we only need to find the maximum distance any single ant has 
    to travel to reach an edge.

    Args:
        left_positions: A list of integers representing positions of ants moving left.
        right_positions: A list of integers representing positions of ants moving right.
        n: The length of the plank.

    Returns:
        The maximum time (integer) until the last ant falls off.

    Examples:
        >>> solve([4, 3], [0, 1], 4)
        4
        >>> solve([0, 1, 2], [3, 4, 5], 10)
        5
    """
    max_time = 0

    # For ants moving left, the time taken is equal to their current position
    # (distance to position 0).
    for position in left_positions:
        if position > max_time:
            max_time = position

    # For ants moving right, the time taken is (n - current position)
    # (distance to position n).
    for position in right_positions:
        time_to_edge = n - position
        if time_to_edge > max_time:
            max_time = time_to_edge

    return max_time
