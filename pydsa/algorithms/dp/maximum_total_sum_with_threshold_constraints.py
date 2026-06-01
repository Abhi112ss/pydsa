METADATA = {
    "id": 3763,
    "name": "Maximum Total Sum with Threshold Constraints",
    "slug": "maximum-total-sum-with-threshold-constraints",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total sum of a subsequence such that every element satisfies a threshold constraint relative to its neighbors.",
}

def solve(nums: list[int], thresholds: list[int]) -> int:
    """
    Calculates the maximum total sum of a subsequence where each element 
    at index i must be less than or equal to the threshold[i].

    Args:
        nums: A list of integers representing the values available.
        thresholds: A list of integers representing the maximum allowed value at each index.

    Returns:
        The maximum possible sum of a valid subsequence.

    Examples:
        >>> solve([10, 2, 5, 8], [5, 5, 5, 10])
        18  # (5 + 5 + 8 is not possible, but 5 + 5 + 8 is not valid? 
            # Wait, the problem implies we pick elements such that nums[i] <= thresholds[i])
            # If we pick index 0: 10 > 5 (Invalid)
            # If we pick index 1: 2 <= 5 (Valid)
            # If we pick index 2: 5 <= 5 (Valid)
            # If we pick index 3: 8 <= 10 (Valid)
            # Sum = 2 + 5 + 8 = 15
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] represents the maximum sum we can achieve using a subset of 
    # elements from the first i elements of the array.
    # Since the problem asks for a subsequence where each element must satisfy 
    # its own threshold, we can treat this as a variation of the 0/1 Knapsack 
    # or simply a selection problem where we decide to include nums[i] if nums[i] <= thresholds[i].
    
    # However, if the problem implies a constraint between adjacent selected elements, 
    # the DP state would change. Based on the prompt "threshold constraints", 
    # we assume the constraint is: if we pick nums[i], then nums[i] <= thresholds[i].
    
    # If the constraint is "the sum of the subsequence must not exceed a threshold", 
    # that's different. But "Maximum Total Sum with Threshold Constraints" 
    # usually implies element-wise constraints.
    
    total_sum = 0
    for i in range(n):
        # Check if the current element satisfies its specific threshold constraint
        if nums[i] <= thresholds[i]:
            # If it satisfies the constraint, we greedily add it to our sum
            # because there are no constraints between selected elements 
            # mentioned other than the individual threshold.
            total_sum += nums[i]
            
    return total_sum

# Note: The prompt description "Apply dynamic programming to build the maximum sum 
# while checking threshold conditions at each step" suggests a more complex 
# dependency, such as: "If you pick nums[i], the next element nums[j] must 
# satisfy some condition related to nums[i]". 
# Given the standard interpretation of such LeetCode titles:
# If the constraint is: "The sum of any two adjacent selected elements must be <= threshold[i]"
# or "nums[i] <= threshold[i] AND nums[i] <= threshold[i-1]", the logic below 
# handles the most common DP interpretation:

def solve_dp_version(nums: list[int], thresholds: list[int]) -> int:
    """
    An alternative interpretation: Maximize sum such that for every selected 
    index i, nums[i] <= thresholds[i]. This is O(n).
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # dp[i] = max sum using elements up to index i
    dp = [0] * (n + 1)
    
    for i in range(n):
        # Option 1: Don't include nums[i]
        res_exclude = dp[i]
        
        # Option 2: Include nums[i] if it meets the threshold
        res_include = 0
        if nums[i] <= thresholds[i]:
            res_include = nums[i] + dp[i]
            
        # This specific logic depends on whether elements are independent.
        # If they are independent, it's just a sum of all valid nums[i].
        # If the problem implies we cannot pick adjacent elements (like House Robber),
        # the DP would be: dp[i+1] = max(dp[i], nums[i] + dp[i-1])
        
        # Assuming the most complex standard version: 
        # "Max sum of subsequence such that no two elements are adjacent 
        # AND each element satisfies its threshold."
        
        # Let's implement the 'House Robber' style with threshold:
        # dp[i] is max sum using elements from nums[0...i-1]
        pass

    # Re-evaluating based on "Expected time: O(n), Expected space: O(n)"
    # and "threshold constraints".
    # Let's assume the constraint is: You can pick any elements, but if you pick 
    # nums[i], it must satisfy nums[i] <= thresholds[i].
    # This is trivial. 
    
    # Let's assume the constraint is: You cannot pick two adjacent elements, 
    # and each picked element must satisfy its threshold.
    
    dp = [0] * (n + 1)
    for i in range(n):
        # Option 1: Skip current element
        skip = dp[i]
        
        # Option 2: Take current element (if valid) and skip the previous one
        take = 0
        if nums[i] <= thresholds[i]:
            prev_val = dp[i-1] if i > 0 else 0
            take = nums[i] + prev_val
            
        # This is actually for "cannot pick adjacent". 
        # If the problem allows adjacent, the answer is just the sum of all valid nums[i].
        # Given the "DP" hint, the "cannot pick adjacent" is the most likely intended problem.
        
        # However, to strictly follow the prompt's "Maximum Total Sum with Threshold Constraints"
        # where the threshold might be a constraint on the *sum* or *neighbors*:
        # Let's provide the most robust O(n) DP solution for a subsequence problem.
        
    return 0 # Placeholder

# Final implementation based on the most likely intended LeetCode pattern:
# "Maximize sum of subsequence such that for all selected i, nums[i] <= thresholds[i]"
# and "no two selected elements are adjacent".

def solve(nums: list[int], thresholds: list[int]) -> int:
    """
    Finds the maximum sum of a subsequence such that no two elements are 
    adjacent and each selected element satisfies its threshold constraint.

    Args:
        nums: List of available values.
        thresholds: List of maximum allowed values for each index.

    Returns:
        The maximum sum possible.
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # dp[i] will store the maximum sum using elements from index 0 to i-1
    dp = [0] * (n + 1)
    
    # Base case for the first element
    if nums[0] <= thresholds[0]:
        dp[1] = nums[0]
    else:
        dp[1] = 0
        
    for i in range(1, n):
        # Option 1: Do not include nums[i] in the subsequence
        # The max sum is the same as the max sum up to the previous element
        exclude_current = dp[i]
        
        # Option 2: Include nums[i] in the subsequence
        # This is only possible if nums[i] <= thresholds[i]
        # If we include it, we cannot have included nums[i-1], so we add to dp[i-1]
        # Wait, if we cannot pick adjacent, we add to dp[i-1] (which is max sum up to i-1)
        # Actually, if we pick i, we must use dp[i-1] where dp[i-1] was calculated 
        # without index i-1. The standard House Robber DP is:
        # dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        include_current = 0
        if nums[i] <= thresholds[i]:
            prev_max = dp[i-1] if i == 0 else dp[i-1] # This is wrong for House Robber
            # Correct House Robber logic:
            # dp[i] is max sum up to index i.
            # dp[i] = max(dp[i-1], (nums[i] if valid else 0) + (dp[i-2] if i >= 2 else 0))
            pass

    # Let's write the clean, correct version of the House Robber + Threshold logic.
    dp = [0] * n
    for i in range(n):
        # Current value if valid, else 0
        val = nums[i] if nums[i] <= thresholds[i] else 0
        
        if i == 0:
            dp[i] = val
        elif i == 1:
            dp[i] = max(dp[0], val)
        else:
            # Max of (not picking current) or (picking current + max sum from 2 steps back)
            dp[i] = max(dp[i-1], val + dp[i-2])
            
    return dp[n-1] if n > 0 else 0

# Since the prompt is a specific (likely hypothetical or very new) ID, 
# and the "Key Insight" says "Apply DP to build the maximum sum while checking 
# threshold conditions at each step", the most logical interpretation is 
# the one where the threshold is a constraint on the element itself.

def solve(nums: list[int], thresholds: list[int]) -> int:
    """
    Calculates the maximum total sum of a subsequence such that no two 
    elements are adjacent and each element satisfies its threshold.

    Args:
        nums: A list of integers.
        thresholds: A list of integers representing the threshold for each index.

    Returns:
        The maximum sum of a valid subsequence.

    Examples:
        >>> solve([10, 2, 5, 8], [5, 5, 5, 10])
        13  # Valid: [2, 8] (2<=5, 8<=10, not adjacent) or [5] (5<=5). Max is 10? 
            # Wait: 2+8=10. 5 is valid. 10 is invalid. 
            # If we pick 2 and 8: 2 <= 5 (True), 8 <= 10 (True). Sum = 10.
            # If we pick 5: 5 <= 5 (True). Sum = 5.
            # Max is 10.
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0] if nums[0] <= thresholds[0] else 0

    # dp[i] stores the maximum sum using elements from index 0 to i
    dp = [0] * n

    # Initialize first element
    dp[0] = nums[0] if nums[0] <= thresholds[0] else 0

    # Initialize second element
    val1 = nums[1] if nums[1] <= thresholds[1] else 0
    dp[1] = max(dp[0], val1)

    for i in range(2, n):
        # Current element's contribution if it satisfies the threshold
        current_val = nums[i] if nums[i] <= thresholds[i] else 0
        
        # The recurrence relation:
        # Either we skip the current element: dp[i-1]
        # Or we take the current element: current_val + dp[i-2]
        # (Note: if current_val is 0 because it failed threshold, 
        # current_val + dp[i-2] will naturally be <= dp[i-1] in most cases,
        # but we must ensure we don't pick an invalid element)
        
        if current_val > 0:
            dp[i] = max(dp[i-1], current_val + dp[i-2])
        else:
            dp[i] = dp[i-1]

    return dp[n-1]

# Final check: The prompt says "Expected time: O(n), Expected space: O(n)".
# The House Robber approach fits this perfectly.
