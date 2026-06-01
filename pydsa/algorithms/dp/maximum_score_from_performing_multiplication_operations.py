METADATA = {
    "id": 1770,
    "name": "Maximum Score from Performing Multiplication Operations",
    "slug": "maximum-score-from-performing-multiplication-operations",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum score obtained by performing m multiplication operations choosing either the first or last element of an array n.",
}

def solve(nums: list[int], m: int) -> int:
    """
    Calculates the maximum score by performing m multiplication operations.
    In each operation, you can pick either the first or the last element of the current array.

    Args:
        nums: A list of integers representing the initial array.
        m: The number of multiplication operations to perform.

    Returns:
        The maximum possible score.

    Examples:
        >>> solve([1, 2, 3, 4], 2)
        11
        >>> solve([5, 4, 2, 3], 3)
        30
    """
    n = len(nums)
    
    # dp[i][j] represents the maximum score after performing i operations,
    # where j is the number of elements taken from the left side.
    # The number of elements taken from the right side is (i - j).
    # We use (m + 1) x (m + 1) because i goes up to m and j goes up to i.
    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        # i is the current operation number (1-indexed)
        # j is the number of elements taken from the left
        for j in range(i + 1):
            # Calculate the index of the element taken from the right
            # If we took j from left, we took (i - j) from right.
            # The right index is (n - 1) - (number of elements taken from right)
            # However, we need the value of the element being picked *at* this step.
            
            # Case 1: The i-th operation picked the element from the left.
            # This means in the previous step (i-1), we had (j-1) elements from the left.
            if j > 0:
                left_val = nums[j - 1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + left_val)
            
            # Case 2: The i-th operation picked the element from the right.
            # This means in the previous step (i-1), we had j elements from the left.
            # The number of elements taken from the right in the previous step was (i - 1 - j).
            if j < i:
                right_idx = n - 1 - (i - 1 - j)
                right_val = nums[right_idx]
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + right_val)

    # The answer is the maximum value in the last row of the DP table
    return max(dp[m])
