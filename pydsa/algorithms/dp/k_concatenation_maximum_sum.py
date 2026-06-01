METADATA = {
    "id": 1191,
    "name": "K-Concatenation Maximum Sum",
    "slug": "k-concatenation-maximum-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "kadane", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum subarray sum in an array concatenated k times.",
}

def solve(arr: list[int], k: int) -> int:
    """
    Calculates the maximum subarray sum of an array concatenated k times.

    The algorithm uses a variation of Kadane's algorithm. 
    If k=1, it's standard Kadane's.
    If k >= 2, we consider the maximum subarray sum within two concatenated copies.
    If the total sum of the array is positive and k > 2, we can include the 
    middle (k-2) full array sums to maximize the result.

    Args:
        arr: The input list of integers.
        k: The number of times the array is concatenated.

    Returns:
        The maximum subarray sum modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2], 3)
        9
        >>> solve([-2, -3, -1], 2)
        -1
        >>> solve([1, -2, 1], 5)
        1
    """
    MOD = 10**9 + 7

    def kadane(nums: list[int]) -> int:
        """Standard Kadane's algorithm to find max subarray sum."""
        max_so_far = float('-inf')
        current_max = 0
        for x in nums:
            current_max += x
            if current_max > max_so_far:
                max_so_far = current_max
            if current_max < 0:
                current_max = 0
        return int(max_so_far)

    if not arr:
        return 0

    # Case 1: Only one concatenation
    if k == 1:
        return kadane(arr) % MOD

    # Case 2: Two or more concatenations
    # We analyze the behavior using two copies of the array.
    # This covers subarrays that wrap around the end of the original array.
    two_copies = arr + arr
    max_sum_two_copies = kadane(two_copies)
    
    total_sum = sum(arr)

    # If the total sum of one array is positive, we can potentially 
    # include (k-2) full copies of the array in the middle of our subarray.
    if total_sum > 0:
        # Result = Max sum in 2 copies + (k-2) * total_sum
        # We use modulo arithmetic carefully.
        result = (max_sum_two_copies + (k - 2) * total_sum) % MOD
        return result
    else:
        # If total sum is non-positive, the maximum subarray cannot 
        # span more than two copies effectively.
        return max_sum_two_copies % MOD
