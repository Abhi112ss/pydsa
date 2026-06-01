METADATA = {
    "id": 3414,
    "name": "Maximum Score of Non-overlapping Intervals",
    "slug": "maximum_score_of_non_overlapping_intervals",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "intervals", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total score obtainable by selecting a set of non-overlapping intervals.",
}

from bisect import bisect_right

def solve(intervals: list[list[int]]) -> int:
    """
    Calculates the maximum score obtainable from a set of non-overlapping intervals.

    Each interval is represented as [start, end, score]. We want to select a 
    subset of intervals such that no two intervals overlap, maximizing the 
    sum of their scores.

    Args:
        intervals: A list of lists, where each inner list is [start, end, score].

    Returns:
        The maximum possible total score.

    Examples:
        >>> solve([[1, 2, 50], [3, 5, 20], [6, 19, 100], [2, 8, 100]])
        150
        >>> solve([[1, 2, 10], [2, 3, 10]])
        10
    """
    if not intervals:
        return 0

    # Sort intervals by their end times to facilitate DP and binary search
    # Sorting by end time allows us to look 'backwards' for the best previous state
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    n = len(sorted_intervals)
    # dp[i] stores the maximum score using a subset of the first i intervals
    dp = [0] * (n + 1)
    
    # Extract end times to perform binary search efficiently
    end_times = [interval[1] for interval in sorted_intervals]

    for i in range(1, n + 1):
        current_start, current_end, current_score = sorted_intervals[i - 1]
        
        # Option 1: Do not include the current interval
        exclude_current = dp[i - 1]
        
        # Option 2: Include the current interval
        # We need to find the latest interval that ends before the current interval starts.
        # Since intervals are [start, end], an interval ending at 't' overlaps 
        # with one starting at 't'. We need end < current_start.
        # bisect_right on end_times with (current_start - 1) finds the index 
        # of the last interval whose end time is <= current_start - 1.
        
        # We use bisect_right to find the position where current_start - 1 could be inserted
        # while maintaining order. The index returned is the first index > current_start - 1.
        # Therefore, index - 1 is the last index where end_time <= current_start - 1.
        idx = bisect_right(end_times, current_start - 1)
        
        # If idx is 0, no previous interval is compatible
        include_current = current_score + dp[idx]
        
        # The DP state is the maximum of including or excluding the current interval
        dp[i] = max(exclude_current, include_current)

    return dp[n]
