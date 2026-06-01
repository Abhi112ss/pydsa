METADATA = {
    "id": 573,
    "name": "Squirrel Simulation",
    "slug": "squirrel_simulation",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum distance a squirrel travels to collect all nuts from trees given its starting position.",
}

def solve(start_pos: int, trees: list[int], nuts: list[int]) -> int:
    """
    Calculates the minimum distance a squirrel travels to collect all nuts.
    
    The squirrel starts at start_pos. Each nut is located at a tree position.
    The squirrel must visit every tree that contains a nut.
    
    Args:
        start_pos: The initial position of the squirrel.
        trees: A list of positions where trees are located.
        nuts: A list of indices representing which tree contains a nut.
        
    Returns:
        The minimum total distance traveled.
        
    Examples:
        >>> solve(0, [1, 5], [0, 1])
        10
        >>> solve(3, [1, 5], [0, 1])
        6
    """
    if not nuts:
        return 0

    # Identify the range of positions that must be visited
    # We only care about the trees that actually have nuts
    min_pos = float('inf')
    max_pos = float('-inf')
    
    for nut_index in nuts:
        tree_pos = trees[nut_index]
        if tree_pos < min_pos:
            min_pos = tree_pos
        if tree_pos > max_pos:
            max_pos = tree_pos

    # If all nuts are at the same location
    if min_pos == max_pos:
        return abs(max_pos - start_pos)

    # The squirrel must cover the entire interval [min_pos, max_pos].
    # The total distance is at least 2 * (max_pos - min_pos) if the squirrel 
    # has to return to the start, but here it just needs to visit all.
    # However, the squirrel starts at start_pos.
    
    # Case 1: start_pos is to the left of the interval
    if start_pos <= min_pos:
        return max_pos - start_pos
    
    # Case 2: start_pos is to the right of the interval
    if start_pos >= max_pos:
        return start_pos - min_pos
    
    # Case 3: start_pos is inside the interval [min_pos, max_pos]
    # The squirrel has two optimal strategies:
    # 1. Go to min_pos first, then to max_pos: dist = (start - min) + (max - min)
    # 2. Go to max_pos first, then to min_pos: dist = (max - start) + (max - min)
    # This is equivalent to: 2 * (max - min) - max(distance_to_min, distance_to_max)
    # Or more simply: (max - min) + min(distance_to_min, distance_to_max)
    
    dist_to_min = start_pos - min_pos
    dist_to_max = max_pos - start_pos
    
    # The total distance is the span of the interval plus the shorter leg 
    # required to reach one of the boundaries from the start.
    return (max_pos - min_pos) + min(dist_to_min, dist_to_max)
