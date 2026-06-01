METADATA = {
    "id": 3245,
    "name": "Alternating Groups III",
    "slug": "alternating_groups_iii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of subarrays of length k that follow an alternating pattern.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays of length k where elements alternate 
    between two values (e.g., [a, b, a, b...]).

    Args:
        nums: A list of integers representing the sequence.
        k: The required length of the alternating subarray.

    Returns:
        The total count of subarrays of length k that satisfy the alternating condition.

    Examples:
        >>> solve([1, 2, 1, 2, 1, 3, 1, 2], 3)
        4
        # Subarrays: [1,2,1], [2,1,2], [1,2,1], [3,1,2] is not alternating, 
        # wait, [1,2,1], [2,1,2], [1,2,1], [3,1,2] -> [1,2,1], [2,1,2], [1,2,1], [3,1,2] is wrong.
        # Let's re-check: [1,2,1], [2,1,2], [1,2,1], [3,1,2] (no), [1,2,1] (yes).
        # Correct logic: [1,2,1], [2,1,2], [1,2,1], [3,1,2] (no), [1,2,1] (no).
        # Actually, for [1,2,1,2,1,3,1,2] k=3:
        # [1,2,1] (Y), [2,1,2] (Y), [1,2,1] (Y), [2,1,3] (N), [1,3,1] (Y), [3,1,2] (N).
        # Total: 4.
    """
    n = len(nums)
    if k > n:
        return 0
    if k == 1:
        return n

    count = 0
    # current_alternating_len tracks how many elements ending at i 
    # satisfy the condition nums[i] != nums[i-1]
    current_alternating_len = 1

    for i in range(1, n):
        # Check if the current element continues the alternating pattern
        if nums[i] != nums[i - 1]:
            current_alternating_len += 1
        else:
            # Pattern broken, reset to 1 (the current element itself)
            current_alternating_len = 1
        
        # If the current alternating sequence is at least k, 
        # it means the subarray ending at i of length k is alternating.
        # However, for "Alternating Groups", the pattern must be a-b-a-b.
        # A sequence of length k is alternating if nums[i] != nums[i-1] 
        # AND nums[i-1] != nums[i-2] ... AND nums[i] == nums[i-2].
        # Wait, the standard definition of alternating in these problems 
        # is usually nums[i] != nums[i-1]. 
        # But "Alternating Groups" specifically implies a-b-a-b.
        # Let's refine: a sequence is alternating if nums[i] != nums[i-1] 
        # AND nums[i] == nums[i-2] for all i >= 2.
        
        # Re-evaluating: The problem asks for a-b-a-b.
        # This is equivalent to: 
        # 1. nums[i] != nums[i-1] for all i in window
        # 2. nums[i] == nums[i-2] for all i in window
        
        # Let's use a different approach: 
        # A window is alternating if for all j in [start+2, end], nums[j] == nums[j-2]
        # AND for all j in [start+1, end], nums[j] != nums[j-1].
        pass

    # Corrected approach for a-b-a-b pattern:
    # A subarray is alternating if:
    # 1. nums[i] != nums[i-1]
    # 2. nums[i] == nums[i-2]
    
    # We can track the length of the "alternating" property.
    # Let 'alt_len' be the length of the suffix ending at i that satisfies 
    # both (nums[i] != nums[i-1]) and (nums[i] == nums[i-2] if i >= 2).
    
    alt_len = 1
    count = 0
    
    # Base case for k=1 is handled. For k >= 2:
    # We start checking from index 1.
    
    # We need to track two things:
    # 1. Is nums[i] != nums[i-1]?
    # 2. Is nums[i] == nums[i-2]?
    
    # Let's use a simpler sliding window:
    # 'valid_len' is the length of the current alternating sequence.
    valid_len = 1
    
    # For i=1, the only condition is nums[1] != nums[0]
    if n > 1:
        if nums[1] != nums[0]:
            valid_len = 2
        else:
            valid_len = 1
            
        if valid_len >= k:
            count += 1

    for i in range(2, n):
        # Condition for alternating: nums[i] != nums[i-1] AND nums[i] == nums[i-2]
        if nums[i] != nums[i-1] and nums[i] == nums[i-2]:
            valid_len += 1
        elif nums[i] != nums[i-1]:
            # It's alternating with the previous, but doesn't match the i-2 pattern.
            # This starts a new alternating sequence of length 2 (e.g., [a, b, c] -> [b, c])
            valid_len = 2
        else:
            # Pattern broken completely (e.g., [a, a])
            valid_len = 1
            
        if valid_len >= k:
            count += 1
            
    # Edge case: if k=1, the loop logic above is slightly different.
    # But the problem usually implies k >= 2 for "alternating".
    # If k=1, every single element is an alternating group.
    if k == 1:
        return n

    return count

# Note: The logic above handles the a-b-a-b pattern.
# If k=2, any [a, b] where a != b is alternating.
# If k=3, [a, b, a] is alternating.
# If k=4, [a, b, a, b] is alternating.
