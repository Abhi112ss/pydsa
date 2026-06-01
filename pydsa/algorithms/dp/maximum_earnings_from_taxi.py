METADATA = {
    "id": 2008,
    "name": "Maximum Earnings From Taxi",
    "slug": "maximum-earnings-from-taxi",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "sorting", "binary search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum profit possible by selecting non-overlapping taxi rides.",
}

from bisect import bisect_right

def solve(n: int, rides: list[list[int]]) -> int:
    """
    Calculates the maximum earnings from non-overlapping taxi rides.

    Args:
        n: The total number of hours available.
        rides: A list of rides where rides[i] = [start_i, end_i, tip_i].

    Returns:
        The maximum total earnings (fare + tip) possible.

    Examples:
        >>> solve(5, [[1, 2, 1], [2, 3, 2], [3, 4, 3], [1, 5, 10]])
        10
        >>> solve(10, [[1, 4, 1], [4, 5, 2], [5, 10, 3], [1, 10, 10]])
        10
    """
    # Sort rides by their end time to facilitate DP processing
    rides.sort(key=lambda x: x[1])
    
    # end_times stores the end time of each ride to allow binary search
    end_times = [ride[1] for ride in rides]
    
    # dp[i] stores the maximum profit considering rides up to index i-1
    # We use a 1-based DP array where dp[i] is the max profit using a subset of first i rides
    num_rides = len(rides)
    dp = [0] * (num_rides + 1)

    for i in range(1, num_rides + 1):
        start, end, tip = rides[i - 1]
        # The profit for the current ride is (end - start + tip)
        current_ride_profit = (end - start) + tip
        
        # Find the latest ride that ends before or at the current ride's start time
        # bisect_right returns the leftmost insertion point that maintains order
        # We search for 'start' in the end_times list
        idx = bisect_right(end_times, start)
        
        # If idx is the insertion point, it means all rides from end_times[0...idx-1] 
        # end at or before 'start'. However, bisect_right might return an index 
        # where end_times[idx-1] == start. Since rides are [start, end], 
        # a ride ending at 'start' is compatible with a ride starting at 'start'.
        # But wait, the problem says "non-overlapping". 
        # Usually, in these problems, [1, 2] and [2, 3] are non-overlapping.
        # Let's check: if end_time == start_time, they don't overlap.
        # bisect_right(end_times, start) gives the count of elements <= start.
        # Because end_times is 0-indexed, the index 'idx' corresponds to dp[idx].
        
        # We need to find the largest j < i such that rides[j-1].end <= rides[i-1].start
        # bisect_right on end_times with value 'start' gives the number of rides 
        # whose end time is <= start.
        idx = bisect_right(end_times, start)
        
        # If the ride at idx-1 ends exactly at 'start', it's valid.
        # However, bisect_right might find a ride that ends at 'start', 
        # but we must ensure we don't pick the current ride itself if it's in the list.
        # Since we are iterating i from 1 to num_rides, and idx is based on end_times,
        # we must ensure idx < i.
        idx = min(idx, i - 1)
        
        # Option 1: Don't take the current ride -> dp[i-1]
        # Option 2: Take the current ride -> current_ride_profit + dp[idx]
        dp[i] = max(dp[i - 1], current_ride_profit + dp[idx])

    return dp[num_rides]
