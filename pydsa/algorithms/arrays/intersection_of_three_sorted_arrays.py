METADATA = {
    "id": 1213,
    "name": "Intersection of Three Sorted Arrays",
    "slug": "intersection-of-three-sorted-arrays",
    "category": "Arrays",
    "aliases": [],
    "tags": ["three_pointers", "arrays", "sorted_arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the intersection of three sorted arrays using a three-pointer approach.",
}

def solve(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    """
    Finds the common elements present in all three sorted arrays.

    Args:
        arr1: The first sorted list of integers.
        arr2: The second sorted list of integers.
        arr3: The third sorted list of integers.

    Returns:
        A list of integers that are present in all three input arrays, 
        maintaining sorted order.

    Examples:
        >>> solve([1, 2, 3], [2, 3, 4], [3, 4, 5])
        [3]
        >>> solve([1, 1, 2], [1, 2, 2], [1, 2, 3])
        [1, 2]
    """
    intersection = []
    i, j, k = 0, 0, 0
    
    # Iterate until we reach the end of any one of the arrays
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If all three elements are equal, we found an intersection point
        if arr1[i] == arr2[j] == arr3[k]:
            intersection.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # Otherwise, increment the pointer pointing to the smallest value
        # to try and "catch up" to the larger values.
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            # This covers the case where arr3[k] is the smallest 
            # or arr1[i] and arr2[j] are both larger than arr3[k]
            k += 1
            
    return intersection
