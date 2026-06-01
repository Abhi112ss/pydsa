METADATA = {
    "id": 2021,
    "name": "Brightest Position on Street",
    "slug": "brightest-position-on-street",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "sorting", "sweep_line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the position on a street with the maximum number of overlapping light intervals.",
}

def solve(lights: list[list[int]]) -> int:
    """
    Finds the position on the street with the maximum number of overlapping lights.
    If multiple positions have the same maximum brightness, returns the smallest one.

    Args:
        lights: A list of intervals where lights[i] = [start_i, end_i].

    Returns:
        The smallest position with the maximum brightness.

    Examples:
        >>> solve([[1, 5], [2, 3], [3, 4]])
        3
        >>> solve([[1, 10], [5, 15], [10, 20]])
        10
    """
    # We use a sweep-line algorithm. 
    # For every interval [start, end], the brightness increases at 'start' 
    # and decreases after 'end'. To handle the inclusive nature of [start, end],
    # we mark the start as +1 and the position immediately after end (end + 1) as -1.
    events = []
    for start, end in lights:
        events.append((start, 1))
        events.append((end + 1, -1))

    # Sort events by position. If positions are equal, the order of +1 and -1 
    # doesn't strictly matter for the final max calculation because we want 
    # the smallest position, but sorting by position is the primary requirement.
    events.sort()

    max_brightness = 0
    current_brightness = 0
    best_position = 0

    # Iterate through the sorted events to track the current brightness level.
    for i in range(len(events)):
        position, change = events[i]
        current_brightness += change

        # Since multiple events can happen at the same position, we only 
        # evaluate the brightness after processing all events for the current position.
        # However, in this specific problem, because we use 'end + 1', 
        # the standard sweep-line logic works by checking max at every event.
        if i + 1 < len(events) and events[i + 1][0] == position:
            continue

        if current_brightness > max_brightness:
            max_brightness = current_brightness
            best_position = position

    return best_position
