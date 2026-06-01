METADATA = {
    "id": 1788,
    "name": "Maximize the Beauty of the Garden",
    "slug": "maximize-the-beauty-of-the-garden",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "monotonic_queue", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum beauty of a garden defined as the difference between the maximum and minimum flower heights in a contiguous subarray of length at least k.",
}

from collections import deque

def solve(flowers: list[int], k: int) -> int:
    """
    Calculates the maximum beauty of a garden using a sliding window approach.
    Beauty is defined as max(flowers[i...j]) - min(flowers[i...j]) where j - i + 1 >= k.

    Args:
        flowers: A list of integers representing flower heights.
        k: The minimum length of the garden subarray.

    Returns:
        The maximum difference between the maximum and minimum height in any valid subarray.

    Examples:
        >>> solve([1, 3, 3, 2, 4, 1], 3)
        3
        >>> solve([1, 1, 1, 1], 2)
        0
    """
    n = len(flowers)
    if n < k:
        return 0

    max_beauty = 0
    # min_deque stores indices of elements in increasing order of values
    min_deque = deque()
    # max_deque stores indices of elements in decreasing order of values
    max_deque = deque()

    # We use a sliding window approach. However, since the window size is 'at least k',
    # we can maintain the min/max of a window that grows.
    # To handle the 'at least k' constraint efficiently, we can observe that
    # for a fixed end index 'right', we want to find a 'left' index such that
    # right - left + 1 >= k and the difference is maximized.
    
    # Actually, a simpler way to view this:
    # For every 'right' index, we want to consider all 'left' such that left <= right - k + 1.
    # But the max/min values change. 
    # A more robust way: The max beauty is either found in a window of exactly size k,
    # or it's found in a larger window. But any window of size > k contains a window of size k.
    # Wait, that's not true for the difference. A larger window can have a larger difference.
    # However, the problem can be solved by iterating through all possible right boundaries.
    # For a fixed right, we want to find left <= right - k + 1 that minimizes flowers[left] 
    # or maximizes flowers[left] relative to the current max/min.
    
    # Correct approach:
    # We need to find max(flowers[i...j]) - min(flowers[i...j]) for j - i + 1 >= k.
    # This is equivalent to finding max(flowers[j] - min_in_range) or max(max_in_range - flowers[j]).
    # Actually, the simplest O(n) is to realize that for a fixed 'right', 
    # the best 'left' is the one that allows the window to be at least size k.
    # We can maintain the min and max of the window [0...right-k+1] using a sliding window
    # but that doesn't account for the fact that the min/max could be at the 'right' index.
    
    # Let's use the property: Max Beauty = max_{j >= k-1} (max(flowers[0...j]) - min(flowers[0...j])) 
    # is NOT correct because the window must be contiguous.
    # The actual logic: For each index i, we want to find the max/min in a window ending at i
    # with length at least k.
    
    # Let's use two monotonic queues to track the min and max of the window [0...i].
    # But we need to ensure the window is at least k.
    # Actually, the maximum difference in a window of size >= k is simply the 
    # maximum difference in the entire array if we don't care about k.
    # With k, we can use a sliding window of size k to get a baseline, 
    # but we can also expand.
    
    # Re-evaluating: The maximum difference in a subarray of length >= k is 
    # simply the maximum difference in the entire array IF the indices of the 
    # global max and global min are at least k-1 apart.
    # If they are closer, we need to check subarrays.
    
    # Standard O(n) approach for "max - min in subarray of length >= k":
    # This is equivalent to: max_{i, j: j-i+1 >= k} (flowers[j] - flowers[i]) 
    # OR max_{i, j: j-i+1 >= k} (flowers[i] - flowers[j]).
    
    # Case 1: flowers[j] is the max, flowers[i] is the min, j > i, j-i+1 >= k
    # We want to maximize flowers[j] - flowers[i] subject to i <= j - k + 1.
    # For a fixed j, we need the minimum flowers[i] in range [0, j - k + 1].
    
    # Case 2: flowers[i] is the max, flowers[j] is the min, j > i, j-i+1 >= k
    # We want to maximize flowers[i] - flowers[j] subject to j >= i + k - 1.
    # For a fixed j, we need the maximum flowers[i] in range [0, j - k + 1].

    min_so_far = [0] * n
    max_so_far = [0] * n
    
    curr_min = flowers[0]
    curr_max = flowers[0]
    
    # Precompute prefix minimums and maximums
    # This allows us to find the best 'i' for a fixed 'j' in O(1)
    # where i is any index from 0 to j - k + 1.
    
    # However, the problem asks for max(flowers[i...j]) - min(flowers[i...j]).
    # This is NOT just flowers[j] - min(flowers[0...j-k+1]).
    # It is max(max_in_window - min_in_window).
    
    # Let's use the sliding window with monotonic queues for a window of size EXACTLY k.
    # Wait, if a window is larger than k, say size k+1, its beauty is 
    # max(window_k_left, window_k_right, new_element, old_element).
    # Actually, any window of size > k will have a beauty >= any window of size k 
    # contained within it. So we just need to find the max beauty of all windows 
    # of size >= k.
    
    # The maximum beauty of a window of size >= k is simply the maximum beauty 
    # of the entire array if we can pick any i, j such that |i-j| >= k-1.
    # No, that's not right. The window must be contiguous.
    # But if we pick i and j such that |i-j| >= k-1, the subarray [min(i,j), max(i,j)]
    # has length at least k.
    
    # So the problem is: Find max |flowers[i] - flowers[j]| such that |i - j| >= k - 1.
    
    # Let's refine:
    # We want to maximize flowers[j] - flowers[i] where j - i >= k - 1
    # OR maximize flowers[i] - flowers[j] where j - i >= k - 1.
    
    # For each j, we want to find min(flowers[i]) for 0 <= i <= j - k + 1.
    # And for each j, we want to find max(flowers[i]) for 0 <= i <= j - k + 1.
    
    prefix_min = [0] * n
    prefix_max = [0] * n
    
    prefix_min[0] = flowers[0]
    prefix_max[0] = flowers[0]
    for i in range(1, n):
        prefix_min[i] = min(prefix_min[i-1], flowers[i])
        prefix_max[i] = max(prefix_max[i-1], flowers[i])
        
    ans = 0
    for j in range(k - 1, n):
        # The window ends at j. The window must have length at least k.
        # So the window can start at any index i from 0 to j - k + 1.
        # The beauty of subarray [i...j] is max(flowers[i...j]) - min(flowers[i...j]).
        # This is still tricky because the max/min could be anywhere in [i...j].
        
        # Let's reconsider: The maximum beauty of a window of size >= k 
        # is the same as the maximum beauty of a window of size EXACTLY k? 
        # NO. Example: [10, 1, 10, 1], k=2. Window [10, 1, 10] has beauty 9.
        # Window [10, 1] has beauty 9.
        # Example: [1, 5, 2, 10], k=2. Window [1, 5, 2, 10] has beauty 9.
        # Window [1, 5] has 4, [5, 2] has 3, [2, 10] has 8.
        # So larger windows ARE better.
        
        # If we want to maximize max(flowers[i...j]) - min(flowers[i...j]) 
        # for j - i + 1 >= k, we can just look at all i, j such that j - i >= k - 1.
        # The beauty of the subarray [i, j] is at least |flowers[i] - flowers[j]|.
        # But it could be larger if the max and min are not at the boundaries.
        # However, if the max and min are at indices p and q, and |p - q| >= k - 1,
        # then the beauty is |flowers[p] - flowers[q]|.
        # If |p - q| < k - 1, we can always expand the window to size k 
        # without decreasing the max or increasing the min (in terms of range).
        # Wait, expanding a window can only increase the max and decrease the min,
        # thus increasing the beauty.
        
        # So the strategy is:
        # 1. Find max |flowers[i] - flowers[j]| where |i - j| >= k - 1.
        # 2. This covers all cases where the max and min are at least k-1 apart.
        # 3. What if the max and min are closer than k-1? 
        #    Then any window of size k containing them will have a beauty 
        #    at least as large as |flowers[i] - flowers[j]|.
        #    So we just need to check all windows of size exactly k.
        
        # Actually, the logic is even simpler:
        # The maximum beauty is achieved by some window [i, j] with j - i + 1 >= k.
        # Let the max be at index p and min be at index q (i <= p, q <= j).
        # If |p - q| >= k - 1, then the beauty is |flowers[p] - flowers[q]|.
        # If |p - q| < k - 1, then the window [i, j] must be at least size k.
        # We can always expand the window [i, j] to a window of size k that 
        # contains both p and q. The beauty of this window of size k will be 
        # at least |flowers[p] - flowers[q]|.
        
        # Therefore, the maximum beauty is:
        # max( max_{|i-j| >= k-1} |flowers[i] - flowers[j]|, 
        #      max_{all windows of size k} (max_in_window - min_in_window) )
        
        # But wait, the second term is actually covered by the first term's logic 
        # if we consider that any window of size k has a max and min.
        # If their distance is >= k-1, it's in the first term.
        # If their distance is < k-1, the first term doesn't cover it, 
        # but the second term does.
        
        # Actually, the first term is:
        # max( (max_{j >= k-1} (flowers[j] - min_{i <= j-k+1} flowers[i])),
        #      (max_{j >= k-1} (max_{i <= j-k+1} flowers[i] - flowers[j])) )
        
        # Let's use the prefix min/max approach for the first term.
        pass

    # Correct O(n) implementation:
    # We want to find max(flowers[j] - flowers[i]) or max(flowers[i] - flowers[j])
    # where j - i >= k - 1.
    
    # Part 1: max(flowers[j] - flowers[i]) for j - i >= k - 1
    # For each j, we need min(flowers[i]) for 0 <= i <= j - k + 1.
    res1 = 0
    min_val = flowers[0]
    for j in range(k - 1, n):
        # The possible i's are 0, 1, ..., j - k + 1
        # As j increases, the range of i expands.
        # We update min_val with the new possible i: j - k + 1
        min_val = min(min_val, flowers[j - k + 1])
        res1 = max(res1, flowers[j] - min_val)
        
    # Part 2: max(flowers[i] - flowers[j]) for j - i >= k - 1
    # This is equivalent to max(flowers[i] - flowers[j]) for i <= j - k + 1
    # For each j, we need max(flowers[i]) for 0 <= i <= j - k + 1.
    res2 = 0
    max_val = flowers[0]
    for j in range(k - 1, n):
        max_val = max(max_val, flowers[j - k + 1])
        res2 = max(res2, max_val - flowers[j])
        
    # Part 3: What if the max and min are within distance < k-1?
    # Then the window must be of size exactly k.
    # We use monotonic queues to find max/min in all windows of size k.
    res3 = 0
    min_q = deque()
    max_q = deque()
    for i in range(n):
        # Maintain monotonic queues for window of size k
        while min_q and flowers[min_q[-1]] >= flowers[i]:
            min_q.pop()
        min_q.append(i)
        while max_q and flowers[max_q[-1]] <= flowers[i]:
            max_q.pop()
        max_q.append(i)
        
        # Remove indices out of window [i-k+1, i]
        if min_q[0] <= i - k:
            min_q.popleft()
        if max_q[0] <= i - k:
            max_q.popleft()
            
        if i >= k - 1:
            res3 = max(res3, flowers[max_q[0]] - flowers[min_q[0]])
            
    return max(res1, res2, res3)

# The logic above is slightly redundant. 
# If the max and min are at distance >= k-1, res1 or res2 will catch it.
# If the max and min are at distance < k-1, then any window of size k 
# containing them will have a beauty >= their difference.
# So max(res1, res2, res3) is correct.
# Actually, res3 (windows of size k) is always >= any window of size k 
# where the max/min are closer than k-1.
# And res1/res2 cover the cases where they are further.
# So max(res1, res2, res3) is the answer.

# Wait, can we simplify?
# Any window of size >= k has a beauty.
# Let that window be [L, R]. Let its max be at p and min be at q.
# If |p-q| >= k-1, then res1 or res2 will find |flowers[p]-flowers[q]|.
# If |p-q| < k-1,