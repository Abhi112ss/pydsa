METADATA = {
    "id": 2406,
    "name": "Divide Intervals Into Minimum Number of Groups",
    "slug": "divide-intervals-into-minimum-number-of-groups",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "intervals", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of groups required to partition intervals such that no two intervals in a group overlap.",
}

import heapq

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the minimum number of groups needed to partition intervals.
    
    The problem is equivalent to finding the maximum number of intervals 
    that overlap at any single point in time. We use a min-heap to track 
    the end times of the last interval in each group.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].

    Returns:
        The minimum number of groups required.

    Examples:
        >>> solve([[1, 3], [2, 4], [3, 6]])
        2
        >>> solve([[1, 5], [2, 3], [3, 4], [4, 6]])
        3
    """
    if not intervals:
        return 0

    # Sort intervals by start time to process them chronologically
    intervals.sort(key=lambda x: x[0])

    # Min-heap to store the end times of the current groups.
    # The size of the heap represents the number of active groups.
    group_end_times = []

    for start, end in intervals:
        # If the earliest ending group finishes before the current interval starts,
        # we can reuse that group. Note: intervals [1, 3] and [3, 6] do NOT overlap.
        if group_end_times and group_end_times[0] < start:
            heapq.heappop(group_end_times)
        
        # Add the current interval's end time to the heap.
        # If we popped, we are updating an existing group.
        # If we didn't pop, we are effectively creating a new group.
        heapq.heappush(group_end_times, end)

    # The total number of groups needed is the maximum number of concurrent groups.
    return len(group_end_times)
