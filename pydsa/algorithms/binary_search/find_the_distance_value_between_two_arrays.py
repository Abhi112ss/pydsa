METADATA = {
    "id": 1385,
    "name": "Find the Distance Value Between Two Arrays",
    "slug": "find-the-distance-value-between-two-arrays",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(m log m + n log m)",
    "space_complexity": "O(1)",
    "description": "Find the count of elements in the first array such that no element in the second array falls within a specific distance range.",
}

import bisect

def solve(arr1: list[int], arr2: list[int], d: int) -> int:
    """
    Calculates the distance value between two arrays.
    
    The distance value is the number of elements in arr1 such that there is no 
    element in arr2 with an absolute difference less than or equal to d.

    Args:
        arr1: The first list of integers.
        arr2: The second list of integers.
        d: The maximum allowed absolute difference.

    Returns:
        The count of elements in arr1 that satisfy the condition.

    Examples:
        >>> solve([4, 5, 8], [10, 9, 1, 8], 2)
        2
        >>> solve([1, 4, 25], [10, 9, 1, 8], 2)
        1
    """
    # Sort the second array to enable binary search
    arr2.sort()
    distance_value_count = 0

    for value in arr1:
        # We need to check if any element in arr2 is in the range [value - d, value + d]
        # Using bisect_left to find the first index where an element is >= value - d
        lower_bound = value - d
        upper_bound = value + d
        
        idx = bisect.bisect_left(arr2, lower_bound)
        
        # If idx is within bounds and the element at idx is <= upper_bound,
        # then an element exists in the forbidden range [value - d, value + d]
        if idx < len(arr2) and arr2[idx] <= upper_bound:
            continue
        else:
            distance_value_count += 1

    return distance_value_count
