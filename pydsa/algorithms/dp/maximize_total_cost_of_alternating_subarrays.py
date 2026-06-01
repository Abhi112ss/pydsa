METADATA = {
    "id": 3196,
    "name": "Maximize Total Cost of Alternating Subarrays",
    "slug": "maximize-total-cost-of-alternating-subarrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum total cost of a collection of non-overlapping alternating subarrays.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum total cost of non-overlapping alternating subarrays.
    An alternating subarray is defined by the pattern: nums[i] - nums[i+1] + nums[i+2] ...
    or nums[i] + nums[i+1] - nums[i+2] ... (effectively starting with + or -).
    Actually, the problem defines the cost of an alternating subarray starting at i 
    as nums[i] - nums[i+1] + nums[i+2] - ...
    
    Args:
        nums: A list of integers representing the array.

    Returns:
        The maximum total cost possible by selecting non-overlapping alternating subarrays.

    Examples:
        >>> solve([2, 0, 1, 5, 3])
        11
        >>> solve([1, 2, 3, 4, 5])
        5
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp_end_pos[i] is the max cost of alternating subarrays ending at index i 
    # where nums[i] was added to the sum (i.e., index i has a '+' sign).
    # dp_end_neg[i] is the max cost where nums[i] was subtracted (i.e., index i has a '-' sign).
    # dp_max_total[i] is the max cost using elements up to index i.
    
    # To optimize space to O(1), we only keep track of the previous states.
    # However, for clarity in a production-grade implementation, we use the logic:
    # current_pos_sum: max cost of an alternating subarray ending at i with +nums[i]
    # current_neg_sum: max cost of an alternating subarray ending at i with -nums[i]
    # total_max: max cost of all non-overlapping subarrays up to index i-1
    
    total_max = 0
    current_pos_sum = 0
    current_neg_sum = 0

    for x in nums:
        # Option 1: Start a new subarray with +x. 
        # The previous total_max represents the best we did before this subarray.
        # Option 2: Continue an existing subarray where the previous element was subtracted.
        new_pos_sum = max(total_max + x, current_neg_sum + x)
        
        # Option 1: Start a new subarray with -x. 
        # Note: An alternating subarray must start with a positive sign per problem definition 
        # (nums[i] - nums[i+1]...). But we can treat the "start" as a single element subarray [x].
        # Actually, the problem says: cost = nums[i] - nums[i+1] + nums[i+2]...
        # This means the first element is always positive.
        # So current_neg_sum can only be formed by extending a current_pos_sum.
        new_neg_sum = current_pos_sum - x
        
        # Update the running maximum of all completed subarrays.
        # We update total_max after calculating new_pos_sum and new_neg_sum 
        # to ensure we don't use the same element twice in the same 'total_max' calculation.
        # But we need to track the best possible sum ending at the current index.
        
        # Let's refine the DP:
        # dp_pos[i]: max cost of an alternating subarray ending at i with +nums[i]
        # dp_neg[i]: max cost of an alternating subarray ending at i with -nums[i]
        # dp_total[i]: max cost of non-overlapping subarrays in nums[0...i]
        
        # We use the values from the previous iteration (i-1)
        # current_pos_sum and current_neg_sum act as dp_pos[i-1] and dp_neg[i-1]
        
        # We need to store the previous total_max to calculate the new one.
        # However, the current element can either:
        # 1. Be the start of a new subarray: total_max_prev + x
        # 2. Continue a subarray: current_neg_sum_prev + x
        # 3. Be the second element of a subarray: current_pos_sum_prev - x
        
        # We must calculate these based on the state at i-1.
        # Let's use temporary variables to avoid using updated values in the same step.
        
        # We'll use a slightly different approach for clarity:
        # dp_pos: max cost of an alternating subarray ending at current index with +
        # dp_neg: max cost of an alternating subarray ending at current index with -
        # dp_total: max cost of non-overlapping subarrays up to current index
        pass

    # Re-implementing with clean logic
    dp_pos = 0 # Max cost of alternating subarray ending at i with +nums[i]
    dp_neg = float('-inf') # Max cost of alternating subarray ending at i with -nums[i]
    dp_total = 0 # Max cost of non-overlapping subarrays up to index i
    
    for x in nums:
        # To calculate dp_pos[i], we either start a new subarray (dp_total[i-1] + x)
        # or continue a subarray that ended with a minus (dp_neg[i-1] + x)
        next_dp_pos = max(dp_total + x, dp_neg + x)
        
        # To calculate dp_neg[i], we must continue a subarray that ended with a plus (dp_pos[i-1] - x)
        next_dp_neg = dp_pos - x
        
        # To calculate dp_total[i], we take the max of:
        # 1. Not including x in any new subarray (dp_total[i-1])
        # 2. Ending a subarray at x (max(next_dp_pos, next_dp_neg))
        next_dp_total = max(dp_total, next_dp_pos, next_dp_neg)
        
        dp_pos = next_dp_pos
        dp_neg = next_dp_neg
        dp_total = next_dp_total
        
    return dp_total
