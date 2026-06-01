METADATA = {
    "id": 3299,
    "name": "Sum of Consecutive Subsequences",
    "slug": "sum-of-consecutive-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of all possible consecutive subsequences of a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of all possible consecutive subsequences of the input array.
    
    A consecutive subsequence (subarray) is defined by a starting index i and 
    an ending index j where 0 <= i <= j < n. The goal is to find the sum 
    of all elements in all such subarrays.

    Args:
        nums: A list of integers.

    Returns:
        The total sum of all consecutive subsequences.

    Examples:
        >>> solve([1, 2, 3])
        20
        # Subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3]
        # Sums: 1 + 2 + 3 + 3 + 5 + 6 = 20
    """
    n = len(nums)
    if n == 0:
        return 0

    # total_sum will store the final result.
    # current_subsequence_sum[i] stores the sum of all subarrays ending at index i.
    # Let S(i) be the sum of all subarrays ending at index i.
    # S(i) = nums[i] + (S(i-1) + nums[i] * i) is not quite right for simple sum.
    # Correct logic: 
    # Let dp[i] be the sum of all subarrays ending at index i.
    # A subarray ending at i is either [nums[i]] or [subarray ending at i-1] + [nums[i]].
    # There are (i + 1) such subarrays ending at index i.
    # Each of the (i) subarrays ending at i-1 is extended by nums[i].
    # Plus, the new single-element subarray [nums[i]].
    # So, dp[i] = dp[i-1] + (i + 1) * nums[i] is incorrect.
    # Let's re-derive:
    # Subarrays ending at i:
    # [nums[i]]
    # [nums[i-1], nums[i]]
    # ...
    # [nums[0], ..., nums[i]]
    # Sum of these = nums[i] + (nums[i-1] + nums[i]) + (nums[i-2] + nums[i-1] + nums[i]) ...
    # Sum = (i + 1) * nums[i] + (sum of all subarrays ending at i-1)
    # Wait, that's not right. Let's use the contribution method.
    # An element nums[i] appears in all subarrays [start, end] where 0 <= start <= i <= end < n.
    # Number of such subarrays = (i + 1) * (n - i).
    # Total sum = sum(nums[i] * (i + 1) * (n - i) for i in range(n)).
    
    # However, the prompt specifically asks for a DP approach.
    # Let dp[i] be the sum of all subarrays ending at index i.
    # dp[i] = dp[i-1] + (i + 1) * nums[i] is actually correct if we define dp[i] 
    # as the sum of elements of all subarrays ending at i.
    # Example [1, 2, 3]:
    # i=0: dp[0] = 1. Total = 1.
    # i=1: dp[1] = dp[0] + (1+1)*2 = 1 + 4 = 5. (Subarrays: [2], [1,2] -> sums 2, 3. 2+3=5). Total = 1+5=6.
    # i=2: dp[2] = dp[1] + (2+1)*3 = 5 + 9 = 14. (Subarrays: [3], [2,3], [1,2,3] -> sums 3, 5, 6. 3+5+6=14). Total = 6+14=20.
    
    total_sum = 0
    current_ending_sum = 0
    
    for i in range(n):
        # Each element nums[i] is added to all (i) subarrays that ended at i-1,
        # and it forms a new subarray [nums[i]] by itself.
        # So, current_ending_sum = (sum of elements in subarrays ending at i-1) + (nums[i] * (i + 1))
        # Wait, the logic is:
        # Sum of elements in subarrays ending at i:
        # = Sum_{j=0 to i} (Sum_{k=j to i} nums[k])
        # = Sum_{j=0 to i} ( (Sum_{k=j to i-1} nums[k]) + nums[i] )
        # = (Sum_{j=0 to i-1} Sum_{k=j to i-1} nums[k]) + (Sum_{j=0 to i} nums[i])
        # = dp[i-1] + (i + 1) * nums[i]
        
        current_ending_sum = current_ending_sum + (i + 1) * nums[i]
        
        # The logic above is actually for the sum of *sums*.
        # Let's re-verify:
        # [1, 2, 3]
        # i=0: current_ending_sum = 0 + (1)*1 = 1. total = 1.
        # i=1: current_ending_sum = 1 + (2)*2 = 5. total = 1 + 5 = 6.
        # i=2: current_ending_sum = 5 + (3)*3 = 14. total = 6 + 14 = 20.
        # This matches the example.
        
        # Note: The prompt asks for the sum of consecutive subsequences.
        # In LeetCode context, "subsequence" usually means non-contiguous, 
        # but "consecutive subsequence" is a synonym for "subarray".
        
        # We need to be careful with the definition of current_ending_sum.
        # Let dp[i] be the sum of all subarrays ending at index i.
        # dp[i] = dp[i-1] + (i + 1) * nums[i] is actually NOT correct.
        # Let's re-calculate:
        # dp[0] = nums[0]
        # dp[1] = nums[1] + (nums[1] + nums[0]) = 2*nums[1] + nums[0]
        # dp[2] = nums[2] + (nums[2] + nums[1]) + (nums[2] + nums[1] + nums[0]) = 3*nums[2] + 2*nums[1] + nums[0]
        # This is: dp[i] = (i + 1) * nums[i] + dp[i-1] is WRONG.
        # Correct recurrence: dp[i] = (i + 1) * nums[i] + (sum of elements in subarrays ending at i-1)
        # No, let's use the contribution method for clarity, it's O(n).
        # Or the correct DP:
        # Let f(i) be the sum of all subarrays ending at index i.
        # f(i) = nums[i] + (f(i-1) + i * nums[i]) is also not quite it.
        # Let's use the property:
        # f(i) = sum_{j=0}^{i} (sum_{k=j}^{i} nums[k])
        # f(i) = sum_{j=0}^{i} (prefix_sum[i] - prefix_sum[j-1])
        # f(i) = (i+1)*prefix_sum[i] - sum_{j=0}^{i} prefix_sum[j-1]
        
        # Let's use the simplest DP:
        # Let S[i] be the sum of all subarrays ending at index i.
        # S[i] = S[i-1] + (i + 1) * nums[i] is actually correct if we look at it this way:
        # S[i] = (nums[i]) + (nums[i] + nums[i-1]) + (nums[i] + nums[i-1] + nums[i-2]) ...
        # S[i] = (i+1)*nums[i] + (i)*nums[i-1] + (i-1)*nums[i-2] ... + 1*nums[0]
        # S[i-1] = (i)*nums[i-1] + (i-1)*nums[i-2] ... + 1*nums[0]
        # Therefore: S[i] = (i+1)*nums[i] + S[i-1]
        
        # This is exactly what I wrote in the code.
        
        total_sum += current_ending_sum
        
    # Wait, the logic above calculates the sum of all elements in all subarrays.
    # Let's re-verify with [1, 2, 3]:
    # i=0: current_ending_sum = 1. total = 1.
    # i=1: current_ending_sum = 1 + 2*2 = 5. total = 1 + 5 = 6.
    # i=2: current_ending_sum = 5 + 3*3 = 14. total = 6 + 14 = 20.
    # Correct.
    
    # However, the problem might imply a modulo if the numbers are large.
    # LeetCode 3299 usually involves large numbers. 
    # But the prompt doesn't specify a modulo. I will return the integer.
    
    return total_sum
