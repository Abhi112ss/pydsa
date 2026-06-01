METADATA = {
    "id": 3671,
    "name": "Sum of Beautiful Subsequences",
    "slug": "sum_of_beautiful_subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of all beautiful subsequences where a subsequence is beautiful if the difference between any two adjacent elements is not equal to k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the sum of all beautiful subsequences.
    A subsequence is beautiful if for every pair of adjacent elements (a, b) 
    in the subsequence, |a - b| != k.

    Args:
        nums: A list of integers representing the input array.
        k: The integer constraint for the beauty condition.

    Returns:
        The sum of all beautiful subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 3], 1)
        # Subsequences: [1], [2], [3], [1, 3]
        # Sums: 1 + 2 + 3 + (1+3) = 10
        >>> solve([1, 1, 1], 0)
        # All subsequences are beautiful if k != 0. If k=0, |1-1|=0, so not beautiful.
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    # count_dp[i] stores the number of beautiful subsequences ending at index i
    count_dp = [0] * n
    # sum_dp[i] stores the sum of all beautiful subsequences ending at index i
    sum_dp = [0] * n

    for i in range(n):
        # Every single element is a beautiful subsequence of length 1
        count_dp[i] = 1
        sum_dp[i] = nums[i]
        
        for j in range(i):
            # Check the beauty condition: |nums[i] - nums[j]| != k
            if abs(nums[i] - nums[j]) != k:
                # If we append nums[i] to a subsequence ending at j:
                # New count = existing count at j
                # New sum = sum of elements in subsequences at j + (nums[i] * count at j)
                count_dp[i] = (count_dp[i] + count_dp[j]) % MOD
                
                # The sum of the new subsequences is the sum of the previous 
                # subsequences plus the new element added 'count_dp[j]' times.
                new_sum_contribution = (sum_dp[j] + (nums[i] * count_dp[j])) % MOD
                sum_dp[i] = (sum_dp[i] + new_sum_contribution) % MOD

    # The answer is the sum of all beautiful subsequences ending at any index i
    total_sum = sum(sum_dp) % MOD
    return total_sum
