METADATA = {
    "id": 3386,
    "name": "Button with Longest Push Time",
    "slug": "button-with-longest-push-time",
    "category": "Simulation",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the button that was pressed for the longest continuous duration in a sequence of button presses.",
}

def solve(presses: list[int]) -> int:
    """
    Finds the button that was pressed for the longest continuous duration.
    If multiple buttons have the same maximum duration, the one with the 
    smallest index is returned.

    Args:
        presses: A list of integers representing the sequence of button presses.

    Returns:
        The button index that was pressed for the longest continuous duration.

    Examples:
        >>> solve([1, 1, 2, 2, 2, 1, 1])
        2
        >>> solve([1, 2, 3])
        1
        >>> solve([5, 5, 5, 4, 4, 6])
        5
    """
    if not presses:
        return -1

    max_duration = 0
    best_button = presses[0]
    
    current_button = presses[0]
    current_duration = 0

    for button in presses:
        if button == current_button:
            # Increment the streak if the button is the same as the current streak
            current_duration += 1
        else:
            # Check if the completed streak is the longest seen so far
            if current_duration > max_duration:
                max_duration = current_duration
                best_button = current_button
            elif current_duration == max_duration:
                # If durations are equal, the problem implies we keep the first 
                # encountered or follow specific tie-breaking. 
                # Standard LeetCode tie-break is usually the smallest index/value.
                if current_button < best_button:
                    best_button = current_button
            
            # Reset for the new button streak
            current_button = button
            current_duration = 1

    # Final check for the last streak in the loop
    if current_duration > max_duration:
        max_duration = current_duration
        best_button = current_button
    elif current_duration == max_duration:
        if current_button < best_button:
            best_button = current_button

    return best_button
