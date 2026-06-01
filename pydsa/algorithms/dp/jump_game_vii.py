METADATA = {
    "id": 1871,
    "name": "Jump Game VII",
    "slug": "jump-game-vii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if you can reach the last index of an array given specific jump constraints and a maximum jump distance.",
}

def solve(nums: list[int], max_jump: int) -> bool:
    """
    Determines if the last index is reachable from the first index.

    Args:
        nums: A list of integers where nums[i] is the maximum jump distance from index i.
        max_jump: The maximum allowed jump distance from any index.

    Returns:
        True if the last index is reachable, False otherwise.

    Examples:
        >>> solve([0, 1, 0], 2)
        False
        >>> solve([1, 1, 1, 1], 1)
        True
    """
    n = len(nums)
    if n == 0:
        return False
    
    # dp[i] is True if index i is reachable from index 0
    dp = [False] * n
    dp[0] = True
    
    # reachable_count tracks how many indices in the current sliding window [i - max_jump, i - 1]
    # are marked as True in the dp array.
    reachable_count = 0
    
    for i in range(1, n):
        # Add the previous index to the sliding window count if it was reachable
        if dp[i - 1]:
            reachable_count += 1
            
        # Remove the index that just fell out of the sliding window range [i - max_jump, i - 1]
        if i > max_jump:
            if dp[i - max_jump - 1]:
                reachable_count -= 1
        
        # An index i is reachable if:
        # 1. There is at least one reachable index in the window [i - max_jump, i - 1]
        # 2. The jump distance from that index (nums[j]) allows reaching i (nums[j] + j >= i)
        # However, the problem states nums[i] is the max jump distance, but the constraint 
        # is actually: can we reach i from some j where j < i, j + nums[j] >= i, AND i - j <= max_jump?
        # Wait, the problem definition is: jump from i to j if i < j <= i + nums[i] AND j - i <= max_jump.
        # This is equivalent to: j is reachable if there exists i such that:
        # i < j, i + nums[i] >= j, and j - i <= max_jump.
        # Actually, the standard interpretation for this specific LeetCode problem is:
        # You can jump from i to j if i < j <= i + nums[i] AND j - i <= max_jump.
        # This is slightly different. Let's re-read: "jump from i to j if i < j <= i + nums[i] AND j - i <= max_jump".
        # This means the jump distance is min(nums[i], max_jump).
        
        # Correction: The sliding window approach works if we track the "reachability" 
        # based on the condition: index i is reachable if there exists j in [i - max_jump, i - 1]
        # such that dp[j] is True AND j + nums[j] >= i.
        # This is a bit more complex for a simple sliding window. 
        # Let's use the property: index i is reachable if there is a j in [i - max_jump, i - 1]
        # such that dp[j] is True AND j + nums[j] >= i.
        
        # Actually, the problem is simpler: we want to know if we can reach index i.
        # We can use a Fenwick tree or Segment tree for O(n log n), 
        # but O(n) is possible using a deque or a sliding window with a priority queue/max-heap.
        # Let's use a sliding window with a deque to maintain the maximum 'j + nums[j]' 
        # for all reachable 'j' within the window [i - max_jump, i - 1].
        pass

    # Re-implementing with the correct O(n) logic using a deque for the sliding window.
    # We need to find if there exists j in [i - max_jump, i - 1] such that dp[j] is True 
    # and j + nums[j] >= i.
    
    # Let's use a different approach: A sliding window of reachable indices.
    # We maintain a deque of indices 'j' such that dp[j] is True and j is within the current window.
    # We want to check if any j in the deque satisfies j + nums[j] >= i.
    # To do this efficiently, we can use a Max-Heap or a Segment Tree, but for O(n),
    # we can use a deque to keep track of indices j where dp[j] is True, 
    # and we only care about the one that provides the maximum reach (j + nums[j]).
    
    # Wait, the condition is: i is reachable if there is a j in [i - max_jump, i - 1] 
    # such that dp[j] is True AND j + nums[j] >= i.
    
    # Correct O(n) approach:
    # Use a deque to store indices 'j' such that dp[j] is True.
    # The deque will be sorted by the value (j + nums[j]) in descending order.
    # However, we also need to ensure j is within [i - max_jump, i - 1].
    
    from collections import deque
    
    dp = [False] * n
    dp[0] = True
    # dq will store indices j such that dp[j] is True, 
    # ordered such that j + nums[j] is decreasing.
    dq = deque([0])
    
    for i in range(1, n):
        # 1. Remove indices from the front that are out of the max_jump range
        while dq and dq[0] < i - max_jump:
            dq.popleft()
            
        # 2. Check if the best index in the deque can reach i
        # The "best" index is the one with the largest j + nums[j].
        # Since we want to maintain the deque such that the front is the max,
        # we need to be careful. A simple deque doesn't work for "max j + nums[j]" 
        # if we also have the "i - max_jump" constraint.
        # Actually, a Max-Heap (Priority Queue) is O(n log n).
        # To get O(n), we can use a sliding window maximum approach (Monotonic Deque)
        # on the values (j + nums[j]).
        
        # Let's use a Monotonic Deque to maintain indices j in the window [i - max_jump, i - 1]
        # such that dp[j] is True, and the deque is sorted by (j + nums[j]) descending.
        
        # Wait, the standard Monotonic Deque works for finding the max in a fixed-size window.
        # Here, the "value" we are looking at is (j + nums[j]), and the "window" is [i - max_jump, i - 1].
        # This is exactly what a Monotonic Deque does.
        
        # Let's refine:
        # For each i:
        #   - If dp[i-1] is True, add i-1 to the monotonic deque.
        #   - When adding i-1, remove elements from the back of the deque whose (j + nums[j]) <= (i-1 + nums[i-1]).
        #   - Remove elements from the front of the deque that are < i - max_jump.
        #   - If deque is not empty and dq[0] + nums[dq[0]] >= i, then dp[i] = True.
        
        # This is O(n) because each index is pushed and popped at most once.
        pass

    # Final implementation logic:
    dp = [False] * n
    dp[0] = True
    dq = deque()
    
    # We'll use the deque to store indices j where dp[j] is True.
    # The deque will be monotonic: dq[k].val < dq[k+1].val where val = j + nums[j].
    # Wait, for sliding window maximum, we want the largest value at the front.
    # So dq[k].val > dq[k+1].val.
    
    for i in range(n):
        # 1. If i > 0, check if i is reachable from the best j in the window
        if i > 0:
            # Remove indices that are too far away
            while dq and dq[0] < i - max_jump:
                dq.popleft()
            
            # If the best index in the window can reach i
            if dq and dq[0] + nums[dq[0]] >= i:
                dp[i] = True
        
        # 2. If i is reachable, prepare to add it to the deque for future indices
        if dp[i]:
            # Maintain monotonic property: dq[k] + nums[dq[k]] > dq[k+1] + nums[dq[k+1]]
            # We want the largest reach at the front.
            while dq and dq[-1] + nums[dq[-1]] <= i + nums[i]:
                dq.pop()
            dq.append(i)
            
    return dp[n-1]

# The above logic is slightly flawed in the loop order. Let's rewrite cleanly.

def solve_final(nums: list[int], max_jump: int) -> bool:
    """
    Determines if the last index is reachable from the first index using O(n) time.
    """
    n = len(nums)
    if n == 0: return False
    if n == 1: return True
    
    dp = [False] * n
    dp[0] = True
    
    # dq stores indices j such that dp[j] is True.
    # It is maintained such that dq[k] + nums[dq[k]] is strictly decreasing.
    from collections import deque
    dq = deque([0])
    
    for i in range(1, n):
        # Remove indices that can no longer reach i due to max_jump constraint
        while dq and dq[0] < i - max_jump:
            dq.popleft()
            
        # Check if the index with the maximum reach in the current window can reach i
        if dq and dq[0] + nums[dq[0]] >= i:
            dp[i] = True
            
            # If i is reachable, add it to the monotonic deque
            # Maintain the property: dq[k] + nums[dq[k]] is decreasing
            while dq and dq[-1] + nums[dq[-1]] <= i + nums[i]:
                dq.pop()
            dq.append(i)
            
    return dp[n-1]

# Re-assigning to the required solve function name
solve = solve_final
