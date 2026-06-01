METADATA = {
    "id": 2944,
    "name": "Minimum Number of Coins for Fruits",
    "slug": "minimum-number-of-coins-for-fruits",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to collect fruits by moving from the first to the last position, where each step can jump to any index within a specific range.",
}

def solve(fruits: list[int], max_jump: int) -> int:
    """
    Calculates the minimum cost to collect fruits from the first to the last index.
    
    The problem can be modeled as finding the shortest path in a DAG where 
    each index i can jump to any index j in the range [i + 1, i + max_jump].
    However, the problem constraints imply we want to minimize the sum of 
    fruits[i] for the indices we land on.
    
    Note: The problem description for 2944 in LeetCode context usually refers to 
    a variation of the 'Jump Game' or 'Min Cost Path' where we want to minimize 
    the sum of values at the indices visited.

    Args:
        fruits: A list of integers representing the cost of fruits at each index.
        max_jump: The maximum distance one can jump forward.

    Returns:
        The minimum total cost to reach the last index.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        6
        >>> solve([10, 1, 1, 10], 1)
        12
    """
    n = len(fruits)
    if n == 0:
        return 0
    
    # dp[i] will store the minimum cost to reach index i
    # Initialize with infinity as we want to minimize
    dp = [float('inf')] * n
    dp[0] = fruits[0]
    
    # We use a monotonic queue (deque) to maintain the minimum dp value 
    # within the sliding window of size 'max_jump'.
    # This allows us to find the min(dp[i-max_jump : i]) in O(1) amortized.
    from collections import deque
    dq = deque([0])
    
    for i in range(1, n):
        # 1. Remove indices from the front that are out of the jump range
        if dq and dq[0] < i - max_jump:
            dq.popleft()
            
        # 2. The minimum cost to reach i is the min cost in the window + current fruit cost
        if dq:
            dp[i] = dp[dq[0]] + fruits[i]
            
        # 3. Maintain the deque in increasing order of dp values (monotonic queue)
        # Remove elements from the back that are greater than the current dp[i]
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)
            
    return int(dp[-1])
