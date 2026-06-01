METADATA = {
    "id": 3079,
    "name": "Find the Sum of Encrypted Integers",
    "slug": "find-the-sum-of-encrypted-integers",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of encrypted integers where each element is the sum of the next i and previous i elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of encrypted integers for a given array.
    
    The encryption rule for an element at index i is:
    nums[i] = sum(nums[i-j] + nums[i+j]) for j from 1 to i.
    
    Args:
        nums: A list of integers.
        
    Returns:
        The sum of all encrypted integers modulo 10^9 + 7.
        
    Examples:
        >>> solve([5, 1, 2, 1, 3])
        22
        >>> solve([1, 2, 3, 4, 5])
        30
    """
    MOD = 10**9 + 7
    n = len(nums)
    if n == 0:
        return 0
    
    # The encryption formula for index i is:
    # E[i] = nums[i-1] + nums[i+1] + nums[i-2] + nums[i+2] ...
    # This is equivalent to saying each nums[k] contributes to E[i] 
    # if 1 <= |i - k| <= i.
    #
    # Let's re-evaluate the contribution of each nums[k] to the total sum.
    # Total Sum = sum_{i=0}^{n-1} E[i]
    # Total Sum = sum_{i=0}^{n-1} sum_{j=1}^{i} (nums[i-j] + nums[i+j])
    # (Note: indices must be within [0, n-1])
    #
    # Instead of calculating E[i] for each i, we calculate how many times 
    # each nums[k] is added to the total sum.
    # nums[k] is added to E[i] if:
    # 1. i > k and i - k <= i  => i > k and k >= 0 (always true for i > k)
    #    Wait, the condition is 1 <= |i - k| <= i.
    #    Case 1: i > k. Condition: i - k <= i => -k <= 0 => k >= 0.
    #            So for a fixed k, it contributes to E[i] for all i > k.
    #    Case 2: i < k. Condition: k - i <= i => k <= 2i => i >= k/2.
    #            So for a fixed k, it contributes to E[i] for all i such that k/2 <= i < k.
    #
    # Let's refine the contribution of nums[k]:
    # For a fixed k:
    # It is a 'right-side' element for index i if i < k and i >= ceil(k/2).
    # It is a 'left-side' element for index i if i > k.
    #
    # Total contribution of nums[k] = nums[k] * (count of i where i < k and i >= k/2) 
    #                                + nums[k] * (count of i where i > k)
    #
    # Count of i in [ceil(k/2), k-1]: (k-1) - ceil(k/2) + 1 = k - ceil(k/2)
    # Count of i in [k+1, n-1]: (n-1) - (k+1) + 1 = n - 1 - k
    
    total_sum = 0
    for k in range(n):
        # Number of indices i where nums[k] is the 'right' element (i < k)
        # The condition is k - i <= i  => k <= 2i => i >= k/2
        # So i is in range [math.ceil(k/2), k-1]
        # Number of such i: (k - 1) - ((k + 1) // 2) + 1 = k - (k + 1) // 2
        # Note: if k=0, range is empty.
        right_count = k - (k + 1) // 2
        
        # Number of indices i where nums[k] is the 'left' element (i > k)
        # The condition is i - k <= i => -k <= 0 (always true for k >= 0)
        # So i is in range [k+1, n-1]
        # Number of such i: (n - 1) - (k + 1) + 1 = n - 1 - k
        left_count = n - 1 - k
        
        # If k=0, right_count is 0 - 0 = 0. Correct.
        # If k=1, right_count is 1 - 1 = 0. Correct (i < 1 and i >= 0.5 => none).
        # If k=2, right_count is 2 - 1 = 1. Correct (i < 2 and i >= 1 => i=1).
        
        contribution = (right_count + left_count) * nums[k]
        total_sum = (total_sum + contribution) % MOD
        
    return total_sum
