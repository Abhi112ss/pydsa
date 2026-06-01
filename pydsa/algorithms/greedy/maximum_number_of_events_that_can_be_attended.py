METADATA = {
    "id": 1353,
    "name": "Maximum Number of Events That Can Be Attended",
    "slug": "maximum-number-of-events-that-can-be-attended",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heaps", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of events you can attend given their start and end days.",
}

import heapq

def solve(events: list[list[int]]) -> int:
    """
    Calculates the maximum number of events that can be attended.
    
    The strategy is to use a greedy approach: on any given day, if multiple 
    events are available, always pick the one that ends the earliest to 
    maximize future availability.

    Args:
        events: A list of lists where events[i] = [startDay_i, endDay_i].

    Returns:
        The maximum number of events that can be attended.

    Examples:
        >>> solve([[1,2],[2,3],[3,4]])
        3
        >>> solve([[1,2],[2,3],[3,4],[1,2]])
        4
    """
    # Sort events by start day to process them chronologically
    events.sort(key=lambda x: x[0])
    
    total_events_attended = 0
    current_day = 0
    event_index = 0
    n = len(events)
    
    # Min-heap to store the end days of events that have started but not yet finished
    min_heap_end_days = []
    
    # Continue as long as there are events to process or events in the heap
    while event_index < n or min_heap_end_days:
        # If no events are currently active, jump to the start day of the next available event
        if not min_heap_end_days:
            current_day = events[event_index][0]
            
        # Add all events that start on the current day to the heap
        while event_index < n and events[event_index][0] <= current_day:
            heapq.heappush(min_heap_end_days, events[event_index][1])
            event_index += 1
            
        # Remove events from the heap that have already ended before the current day
        while min_heap_end_days and min_heap_end_days[0] < current_day:
            heapq.heappop(min_heap_end_days)
            
        # If there are valid events, attend the one that ends the earliest
        if min_heap_end_days:
            heapq.heappop(min_heap_end_days)
            total_events_attended += 1
            current_day += 1
            
    return total_events_attended
