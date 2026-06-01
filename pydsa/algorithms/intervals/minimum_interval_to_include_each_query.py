METADATA = {
    "id": 1851,
    "name": "Minimum Interval to Include Each Query",
    "slug": "minimum-interval-to-include-each-query",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "intervals", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(N log N + Q log Q)",
    "space_complexity": "O(N + Q)",
    "description": "Find the smallest interval that contains each given query point using a min-heap and sorting.",
}

import heapq

def solve(intervals: list[list[int]], queries: list[int]) -> list[int]:
    """
    Finds the minimum interval size that covers each query.

    Args:
        intervals: A list of intervals where intervals[i] = [left_i, right_i].
        queries: A list of query points.

    Returns:
        A list of integers where the i-th element is the size of the smallest 
        interval containing queries[i], or -1 if no such interval exists.

    Examples:
        >>> solve([[1,4],[2,3],[3,6],[2,4],[4,5]], [4,1,5])
        [3, 3, 1]
        >>> solve([[1,2],[3,4],[5,6],[7,8]], [9,1,5])
        [-1, 2, 2]
    """
    # Sort intervals by their start time to process them greedily
    intervals.sort()
    
    # Store queries with their original indices to return results in correct order
    indexed_queries = sorted([(q, i) for i, q in enumerate(queries)])
    
    results = [-1] * len(queries)
    # Min-heap to store (interval_size, interval_end_time)
    # We prioritize smaller interval sizes
    min_heap: list[tuple[int, int]] = []
    
    interval_idx = 0
    num_intervals = len(intervals)
    
    for query_val, original_idx in indexed_queries:
        # 1. Add all intervals that start before or at the current query point
        while interval_idx < num_intervals and intervals[interval_idx][0] <= query_val:
            start, end = intervals[interval_idx]
            size = end - start + 1
            heapq.heappush(min_heap, (size, end))
            interval_idx += 1
            
        # 2. Remove intervals from the heap that end before the current query point
        # These intervals can never satisfy this or any future (larger) query
        while min_heap and min_heap[0][1] < query_val:
            heapq.heappop(min_heap)
            
        # 3. The top of the heap is the smallest interval that covers the query
        if min_heap:
            results[original_idx] = min_heap[0][0]
            
    return results
