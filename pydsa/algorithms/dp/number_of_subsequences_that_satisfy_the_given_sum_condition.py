METADATA = {
    "id": 1498,
    "name": "Number of Subsequences That Satisfy the Given Sum Condition",
    "slug": "number-of-subsequences-that-satisfy-the-given-sum-condition",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "two_pointer", "math", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of non-empty subsequences where the sum of the minimum and maximum elements is less than or equal to a target.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of non-empty subsequences where min(subsequence) + max(subsequence) <= target.

    The algorithm sorts the array and uses a two-pointer approach. For a fixed minimum 
    element at index 'left', we find the largest possible index 'right' such that 
    nums[left] + nums[right] <= target. Any subsequence formed using nums[left] 
    and any subset of elements from the range (left + 1, right) will satisfy the condition.

    Args:
        nums: A list of integers.
        target: The target sum threshold.

    Returns:
        The number of valid subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([3, 5, 6, 7], 9)
        3
        >>> solve([1, 2, 3, 4, 5], 5)
        6
    """
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    
    # Precompute powers of 2 to avoid repeated O(n) exponentiation inside the loop
    # pow2[i] = 2^i % MOD
    pow2 = [1] * n
    for i in range(1, n):
        pow2[i] = (pow2[i - 1] * 2) % MOD
        
    count = 0
    left = 0
    right = n - 1
    
    # Use two pointers to find the range [left, right]
    while left <= right:
        if nums[left] + nums[right] <= target:
            # If nums[left] + nums[right] <= target, then for the fixed minimum nums[left],
            # any subsequence formed by picking nums[left] and any combination of 
            # elements in the range (left + 1, right) is valid.
            # The number of such elements is (right - left).
            # Total subsequences for this 'left' is 2^(right - left).
            count = (count + pow2[right - left]) % MOD
            left += 1
        else:
            # If the sum is too large, we must decrease the maximum element
            right -= 1
            
    return count
