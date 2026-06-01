METADATA = {
    "id": 2369,
    "name": "Check if There is a Valid Partition For The Array",
    "slug": "check-if-there-is-a-valid-partition-for-the-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be partitioned into subarrays of length 2 (equal elements) or length 3 (all elements equal).",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array can be partitioned into valid subarrays.
    A valid subarray is either:
    1. Two equal elements.
    2. Three equal elements.

    Args:
        nums: A list of integers representing the array.

    Returns:
        True if a valid partition exists, False otherwise.

    Examples:
        >>> solve([2, 2, 2, 2, 2])
        True
        >>> solve([1, 2, 3, 4])
        False
    """
    n = len(nums)
    # dp[i] indicates if the prefix nums[0...i-1] can be validly partitioned.
    # We use size n + 1 to handle the base case dp[0] = True.
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        # Case 1: Check if the last 2 elements form a valid pair (nums[i-2] == nums[i-1])
        if i >= 2 and nums[i - 1] == nums[i - 2]:
            if dp[i - 2]:
                dp[i] = True

        # Case 2: Check if the last 3 elements form a valid triplet (nums[i-3] == nums[i-2] == nums[i-1])
        # We use 'if not dp[i]' to avoid redundant checks if Case 1 already satisfied dp[i].
        if not dp[i] and i >= 3:
            if nums[i - 1] == nums[i - 2] == nums[i - 3]:
                if dp[i - 3]:
                    dp[i] = True

    return dp[n]
