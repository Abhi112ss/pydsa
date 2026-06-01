METADATA = {
    "id": 1713,
    "name": "Minimum Operations to Make a Subsequence",
    "slug": "minimum-operations-to-make-a-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["binary_search", "greedy", "longest_increasing_subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make nums1 a subsequence of nums2 by transforming elements of nums1.",
}

import bisect

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum operations to make nums1 a subsequence of nums2.
    
    The problem asks for the minimum operations to make nums1 a subsequence of nums2.
    Since nums1 elements are unique, the problem is equivalent to finding the 
    Longest Common Subsequence (LCS) between nums1 and nums2. 
    Because nums1 contains unique elements, we can map each element in nums1 
    to its index and transform nums2 into a sequence of these indices. 
    The LCS then becomes the Longest Increasing Subsequence (LIS) of the transformed nums2.

    Args:
        nums1: A list of unique integers.
        nums2: A list of integers.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 3, 2], [1, 2, 3, 4])
        1
        >>> solve([1, 2, 3], [3, 2, 1])
        2
    """
    # Map each value in nums1 to its index for O(1) lookup
    # This allows us to transform the problem into finding the LIS
    value_to_index = {val: i for i, val in enumerate(nums1)}
    
    # Transform nums2 into a list of indices based on their position in nums1
    # We only care about elements that actually exist in nums1
    transformed_indices = []
    for val in nums2:
        if val in value_to_index:
            transformed_indices.append(value_to_index[val])
            
    # Find the length of the Longest Increasing Subsequence (LIS) of transformed_indices
    # We use the Patience Sorting algorithm (O(n log n))
    lis_tails = []
    for index in transformed_indices:
        # Find the insertion point to maintain a sorted list of tails
        pos = bisect.bisect_left(lis_tails, index)
        
        if pos < len(lis_tails):
            # Replace the existing tail to keep it as small as possible
            lis_tails[pos] = index
        else:
            # Extend the LIS
            lis_tails.append(index)
            
    # The number of operations is the total elements in nums1 minus the 
    # number of elements we can keep (the length of the LCS/LIS)
    lcs_length = len(lis_tails)
    return len(nums1) - lcs_length
