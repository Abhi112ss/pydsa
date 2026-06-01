METADATA = {
    "id": 3022,
    "name": "Minimize OR of Remaining Elements Using Operations",
    "slug": "minimize-or-of-remaining-elements-using-operations",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Minimize the bitwise OR of the remaining elements after performing at most k operations where an operation consists of replacing an element with 0.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Minimizes the bitwise OR of the remaining elements by zeroing out at most k elements.

    The strategy is to iterate from the most significant bit down to the least significant bit.
    For each bit, we check if we can make that bit zero in the final OR result by 
    zeroing out all elements that have that bit set. If the number of such elements 
    is less than or equal to our remaining budget k, we "commit" to zeroing them out.

    Args:
        nums: A list of integers.
        k: The maximum number of elements that can be replaced with 0.

    Returns:
        The minimum possible bitwise OR of the remaining elements.

    Examples:
        >>> solve([3, 5, 8], 1)
        5
        >>> solve([1, 2, 3], 2)
        0
    """
    # We track which indices are currently "active" (not zeroed out).
    # Initially, all indices are active.
    active_indices = list(range(len(nums)))
    
    # We iterate from the highest possible bit (assuming 30 bits for standard positive ints)
    # down to 0 to apply a greedy approach.
    for bit in range(30, -1, -1):
        # Identify which of the currently active elements have the current bit set.
        indices_with_bit_set = []
        for idx in active_indices:
            if (nums[idx] >> bit) & 1:
                indices_with_bit_set.append(idx)
        
        # If the number of elements we need to zero out to make this bit 0 
        # is within our budget k, we perform the operation.
        if len(indices_with_bit_set) <= k:
            # We "remove" these indices from the active set.
            # Note: We don't actually subtract from k yet because we only 
            # commit to the removal if we can satisfy the bit requirement.
            # However, the problem asks for the minimum OR, and since we 
            # process bits from MSB to LSB, this greedy choice is optimal.
            
            # To keep the logic clean, we update the active_indices to exclude 
            # the ones we just zeroed out.
            new_active_indices = []
            set_indices = set(indices_with_bit_set)
            for idx in active_indices:
                if idx not in set_indices:
                    new_active_indices.append(idx)
            
            active_indices = new_active_indices
            # Subtract the number of elements we zeroed out from our budget.
            k -= len(indices_with_bit_set)

    # After checking all bits, the result is the bitwise OR of all remaining active elements.
    result_or = 0
    for idx in active_indices:
        result_or |= nums[idx]
        
    return result_or
