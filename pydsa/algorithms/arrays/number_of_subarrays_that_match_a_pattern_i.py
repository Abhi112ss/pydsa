METADATA = {
    "id": 3034,
    "name": "Number of Subarrays That Match a Pattern I",
    "slug": "number-of-subarrays-that-match-a-pattern-i",
    "category": "Array",
    "aliases": [],
    "tags": ["string_matching", "sliding_window", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Count the number of subarrays whose absolute differences between adjacent elements match a given pattern.",
}

def solve(nums: list[int], pattern: list[int]) -> int:
    """
    Counts the number of subarrays in nums that match the given pattern.
    
    A subarray matches the pattern if the absolute differences between 
    consecutive elements in the subarray are equal to the pattern elements.

    Args:
        nums: A list of integers.
        pattern: A list of integers representing the required absolute differences.

    Returns:
        The total count of subarrays that match the pattern.

    Examples:
        >>> solve([1, 2, 1, 4, 1, 2, 1], [1, 1, 2, 1, 1])
        1
        >>> solve([1, 4, 2, 3, 5], [3, 2, 1])
        1
    """
    n = len(nums)
    m = len(pattern)
    
    # The pattern length m corresponds to m+1 elements in the original array.
    # If the pattern is longer than the possible differences, return 0.
    if m >= n:
        return 0

    # Step 1: Transform the input array into a difference array.
    # diffs[i] = abs(nums[i+1] - nums[i])
    # The length of diffs will be n - 1.
    diffs = []
    for i in range(n - 1):
        diffs.append(abs(nums[i + 1] - nums[i]))

    # Step 2: Use a sliding window or KMP-style approach to find pattern matches.
    # Since this is 'Pattern I' (constraints are small), a simple sliding window 
    # or direct comparison is efficient. For O(n) strictly, we use KMP.
    
    # Precompute KMP failure function (Partial Match Table) for the pattern.
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    # Step 3: Perform KMP search on the diffs array.
    count = 0
    j = 0  # index for pattern
    for i in range(len(diffs)):  # index for diffs
        while j > 0 and diffs[i] != pattern[j]:
            j = pi[j - 1]
        if diffs[i] == pattern[j]:
            j += 1
        
        if j == m:
            count += 1
            j = pi[j - 1]

    return count
