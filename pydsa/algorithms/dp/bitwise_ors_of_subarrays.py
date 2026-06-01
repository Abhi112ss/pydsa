METADATA = {
    "id": 898,
    "name": "Bitwise ORs of Subarrays",
    "slug": "bitwise_ors_of_subarrays",
    "category": "Bitwise",
    "aliases": [],
    "tags": ["hash_set", "bitwise", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(N * log(max(arr)))",
    "space_complexity": "O(N * log(max(arr)))",
    "description": "Find the number of unique bitwise OR values that can be obtained from all possible non-empty subarrays.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the number of unique bitwise OR results from all possible subarrays.

    The algorithm uses the property that for a fixed ending index, the number of 
    distinct bitwise OR values of subarrays ending at that index is at most 
    the number of bits in the maximum element (log2(max_val)). This is because 
    as we extend a subarray to the left, the OR value can only increase by 
    setting new bits.

    Args:
        arr: A list of non-negative integers.

    Returns:
        The count of unique bitwise OR values found across all subarrays.

    Examples:
        >>> solve([1, 1, 2])
        3
        >>> solve([1, 2, 4])
        6
    """
    if not arr:
        return 0

    # all_unique_ors stores every unique OR value encountered so far
    all_unique_ors = set()
    
    # current_ors stores unique OR values of subarrays ending at the previous index
    current_ors = set()

    for x in arr:
        # next_ors will store unique OR values of subarrays ending at the current index
        # We start with the element itself (subarray of length 1)
        next_ors = {x}
        
        # For every OR value ending at the previous index, OR it with the current element
        # to get the OR values of subarrays ending at the current index
        for prev_or in current_ors:
            next_ors.add(prev_or | x)
        
        # Update the global set with the new values found at this index
        all_unique_ors.update(next_ors)
        
        # Move to the next index
        current_ors = next_ors

    return len(all_unique_ors)
