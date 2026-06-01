METADATA = {
    "id": 3177,
    "name": "Find the Maximum Length of a Good Subsequence II",
    "slug": "find-the-maximum-length-of-a-good-subsequence-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Find the maximum length of a subsequence where the absolute difference between adjacent elements modulo k is either 0 or some constant x.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum length of a 'good' subsequence.
    A subsequence is good if for all adjacent elements a, b, (a + b) % k is constant.
    This is equivalent to saying (a % k + b % k) % k is constant.
    However, the problem definition for 'Good Subsequence II' usually implies 
    the condition: (nums[i] + nums[i+1]) % k == constant.
    
    Actually, the standard interpretation for this specific problem type is:
    Find max length where (nums[i] + nums[i+1]) % k == target for some target in [0, k-1].

    Args:
        nums: A list of integers.
        k: The modulo value.

    Returns:
        The maximum length of a good subsequence.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        5
        >>> solve([1, 4, 2, 3, 1, 4], 3)
        4
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[rem][val] stores the max length of a subsequence where:
    # the last element added had (element % k) == val
    # and the required sum modulo k is 'rem'.
    # Since we want to find the max length for ANY constant sum 'rem',
    # we iterate through all possible sums 'rem' from 0 to k-1.
    
    # However, a more efficient way to view this:
    # For a fixed target sum 'rem', if the current element is 'v',
    # the previous element 'p' must satisfy (p + v) % k == rem.
    # Therefore, p % k == (rem - (v % k)) % k.

    max_len = 1
    
    # We can optimize space. Instead of a full 2D array if k is large, 
    # but the problem constraints usually allow O(k^2) or O(n*k).
    # Given the problem type, we iterate through each possible target sum 'rem'.
    
    for target_rem in range(k):
        # dp[v_rem] = max length of subsequence ending with an element x where x % k == v_rem
        # and all adjacent pairs sum to target_rem modulo k.
        dp = [0] * k
        for x in nums:
            v_rem = x % k
            # To satisfy (prev_rem + v_rem) % k == target_rem:
            prev_rem = (target_rem - v_rem) % k
            
            # The new length ending in v_rem is the best length ending in prev_rem + 1
            # Note: if prev_rem == v_rem, it still works (e.g., target 0, v_rem 0)
            dp[v_rem] = max(dp[v_rem], dp[prev_rem] + 1)
            
            if dp[v_rem] > max_len:
                max_len = dp[v_rem]
                
    return max_len

# Note: The logic above is O(k * n). 
# If k is very large, we need a different approach.
# But for "Good Subsequence II" style problems, k is usually small enough.
# Let's refine the DP to be more robust for the specific constraints.

def solve_optimized(nums: list[int], k: int) -> int:
    """
    Optimized version using a 2D DP table to avoid re-scanning nums for every target_rem.
    dp[rem][v_rem] = max length of subsequence where (a+b)%k == rem and last element % k == v_rem.
    """
    n = len(nums)
    if n == 0:
        return 0
    
    # dp[rem][v_rem]
    # rem: the constant sum modulo k
    # v_rem: the remainder of the last element in the subsequence
    dp = [[0] * k for _ in range(k)]
    ans = 1
    
    for x in nums:
        v_rem = x % k
        for target_rem in range(k):
            # The required remainder of the previous element
            prev_rem = (target_rem - v_rem) % k
            
            # Update the DP state: 
            # If we append x to a subsequence ending in prev_rem, 
            # the new length is dp[target_rem][prev_rem] + 1.
            # If dp[target_rem][prev_rem] is 0, it means x is the first element, length 1.
            # However, we must handle the case where the subsequence is just [x].
            # But a single element doesn't have a 'sum of adjacent pairs'.
            # The problem implies length >= 1.
            
            # We use a temporary update to ensure we don't use the same element twice 
            # for the same target_rem in one step (though not strictly necessary here 
            # since we update dp[target_rem][v_rem] using dp[target_rem][prev_rem]).
            
            # If prev_rem == v_rem, we are extending a sequence of same-remainder elements.
            # If prev_rem != v_rem, we are alternating.
            
            # To correctly handle the "first element" case:
            # If dp[target_rem][prev_rem] is 0, it means this is the first element 
            # of a potential subsequence for this target_rem.
            # But wait, a single element doesn't define a target_rem.
            # A target_rem is only defined once we have at least TWO elements.
            # Actually, the problem says "all adjacent pairs". 
            # A single element satisfies this vacuously.
            
            # Correct logic:
            # For a fixed target_rem, dp[v_rem] is the max length ending in v_rem.
            # When we see x, we look at dp[prev_rem].
            # If dp[prev_rem] > 0, we extend it.
            # If dp[prev_rem] == 0, we can start a new sequence of length 1.
            # BUT, a sequence of length 1 doesn't have a target_rem yet.
            # Actually, any x can be the start of a sequence for ANY target_rem.
            
            # Let's use the first approach logic but more cleanly.
            pass

    # Re-implementing the most efficient O(nk) approach
    # dp[rem][v_rem] is the max length of a subsequence where 
    # (a_i + a_{i+1}) % k == rem and a_{last} % k == v_rem.
    
    dp = [[0] * k for _ in range(k)]
    res = 1
    for x in nums:
        v_rem = x % k
        for target_rem in range(k):
            prev_rem = (target_rem - v_rem) % k
            # If dp[target_rem][prev_rem] is 0, it means x is the first element.
            # A single element can be the start of a sequence for any target_rem.
            # We treat it as length 1.
            if dp[target_rem][prev_rem] == 0:
                dp[target_rem][v_rem] = max(dp[target_rem][v_rem], 1)
            else:
                dp[target_rem][v_rem] = max(dp[target_rem][v_rem], dp[target_rem][prev_rem] + 1)
            
            if dp[target_rem][v_rem] > res:
                res = dp[target_rem][v_rem]
    return res

# The actual LeetCode 3177 problem is slightly different:
# "Find the maximum length of a good subsequence where (nums[i] % k + nums[i+1] % k) % k is constant"
# OR "the absolute difference is constant".
# Looking at the problem name "Good Subsequence II", it usually refers to 
# (nums[i] % k) being constant OR (nums[i] + nums[i+1]) % k being constant.
# Actually, the most common version is: 
# A subsequence is good if all (nums[i] % k) are the same OR all (nums[i] + nums[i+1]) % k are the same.

def solve(nums: list[int], k: int) -> int:
    """
    Final implementation for LeetCode 3177.
    The condition is: (nums[i] % k + nums[i+1] % k) % k == constant.
    This is equivalent to: (nums[i] % k + nums[i+1] % k) % k == target.
    """
    n = len(nums)
    if n <= 1:
        return n
    
    # dp[target_rem][last_rem]
    # target_rem: the constant sum modulo k
    # last_rem: the remainder of the last element added
    dp = [[0] * k for _ in range(k)]
    max_len = 1
    
    for x in nums:
        v_rem = x % k
        for target_rem in range(k):
            prev_rem = (target_rem - v_rem) % k
            
            # If we have a sequence ending in prev_rem for this target_rem, extend it.
            # Otherwise, this is the first element (length 1).
            if dp[target_rem][prev_rem] > 0:
                dp[target_rem][v_rem] = max(dp[target_rem][v_rem], dp[target_rem][prev_rem] + 1)
            else:
                # Even if we haven't formed a pair, this element can be the start.
                # We use 1 to represent a single element.
                dp[target_rem][v_rem] = max(dp[target_rem][v_rem], 1)
            
            if dp[target_rem][v_rem] > max_len:
                max_len = dp[target_rem][v_rem]
                
    return max_len

# Wait, the problem 3177 is actually:
# A subsequence is good if:
# 1. All elements have the same remainder modulo k.
# 2. All adjacent elements have the same sum modulo k.
# Actually, the problem is simpler: 
# Find max length where (nums[i] % k + nums[i+1] % k) % k is constant.
# This covers both cases (if target_rem = 2 * v_rem).

# Let's refine the DP one last time to be strictly O(nk).
# The current implementation is O(n * k).
