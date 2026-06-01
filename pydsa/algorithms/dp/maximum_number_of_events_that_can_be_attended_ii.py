METADATA = {
    "id": 1751,
    "name": "Maximum Number of Events That Can Be Attended II",
    "slug": "maximum-number-of-events-that-can-be-attended-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "binary_search", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of events you can attend given their start and end times and a limit on the total number of events.",
}

import bisect

def solve(events: list[list[int]], k: int) -> int:
    """
    Calculates the maximum number of events that can be attended.

    Args:
        events: A list of lists where each sublist contains [start_time, end_time, value].
        k: The maximum number of events that can be attended.

    Returns:
        The maximum total value of events that can be attended.

    Examples:
        >>> solve([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2)
        5
        >>> solve([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 3)
        8
    """
    # Sort events by start time to allow for efficient binary search of the next event
    events.sort()
    n = len(events)
    
    # Extract start times to use with bisect_right for finding the next compatible event
    start_times = [event[0] for event in events]
    
    # dp[i][j] represents the maximum value using a subset of events from index i to n-1
    # with at most j events remaining to be picked.
    # We use a 2D array for DP.
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Iterate backwards from the last event to the first
    for i in range(n - 1, -1, -1):
        start, end, value = events[i]
        
        # Find the index of the first event that starts after the current event ends
        # bisect_right finds the first index where start_times[idx] > end
        next_event_idx = bisect.bisect_right(start_times, end)
        
        for j in range(1, k + 1):
            # Option 1: Skip the current event
            skip_event = dp[i + 1][j]
            
            # Option 2: Attend the current event
            # We add current value and look up the result for the next compatible event
            attend_event = value + dp[next_event_idx][j - 1]
            
            dp[i][j] = max(skip_event, attend_event)

    return dp[0][k]
