METADATA = {
    "id": 2499,
    "name": "Minimum Total Cost to Make Arrays Unequal",
    "slug": "minimum-total-cost-to-make-arrays-unequal",
    "category": "Greedy",
    "aliases": [],
    "tags": ["arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to make two arrays unequal by changing elements such that no index has equal values in both arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum cost to make two arrays unequal.
    
    The cost to change an element at index i is 1 if nums1[i] != nums2[i].
    If nums1[i] == nums2[i], we must change one of them. 
    If all elements are equal, we might need a cost of 2 for one index to avoid 
    creating a new equality.

    Args:
        nums1: The first integer array.
        nums2: The second integer array.

    Returns:
        The minimum total cost to make the arrays unequal.

    Examples:
        >>> solve([1, 1, 1], [1, 1, 1])
        4
        >>> solve([1, 2, 3], [1, 2, 3])
        4
        >>> solve([1, 2, 3], [4, 5, 6])
        0
    """
    n = len(nums1)
    diff_count = 0
    equal_count = 0
    
    # Count how many elements are already different and how many are equal
    for i in range(n):
        if nums1[i] != nums2[i]:
            diff_count += 1
        else:
            equal_count += 1
            
    # If all elements are already different, cost is 0
    if equal_count == 0:
        return 0
    
    # If there are unequal elements, we can change each equal pair with cost 1
    # by picking a value that doesn't match the other array at that index.
    # However, if all elements in the arrays are identical (e.g., [1,1] and [1,1]),
    # changing one element to something else might still result in an equality 
    # elsewhere if we aren't careful. 
    # Actually, the constraint is simpler: 
    # If we have at least one pair that is already different, we can always 
    # resolve an equality with cost 1.
    # If ALL pairs are equal, we need cost 1 for (n-1) pairs and cost 2 for the last one.
    
    if diff_count > 0:
        return equal_count
    else:
        # Case where all elements are equal: nums1[i] == nums2[i] for all i.
        # We change n-1 elements with cost 1, and the last one with cost 2.
        return equal_count + 1
