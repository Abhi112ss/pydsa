METADATA = {
    "id": 673,
    "name": "Number of Longest Increasing Subsequence",
    "slug": "number-of-longest-increasing-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["lis", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the number of longest increasing subsequences in a given integer array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the number of longest increasing subsequences in the input array.

    Args:
        nums: A list of integers.

    Returns:
        The total count of longest increasing subsequences.

    Examples:
        >>> solve([1, 3, 5, 4, 7])
        2
        >>> solve([2, 2, 2, 2, 2])
        5
    """
    if not nums:
        return 0

    n = len(nums)
    # lengths[i] stores the length of the LIS ending at index i
    lengths = [1] * n
    # counts[i] stores the number of LIS of length lengths[i] ending at index i
    counts = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                # If we found a longer subsequence ending at i through j
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                # If we found another subsequence of the same maximum length ending at i
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]

    max_length = max(lengths)
    
    # Sum up the counts of all subsequences that have the maximum length
    total_count = 0
    for i in range(n):
        if lengths[i] == max_length:
            total_count += counts[i]

    return total_count
