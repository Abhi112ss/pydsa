METADATA = {
    "id": 2770,
    "name": "Maximum Number of Jumps to Reach the Last Index",
    "slug": "maximum-number-of-jumps-to-reach-the-last-index",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of jumps required to reach the last index of an array where each element represents the maximum jump length from that position.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum number of jumps to reach the last index of the array.

    Args:
        nums: A list of integers where nums[i] is the maximum jump length from index i.

    Returns:
        The maximum number of jumps to reach the last index. Returns -1 if the 
        last index is unreachable.

    Examples:
        >>> solve([1, 1, 1, 1])
        3
        >>> solve([2, 3, 1, 1, 4])
        3
        >>> solve([1, 0, 1])
        -1
    """
    n = len(nums)
    if n <= 1:
        return 0

    # dp[i] stores the maximum jumps to reach index i.
    # Initialize with -1 to represent unreachable indices.
    dp = [-1] * n
    dp[0] = 0

    for i in range(n):
        # If the current index is unreachable, we cannot jump from it.
        if dp[i] == -1:
            continue

        # Calculate the maximum jump distance from the current index.
        max_jump_distance = nums[i]
        
        # Try all possible jump lengths from 1 to max_jump_distance.
        # We iterate through all reachable indices from i.
        for jump_length in range(1, max_jump_distance + 1):
            next_index = i + jump_length
            
            # Ensure we don't jump out of bounds.
            if next_index < n:
                # Update the next index with the maximum jumps found so far.
                # We want to maximize the number of jumps.
                dp[next_index] = max(dp[next_index], dp[i] + 1)
            else:
                # Since jump_length is increasing, if i + jump_length >= n,
                # further jump_lengths will also be out of bounds.
                break

    return dp[n - 1]
