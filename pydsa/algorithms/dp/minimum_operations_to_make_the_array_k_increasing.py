METADATA = {
    "id": 2111,
    "name": "Minimum Operations to Make the Array K-Increasing",
    "slug": "minimum-operations-to-make-the-array-k-increasing",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "lis", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make an array k-increasing by transforming elements into any positive integer.",
}

import bisect

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum operations to make the array k-increasing.
    
    An array is k-increasing if for every index i, nums[i] <= nums[i + k].
    To minimize operations, we maximize the number of elements we keep.
    For each subsequence formed by indices (i, i+k, i+2k...), we find the 
    Longest Non-Decreasing Subsequence.

    Args:
        nums: A list of positive integers.
        k: The step size for the k-increasing condition.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        2
        >>> solve([1, 1, 1, 1, 1], 2)
        0
    """
    n = len(nums)
    total_operations = 0

    # The problem decomposes into k independent subsequences.
    # Subsequence 0: nums[0], nums[k], nums[2k]...
    # Subsequence 1: nums[1], nums[k+1], nums[2k+1]...
    for start_index in range(k):
        subsequence = []
        for i in range(start_index, n, k):
            subsequence.append(nums[i])
        
        # To minimize operations, we maximize elements kept.
        # This is equivalent to finding the Longest Non-Decreasing Subsequence (LNDS).
        # Note: The problem asks for non-decreasing (nums[i] <= nums[i+k]), 
        # so we use bisect_right instead of bisect_left.
        lnds_length = get_lnds_length(subsequence)
        
        # Operations needed for this subsequence = total elements - elements kept
        total_operations += (len(subsequence) - lnds_length)

    return total_operations

def get_lnds_length(arr: list[int]) -> int:
    """
    Computes the length of the Longest Non-Decreasing Subsequence using patience sorting.
    
    Args:
        arr: A list of integers.

    Returns:
        The length of the longest non-decreasing subsequence.
    """
    if not arr:
        return 0
    
    # tails[i] will store the smallest tail of all non-decreasing subsequences of length i+1
    tails = []
    
    for x in arr:
        # Use bisect_right to find the insertion point for a non-decreasing subsequence.
        # This allows duplicate values to extend the subsequence.
        idx = bisect.bisect_right(tails, x)
        
        if idx < len(tails):
            tails[idx] = x
        else:
            tails.append(x)
            
    return len(tails)
