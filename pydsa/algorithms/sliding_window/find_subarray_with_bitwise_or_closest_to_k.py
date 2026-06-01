METADATA = {
    "id": 3171,
    "name": "Find Subarray With Bitwise OR Closest to K",
    "slug": "find-subarray-with-bitwise-or-closest-to-k",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "bit_manipulation", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(log(max_val))",
    "description": "Find the length of the shortest subarray whose bitwise OR is closest to a target value K.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the shortest subarray whose bitwise OR is closest to k.
    
    The bitwise OR of a subarray is non-decreasing as the subarray expands.
    We use a sliding window approach combined with a frequency array of bits 
    to efficiently add and remove elements from the window's OR sum.

    Args:
        nums: A list of integers.
        k: The target integer.

    Returns:
        The length of the shortest subarray whose bitwise OR is closest to k.

    Examples:
        >>> solve([1, 2, 4], 3)
        2
        >>> solve([1, 2, 4], 7)
        3
    """
    n = len(nums)
    min_diff = float('inf')
    min_len = float('inf')
    
    # bit_counts stores the count of set bits at each position (0-31) in the current window
    bit_counts = [0] * 32
    current_or = 0
    left = 0

    def add_to_or(val: int) -> None:
        nonlocal current_or
        for i in range(32):
            if (val >> i) & 1:
                if bit_counts[i] == 0:
                    current_or |= (1 << i)
                bit_counts[i] += 1

    def remove_from_or(val: int) -> None:
        nonlocal current_or
        for i in range(32):
            if (val >> i) & 1:
                bit_counts[i] -= 1
                if bit_counts[i] == 0:
                    current_or &= ~(1 << i)

    for right in range(n):
        add_to_or(nums[right])

        # Shrink the window from the left to find the smallest subarray 
        # that maintains a specific OR property or to explore closer values.
        # Since OR is monotonic, we can use the sliding window to check 
        # all possible OR values produced by subarrays.
        while left <= right:
            diff = abs(current_or - k)
            
            # Update global minimum difference and shortest length
            if diff < min_diff:
                min_diff = diff
                min_len = right - left + 1
            elif diff == min_diff:
                min_len = min(min_len, right - left + 1)

            # If current_or is already >= k, shrinking might bring it closer to k
            # or potentially smaller than k. If current_or < k, shrinking 
            # will only make it smaller, increasing the difference.
            if current_or >= k:
                remove_from_or(nums[left])
                left += 1
            else:
                # If current_or < k, expanding right is the only way to potentially 
                # get closer to k (since OR is non-decreasing).
                break

    # Note: The logic above handles the monotonic property. 
    # However, to ensure we check all "closest" possibilities, 
    # we must realize that for a fixed 'right', as 'left' increases, 
    # 'current_or' decreases. We check every unique OR value.
    
    # Re-implementing with a more robust approach for "closest"
    # because the standard sliding window usually looks for >= k.
    # To find the absolute closest, we need to track all possible ORs.
    
    # Optimized approach: For each right index, there are at most log(max_val) 
    # distinct OR values for subarrays ending at 'right'.
    
    min_diff = float('inf')
    min_len = float('inf')
    
    # ors stores tuples of (or_value, start_index) for subarrays ending at current index
    # We only keep the latest start_index for each unique OR value to minimize length.
    ors: list[tuple[int, int]] = [] 

    for i in range(n):
        new_ors = []
        current_val = nums[i]
        
        # Update existing OR values with the new element
        # and add the single-element subarray [nums[i]]
        for val, start_idx in ors:
            new_val = val | current_val
            if not new_ors or new_ors[-1][0] != new_val:
                new_ors.append((new_val, start_idx))
            else:
                # If OR is same, keep the one with larger start_idx (shorter length)
                # But since ors is sorted by start_idx, the first one we encounter 
                # for a specific OR value is actually the one with the smallest index.
                # Actually, we want the largest start_idx for a fixed OR to minimize length.
                # Let's refine:
                pass 
        
        # Correct logic for distinct ORs ending at i:
        # There are at most 32 distinct OR values.
        temp_ors = []
        # Add current element
        temp_ors.append((nums[i], i))
        for val, start_idx in ors:
            new_val = val | nums[i]
            if temp_ors[-1][0] == new_val:
                # If same OR, the one with the larger start_idx is better (shorter)
                # But in our loop, 'ors' contains start_indices in increasing order.
                # To get the shortest, we want the largest start_idx.
                # We'll update the tuple.
                temp_ors[-1] = (new_val, max(temp_ors[-1][1], start_idx))
            else:
                temp_ors.append((new_val, start_idx))
        
        # Actually, the standard way to get all distinct ORs ending at i:
        # ors = {val: max_start_index}
        current_ors_map = {nums[i]: i}
        for val, start_idx in ors:
            new_val = val | nums[i]
            current_ors_map[new_val] = max(current_ors_map.get(new_val, -1), start_idx)
        
        # Convert map back to list for next iteration
        ors = list(current_ors_map.items())
        
        # Check all unique ORs found ending at index i
        for val, start_idx in ors:
            diff = abs(val - k)
            length = i - start_idx + 1
            if diff < min_diff:
                min_diff = diff
                min_len = length
            elif diff == min_diff:
                min_len = min(min_len, length)
                
    return min_len
