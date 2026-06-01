METADATA = {
    "id": 3287,
    "name": "Find the Maximum Sequence Value of Array",
    "slug": "find-the-maximum-sequence-value-of-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sequence value of an array where a sequence is defined by specific subsequence rules involving products and sums.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum sequence value found in the array.
    """
    n = len(nums)
    if n == 0:
        return 0

    dp = [0] * n
    
    for i in range(n):
        dp[i] = nums[i]
        
        if i >= 1:
            dp[i] = max(dp[i], nums[i-1] * nums[i])
            
        if i >= 2:
            dp[i] = max(dp[i], nums[i-2] * nums[i-1] * nums[i])
            
        if i >= 1:
            dp[i] = max(dp[i], dp[i-1] + nums[i])
            
        if i >= 2:
            dp[i] = max(dp[i], dp[i-2] + nums[i-1] * nums[i])
            
        if i >= 3:
            dp[i] = max(dp[i], dp[i-3] + nums[i-2] * nums[i-1] * nums[i])

    max_val = float('-inf')
    for i in range(n):
        if dp[i] > max_val:
            max_val = dp[i]
            
    return int(max_val)

def solve_optimized(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum sequence value found in the array.
    """
    n = len(nums)
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        val = nums[i-1]
        
        dp[i] = max(dp[i], dp[i-1] + val)
        
        if i >= 2:
            dp[i] = max(dp[i], dp[i-2] + nums[i-2] * nums[i-1])
            
        if i >= 3:
            dp[i] = max(dp[i], dp[i-3] + nums[i-3] * nums[i-2] * nums[i-1])
            
    return int(dp[n])

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers.

    Returns:
        The maximum sequence value found in the array.
    """
    n = len(nums)
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        current_val = nums[i-1]
        
        dp[i] = max(dp[i], dp[i-1] + current_val)
        
        if i >= 2:
            product_two = nums[i-2] * nums[i-1]
            dp[i] = max(dp[i], dp[i-2] + product_two)
            
        if i >= 3:
            product_three = nums[i-3] * nums[i-2] * nums[i-1]
            dp[i] = max(dp[i], dp[i-3] + product_three)
            
    return int(dp[n])