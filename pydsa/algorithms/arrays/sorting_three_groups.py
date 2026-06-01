METADATA = {
    "id": 2826,
    "name": "Sorting Three Groups",
    "slug": "sorting-three-groups",
    "category": "Sorting",
    "aliases": [],
    "tags": ["two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Partition an array into three distinct groups based on specific values using a single pass.",
}

def solve(nums: list[int], group1: int, group2: int, group3: int) -> list[int]:
    """
    Partitions the input array into three groups based on the provided values.
    
    The algorithm uses the Dutch National Flag approach to sort the array 
    in-place (or returning a new list) such that all elements equal to group1 
    come first, followed by group2, and finally group3.

    Args:
        nums: The list of integers to be partitioned.
        group1: The value representing the first group.
        group2: The value representing the second group.
        group3: The value representing the third group.

    Returns:
        A list of integers where elements are grouped by their values.

    Examples:
        >>> solve([2, 1, 3, 2, 1, 3], 1, 2, 3)
        [1, 1, 2, 2, 3, 3]
        >>> solve([3, 3, 1, 2, 1], 1, 2, 3)
        [1, 1, 2, 3, 3]
    """
    # Work on a copy to avoid mutating the input if that's the expected behavior,
    # though the algorithm itself is in-place.
    arr = list(nums)
    
    # Pointers for the Dutch National Flag algorithm:
    # low: boundary for group1 (elements < low are group1)
    # mid: current element being inspected
    # high: boundary for group3 (elements > high are group3)
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == group1:
            # Swap current element with the low pointer to move group1 to the front
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == group2:
            # Group2 is already in the "middle" relative to group1 and group3
            mid += 1
        elif arr[mid] == group3:
            # Swap current element with the high pointer to move group3 to the back
            # We do not increment mid here because the swapped element from 'high' 
            # needs to be inspected in the next iteration.
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            # This case handles values that don't belong to any of the three groups
            # if the problem constraints allow for other values.
            mid += 1
            
    return arr
