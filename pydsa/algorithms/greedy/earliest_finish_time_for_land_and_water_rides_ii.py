METADATA = {
    "id": 3635,
    "name": "Earliest Finish Time for Land and Water Rides II",
    "slug": "earliest-finish-time-for-land-and-water-rides-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the earliest time all rides can be completed given their start times, durations, and resource constraints.",
}

import heapq

def solve(rides: list[list[int]]) -> int:
    """
    Calculates the earliest finish time for all rides using a greedy approach 
    with a priority queue.

    Args:
        rides: A list of lists where each sublist contains [start_time, duration, type].
               type 0 represents Land, type 1 represents Water.

    Returns:
        The earliest time by which all rides are completed.

    Examples:
        >>> solve([[1, 5, 0], [2, 3, 1], [4, 2, 0]])
        8
    """
    # Sort rides by their available start time to process them chronologically
    rides.sort(key=lambda x: x[0])
    
    # Min-heaps to track the next available time for each ride type
    # land_heap stores the time when a land ride becomes free
    # water_heap stores the time when a water ride becomes free
    land_heap: list[int] = []
    water_heap: list[int] = []
    
    max_finish_time: int = 0
    
    for start_time, duration, ride_type in rides:
        if ride_type == 0:  # Land Ride
            if not land_heap:
                # If no land ride is currently running, it starts at its start_time
                finish_time = start_time + duration
                heapq.heappush(land_heap, finish_time)
            else:
                # If a land ride is running, the new ride starts at max(its start_time, previous finish_time)
                earliest_available = heapq.heappop(land_heap)
                actual_start = max(start_time, earliest_available)
                finish_time = actual_start + duration
                heapq.heappush(land_heap, finish_time)
            max_finish_time = max(max_finish_time, finish_time)
            
        else:  # Water Ride
            if not water_heap:
                # If no water ride is currently running, it starts at its start_time
                finish_time = start_time + duration
                heapq.heappush(water_heap, finish_time)
            else:
                # If a water ride is running, the new ride starts at max(its start_time, previous finish_time)
                earliest_available = heapq.heappop(water_heap)
                actual_start = max(start_time, earliest_available)
                finish_time = actual_start + duration
                heapq.heappush(water_heap, finish_time)
            max_finish_time = max(max_finish_time, finish_time)

    return max_finish_time
