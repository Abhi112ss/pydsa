METADATA = {
    "id": 2321,
    "name": "Maximum Score Of Spliced Array",
    "slug": "maximum-score-of-spliced-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["prefix_sum", "kadane_algorithm", "subarray"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum score possible by swapping a contiguous subarray of one array with a contiguous subarray of another array.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the maximum score possible by splicing a subarray of nums1 
    with a subarray of nums2.

    The problem is equivalent to finding the maximum subarray sum (Kadane's) 
    of (nums1[i] - nums2[i]) and (nums2[i] - nums1[i]) and adding it to the 
    total sum of the respective arrays.

    Args:
        nums1: The first integer array.
        nums2: The second integer array.

    Returns:
        The maximum score possible after splicing.

    Examples:
        >>> solve([3, 7, 1, 3, 1, 3, 1, 4, 5, 2, 6, 3, 6, 7], [2, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        42
        >>> solve([2, 1, 5, 1], [1, 2, 3, 4])
        12
    """
    def get_max_gain(arr_a: list[int], arr_b: list[int]) -> int:
        """
        Calculates the maximum increase in sum if we replace a subarray 
        of arr_a with the corresponding subarray of arr_b.
        """
        max_gain = 0
        current_gain = 0
        
        for i in range(len(arr_a)):
            # The gain of choosing index i is the difference between 
            # the element we want to put in and the element we are removing.
            diff = arr_b[i] - arr_a[i]
            
            # Standard Kadane's algorithm to find the maximum subarray sum of differences
            current_gain = max(diff, current_gain + diff)
            max_gain = max(max_gain, current_gain)
            
        return max_gain

    # Total sum if we don't change anything is sum(nums1) or sum(nums2).
    # However, the problem asks for the maximum score after a splice.
    # A splice of nums2 into nums1 means: sum(nums1) - sum(subarray_nums1) + sum(subarray_nums2)
    # This is equivalent to: sum(nums1) + (sum(subarray_nums2) - sum(subarray_nums1))
    
    # Case 1: Splicing a subarray of nums2 into nums1
    gain_nums2_into_nums1 = get_max_gain(nums1, nums2)
    score1 = sum(nums1) + gain_nums2_into_nums1
    
    # Case 2: Splicing a subarray of nums1 into nums2
    gain_nums1_into_nums2 = get_max_gain(nums2, nums1)
    score2 = sum(nums2) + gain_nums1_into_nums2
    
    return max(score1, score2)
