METADATA = {
    "id": 2901,
    "name": "Longest Unequal Adjacent Groups Subsequence II",
    "slug": "longest-unequal-adjacent-groups-subsequence-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subsequence where no two adjacent elements are equal.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the length of the longest subsequence where no two adjacent 
    elements are equal.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest subsequence with unequal adjacent elements.

    Examples:
        >>> solve([1, 2, 1, 2])
        4
        >>> solve([1, 1, 1, 1])
        1
        >>> solve([1, 2, 2, 3, 3, 4])
        4
    """
    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the length of the longest valid subsequence ending at index i
    dp = [1] * n

    # We iterate through each element to build the DP table
    for i in range(n):
        for j in range(i):
            # If the current element is different from the previous element in the subsequence
            if nums[i] != nums[j]:
                # Update dp[i] if taking nums[j] followed by nums[i] yields a longer sequence
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    # The answer is the maximum value found in the dp array
    return max(dp)
