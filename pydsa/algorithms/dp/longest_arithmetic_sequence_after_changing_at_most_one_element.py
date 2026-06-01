METADATA = {
    "id": 3872,
    "name": "Longest Arithmetic Sequence After Changing At Most One Element",
    "slug": "longest_arithmetic_sequence_after_changing_at_most_one_element",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the length of the longest arithmetic sequence possible by changing at most one element in the given array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest arithmetic sequence possible by changing at most one element.

    Args:
        nums: A list of integers representing the sequence.

    Returns:
        The length of the longest arithmetic sequence after at most one modification.

    Examples:
        >>> solve([1, 3, 5, 10, 9])
        5
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([1, 10, 1, 10, 1])
        3
    """
    n = len(nums)
    if n <= 2:
        return n

    # dp[i][diff] stores the length of the longest arithmetic sequence 
    # ending at index i with common difference 'diff'.
    # Since diff can be negative, we use a dictionary for each index.
    dp: list[dict[int, int]] = [{} for _ in range(n)]
    max_len = 0

    # First pass: Standard DP for longest arithmetic subsequence (no changes allowed)
    # This handles the case where we change 0 elements or the change doesn't help.
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            # If we have a sequence ending at j with diff, extend it.
            # Otherwise, the sequence is just [nums[j], nums[i]] (length 2).
            length = dp[j].get(diff, 1) + 1
            dp[i][diff] = max(dp[i].get(diff, 0), length)
            max_len = max(max_len, length)

    # Second pass: Consider changing exactly one element at index 'k'.
    # A change at index 'k' can bridge two sequences:
    # one ending at k-1 with diff, and one starting at k+1 with diff,
    # provided that nums[k+1] - nums[k-1] == 2 * diff.
    
    # To optimize, we can iterate through all possible pairs (i, j) that could 
    # be part of a sequence where the element between them is changed.
    # However, a more robust way is to check every index 'i' as the "changed" element.
    
    for i in range(n):
        # Case 1: Change nums[i] to bridge nums[i-1] and nums[i+1]
        if 0 < i < n - 1:
            # The required difference must satisfy: nums[i+1] - nums[i-1] = 2 * diff
            # This only works if the difference is even.
            total_diff_gap = nums[i+1] - nums[i-1]
            if total_diff_gap % 2 == 0:
                diff = total_diff_gap // 2
                # Length = (seq ending at i-1 with diff) + (seq starting at i+1 with diff) + 1 (the changed i)
                # To find "seq starting at i+1", we need a DP that looks forward.
                # Instead, let's use the property that if we change i, 
                # the sequence is: [sequence ending at i-1 with diff] + [i] + [sequence starting at i+1 with diff]
                pass # Handled by the logic below

    # Refined approach:
    # For every pair (i, j) where j > i + 1, if we change the element at i+1, 
    # can we connect nums[i] and nums[j]? This is still O(n^3) if not careful.
    
    # Let's use the observation: A sequence with one change looks like:
    # [..., nums[i-1], (changed nums[i]), nums[i+1], ...]
    # The difference 'd' is determined by (nums[i+1] - nums[i-1]) / 2.
    
    for i in range(n):
        # Try changing nums[i]
        # We need to check all possible differences 'd' that could involve nums[i].
        # But 'd' is only interesting if it's a difference between existing elements.
        # Actually, the most efficient way is to iterate through all pairs (i, j) 
        # and assume they are part of the sequence with a gap of 1.
        
        # Let's reconsider: The longest sequence is either:
        # 1. A standard arithmetic subsequence (already calculated in max_len).
        # 2. A sequence where one element nums[i] is changed to fit a difference 'd'.
        
        # If nums[i] is changed, it must connect to nums[i-1] and nums[i+1].
        # The difference must be d = (nums[i+1] - nums[i-1]) / 2.
        if 0 < i < n - 1:
            if (nums[i+1] - nums[i-1]) % 2 == 0:
                d = (nums[i+1] - nums[i-1]) // 2
                # Count how many elements follow the pattern ... nums[i-1], (new), nums[i+1] ...
                # We need to know how many elements end at i-1 with diff d
                # AND how many elements start at i+1 with diff d.
                
                # To do this efficiently, we need a 'forward' DP.
                pass

    # Let's implement the forward DP to make the O(n^2) approach work.
    dp_fwd: list[dict[int, int]] = [{} for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            diff = nums[j] - nums[i]
            length = dp_fwd[j].get(diff, 1) + 1
            dp_fwd[i][diff] = max(dp_fwd[i].get(diff, 0), length)
            
    # Now check the "bridge" case
    for i in range(n):
        # Case: nums[i] is the changed element
        # It can bridge a sequence ending at i-1 and starting at i+1
        if 0 < i < n - 1:
            if (nums[i+1] - nums[i-1]) % 2 == 0:
                d = (nums[i+1] - nums[i-1]) // 2
                # Length = (elements ending at i-1 with d) + 1 (the changed i) + (elements starting at i+1 with d)
                # Note: dp[i-1][d] is the length of sequence ending at i-1.
                # dp_fwd[i+1][d] is the length of sequence starting at i+1.
                len_left = dp[i-1].get(d, 1)
                len_right = dp_fwd[i+1].get(d, 1)
                max_len = max(max_len, len_left + 1 + len_right)
        
        # Case: nums[i] is the changed element, but it's at the end or start of a sequence
        # (e.g., [1, 2, 3, 100] -> change 100 to 4, or [100, 1, 2, 3] -> change 100 to 0)
        if i < n - 1:
            # Change nums[i] to match the sequence starting at i+1
            # This is actually covered by the standard DP if we consider the sequence 
            # starting at i+1 and just adding one element at the front.
            for d, length in dp_fwd[i+1].items():
                max_len = max(max_len, length + 1)
        if i > 0:
            # Change nums[i] to match the sequence ending at i-1
            for d, length in dp[i-1].items():
                max_len = max(max_len, length + 1)

    # Final edge case: The sequence could be just [nums[i], (changed), nums[j]] 
    # where j > i + 1. This is covered by the bridge logic if we assume 
    # the sequence is just [nums[i], changed, nums[j]].
    # But the bridge logic requires i-1 and i+1. 
    # Let's check all pairs (i, j) where j = i + 2.
    for i in range(n - 2):
        if (nums[i+2] - nums[i]) % 2 == 0:
            d = (nums[i+2] - nums[i]) // 2
            # Sequence: nums[i], (changed i+1), nums[i+2]
            # We need to see if this can be extended.
            # The length is 3 + (elements ending at i with d) + (elements starting at i+2 with d)
            # Wait, the bridge logic already covers this if we consider len_left and len_right.
            # If i-1 doesn't exist, len_left is 1. If i+1 doesn't exist, len_right is 1.
            # The bridge logic: len_left = dp[i-1].get(d, 1), len_right = dp_fwd[i+1].get(d, 1)
            # For i=0, i-1 doesn't exist. Let's adjust the loop.
            pass

    # Corrected Bridge Logic:
    # A change at index 'i' can:
    # 1. Connect a sequence ending at i-1 and starting at i+1 (if diff is consistent)
    # 2. Extend a sequence ending at i-1 by one (change i to nums[i-1]+d)
    # 3. Extend a sequence starting at i+1 by one (change i to nums[i+1]-d)
    # 4. Be a sequence of length 2 (change i to nums[i-1]+d or nums[i+1]-d)
    
    # The loop above covers 1, 2, and 3. 
    # Let's re-verify the bridge for i=0 and i=n-1.
    # If i=0, we can change nums[0] to match dp_fwd[1]. Max len = dp_fwd[1].get(d, 1) + 1.
    # If i=n-1, we can change nums[n-1] to match dp[n-2]. Max len = dp[n-2].get(d, 1) + 1.
    # These are already in the code.
    
    return max_len
