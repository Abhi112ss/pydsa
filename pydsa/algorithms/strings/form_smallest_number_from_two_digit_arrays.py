METADATA = {
    "id": 2605,
    "name": "Form Smallest Number From Two Digit Arrays",
    "slug": "form-smallest-number-from-two-digit-arrays",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Form the smallest possible number by concatenating elements from two arrays using a greedy approach.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Forms the smallest possible number by concatenating elements from two arrays.
    
    The strategy is to sort both arrays and then greedily pick the element 
    from either array that results in a smaller concatenation when appended 
    to the current result.

    Args:
        nums1: A list of integers.
        nums2: A list of integers.

    Returns:
        The smallest integer formed by concatenating elements from both arrays.

    Examples:
        >>> solve([1, 2], [3, 4])
        1234
        >>> solve([4, 1], [3, 2])
        1234
    """
    # Sort both arrays to ensure we consider smaller elements first
    nums1.sort()
    nums2.sort()
    
    result_str = ""
    i, j = 0, 0
    n1, n2 = len(nums1), len(nums2)
    
    # Use a greedy approach to decide which element to pick next
    while i < n1 or j < n2:
        if i < n1 and j < n2:
            # Compare the current element of nums1 with nums2.
            # We compare the string representations to see which one 
            # produces a smaller number when placed first.
            # Note: For single digits, simple comparison works, but 
            # string comparison is robust for multi-digit logic.
            val1 = str(nums1[i])
            val2 = str(nums2[j])
            
            if val1 + val2 < val2 + val1:
                result_str += val1
                i += 1
            else:
                result_str += val2
                j += 1
        elif i < n1:
            # Only nums1 has remaining elements
            result_str += str(nums1[i])
            i += 1
        else:
            # Only nums2 has remaining elements
            result_str += str(nums2[j])
            j += 1
            
    return int(result_str)
