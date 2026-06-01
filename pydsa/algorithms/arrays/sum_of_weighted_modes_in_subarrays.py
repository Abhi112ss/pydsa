METADATA = {
    "id": 3672,
    "name": "Sum of Weighted Modes in Subarrays",
    "slug": "sum_of_weighted_modes_in_subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "subarray"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of the weighted modes for all possible subarrays of a given array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of weighted modes for all subarrays.
    
    A mode is the element that appears most frequently in a subarray. 
    If there are multiple modes, the one with the smallest value is chosen.
    The weight of a mode is defined as (frequency * value).

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The total sum of the weighted modes of all subarrays.

    Examples:
        >>> solve([1, 2, 2])
        # Subarrays:
        # [1] -> mode 1, freq 1, weight 1*1 = 1
        # [2] -> mode 2, freq 1, weight 1*2 = 2
        # [2] -> mode 2, freq 1, weight 1*2 = 2
        # [1, 2] -> mode 1, freq 1, weight 1*1 = 1 (smallest value tie-break)
        # [2, 2] -> mode 2, freq 2, weight 2*2 = 4
        # [1, 2, 2] -> mode 2, freq 2, weight 2*2 = 4
        # Total: 1 + 2 + 2 + 1 + 4 + 4 = 14
        14
    """
    n = len(nums)
    total_weighted_sum = 0

    # Iterate through every possible starting index of a subarray
    for start in range(n):
        frequencies = {}
        max_freq = 0
        # current_mode tracks the value with max frequency (with tie-break logic)
        current_mode = float('inf')

        # Expand the subarray from 'start' to the end of the array
        for end in range(start, n):
            val = nums[end]
            frequencies[val] = frequencies.get(val, 0) + 1
            freq = frequencies[val]

            # Update the mode if:
            # 1. We found a new higher frequency
            # 2. We found the same frequency but the value is smaller (tie-break)
            if freq > max_freq:
                max_freq = freq
                current_mode = val
            elif freq == max_freq:
                if val < current_mode:
                    current_mode = val
            
            # Note: If the current_mode's frequency was already max_freq, 
            # but the new element 'val' is NOT the new mode, we don't update.
            # However, we must ensure that if the current_mode's frequency 
            # is no longer the max_freq (which is impossible in this expansion), 
            # we would update. Since freq only increases, we only check the new val.
            
            # Re-check tie-break for the existing mode if the new element 
            # didn't become the mode but might have matched the frequency.
            # Actually, the logic above handles it: if freq == max_freq, 
            # we check if val is smaller. If freq > max_freq, it's the new mode.
            
            # There is a edge case: if the current_mode's frequency is max_freq,
            # and the new element 'val' reaches max_freq, we check if val < current_mode.
            # But what if the current_mode is no longer the mode? 
            # In an expansion, max_freq only increases or stays same.
            # If max_freq stays same, the only way the mode changes is if 
            # the new element 'val' reaches that same max_freq and is smaller.
            
            # Correcting logic: The mode can only change if the new element 
            # becomes the new mode (higher freq) or ties the current max freq 
            # with a smaller value.
            
            total_weighted_sum += (max_freq * current_mode)

    return total_weighted_sum
