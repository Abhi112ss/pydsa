METADATA = {
    "id": 1235,
    "name": "Maximum Profit in Job Scheduling",
    "slug": "maximum-profit-in-job-scheduling",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "binary_search", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum profit you can achieve by scheduling non-overlapping jobs.",
}

from bisect import bisect_right

def solve(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    """
    Calculates the maximum profit from a set of jobs with start times, end times, and profits.

    Args:
        startTime: A list of integers representing the start time of each job.
        endTime: A list of integers representing the end time of each job.
        profit: A list of integers representing the profit of each job.

    Returns:
        The maximum profit possible by selecting non-overlapping jobs.

    Examples:
        >>> solve([1,2,3,3], [3,4,5,6], [50,10,40,70])
        120
        >>> solve([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
        120
    """
    # Combine job attributes into a list of tuples and sort by end time.
    # Sorting by end time allows us to build the DP solution incrementally.
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    
    n = len(jobs)
    # dp[i] stores the maximum profit achievable using a subset of the first i jobs.
    # We use a list of (end_time, max_profit) to facilitate binary search.
    # Initial state: at time 0, profit is 0.
    dp = [(0, 0)]
    
    for start, end, current_profit in jobs:
        # Find the latest job that ends before or at the current job's start time.
        # bisect_right finds the insertion point to maintain order; 
        # we search for the 'start' time in the list of end times.
        idx = bisect_right(dp, (start, float('inf'))) - 1
        
        # The profit if we include the current job is:
        # profit of current job + max profit from the last compatible job.
        potential_profit = current_profit + dp[idx][1]
        
        # If this new potential profit is better than the current maximum profit,
        # we add this job's end time and the new profit to our DP table.
        if potential_profit > dp[-1][1]:
            dp.append((end, potential_profit))
            
    return dp[-1][1]
