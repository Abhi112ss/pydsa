METADATA = {
    "id": 2592,
    "name": "Maximize Greatness of an Array",
    "slug": "maximize-greatness-of-an-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the sum of greatness by reordering elements of nums2 such that each element in nums1 is matched with a larger element in nums2.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the maximum possible greatness of an array by reordering nums2.
    
    Greatness is defined as the sum of max(0, nums2[i] - nums1[i]) for all i.
    To maximize this, we use a greedy approach with two pointers on sorted arrays.

    Args:
        nums1: The first array of integers.
        nums2: The second array of integers to be reordered.

    Returns:
        The maximum total greatness achievable.

    Examples:
        >>> solve([4, 8, 1, 2], [1, 3, 5, 7])
        6
        >>> solve([1, 1, 1, 1], [1, 1, 1, 1])
        0
        >>> solve([1, 2, 3, 4], [1, 2, 3, 4])
        0
    """
    # Sort both arrays to enable a greedy two-pointer strategy.
    # Sorting allows us to match the smallest possible 'greater' element 
    # from nums2 to the current element in nums1.
    nums1.sort()
    nums2.sort()

    total_greatness = 0
    nums2_index = 0
    n = len(nums1)

    # Iterate through each element in the sorted nums1.
    for nums1_val in nums1:
        # Move the nums2 pointer until we find an element strictly greater than nums1_val.
        # Because nums1 is sorted, if nums2[nums2_index] is not greater than nums1_val,
        # it will also not be greater than any subsequent (larger) elements in nums1.
        while nums2_index < n and nums2[nums2_index] <= nums1_val:
            nums2_index += 1
        
        # If we found a valid element in nums2, add the difference to greatness.
        if nums2_index < n:
            total_greatness += nums2[nums2_index] - nums1_val
            # Increment pointer to ensure each element in nums2 is used at most once.
            nums2_index += 1
        else:
            # If no more elements in nums2 can satisfy the condition, we can stop.
            break

    return total_greatness
