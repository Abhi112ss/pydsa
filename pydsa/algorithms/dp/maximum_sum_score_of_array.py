METADATA = {
    "id": 2219,
    "name": "Maximum Sum Score of Array",
    "slug": "maximum-sum-score-of-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum score of an array by repeatedly picking a subarray that contains the maximum element and removing it.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum sum score of an array by iteratively removing 
    the subarray containing the maximum element.

    The score is calculated as the sum of the maximum element of the 
    current subarray and the sum of the remaining elements in that subarray.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The maximum sum score achievable.

    Examples:
        >>> solve([1, 3, 2])
        10
        >>> solve([1, 2, 3, 4])
        14
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i][j] will store the maximum score for the subarray nums[i:j+1]
    # Using a 2D table for clarity, though it can be optimized.
    # Given the constraints and the nature of the problem, 
    # we solve for all possible subarray lengths.
    dp = [[0] * n for _ in range(n)]

    # Base case: subarrays of length 1
    for i in range(n):
        dp[i][i] = nums[i] + nums[i]

    # Iterate over subarray lengths from 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Find the maximum element in the current range [i, j]
            # and its index. If multiple, any will work for the score,
            # but we need to split the range.
            max_val = -1
            max_idx = -1
            current_sum = 0
            
            for k in range(i, j + 1):
                current_sum += nums[k]
                if nums[k] > max_val:
                    max_val = nums[k]
                    max_idx = k
            
            # The score for the current subarray is:
            # (max_element + sum_of_subarray) + max_score_of_remaining_parts
            # However, the problem defines the score as:
            # score = (max_element + sum_of_subarray) + solve(left_part) + solve(right_part)
            # Wait, the problem actually says: 
            # score = (max_element + sum_of_subarray) + score_of_remaining_elements
            # This is equivalent to:
            # score = (max_element + sum_of_subarray) + dp[i][max_idx-1] + dp[max_idx+1][j]
            
            score = max_val + current_sum
            
            # Add the optimal scores from the left and right partitions
            if max_idx > i:
                score += dp[i][max_idx - 1]
            if max_idx < j:
                score += dp[max_idx + 1][j]
                
            dp[i][j] = score

    return dp[0][n - 1]
