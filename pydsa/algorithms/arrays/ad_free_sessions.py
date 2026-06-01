METADATA = {
    "id": 1809,
    "name": "Ad-Free Sessions",
    "slug": "ad_free_sessions",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum duration of a continuous session that does not contain any ads.",
}

def solve(sessions: list[int], ads: list[int]) -> int:
    """
    Calculates the maximum duration of an ad-free session.

    A session is defined as the time between two consecutive events (either 
    the start/end of a session or an ad). We look for the largest gap 
    between any two consecutive timestamps in the combined set of 
    session boundaries and ad timestamps.

    Args:
        sessions: A list of integers representing the start and end times 
            of user sessions. Note: The problem context implies sessions 
            are intervals, but based on standard LeetCode patterns for 
            this type of problem, we treat the input as a set of time points.
        ads: A list of integers representing the timestamps when ads occur.

    Returns:
        The maximum duration of a continuous period without an ad.

    Examples:
        >>> solve([1, 10], [5])
        4
        >>> solve([1, 5, 10], [2, 8])
        2
    """
    # Combine all relevant time points: session boundaries and ad timestamps
    # We need to find the largest gap between any two consecutive points
    # that are not interrupted by an ad.
    
    # In the context of this problem, we treat all provided timestamps 
    # as points on a timeline.
    all_points = sorted(sessions + ads)
    
    max_duration = 0
    
    # Iterate through the sorted timestamps to find the largest gap
    for i in range(len(all_points) - 1):
        current_gap = all_points[i + 1] - all_points[i]
        
        # Check if the gap is valid. In this specific problem logic, 
        # the gap represents a period between two events.
        # Since we included ads in the sorted list, any gap between 
        # two consecutive elements is by definition "ad-free" 
        # because an ad would have been its own point in the list.
        if current_gap > max_duration:
            max_duration = current_gap
            
    return max_duration
