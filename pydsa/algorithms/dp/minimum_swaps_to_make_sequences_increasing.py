METADATA = {
    "id": 801,
    "name": "Minimum Swaps To Make Sequences Increasing",
    "slug": "minimum-swaps-to-make-sequences-increasing",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "state_machine", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps to make two integer sequences strictly increasing.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum number of swaps required to make both nums1 and nums2 strictly increasing.

    Args:
        nums1: A list of strictly increasing integers.
        nums2: A list of strictly increasing integers.

    Returns:
        The minimum number of swaps needed.

    Examples:
        >>> solve([1, 3, 5], [1, 2, 4])
        0
        >>> solve([1, 3, 5], [2, 1, 4])
        1
    """
    n = len(nums1)
    
    # keep[i] is the min swaps for prefix up to i, where we do NOT swap at index i.
    # swap[i] is the min swaps for prefix up to i, where we DO swap at index i.
    # We only need the previous state, so we use O(1) space.
    keep = 0
    swap = 1
    
    for i in range(1, n):
        # Case 1: The sequences are already increasing without swapping at current index
        # (nums1[i-1] < nums1[i] AND nums2[i-1] < nums2[i])
        is_natural_order = nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]
        
        # Case 2: The sequences become increasing if we swap at BOTH i and i-1
        # (nums1[i-1] < nums1[i] after swap, which means nums1[i] < nums1[i-1] is false, 
        # but we check the cross-relationship: nums2[i-1] < nums1[i] and nums1[i-1] < nums2[i])
        # Actually, the condition for "swapping both" is:
        # nums1[i-1] < nums1[i] is NOT required if we swap both, 
        # but the cross condition must hold: nums2[i-1] < nums1[i] and nums1[i-1] < nums2[i]
        # Wait, the standard logic: if we swap both, the relative order of elements 
        # at i-1 and i is flipped. So we check if nums1[i-1] < nums1[i] is false 
        # but the cross-elements satisfy the order.
        is_swapped_order = nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i] # This is wrong logic, let's refine.
        
        # Correct logic for DP transitions:
        # Let's re-evaluate the conditions:
        # Condition A: nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]
        # Condition B: nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]
        
        # If Condition A is true:
        #   - If we don't swap at i: we could have either swapped or not swapped at i-1.
        #     keep_new = min(keep_old, swap_old) -> No, if we don't swap at i, 
        #     and A is true, we can keep the state of i-1.
        #     If we didn't swap at i-1, we don't swap at i.
        #     If we did swap at i-1, we don't swap at i.
        #   - If we swap at i: we MUST have swapped at i-1 to maintain order.
        
        # Let's use the standard robust logic:
        # can_keep_without_swap: nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]
        # can_keep_with_swap: nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]
        
        can_keep_without_swap = nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]
        can_keep_with_swap = nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]
        
        new_keep = float('inf')
        new_swap = float('inf')
        
        if can_keep_without_swap:
            # If we don't swap at i, and the natural order holds:
            # 1. We could have not swapped at i-1 (keep)
            # 2. We could have swapped at i-1 (swap)
            new_keep = keep
            
        if can_keep_with_swap:
            # If we swap at i, and the cross order holds:
            # 1. We could have not swapped at i-1 (but now we must swap at i, so swap_old + 1)
            #    Wait, if we swap at i, and we didn't swap at i-1, we need the cross condition.
            #    If we swap at i, and we DID swap at i-1, we need the natural condition.
            # Let's re-map:
            # If we swap at i:
            #    If we didn't swap at i-1, we need cross condition (nums1[i-1] < nums2[i]...)
            #    If we did swap at i-1, we need natural condition (nums1[i-1] < nums1[i]...)
            # This is getting confusing. Let's use the standard two-case logic:
            pass

        # Standard DP approach for this problem:
        # If natural order holds:
        #    new_keep = keep
        #    new_swap = swap + 1
        # If cross order holds:
        #    new_keep = min(new_keep, swap)
        #    new_swap = min(new_swap, keep + 1)
        
        # Let's reset and implement the clean version:
        break

    # Re-implementing cleanly
    keep = 0
    swap = 1
    for i in range(1, n):
        # Condition 1: Natural order (nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i])
        # Condition 2: Swapped order (nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i])
        
        # We use temporary variables to store the previous state
        prev_keep = keep
        prev_swap = swap
        
        # Initialize with infinity to handle cases where conditions aren't met
        keep = float('inf')
        swap = float('inf')
        
        # If natural order holds, we can stay in 'keep' state from prev_keep
        # or we can transition to 'swap' state from prev_swap (swapping both i and i-1)
        if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
            keep = prev_keep
            # If we swap at i, we must have swapped at i-1 to maintain order
            # because the natural order is what allows the swap-swap transition
            # Actually, if natural order holds, swapping at i requires swapping at i-1
            # to keep the sequence increasing.
            swap = prev_swap + 1
            
        # If cross order holds, we can transition from prev_swap to keep
        # or from prev_keep to swap
        if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
            # If we don't swap at i, we must have swapped at i-1
            keep = min(keep, prev_swap)
            # If we swap at i, we must have not swapped at i-1
            swap = min(swap, prev_keep + 1)
            
    return int(min(keep, swap))

# The logic above has a slight overlap. Let's refine the logic to be 100% correct.
# If natural order holds:
#    new_keep = prev_keep
#    new_swap = prev_swap + 1
# If cross order holds:
#    new_keep = min(new_keep, prev_swap)
#    new_swap = min(new_swap, prev_keep + 1)
# Note: If BOTH hold, we take the minimums.

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum number of swaps required to make both nums1 and nums2 strictly increasing.

    Args:
        nums1: A list of strictly increasing integers.
        nums2: A list of strictly increasing integers.

    Returns:
        The minimum number of swaps needed.
    """
    n = len(nums1)
    keep = 0
    swap = 1
    
    for i in range(1, n):
        # prev_keep/swap represent the min swaps for the prefix ending at i-1
        prev_keep = keep
        prev_swap = swap
        
        # Initialize current states
        keep = float('inf')
        swap = float('inf')
        
        # Case 1: The elements are already in increasing order relative to each other
        if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
            # If we don't swap at i, we don't necessarily need to have swapped at i-1
            keep = prev_keep
            # If we swap at i, we must have swapped at i-1 to maintain the sequence
            swap = prev_swap + 1
            
        # Case 2: The elements are in increasing order only if we swap at i (or i-1)
        # This is the "cross" condition.
        if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
            # If we don't swap at i, we must have swapped at i-1
            keep = min(keep, prev_swap)
            # If we swap at i, we must have not swapped at i-1
            swap = min(swap, prev_keep + 1)
            
    return int(min(keep, swap))
