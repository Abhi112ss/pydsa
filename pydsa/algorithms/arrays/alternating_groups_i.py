METADATA = {
    "id": 3206,
    "name": "Alternating Groups I",
    "slug": "alternating_groups_i",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array", "circular"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of circular subarrays of length k where elements alternate between two values.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of circular subarrays of length k that consist of 
    alternating elements.

    Args:
        nums: A list of integers representing the circular array.
        k: The length of the subarray to check.

    Returns:
        The total count of alternating subarrays of length k.

    Examples:
        >>> solve([1, 2, 1, 2, 1], 3)
        3
        >>> solve([1, 2, 1, 2, 3], 3)
        2
    """
    n = len(nums)
    if k > n:
        return 0

    # To handle the circular nature, we can conceptually extend the array.
    # However, we only need to check up to n + k - 2 elements to cover all windows.
    # Instead of creating a new array, we use modulo arithmetic.
    
    # current_alternating_len tracks how many elements ending at the current index
    # follow the alternating pattern (nums[i] != nums[i-1]).
    current_alternating_len = 1
    total_alternating_groups = 0

    # We iterate through the array once. To handle circularity, we iterate up to n + k - 1.
    # The window starts at index 0 and ends at index n + k - 2.
    for i in range(1, n + k - 1):
        # Use modulo to simulate the circular array
        prev_idx = (i - 1) % n
        curr_idx = i % n
        
        if nums[curr_idx] != nums[prev_idx]:
            current_alternating_len += 1
        else:
            current_alternating_len = 1
            
        # If the current alternating sequence is at least k long, 
        # it means the window ending at i is a valid alternating group.
        # We only count windows that start within the original array bounds [0, n-1].
        # A window ending at i covers indices [i-k+1, i]. 
        # The window is valid if its starting index (i-k+1) is within the first n elements.
        if current_alternating_len >= k:
            # We must ensure we don't count the same window multiple times 
            # if the loop goes beyond the original array length.
            # The loop range (n + k - 1) ensures we check all possible starting positions.
            if i < n + k - 1:
                # To avoid double counting in a circular array, we only count 
                # windows whose starting index is in [0, n-1].
                # The window starting at index 'start' ends at 'start + k - 1'.
                # We check if the window ending at 'i' is a unique window.
                # A window is unique if its start index (i - k + 1) is < n.
                if (i - k + 1) < n:
                    total_alternating_groups += 1

    # The logic above can be simplified: 
    # A window of length k is alternating if all k-1 adjacent pairs are different.
    # Let's re-implement with a cleaner sliding window approach.
    
    return _solve_clean(nums, k)

def _solve_clean(nums: list[int], k: int) -> int:
    """
    A cleaner implementation of the sliding window for circular alternating groups.
    """
    n = len(nums)
    # count_diff tracks how many adjacent pairs (i, i+1) are different
    # in the current window of size k.
    count_diff = 0
    
    # Initialize the first window of size k
    for i in range(k - 1):
        if nums[i] != nums[i + 1]:
            count_diff += 1
            
    total_groups = 0
    # If all k-1 pairs in the first window are different, it's an alternating group
    if count_diff == k - 1:
        total_groups += 1
        
    # Slide the window across the circular array
    # There are n total possible windows of length k in a circular array of size n.
    # The first window starts at 0, the last window starts at n-1.
    for start in range(1, n):
        # Remove the effect of the pair that is leaving the window
        # The pair leaving is (start-1, start)
        if nums[start - 1] != nums[start % n]:
            count_diff -= 1
            
        # Add the effect of the new pair entering the window
        # The new pair is (start + k - 2, start + k - 1)
        # Using modulo for circularity
        idx_prev = (start + k - 2) % n
        idx_curr = (start + k - 1) % n
        if nums[idx_prev] != nums[idx_curr]:
            count_diff += 1
            
        if count_diff == k - 1:
            total_groups += 1
            
    return total_groups

# Re-assigning solve to the clean version for the final output
solve = _solve_clean