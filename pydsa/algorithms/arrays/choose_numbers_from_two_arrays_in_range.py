METADATA = {
    "id": 2143,
    "name": "Choose Numbers From Two Arrays in Range",
    "slug": "choose-numbers-from-two-arrays-in-range",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "two_pointer", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of elements from two arrays such that all chosen elements fall within a given range [left, right].",
}

def solve(nums1: list[int], nums2: list[int], left: int, right: int) -> int:
    """
    Finds the maximum number of elements from two arrays that fall within [left, right].

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.
        left: The lower bound of the range (inclusive).
        right: The upper bound of the range (inclusive).

    Returns:
        The maximum count of elements from both arrays that are within the range.

    Examples:
        >>> solve([1, 2, 3], [4, 5, 6], 2, 5)
        4
        >>> solve([1, 1, 1], [1, 1, 1], 1, 1)
        6
    """
    # Filter elements from both arrays that fall within the [left, right] range
    # We only care about elements that satisfy the condition.
    valid_nums1 = [x for x in nums1 if left <= x <= right]
    valid_nums2 = [x for x in nums2 if left <= x <= right]

    # If no elements are within range, return 0
    if not valid_nums1 and not valid_nums2:
        return 0

    # Sort the filtered lists to allow for a sliding window/two-pointer approach
    # However, the problem asks for the maximum count of elements from BOTH arrays
    # that fall in the range. Since the range is fixed [left, right], we simply
    # count how many elements in nums1 are in range and how many in nums2 are in range.
    # Wait, the problem description for 2143 is actually: 
    # "You are given two arrays nums1 and nums2 and two integers left and right.
    # You can choose any number of elements from nums1 and nums2 such that 
    # all chosen elements are in the range [left, right]. 
    # Return the maximum number of elements you can choose."
    
    # Re-reading the logic: The constraint is simply that every chosen element 
    # must be >= left and <= right. There is no constraint on the difference 
    # between the elements themselves (unlike some other problems).
    
    # Therefore, the optimal strategy is to pick ALL elements from both arrays
    # that satisfy the condition.
    
    count = 0
    for num in valid_nums1:
        count += 1
    for num in valid_nums2:
        count += 1
        
    return count

# Note: The prompt's "Key insight" mentioned sorting and two-pointer, 
# which usually applies to problems like "find max elements in a range [x, x+k]".
# But for LeetCode 2143 specifically, the range [left, right] is fixed.
# If the problem meant "find a range [x, x+k] that maximizes elements", 
# that would be a different problem. 
# For 2143, the range is provided as input.

def solve_optimized(nums1: list[int], nums2: list[int], left: int, right: int) -> int:
    """
    An optimized version of the solve function.
    
    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.
        left: The lower bound of the range (inclusive).
        right: The upper bound of the range (inclusive).

    Returns:
        The maximum number of elements from both arrays that are within the range.
    """
    count = 0
    
    # Iterate through the first array and count elements in range
    for num in nums1:
        if left <= num <= right:
            count += 1
            
    # Iterate through the second array and count elements in range
    for num in nums2:
        if left <= num <= right:
            count += 1
            
    return count

# Assigning the optimized version to solve
solve = solve_optimized