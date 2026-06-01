METADATA = {
    "id": 2488,
    "name": "Count Subarrays With Median K",
    "slug": "count-subarrays-with-median-k",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays where the median is equal to k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays where the median is exactly k.
    
    For an odd-length subarray, the median is the middle element.
    For an even-length subarray, the median is defined as the (n/2)-th 
    element in sorted order (the smaller of the two middle elements).
    
    Args:
        nums: A list of integers.
        k: The target median value.
        
    Returns:
        The total count of subarrays with median k.
        
    Examples:
        >>> solve([3, 2, 1, 4, 5], 4)
        3
        >>> solve([1, 2, 3], 2)
        2
    """
    n = len(nums)
    k_index = -1
    
    # Find the position of k. If k is not in nums, no subarray can have median k.
    for i in range(n):
        if nums[i] == k:
            k_index = i
            break
            
    if k_index == -1:
        return 0

    # We transform the problem into finding subarrays containing k where:
    # (count of elements > k) - (count of elements < k) is either 0 or 1.
    # Let x be the count of elements > k and y be the count of elements < k.
    # For odd length: x == y (diff = 0) or x == y + 1 (diff = 1) is not quite right.
    # Let's use the property: 
    # A subarray has median k if:
    # 1. It contains k.
    # 2. Let 'greater' be count of elements > k, 'smaller' be count of elements < k.
    #    For odd length: greater == smaller (diff 0) or greater == smaller + 1 (diff 1) is wrong.
    # Correct logic:
    # Let val = 1 if nums[i] > k, -1 if nums[i] < k, 0 if nums[i] == k.
    # A subarray [i, j] containing k has median k if:
    # Sum of transformed values is 0 (for odd length, e.g., [-1, 0, 1] sum=0)
    # Sum of transformed values is 1 (for even length, e.g., [0, 1] sum=1)
    
    # Map to store frequency of prefix sums encountered before k_index
    # prefix_sum_counts[sum] = frequency
    prefix_sum_counts = {0: 1}
    current_sum = 0
    
    # Traverse left from k_index to collect prefix sums of the left part
    for i in range(k_index - 1, -1, -1):
        if nums[i] < k:
            current_sum -= 1
        elif nums[i] > k:
            current_sum += 1
        prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1
        
    # Traverse right from k_index to find matching prefix sums
    # We reset current_sum for the right side calculation
    ans = 0
    current_sum = 0
    
    # Check the case where the subarray is just [k] or extends only to the left/right
    # The loop below handles the right side starting from k_index
    for i in range(k_index, n):
        if i > k_index:
            if nums[i] < k:
                current_sum -= 1
            elif nums[i] > k:
                current_sum += 1
        
        # We need (left_sum + right_sum) to be 0 or 1.
        # Note: current_sum here is the sum of elements from k_index to i.
        # We need left_sum + current_sum = 0  => left_sum = -current_sum
        # We need left_sum + current_sum = 1  => left_sum = 1 - current_sum
        
        # However, the 'current_sum' logic above is slightly different.
        # Let's redefine: 
        # Let S_left be sum of elements in [i, k_index-1]
        # Let S_right be sum of elements in [k_index+1, j]
        # Total sum = S_left + 0 (for k) + S_right
        # We want S_left + S_right == 0 OR S_left + S_right == 1
        
        # In the loop above, for i = k_index, current_sum is 0.
        # For i > k_index, current_sum is sum(nums[k_index+1...i])
        # Wait, the loop logic needs to be precise.
        pass

    # Re-implementing the traversal clearly:
    prefix_sum_counts = {0: 1}
    current_sum = 0
    # Left side: elements from k_index-1 down to 0
    for i in range(k_index - 1, -1, -1):
        if nums[i] < k:
            current_sum -= 1
        else:
            current_sum += 1
        prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1
        
    ans = 0
    current_sum = 0
    # Right side: elements from k_index up to n-1
    # Note: we include k_index in the right side sum calculation to simplify
    # but k itself contributes 0 to the sum.
    for i in range(k_index, n):
        if i > k_index:
            if nums[i] < k:
                current_sum -= 1
            else:
                current_sum += 1
        
        # We want (left_sum + current_sum) == 0 or (left_sum + current_sum) == 1
        # left_sum = -current_sum OR left_sum = 1 - current_sum
        target0 = -current_sum
        target1 = 1 - current_sum
        
        ans += prefix_sum_counts.get(target0, 0)
        ans += prefix_sum_counts.get(target1, 0)
        
    # Wait, the logic above double counts if target0 == target1, 
    # but since 0 != 1, that's impossible.
    # However, the 'prefix_sum_counts' includes the '0' sum which represents 
    # the empty left side. This is correct.
    
    # One edge case: the loop for 'ans' starts at k_index.
    # If i = k_index, current_sum = 0.
    # target0 = 0, target1 = 1.
    # ans += counts[0] (empty left side) + counts[1] (left side sum 1)
    # This correctly counts subarrays [k_index, k_index] and others.
    
    # Let's re-verify the logic with an example: nums=[3,2,1,4,5], k=4
    # k_index = 3.
    # Left side:
    # i=2 (nums[2]=1 < 4): current_sum = -1. counts = {0:1, -1:1}
    # i=1 (nums[1]=2 < 4): current_sum = -2. counts = {0:1, -1:1, -2:1}
    # i=0 (nums[0]=3 < 4): current_sum = -3. counts = {0:1, -1:1, -2:1, -3:1}
    # Right side:
    # i=3 (k): current_sum = 0. target0=0, target1=1. ans += counts[0](1) + counts[1](0) = 1. (Subarray [4])
    # i=4 (nums[4]=5 > 4): current_sum = 1. target0=-1, target1=0. ans += counts[-1](1) + counts[0](1) = 2. (Subarrays [1,4,5], [4,5])
    # Total ans = 3. Correct.
    
    return ans
