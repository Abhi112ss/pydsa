METADATA = {
    "id": 2054,
    "name": "Two Best Non-Overlapping Events",
    "slug": "two-best-non-overlapping-events",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["greedy", "binary_search", "dp"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of values of two non-overlapping events.",
}

import bisect

def solve(startTime: list[int], endTime: list[int], value: list[int]) -> int:
    """
    Finds the maximum sum of values of two non-overlapping events.

    Args:
        startTime: A list of integers representing the start times of events.
        endTime: A list of integers representing the end times of events.
        value: A list of integers representing the values of events.

    Returns:
        The maximum sum of values of two non-overlapping events.

    Examples:
        >>> solve([1, 2, 3, 4], [2, 3, 4, 5], [4, 3, 1, 2])
        6
        >>> solve([1, 1, 1], [2, 2, 2], [1, 2, 3])
        0
    """
    n = len(startTime)
    # Combine event data into a list of tuples for easier sorting
    # Each tuple: (end_time, start_time, value)
    events = []
    for i in range(n):
        events.append((endTime[i], startTime[i], value[i]))

    # Sort events by end time to facilitate binary search for non-overlapping predecessors
    events.sort()

    # Extract sorted end times for binary search
    sorted_end_times = [e[0] for e in events]
    
    # prefix_max[i] stores the maximum value of a single event among the first i events (sorted by end time)
    prefix_max = [0] * (n + 1)
    current_max = 0
    for i in range(n):
        current_max = max(current_max, events[i][2])
        prefix_max[i + 1] = current_max

    max_total_value = 0

    for i in range(n):
        curr_end, curr_start, curr_val = events[i]

        # Find the rightmost event that ends before the current event starts.
        # bisect_left returns the leftmost insertion point to maintain order.
        # We want the index of the event where event.end_time < curr_start.
        # bisect_left on sorted_end_times with curr_start gives the index of the first 
        # event that ends >= curr_start. Therefore, index - 1 is the last event that ends < curr_start.
        idx = bisect.bisect_left(sorted_end_times, curr_start)
        
        # If idx > 0, there is at least one event that ends before the current one starts
        if idx > 0:
            # The best non-overlapping event is the one with the maximum value 
            # among all events ending before curr_start.
            # We use prefix_max[idx] because prefix_max is 1-indexed relative to events.
            max_total_value = max(max_total_value, curr_val + prefix_max[idx])

    return max_total_value
