METADATA = {
    "id": 2382,
    "name": "Maximum Segment Sum After Removals",
    "slug": "maximum-segment-sum-after-removals",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "greedy", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum segment sum after removing exactly one element from the array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum segment sum possible after removing exactly one element.

    The problem asks for the maximum sum of a contiguous subarray after one element 
    is removed. This is equivalent to finding the maximum sum of two adjacent 
    subarrays (one ending before the removed element and one starting after it).

    Args:
        nums: A list of integers representing the original array.

    Returns:
        The maximum segment sum after removing one element.

    Examples:
        >>> solve([1, -2, 3, 4])
        7
        >>> solve([-1, -2, -3])
        -1
        >>> solve([1, 2, 3])
        5
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        # Based on problem constraints, if only one element exists, 
        # removing it leaves an empty segment (sum 0) or is undefined.
        # However, standard LeetCode interpretation for "removing one" 
        # usually implies the remaining elements form the segment.
        return 0

    # left_max[i] stores the maximum subarray sum ending at index i-1
    left_max = [0] * n
    current_max = 0
    for i in range(n):
        left_max[i] = current_max
        # Standard Kadane's logic to find max subarray sum ending at i
        current_max = max(nums[i], current_max + nums[i])
        # We actually want the max subarray sum ending AT OR BEFORE i.
        # But for the "removal" logic, we need the max sum ending exactly at i-1.
        # Let's refine: left_max[i] = max subarray sum ending at index i-1.
    
    # Re-calculating left_max correctly:
    # left_max[i] is the max sum of a subarray ending at index i-1
    left_max = [0] * n
    running_sum = 0
    for i in range(n):
        # Max subarray sum ending at i-1
        if i == 0:
            left_max[i] = 0 # No element before index 0
        else:
            # We use a local Kadane to find max sum ending at i-1
            pass 

    # Let's use a cleaner approach:
    # left_max[i]: max subarray sum ending at index i-1
    # right_max[i]: max subarray sum starting at index i+1
    
    left_max = [0] * n
    current_ending_here = 0
    for i in range(n):
        left_max[i] = current_ending_here
        # Update current_ending_here for the next index
        # If we are at index i, current_ending_here will be max sum ending at i
        if i == 0:
            current_ending_here = nums[i]
        else:
            current_ending_here = max(nums[i], current_ending_here + nums[i])
            
    # Wait, the logic above is slightly flawed for the "removal" bridge.
    # Let's use:
    # L[i] = max subarray sum ending at index i
    # R[i] = max subarray sum starting at index i
    
    L = [0] * n
    current_sum = 0
    for i in range(n):
        if i == 0:
            L[i] = nums[i]
        else:
            L[i] = max(nums[i], L[i-1] + nums[i])
            
    R = [0] * n
    current_sum = 0
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            R[i] = nums[i]
        else:
            R[i] = max(nums[i], R[i+1] + nums[i])

    # The maximum sum after removing nums[i] is either:
    # 1. A subarray entirely to the left of i (max of L[0...i-1])
    # 2. A subarray entirely to the right of i (max of R[i+1...n-1])
    # 3. A subarray that bridges across the gap (L[i-1] + R[i+1])
    
    # To handle "entirely to the left/right" efficiently, we precompute prefix/suffix maxes
    # of the L and R arrays.
    
    prefix_max_L = [0] * n
    prefix_max_L[0] = L[0]
    for i in range(1, n):
        prefix_max_L[i] = max(prefix_max_L[i-1], L[i])
        
    suffix_max_R = [0] * n
    suffix_max_R[n-1] = R[n-1]
    for i in range(n - 2, -1, -1):
        suffix_max_R[i] = max(suffix_max_R[i+1], R[i])

    max_segment_sum = float('-inf')

    for i in range(n):
        # Option 1: Remove nums[i], segment is to the left
        if i > 0:
            max_segment_sum = max(max_segment_sum, prefix_max_L[i-1])
        
        # Option 2: Remove nums[i], segment is to the right
        if i < n - 1:
            max_segment_sum = max(max_segment_sum, suffix_max_R[i+1])
            
        # Option 3: Remove nums[i], segment bridges the gap
        if i > 0 and i < n - 1:
            # The bridge is the max sum ending at i-1 + max sum starting at i+1
            # However, the problem asks for a SINGLE contiguous segment.
            # If we remove nums[i], the elements at i-1 and i+1 become adjacent.
            # So the new segment sum is (sum ending at i-1) + (sum starting at i+1)
            # BUT only if we consider the bridge. 
            # Actually, the bridge is simply L[i-1] + R[i+1] if we treat them as one.
            # Wait, the problem says "Maximum Segment Sum". 
            # If we remove nums[i], the array becomes [nums[0]...nums[i-1], nums[i+1]...nums[n-1]].
            # A segment in this new array can either be within the left part, 
            # within the right part, or cross the junction.
            # If it crosses the junction, it is (some suffix of left part) + (some prefix of right part).
            # The max such sum is (max sum ending at i-1) + (max sum starting at i+1).
            
            # We need the max sum ending AT i-1 and starting AT i+1.
            # We already have L[i-1] and R[i+1].
            max_segment_sum = max(max_segment_sum, L[i-1] + R[i+1])

    return int(max_segment_sum)
