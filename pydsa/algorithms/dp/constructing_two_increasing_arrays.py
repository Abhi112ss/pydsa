METADATA = {
    "id": 3269,
    "name": "Constructing Two Increasing Arrays",
    "slug": "constructing-two-increasing-arrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be partitioned into two strictly increasing subsequences.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array can be partitioned into two strictly increasing subsequences.

    The problem can be solved using dynamic programming. We maintain the minimum possible 
    last element of one subsequence given that the other subsequence ends with the 
    current element nums[i].

    Args:
        nums: A list of integers representing the input array.

    Returns:
        True if the array can be partitioned into two strictly increasing subsequences, 
        False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4])
        True
        >>> solve([3, 2, 1])
        False
        >>> solve([1, 5, 2, 3])
        True
    """
    n = len(nums)
    if n == 0:
        return True

    # dp[i] stores the minimum possible value of the last element of the "other" 
    # subsequence when the current element nums[i] is the end of the "active" subsequence.
    # We initialize with infinity to represent an impossible state.
    inf = float('inf')
    dp = [inf] * n

    # Base case: For the first element, the "other" subsequence is empty.
    # We represent an empty subsequence's last element as -infinity.
    dp[0] = -inf

    for i in range(1, n):
        # Case 1: nums[i] continues the same subsequence that nums[i-1] was part of.
        # This is possible if nums[i] > nums[i-1].
        # In this case, the "other" subsequence's last element remains the same as dp[i-1].
        if nums[i] > nums[i - 1]:
            dp[i] = min(dp[i], dp[i - 1])

        # Case 2: nums[i] starts a new subsequence or switches, meaning nums[i-1] 
        # was the end of the "other" subsequence.
        # This is possible if nums[i] > dp[i-1] (the previous 'other' element).
        # If this happens, the new "other" element becomes nums[i-1].
        if nums[i] > dp[i - 1]:
            dp[i] = min(dp[i], nums[i - 1])

    # If dp[n-1] is not infinity, it means we successfully reached the end.
    return dp[n - 1] != inf
