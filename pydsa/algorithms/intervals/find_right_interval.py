METADATA = {
    "id": 436,
    "name": "Find Right Interval",
    "slug": "find-right-interval",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "For each interval, find the interval whose start time is greater than or equal to the current interval's end time.",
}

def solve(intervals: list[list[int]]) -> list[int]:
    """
    Finds the right interval for each given interval using binary search.

    For each interval i, a 'right interval' is an interval j such that 
    start_j >= end_i and start_j is minimized.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].

    Returns:
        A list of indices representing the right interval for each input interval.
        If no such interval exists, returns -1 for that index.

    Examples:
        >>> solve([[3,4],[2,3],[1,2]])
        [-1, -1, -1]
        >>> solve([[1,4],[2,3],[3,4]])
        [2, 2, -1]
    """
    n = len(intervals)
    # Create a list of (start_time, original_index) to preserve index after sorting
    starts = []
    for index, interval in enumerate(intervals):
        starts.append((interval[0], index))
    
    # Sort the starts list by start_time to enable binary search
    starts.sort()
    
    # Extract just the sorted start times for the bisect-like search
    sorted_start_times = [item[0] for item in starts]
    
    result = []
    for interval in intervals:
        end_time = interval[1]
        
        # Perform binary search to find the smallest start_time >= end_time
        # This is equivalent to finding the insertion point for end_time
        low = 0
        high = n - 1
        found_index = -1
        
        while low <= high:
            mid = (low + high) // 2
            if sorted_start_times[mid] >= end_time:
                # This is a potential candidate, but look for a smaller one on the left
                found_index = starts[mid][1]
                high = mid - 1
            else:
                low = mid + 1
        
        result.append(found_index)
        
    return result
