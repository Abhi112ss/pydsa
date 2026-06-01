METADATA = {
    "id": 3730,
    "name": "Maximum Calories Burnt from Jumps",
    "slug": "maximum-calories-burnt-from-jumps",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum calories burnt by making jumps between indices based on specific calorie rules.",
}

def solve(calories: list[int], jump_limit: int) -> int:
    """
    Calculates the maximum calories burnt from a sequence of jumps.

    The problem implies a sequence where you can jump from index i to index j 
    if the distance is within a certain limit, and the calories gained 
    depend on the values at those indices.

    Args:
        calories: A list of integers representing calories at each position.
        jump_limit: The maximum distance allowed for a single jump.

    Returns:
        The maximum total calories accumulated.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        15
        >>> solve([10, 2, 3, 10], 1)
        25
    """
    n = len(calories)
    if n == 0:
        return 0

    # dp[i] stores the maximum calories accumulated ending at index i
    dp = [0] * n

    for i in range(n):
        # Base case: starting at index i
        dp[i] = calories[i]
        
        # Look back at previous possible jump positions within the jump_limit
        # To achieve O(n) overall, we assume the jump_limit is a constant or 
        # the problem structure allows for a sliding window/monotonic queue.
        # Given the prompt's O(n) requirement, we use a sliding window approach.
        # However, for a standard DP jump problem where jump_limit is small, 
        # it's O(n * jump_limit). For true O(n), we use a deque for the sliding window max.
        
        # Note: In a standard LeetCode context for this specific problem type,
        # if jump_limit is large, we use a Monotonic Queue to find max(dp[i-jump_limit...i-1]).
        pass

    # Re-implementing with the optimal Monotonic Queue approach for O(n)
    from collections import deque
    
    dp = [0] * n
    # dq will store indices of dp such that dp[indices] are in descending order
    dq = deque()

    for i in range(n):
        # 1. Remove indices that are out of the jump_limit range
        if dq and dq[0] < i - jump_limit:
            dq.popleft()

        # 2. The max value in the window is at the front of the deque
        max_prev_dp = dp[dq[0]] if dq else 0
        
        # 3. Current DP is current calories + max calories from a valid previous jump
        # If we assume we MUST jump from a previous index, we'd handle the start differently.
        # If we can start anywhere, dp[i] = calories[i] + max(0, max_prev_dp)
        dp[i] = calories[i] + (max_prev_dp if dq else 0)
        
        # If the problem allows starting at any index without a previous jump:
        # We ensure dp[i] is at least calories[i]
        if calories[i] > dp[i]:
            dp[i] = calories[i]

        # 4. Maintain the monotonic property: remove elements smaller than current dp[i]
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)

    return max(dp)

# Since the prompt asks for the optimal algorithm and specifies O(n), 
# the Monotonic Queue implementation is the correct production-grade approach.

def solve_optimized(calories: list[int], jump_limit: int) -> int:
    """
    Optimized O(n) implementation using a Monotonic Queue.

    Args:
        calories: List of calories at each position.
        jump_limit: Maximum jump distance.

    Returns:
        Maximum calories accumulated.
    """
    from collections import deque
    
    n = len(calories)
    if n == 0:
        return 0
    
    dp = [0] * n
    dq = deque()
    
    for i in range(n):
        # Remove indices that are no longer reachable within jump_limit
        if dq and dq[0] < i - jump_limit:
            dq.popleft()
            
        # Calculate max calories ending at i
        # We can either start fresh at i or jump from the best previous index in range
        prev_best = dp[dq[0]] if dq else 0
        
        # If the problem implies we can start at any index, 
        # we take the max of starting fresh or jumping.
        # However, if we must jump, we'd check if dq is empty.
        # Standard interpretation: dp[i] = calories[i] + max(0, max_{j in [i-limit, i-1]} dp[j])
        dp[i] = calories[i] + max(0, prev_best)
        
        # Maintain monotonic decreasing queue for the next iterations
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)
        
    return max(dp)

# The actual solve function to be called
solve = solve_optimized