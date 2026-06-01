METADATA = {
    "id": 3208,
    "name": "Alternating Groups II",
    "slug": "alternating-groups-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of alternating groups of length k in a circular array.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the number of alternating groups of length k in a circular array.
    An alternating group is a subarray where every adjacent pair of elements 
    is different.

    Args:
        nums: A list of integers representing the circular array.
        k: The required length of the alternating group.

    Returns:
        The total count of alternating groups of length k.

    Examples:
        >>> solve([2, 2, 2, 2, 2], 2)
        0
        >>> solve([2, 2, 2, 2, 2], 3)
        0
        >>> solve([1, 2, 1, 2, 1], 3)
        5
    """
    n = len(nums)
    if k > n:
        return 0
    
    # To handle circularity, we conceptually extend the array.
    # However, we only need to check up to n + k - 1 elements to cover all windows.
    # Instead of doubling the array, we use modulo arithmetic.
    
    total_alternating_groups = 0
    current_alternating_length = 1
    
    # We iterate through the array up to n + k - 1 to account for circularity.
    # The loop runs for n + k - 1 iterations to ensure every starting position 
    # is evaluated for a window of size k.
    for i in range(n + k - 1):
        # Compare current element with the previous one (circularly)
        # We start checking from the second element in our virtual extended array
        if i > 0:
            prev_idx = (i - 1) % n
            curr_idx = i % n
            
            if nums[curr_idx] != nums[prev_idx]:
                current_alternating_length += 1
            else:
                current_alternating_length = 1
        
        # If the current alternating sequence is at least k, 
        # it means the window ending at i is a valid alternating group.
        # We only count windows that start within the original array bounds [0, n-1].
        # A window of length k ending at i starts at index (i - k + 1).
        # We must ensure the window's start index is within the first n elements.
        if current_alternating_length >= k:
            # The window ending at i is valid if its start index (i - k + 1) 
            # is less than n.
            if (i - k + 1) < n:
                total_alternating_groups += 1
                
    return total_alternating_groups
