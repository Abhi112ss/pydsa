METADATA = {
    "id": 813,
    "name": "Largest Sum of Averages",
    "slug": "largest-sum-of-averages",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(k * n^2)",
    "space_complexity": "O(n)",
    "description": "Partition an array into at most k non-empty adjacent groups to maximize the sum of their averages.",
}

def solve(avgs: list[int], k: int) -> float:
    """
    Calculates the maximum sum of averages by partitioning the array into at most k groups.

    Args:
        avgs: A list of integers representing the input array.
        k: The maximum number of partitions allowed.

    Returns:
        The maximum sum of averages as a float.

    Examples:
        >>> solve([1, 3, -1, -3, 4, 5, 6], 4)
        6.333333333333333
        >>> solve([1, 0, 2, 3, 0, -1], 2)
        3.0
    """
    n = len(avgs)
    
    # Precompute prefix sums to calculate range sums in O(1)
    prefix_sums = [0.0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + avgs[i]

    def get_avg(start: int, end: int) -> float:
        """Returns the average of the subarray from index start to end (inclusive)."""
        return (prefix_sums[end + 1] - prefix_sums[start]) / (end - start + 1)

    # dp[i] stores the maximum sum of averages for the first i elements
    # using 'current_k' partitions.
    # We use a 1D array to optimize space from O(k*n) to O(n).
    dp = [get_avg(0, i) for i in range(n)]

    # We iterate from 2 partitions up to k
    for group_count in range(2, k + 1):
        # new_dp will store results for the current number of groups
        new_dp = [0.0] * n
        # A partition of 'group_count' groups requires at least 'group_count' elements
        for i in range(group_count - 1, n):
            # Try all possible split points 'j' for the last group
            # The last group will be from index j+1 to i
            # The previous groups (group_count - 1) will cover index 0 to j
            for j in range(group_count - 2, i):
                current_sum = dp[j] + get_avg(j + 1, i)
                if current_sum > new_dp[i]:
                    new_dp[i] = current_sum
            
            # If we can't find a better split, the current dp[i] (from group_count-1)
            # is technically a candidate, but since we want to maximize and 
            # adding groups usually increases the sum of averages (or keeps it same),
            # we focus on the split logic.
            if dp[i] > new_dp[i]:
                new_dp[i] = dp[i]
        
        dp = new_dp

    return dp[n - 1]
