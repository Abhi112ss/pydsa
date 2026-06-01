METADATA = {
    "id": 2251,
    "name": "Number of Flowers in Full Bloom",
    "slug": "number-of-flowers-in-full-bloom",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sorting", "intervals"],
    "difficulty": "hard",
    "time_complexity": "O((n + m) log n)",
    "space_complexity": "O(n)",
    "description": "Given flower blooming intervals and time points, return the number of flowers in bloom at each time point.",
}

import bisect

def solve(flowers: list[list[int]], time_points: list[int]) -> list[int]:
    """
    Calculates the number of flowers in bloom at each given time point.

    A flower is in bloom if the time point falls within [start, end] inclusive.
    The algorithm uses two sorted arrays representing start and end times to 
    efficiently count active intervals using binary search.

    Args:
        flowers: A list of intervals where flowers[i] = [start_i, end_i].
        time_points: A list of time points to query.

    Returns:
        A list of integers representing the count of flowers in bloom at each time point.

    Examples:
        >>> solve([[1, 3], [2, 3]], [2, 3])
        [2, 2]
        >>> solve([[1, 2], [3, 4]], [1, 2, 3, 4, 5])
        [1, 1, 1, 1, 0]
    """
    # Extract and sort start and end times independently
    # This allows us to use binary search to count how many flowers have started
    # and how many flowers have already finished blooming.
    start_times = sorted([f[0] for f in flowers])
    end_times = sorted([f[1] for f in flowers])
    
    results = []
    
    for time in time_points:
        # Find the number of flowers that have started blooming by 'time'
        # bisect_right returns the index where 'time' could be inserted while maintaining order,
        # effectively counting all starts <= time.
        started_count = bisect.bisect_right(start_times, time)
        
        # Find the number of flowers that have finished blooming before 'time'
        # bisect_left returns the index of the first element >= time.
        # Elements at indices < this index have end_time < time.
        finished_count = bisect.bisect_left(end_times, time)
        
        # The number of flowers in bloom is (total started) - (total finished)
        results.append(started_count - finished_count)
        
    return results
