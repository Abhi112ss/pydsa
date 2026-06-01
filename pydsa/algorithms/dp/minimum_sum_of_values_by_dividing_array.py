METADATA = {
    "id": 3117,
    "name": "Minimum Sum of Values by Dividing Array",
    "slug": "minimum-sum-of-values-by-dividing-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Divide an array into non-empty subarrays such that the sum of the maximum values of each subarray is minimized.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Args:
        nums: A list of integers representing the array.
        k: The number of subarrays to divide the array into.

    Returns:
        The minimum possible sum of the maximum values of the k subarrays.
    """
    n = len(nums)
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0

    for subarray_count in range(1, k + 1):
        new_dp = [inf] * (n + 1)
        for end_index in range(subarray_count, n + 1):
            current_max = 0
            for start_index in range(end_index - 1, subarray_count - 2, -1):
                if nums[start_index] > current_max:
                    current_max = nums[start_index]
                
                if dp[start_index] != inf:
                    potential_sum = dp[start_index] + current_max
                    if potential_sum < new_dp[end_index]:
                        new_dp[end_index] = potential_sum
        dp = new_dp

    return int(dp[n])