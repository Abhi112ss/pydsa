METADATA = {
    "id": 3673,
    "name": "Find Zombie Sessions",
    "slug": "find_zombie_sessions",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "sweep-line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify sessions that are part of a continuous sequence of overlapping or adjacent time intervals.",
}

def solve(sessions: list[list[int]]) -> list[list[int]]:
    """
    Identifies continuous blocks of zombie sessions by merging overlapping or 
    adjacent time intervals.

    Args:
        sessions: A list of intervals where each interval is [start, end].

    Returns:
        A list of merged intervals representing the continuous zombie sessions.

    Examples:
        >>> solve([[1, 3], [2, 4], [6, 8]])
        [[1, 4], [6, 8]]
        >>> solve([[1, 2], [2, 3], [4, 5]])
        [[1, 3], [4, 5]]
    """
    if not sessions:
        return []

    # Sort sessions by start time to allow a single-pass sweep-line approach
    sorted_sessions = sorted(sessions, key=lambda x: x[0])
    
    merged_sessions: list[list[int]] = []
    
    # Initialize the current working interval with the first session
    current_start, current_end = sorted_sessions[0]

    for i in range(1, len(sorted_sessions)):
        next_start, next_end = sorted_sessions[i]

        # If the next session starts before or exactly when the current one ends,
        # they are part of the same continuous zombie session.
        if next_start <= current_end:
            # Update the end time to the maximum end time seen so far in this block
            current_end = max(current_end, next_end)
        else:
            # There is a gap; the current continuous session is finished.
            merged_sessions.append([current_start, current_end])
            # Start a new continuous session
            current_start, current_end = next_start, next_end

    # Append the final session block remaining after the loop
    merged_sessions.append([current_start, current_end])

    return merged_sessions
