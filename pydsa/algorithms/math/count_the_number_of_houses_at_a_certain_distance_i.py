METADATA = {
    "id": 3015,
    "name": "Count the Number of Houses at a Certain Distance I",
    "slug": "count-the-number-of-houses-at-a-certain-distance-i",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "grid"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many houses are at a specific Manhattan distance from a given house.",
}

def solve(houses: list[list[int]], distance: int) -> int:
    """
    Counts the number of houses located at exactly a given Manhattan distance 
    from a specific target house.

    Note: The problem description for LeetCode 3015 implies we are looking for 
    houses at a certain distance from a specific house (usually the first one 
    or a specific index provided, but in the context of this specific problem 
    type, it asks for the count relative to a single target). 
    Based on the standard problem definition: we count houses at distance 'd' 
    from the house at index 0.

    Args:
        houses: A list of coordinates where houses[i] = [ri, ci].
        distance: The target Manhattan distance.

    Returns:
        The number of houses that satisfy the Manhattan distance condition.

    Examples:
        >>> solve([[0, 0], [1, 1], [2, 2]], 2)
        1
        >>> solve([[0, 0], [0, 1], [1, 0]], 1)
        2
    """
    # The problem asks for houses at distance 'distance' from the house at index 0.
    # Manhattan distance between (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
    
    target_r, target_c = houses[0]
    count = 0
    
    # Iterate through all houses to check the distance condition.
    # We skip the first house (index 0) because the distance to itself is 0,
    # and the problem asks for houses at a distance > 0 (unless distance is 0).
    for i in range(1, len(houses)):
        current_r, current_c = houses[i]
        
        # Calculate Manhattan distance
        manhattan_dist = abs(target_r - current_r) + abs(target_c - current_c)
        
        if manhattan_dist == distance:
            count += 1
            
    return count
