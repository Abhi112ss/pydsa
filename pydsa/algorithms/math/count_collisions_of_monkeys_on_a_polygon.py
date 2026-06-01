METADATA = {
    "id": 2550,
    "name": "Count Collisions of Monkeys on a Polygon",
    "slug": "count-collisions-of-monkeys-on-a-polygon",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of collisions of monkeys moving on a polygon based on their initial positions and directions.",
}

def solve(n: int, positions: list[int], directions: str) -> int:
    """
    Calculates the total number of collisions of monkeys on a polygon.

    A collision occurs when two monkeys move towards each other. On a polygon,
    if there is at least one monkey moving clockwise and at least one monkey 
    moving counter-clockwise, all monkeys will eventually collide. 
    The total number of collisions is equal to the number of monkeys that 
    are not already in a state that prevents a collision (i.e., they are 
    part of a group that will eventually meet).

    Args:
        n: The number of monkeys.
        positions: A list of integers representing the positions of the monkeys.
        directions: A string of length n where 'R' means clockwise and 'L' 
            means counter-clockwise.

    Returns:
        The total number of collisions.

    Examples:
        >>> solve(3, [1, 2, 3], "RRL")
        3
        >>> solve(4, [1, 2, 3, 4], "RRRR")
        0
        >>> solve(4, [1, 2, 3, 4], "LLLL")
        0
    """
    # If all monkeys move in the same direction, no collisions can ever occur.
    # We check if there is at least one 'R' and at least one 'L'.
    has_clockwise = False
    has_counter_clockwise = False
    
    for direction in directions:
        if direction == 'R':
            has_clockwise = True
        else:
            has_counter_clockwise = True
            
        # Optimization: if we found both, we can stop checking directions
        if has_clockwise and has_counter_clockwise:
            break
            
    if not (has_clockwise and has_counter_clockwise):
        return 0

    # If there is at least one monkey moving in each direction, 
    # every monkey will eventually participate in a collision.
    # This is because on a closed polygon, the relative distance between 
    # any two monkeys moving in opposite directions will eventually close.
    return n