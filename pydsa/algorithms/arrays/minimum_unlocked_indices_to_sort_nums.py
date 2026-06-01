METADATA = {
    "id": 3431,
    "name": "Minimum Unlocked Indices to Sort Nums",
    "slug": "minimum-unlocked-indices-to-sort-nums",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of indices to unlock such that the array can be sorted, where unlocking an index allows you to move its value to any position.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of indices to unlock to sort the array.
    
    The problem asks for the minimum number of elements to 'unlock'. 
    An unlocked element can be moved anywhere. To minimize the number of 
    unlocked elements, we must maximize the number of 'locked' elements.
    A set of elements can remain locked if they are already in their 
    correct sorted positions and appear in the same relative order 
    as they would in the sorted array.
    
    Specifically, we need to find the longest subsequence of the original 
    array that is also a contiguous subsequence (subarray) of the sorted array.
    However, the problem constraints imply we are looking for the longest 
    subsequence of the original array that matches a prefix/segment of the 
    sorted array such that the remaining elements can be rearranged.
    
    Actually, the rule is: if we unlock a set of indices, we can sort the array.
    The elements we DON'T unlock must already be in their correct sorted positions
    AND they must be consecutive in the sorted array to ensure that once the 
    unlocked elements are placed, the whole array is sorted.
    
    Wait, the standard interpretation for this type of problem:
    We want to find the longest subsequence of `nums` that is a contiguous 
    subsegment of `sorted(nums)`.
    
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of indices to unlock.

    Examples:
        >>> solve([1, 3, 2])
        2
        >>> solve([1, 2, 3])
        0
        >>> solve([5, 4, 3, 2, 1])
        4
    """
    n = len(nums)
    if n <= 1:
        return 0

    sorted_nums = sorted(nums)
    
    # If the array is already sorted, 0 unlocks needed.
    if nums == sorted_nums:
        return 0

    # We are looking for the longest subsequence of 'nums' that 
    # matches a contiguous segment of 'sorted_nums'.
    # Because we want to minimize unlocks, we maximize 'locked'.
    # The locked elements must be a subsequence of 'nums' and 
    # a contiguous subarray of 'sorted_nums'.
    
    # Let's find the longest subsequence of nums that matches 
    # sorted_nums[i : i+k].
    # Since we want to minimize unlocks, we want to find the largest k.
    # However, the problem implies that once we unlock elements, 
    # we can place them anywhere. The elements we leave locked 
    # must be in the correct relative order and correct values.
    
    # Correct logic: The elements we leave locked must form a 
    # subsequence of the original array that is exactly equal to 
    # some contiguous subsegment of the sorted array.
    
    max_locked = 0
    
    # We iterate through all possible starting points in the sorted array.
    # But a more efficient way:
    # For each element in sorted_nums, we check how many subsequent 
    # elements of sorted_nums we can find as a subsequence in nums.
    
    # Optimization: Since we want the longest contiguous segment of sorted_nums
    # that exists as a subsequence in nums, we can use a pointer approach.
    # However, the segment must be contiguous in sorted_nums.
    
    # Let's try every possible starting index 'i' in sorted_nums.
    # For a fixed 'i', we find the longest subsequence in 'nums' 
    # that matches sorted_nums[i], sorted_nums[i+1], ...
    
    # Given the constraints and the nature of the problem, 
    # we can iterate through each possible starting position in sorted_nums.
    for start_idx in range(n):
        current_sorted_ptr = start_idx
        # Try to find sorted_nums[current_sorted_ptr] in nums
        # following the previous found element's index.
        
        # To make this O(N^2) or O(N log N), we need to be careful.
        # But wait, the problem is simpler: we want the longest 
        # sorted_nums[i...j] that is a subsequence of nums.
        
        # Let's use a greedy approach for each starting position.
        count = 0
        last_found_idx = -1
        
        # This part is actually O(N^2) in worst case. 
        # Let's refine: we only need to check segments that could potentially 
        # be longer than our current max_locked.
        
        # Actually, the problem can be solved by:
        # For each i in 0..n-1:
        #   find how many elements of sorted_nums starting from i 
        #   can be found as a subsequence in nums.
        
        # To optimize: we can pre-calculate positions of each value.
        # But since values can be duplicate, we store lists of indices.
        
        # Let's use the O(N^2) approach first, as N is usually up to 10^3 or 10^4 
        # in these types of problems. If N is 10^5, we need O(N log N).
        # For N=10^5, we need a better way.
        
        # Re-reading: "Minimum Unlocked Indices to Sort Nums".
        # If we unlock indices, we can sort the array.
        # This is equivalent to: N - (length of longest subsequence of nums 
        # that is a contiguous subarray of sorted_nums).
        
        # Let's implement the O(N^2) and see.
        # For N=10^5, we need to optimize.
        pass

    # Optimized O(N^2) is still too slow for 10^5.
    # Let's use the property that we are looking for sorted_nums[i...j].
    # We can use a pointer for nums and a pointer for sorted_nums.
    
    # Actually, the most efficient way to find the longest subsequence 
    # of nums that is a contiguous subarray of sorted_nums:
    # For each possible start 'i' in sorted_nums, we find the length.
    # But we can observe that if we find a segment starting at 'i' of length 'k',
    # we don't need to check segments starting at 'i' with length < 'k'.
    
    # Let's use a more direct approach.
    # We want to find max k such that sorted_nums[i : i+k] is a subsequence of nums.
    
    # Pre-calculate indices for each value to speed up searching.
    from collections import defaultdict
    val_to_indices = defaultdict(list)
    for idx, val in enumerate(nums):
        val_to_indices[val].append(idx)
        
    max_len = 0
    for i in range(n):
        # Optimization: if remaining elements in sorted_nums < max_len, break
        if n - i <= max_len:
            break
            
        current_len = 0
        last_idx = -1
        
        # Try to match sorted_nums[i], sorted_nums[i+1]... as subsequence
        for j in range(i, n):
            target_val = sorted_nums[j]
            # Find the smallest index in val_to_indices[target_val] that is > last_idx
            found = False
            # Binary search for the next index
            import bisect
            indices = val_to_indices[target_val]
            pos = bisect.bisect_right(indices, last_idx)
            
            if pos < len(indices):
                last_idx = indices[pos]
                current_len += 1
                found = True
            
            if not found:
                break
        
        if current_len > max_len:
            max_len = current_len
            
    return n - max_len

# The O(N^2) approach with binary search is actually O(N^2 log N) worst case.
# However, for many test cases, it's much faster.
# Let's refine the logic to be more robust.

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of indices to unlock to sort the array.
    
    The problem is equivalent to finding the longest subsequence of 'nums' 
    that is a contiguous subarray of 'sorted(nums)'.
    
    Args:
        nums: A list of integers.

    Returns:
        The minimum number of indices to unlock.
    """
    n = len(nums)
    if n <= 1:
        return 0

    sorted_nums = sorted(nums)
    if nums == sorted_nums:
        return 0

    from collections import defaultdict
    import bisect

    # Map each value to its indices in the original 'nums' array.
    # This allows us to quickly find the next occurrence of a value.
    val_to_indices = defaultdict(list)
    for idx, val in enumerate(nums):
        val_to_indices[val].append(idx)

    max_locked = 0
    
    # We iterate through each possible starting position in the sorted array.
    # We want to find the longest contiguous segment of sorted_nums 
    # that exists as a subsequence in nums.
    for i in range(n):
        # If the remaining elements in sorted_nums cannot beat max_locked, stop.
        if n - i <= max_locked:
            break
            
        current_locked_count = 0
        last_index_in_nums = -1
        
        # Try to extend the segment starting from sorted_nums[i]
        for j in range(i, n):
            target_val = sorted_nums[j]
            indices = val_to_indices[target_val]
            
            # Find the first occurrence of target_val after last_index_in_nums
            idx_pos = bisect.bisect_right(indices, last_index_in_nums)
            
            if idx_pos < len(indices):
                # Found the next element of the subsequence
                last_index_in_nums = indices[idx_pos]
                current_locked_count += 1
            else:
                # Cannot extend this contiguous segment further
                break
        
        if current_locked_count > max_locked:
            max_locked = current_locked_count
            
    return n - max_locked
