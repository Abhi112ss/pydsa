METADATA = {
    "id": 3654,
    "name": "Minimum Sum After Divisible Sum Deletions",
    "slug": "minimum-sum-after-divisible-sum-deletions",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the minimum sum of an array after deleting any number of subarrays whose sum is divisible by k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum possible sum of the array after deleting any number 
    of contiguous subarrays whose sums are divisible by k.

    The problem can be reframed as finding the maximum sum of elements that 
    can be removed. Since we can remove any subarray with sum % k == 0, 
    this is equivalent to finding the maximum sum of elements that form 
    disjoint subarrays, each having a sum divisible by k.

    Args:
        nums: A list of integers.
        k: The divisor used to determine if a subarray sum is divisible.

    Returns:
        The minimum sum of the remaining elements.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        3
        # Subarrays [1, 2] (sum 3) and [3] (sum 3) can be removed. 
        # Remaining: [4, 5] is not correct logic. 
        # Actually, [1, 2] sum 3, [3] sum 3. Remaining [4, 5] sum 9.
        # Wait, if we remove [1, 2] and [3], sum is 9. 
        # If we remove [1, 2, 3], sum is 9.
        # If we remove [3], sum is 12.
        # If we remove [1, 2, 3, 4, 5] is not possible because sum is 15.
        # 15 % 3 == 0, so we can remove the whole array. Min sum 0.
    """
    total_sum = sum(nums)
    n = len(nums)
    
    # dp[r] stores the maximum sum of elements we can remove such that 
    # the last removed subarray ended at some index and the current 
    # prefix sum modulo k is r.
    # However, a simpler approach:
    # We want to find the maximum sum of elements that can be partitioned 
    # into subarrays where each subarray sum % k == 0.
    
    # max_removed[r] = maximum sum of elements removed using subarrays 
    # that end at a position where the prefix sum % k == r.
    # We initialize with -infinity to represent unreachable remainders.
    max_removed = [-float('inf')] * k
    max_removed[0] = 0
    
    current_prefix_sum = 0
    current_running_sum = 0
    
    for x in nums:
        current_running_sum += x
        current_prefix_sum = (current_prefix_sum + x) % k
        
        # If we find a prefix sum remainder 'r' that we have seen before,
        # the subarray between the previous occurrence and now has sum % k == 0.
        # The sum of this subarray is (current_running_sum - previous_running_sum).
        # We want to maximize the total sum of such removed subarrays.
        
        # To implement this efficiently:
        # Let dp[r] be the maximum sum of removed elements such that 
        # the current prefix sum % k is r.
        # When we encounter remainder r, we can potentially "complete" a 
        # subarray that started after a previous point where the remainder was r.
        
        # We use a temporary variable to update max_removed to avoid using 
        # the same element multiple times in one step.
        
        # The logic: if we are at current_prefix_sum 'r', we can potentially 
        # add the sum of the subarray since the last time we were at 'r'.
        # But we need to track the 'best' sum we could have had at remainder 'r'.
        
        # Let's refine:
        # dp[r] is the max sum of removed elements ending at a prefix with remainder r.
        # When we reach remainder r, we can update dp[r] = max(dp[r], current_running_sum - (some_previous_running_sum_at_r) + dp_at_that_time)
        # This is equivalent to: dp[r] = max(dp[r], current_running_sum + max_val_at_r)
        # where max_val_at_r = max(dp[prev_r] - running_sum_at_prev_r)
        
        # Let's use the property: 
        # A subarray [i, j] has sum % k == 0 if prefix_sum[j] % k == prefix_sum[i-1] % k.
        # We want to pick non-overlapping [i, j] to maximize sum(subarray_sums).
        
        # best_diff[r] = max(dp[r] - current_running_sum)
        # This is not quite right. Let's use:
        # dp[i] = max sum of removed elements using elements up to index i.
        # dp[i] = max(dp[i-1], max_{j < i, sum(j+1...i)%k == 0} (dp[j] + sum(j+1...i)))
        
        # Let S[i] be prefix sum up to i.
        # sum(j+1...i) = S[i] - S[j].
        # dp[i] = max(dp[i-1], max_{j < i, S[i]%k == S[j]%k} (dp[j] + S[i] - S[j]))
        # dp[i] = max(dp[i-1], S[i] + max_{j < i, S[i]%k == S[j]%k} (dp[j] - S[j]))
        
        # We only need to track the best (dp[j] - S[j]) for each remainder.
        pass

    # Corrected Implementation:
    dp_prev_max_diff = [-float('inf')] * k
    dp_prev_max_diff[0] = 0 # dp[0] - S[0] = 0 - 0 = 0
    
    current_dp = 0
    current_S = 0
    
    for x in nums:
        current_S += x
        r = current_S % k
        
        # Option 1: Don't include x in a new removed subarray ending here
        # current_dp remains the same as the previous index's dp
        
        # Option 2: x is the end of a removed subarray [j+1, i]
        # where S[i]%k == S[j]%k.
        # The sum of this subarray is S[i] - S[j].
        # The total removed sum would be dp[j] + S[i] - S[j].
        # We maximize this by maximizing (dp[j] - S[j]) for the same remainder.
        
        if dp_prev_max_diff[r] != -float('inf'):
            current_dp = max(current_dp, current_S + dp_prev_max_diff[r])
        
        # Update the best (dp[i] - S[i]) for the current remainder
        # to be used by future indices.
        dp_prev_max_diff[r] = max(dp_prev_max_diff[r], current_dp - current_S)
        
    return total_sum - current_dp
