METADATA = {
    "id": 3317,
    "name": "Find the Number of Possible Ways for an Event",
    "slug": "find_the_number_of_possible_ways_for_an_event",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of ways to choose elements from groups such that the total sum equals a target, using dynamic programming.",
}

def solve(groups: list[list[int]], target: int) -> int:
    """
    Calculates the number of ways to select exactly one element from each group 
    such that the sum of the selected elements equals the target.

    Args:
        groups: A list of lists, where each inner list contains integers 
                representing possible values from that group.
        target: The required sum of the selected elements.

    Returns:
        The total number of ways to achieve the target sum.

    Examples:
        >>> solve([[1, 2], [1, 2]], 3)
        2
        >>> solve([[1], [2], [3]], 6)
        1
    """
    MOD = 10**9 + 7
    
    # dp[s] stores the number of ways to get sum 's' using elements 
    # from the groups processed so far.
    dp = [0] * (target + 1)
    dp[0] = 1

    for group in groups:
        # next_dp will store the ways including the current group
        next_dp = [0] * (target + 1)
        
        # Optimization: Pre-calculate frequencies of values in the current group
        # to avoid redundant additions in the inner loop.
        counts = {}
        for val in group:
            counts[val] = counts.get(val, 0) + 1
            
        # Iterate through all possible sums achieved by previous groups
        for current_sum in range(target + 1):
            if dp[current_sum] == 0:
                continue
            
            # For every unique value in the current group, update the new sums
            for val, count in counts.items():
                new_sum = current_sum + val
                if new_sum <= target:
                    # Add (ways to reach current_sum) * (occurrences of val)
                    # to the ways to reach new_sum
                    next_dp[new_sum] = (next_dp[new_sum] + dp[current_sum] * count) % MOD
        
        # Move to the next group state
        dp = next_dp

    return dp[target]
