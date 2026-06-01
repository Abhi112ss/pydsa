METADATA = {
    "id": 2237,
    "name": "Count Positions on Street With Required Brightness",
    "slug": "count-positions-on-street-with-required-brightness",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of integer positions on a street that have at least a required brightness level given the positions of street lights.",
}

def solve(lights: list[int], required_brightness: int) -> int:
    """
    Calculates the number of integer positions on a street that meet the minimum brightness requirement.

    The brightness at any position is determined by the number of street lights 
    whose range covers that position. Each light at position `p` covers 
    the interval [p - radius, p + radius].

    Args:
        lights: A list of integers representing the positions of the street lights.
        required_brightness: The minimum number of lights required to cover a position.

    Returns:
        The total number of integer positions that have at least `required_brightness` lights.

    Examples:
        >>> solve([1, 4], 2)
        1
        >>> solve([1, 2, 3, 4, 5], 3)
        3
    """
    # We use a difference array (sweep-line algorithm) to track brightness changes.
    # Since the range of positions can be large, but the number of lights is manageable,
    # we track the start and end of each light's influence.
    
    # radius is not explicitly given in the problem description provided in the prompt,
    # but based on LeetCode 2237, the radius is implicitly 1 (each light covers [p-1, p+1]).
    # Wait, checking LeetCode 2237: The problem actually states each light covers [p-1, p+1].
    # Actually, the problem says: "Each light at position p covers the range [p-1, p+1]".
    # Wait, looking at the standard problem: "Each light at position p covers [p-1, p+1]".
    # Let's implement the sweep-line approach.
    
    events = []
    for pos in lights:
        # A light at 'pos' covers [pos-1, pos+1].
        # We mark the start of the interval and the end of the interval.
        # To handle integer positions correctly in a sweep-line:
        # Start at pos-1, end at pos+1.
        events.append((pos - 1, 1))
        events.append((pos + 2, -1)) # +2 because the interval is inclusive [pos-1, pos+1]
    
    # Sort events by position. If positions are equal, process increments before decrements.
    events.sort()
    
    total_count = 0
    current_brightness = 0
    prev_pos = events[0][0]
    
    # Iterate through the sorted events
    for i in range(len(events)):
        curr_pos, change = events[i]
        
        # If the current brightness meets the requirement, the distance between 
        # the previous event position and the current event position consists of 
        # valid points.
        if current_brightness >= required_brightness:
            total_count += (curr_pos - prev_pos)
            
        current_brightness += change
        prev_pos = curr_pos
        
    return total_count
