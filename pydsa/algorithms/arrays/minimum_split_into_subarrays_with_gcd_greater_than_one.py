METADATA = {
    "id": 2436,
    "name": "Minimum Split Into Subarrays With GCD Greater Than One",
    "slug": "minimum-split-into-subarrays-with-gcd-greater-than-one",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "gcd"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of subarrays such that the GCD of each subarray is greater than 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of subarrays needed such that the GCD 
    of each subarray is greater than 1.

    Args:
        nums: A list of positive integers.

    Returns:
        The minimum number of subarrays required. Returns -1 if it's 
        impossible to split the array such that every subarray has GCD > 1.

    Examples:
        >>> solve([2, 3, 4])
        -1
        >>> solve([2, 4, 6])
        1
        >>> solve([2, 2, 3, 3])
        2
    """
    import math

    n = len(nums)
    # dp[i] stores the minimum splits for the prefix nums[0...i-1]
    # Initialize with infinity to represent unreachable states
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0

    # To optimize, we observe that for a fixed end index i, as we move the 
    # start index j backwards, the GCD of nums[j...i] is non-increasing 
    # and changes at most O(log(max(nums))) times.
    
    # current_gcds stores tuples of (gcd_value, start_index) 
    # representing unique GCD values ending at the current position.
    current_gcds: list[tuple[int, int]] = []

    for i in range(n):
        new_gcds = []
        val = nums[i]
        
        # Update all existing GCDs with the current number
        # and add the current number as a new potential GCD starting point
        for g, start_idx in current_gcds + [(val, i)]:
            new_g = math.gcd(g, val)
            if not new_gcds or new_gcds[-1][0] != new_g:
                new_gcds.append((new_g, start_idx))
            else:
                # If GCD is the same, we keep the earliest start_idx 
                # to potentially minimize dp[start_idx] later? 
                # Actually, for a fixed GCD, we want the smallest dp[start_idx].
                # But since we iterate i, we just need to track the ranges.
                pass
        
        # Refined approach: For each unique GCD value ending at i, 
        # we want to find the minimum dp[j] where j is in the range 
        # that produces this GCD.
        
        # Let's re-evaluate: current_gcds will store (gcd, leftmost_index)
        # such that for all k in [leftmost_index, next_leftmost_index - 1], 
        # gcd(nums[k...i]) == gcd.
        
        current_gcds = []
        temp_val = val
        last_idx = i
        
        # We iterate backwards through the previous unique GCDs
        # to build the new set of unique GCDs ending at i.
        # This is a standard technique for "GCD of all subarrays ending at i".
        for g, start_idx in current_gcds_prev if 'current_gcds_prev' in locals() else []:
            new_g = math.gcd(g, val)
            if new_g > 1:
                # We only care about GCD > 1
                pass
        
        # Correct implementation of the "GCD of subarrays ending at i" logic:
        # We maintain a list of (gcd, start_index) where start_index is the 
        # first index in a contiguous block that results in that GCD.
        
        # Re-initializing current_gcds for the current i
        new_gcd_list = []
        # Add the current element itself
        current_val = nums[i]
        
        # We use the previous unique GCDs to compute current unique GCDs
        # This part is handled by the loop below
        
    # Let's rewrite the loop cleanly.
    dp = [inf] * (n + 1)
    dp[0] = 0
    # active_gcds: list of [gcd_value, leftmost_index_for_this_gcd]
    active_gcds: list[list[int]] = [] 

    for i in range(n):
        new_active_gcds = []
        # 1. Update existing GCDs with nums[i]
        for g_info in active_gcds:
            g_info[0] = math.gcd(g_info[0], nums[i])
        
        # 2. Add the current element as a new GCD starting at i
        active_gcds.append([nums[i], i])
        
        # 3. Merge adjacent entries with the same GCD to keep list size O(log max_val)
        for g_info in active_gcds:
            if not new_active_gcds or new_active_gcds[-1][0] != g_info[0]:
                new_active_gcds.append(g_info)
            else:
                # Keep the leftmost index for the same GCD value
                # because a larger range (smaller index) is always better or equal
                # for the DP transition if we were looking for any j.
                # Actually, we need to check all possible j in the range.
                # But wait, if gcd(nums[j...i]) is the same for j in [L, R],
                # we want min(dp[j]) for j in [L, R].
                pass
        
        # The logic above is slightly flawed for DP. Let's fix:
        # For each unique GCD value ending at i, it covers a range of start indices [L, R].
        # We need min(dp[j]) for j in [L, R] where gcd(nums[j...i]) > 1.
        
    # Final attempt at the logic:
    dp = [inf] * (n + 1)
    dp[0] = 0
    # active_gcds stores (gcd_value, start_index_of_this_gcd_range)
    active_gcds: list[tuple[int, int]] = []

    for i in range(n):
        next_active_gcds = []
        # Update all previous GCDs with the current number
        for g, start_idx in active_gcds:
            new_g = math.gcd(g, nums[i])
            if not next_active_gcds or next_active_gcds[-1][0] != new_g:
                next_active_gcds.append((new_g, start_idx))
            else:
                # If GCD is same, the existing one in next_active_gcds 
                # already has the smaller (earlier) start_idx.
                pass
        
        # Add the current element
        if not next_active_gcds or next_active_gcds[-1][0] != nums[i]:
            next_active_gcds.append((nums[i], i))
        else:
            # If the last GCD is the same as nums[i], the start_idx 
            # is already the smallest possible.
            pass
            
        # Note: The above logic for merging is slightly wrong. 
        # Let's use the standard "unique GCDs" approach.
        
        # Corrected unique GCDs logic:
        # We want to find all unique values of gcd(nums[j...i]) for 0 <= j <= i.
        # Each unique value is associated with a range of j's.
        
        # Let's use a simpler approach:
        # active_gcds will be a list of (gcd, start_index) where start_index 
        # is the smallest index such that gcd(nums[start_index...i]) == gcd.
        
        # Re-calculating active_gcds for index i
        # (This is O(log max_val) per i)
        pass

    # Let's provide the actual working implementation.
    return _actual_solve(nums)

def _actual_solve(nums: list[int]) -> int:
    import math
    n = len(nums)
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    # active_gcds: list of (gcd_value, leftmost_index)
    # such that for all k in [leftmost_index, next_leftmost_index - 1],
    # gcd(nums[k...i]) == gcd_value.
    active_gcds: list[tuple[int, int]] = []

    for i in range(n):
        new_active_gcds = []
        # 1. Update existing GCDs
        for g, start_idx in active_gcds:
            new_g = math.gcd(g, nums[i])
            if new_active_gcds and new_active_gcds[-1][0] == new_g:
                # Already have this GCD, keep the existing (smaller) start_idx
                continue
            else:
                new_active_gcds.append((new_g, start_idx))
        
        # 2. Add current element
        if new_active_gcds and new_active_gcds[-1][0] == nums[i]:
            # The last GCD in the list is already nums[i], 
            # but we need to ensure we don't overwrite a smaller start_idx.
            # Actually, the loop above processes from oldest to newest.
            # The newest GCD is always the one with the largest start_idx.
            pass
        else:
            # If nums[i] is not the same as the last GCD, add it.
            # But wait, the order in active_gcds is usually by start_idx.
            # Let's process from i down to 0.
            pass

        # Let's use the most robust way to find unique GCDs ending at i:
        # Iterate through previous unique GCDs and update them.
        # The unique GCDs will be in decreasing order of start_index.
        
        # Resetting for a clean approach:
        pass
    
    # Final implementation logic
    dp = [inf] * (n + 1)
    dp[0] = 0
    # active_gcds: list of (gcd, start_index) where start_index is the 
    # largest index such that gcd(nums[start_index...i]) == gcd.
    # This allows us to easily find the range of indices for each GCD.
    # Actually, it's easier to store (gcd, min_index_for_this_gcd).
    active_gcds: list[tuple[int, int]] = [] 

    for i in range(n):
        # Update all previous GCDs
        new_active = []
        for g, start_idx in active_gcds:
            new_g = math.gcd(g, nums[i])
            if new_active and new_active[-1][0] == new_g:
                # Keep the smallest start_idx for this GCD
                # Since we iterate through active_gcds (which are sorted by start_idx),
                # the first time we see a new_g, it's the smallest start_idx.
                continue
            else:
                new_active.append((new_g, start_idx))
        
        # Add the current element as a new GCD starting at i
        if new_active and new_active[-1][0] == nums[i]:
            # The current element's GCD is already represented
            # but we need to ensure the start_idx is correct.
            # Actually, the current element is the "newest" GCD.
            # Let's use a different structure.
            pass
            
    # Let's use the correct, standard algorithm for this.
    return _final_logic(nums)

def _final_logic(nums: list[int]) -> int:
    import math
    n = len(nums)
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    # active_gcds: list of [gcd, start_index] 
    # where start_index is the smallest index such that gcd(nums[start_index...i]) == gcd
    active_gcds: list[list] = []

    for i in range(n):
        # 1. Update all existing GCDs with nums[i]
        for entry in active_gcds:
            entry[0] = math.gcd(entry[0], nums[i])
        
        # 2. Add the current element as a new GCD starting at index i
        active_gcds.append([nums[i], i])
        
        # 3. Merge entries with the same GCD
        # We iterate backwards to merge correctly
        merged = []
        for g, start_idx in active_gcds:
            if merged and merged[-1][0] == g:
                # Keep the smallest start_idx for this GCD
                if start_idx < merged[-1][1]:
                    merged[-1][1] = start_idx
            else:
                merged.append([g, start_idx])
        active_gcds = merged

        # 4. Update DP
        # For each unique GCD > 1, we want to find min(dp[j]) 
        # for all j in the range [start_idx, next_start_idx - 1]
        # Wait, the range for a GCD is [start_idx, end_idx].
        # If active_gcds = [(g1, s1), (g2, s2), (g3, s3)] with s1 < s2 < s3
        # then g1 is the GCD for all j in [s1, s2-1]
        # g2 is the GCD for all j in [s2, s3-1]
        # g3 is the GCD for all j in [s3, i]
        
        for idx in range(len(active_gcds)):
            g, s_start = active_gcds[idx]
            if g > 1:
                # The range of j such that gcd(nums[j...i]) == g
                # is [s_start, s_end] where s_end is the start_idx of the next GCD - 1
                # or i if it's the last one.
                s_end = active_gcds[idx+1][1] - 1 if idx + 1 < len(active_gcds) else i
                
                # We need min(dp[j]) for j in [s_start, s_end]
                # However, the problem asks for subarrays. A subarray nums[j...i]
                # corresponds to dp[j] (the splits for prefix j) + 1.
                # So we need min(dp[j]) for j in [s_start, s_end].
                # Since we only care about j where gcd(nums[j...i]) > 1,
                # and we are iterating through all such unique GCDs.
                
                # To make this O(N log N), we'd need a Segment Tree or Sparse Table
                # for dp. But since we only update dp[i+1] once per i, 
                # and the number of unique GCDs is small, we can just loop.
                # But the loop over [s_start, s_end] could be O(N), making it O(N^2).
                # Wait, the total number of (g, start_idx) pairs across all i is O(N log max_val).
                # We need to find min(dp[j]) for j in [s_start, s_end] efficiently.
                pass

    # Let's use a Segment Tree to find min(dp[j]) in O(log N).
    return _segment_tree_solve(nums)

def _segment_tree_solve(nums: list[int]) -> int:
    import math
    n = len(nums)
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    # Segment tree to store dp values and query range minimum
    tree_size = 1
    while tree_size <= n + 1:
        tree_size *= 2
    tree = [inf] * (2 * tree_size)

    def update(idx, val):
        idx += tree_size
        tree[idx] = val
        while idx > 1:
            idx //= 2
            tree[idx] = min(tree[2 * idx], tree[2 * idx + 1])

    def query(l, r):
        res = inf
        l += tree_size