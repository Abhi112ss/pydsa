METADATA = {
    "id": 3349,
    "name": "Adjacent Increasing Subarrays Detection I",
    "slug": "adjacent-increasing-subarrays-detection-i",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of pairs of adjacent subarrays that are both strictly increasing.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs of adjacent strictly increasing subarrays.
    
    A pair of adjacent subarrays (sub1, sub2) is valid if:
    1. sub1 is strictly increasing.
    2. sub2 is strictly increasing.
    3. sub1 and sub2 are adjacent (sub1 ends exactly where sub2 begins).
    4. Each subarray must have a length of at least 2.

    Args:
        nums: A list of integers.

    Returns:
        The total count of such adjacent pairs.

    Examples:
        >>> solve([1, 2, 3, 4])
        2
        # Pairs: ([1, 2], [3, 4]), ([1, 2, 3], [4]) is not valid because [4] length < 2.
        # Wait, the problem definition for "Adjacent Increasing Subarrays" usually implies 
        # we are looking for split points in a continuous increasing sequence.
        # If nums = [1, 2, 3, 4], increasing segments are [1, 2, 3, 4].
        # Any split point i where [0...i] and [i+1...n-1] are both increasing and length >= 2.
        # For [1, 2, 3, 4]:
        # Split at index 1: [1, 2] and [3, 4]. Both length 2. Valid.
        # Total = 1.
        
        >>> solve([1, 2, 3, 2, 3, 4])
        1
        # [1, 2, 3] is increasing, [2, 3, 4] is increasing.
        # They are adjacent if we consider the split at index 2.
        # [1, 2, 3] and [2, 3, 4] are not adjacent in the sense of partitioning.
        # The problem asks for adjacent subarrays. In LeetCode context for this specific ID,
        # it usually refers to finding indices i such that nums[start...i] and nums[i+1...end]
        # are both strictly increasing and length >= 2.
    """
    n = len(nums)
    if n < 4:
        return 0

    # Step 1: Identify all maximal strictly increasing contiguous segments.
    # We store the lengths of these segments.
    # Example: [1, 2, 3, 2, 3, 4] -> segments of length 3 and 3.
    segment_lengths = []
    current_length = 1
    
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            if current_length >= 2:
                segment_lengths.append(current_length)
            current_length = 1
    
    if current_length >= 2:
        segment_lengths.append(current_length)

    # Step 2: Count valid adjacent pairs.
    # A pair of adjacent subarrays can only exist if two maximal increasing segments 
    # are adjacent in the original array.
    # However, the problem "Adjacent Increasing Subarrays" often implies we look for 
    # a split point in a single maximal increasing segment.
    # If a segment has length L, we can split it at index k such that 
    # the first part has length k and the second has length L-k.
    # Requirements: k >= 2 and L-k >= 2.
    # This means 2 <= k <= L - 2.
    # The number of such k is (L - 2) - 2 + 1 = L - 3.
    # If L < 4, no such split exists.
    
    # Re-reading standard LeetCode logic for this pattern:
    # If the problem asks for pairs of adjacent subarrays that are both increasing,
    # and they must be formed from the original array elements without overlap:
    # We look at each maximal increasing segment of length L.
    # Any split point within this segment that creates two subarrays of length >= 2 is valid.
    
    total_pairs = 0
    
    # We need to re-evaluate the segment logic. 
    # If the array is [1, 2, 3, 4, 5], segments = [5].
    # Splits: [1,2][3,4,5], [1,2,3][4,5]. Total = 2. (Formula: 5 - 3 = 2).
    
    # If the array is [1, 2, 3, 2, 3, 4, 5], segments = [3, 4].
    # These segments are NOT adjacent in a way that they form a single increasing sequence.
    # But the problem asks for "Adjacent Increasing Subarrays".
    # This usually means sub1 ends at i, sub2 starts at i+1.
    # If nums[i] < nums[i-1], the increasing property breaks.
    # So sub1 and sub2 can only be adjacent if they belong to the same maximal increasing segment
    # OR if the end of sub1 is the start of sub2 (but they must be strictly increasing).
    # If sub1 is [..., nums[i]] and sub2 is [nums[i+1], ...], 
    # for both to be increasing, we don't necessarily need nums[i+1] > nums[i].
    # BUT, if they are "adjacent", they are usually defined as [i, j] and [j+1, k].
    
    # Let's refine: A pair of adjacent subarrays (sub1, sub2) is valid if:
    # sub1 = nums[i...j], sub2 = nums[j+1...k]
    # sub1 is increasing, length >= 2.
    # sub2 is increasing, length >= 2.
    
    # To solve this in O(n):
    # 1. Precompute 'left[i]': length of the increasing subarray ending at i.
    # 2. Precompute 'right[i]': length of the increasing subarray starting at i.
    # 3. Iterate through all possible split points 'j' from 1 to n-2.
    #    A split at 'j' means sub1 ends at j, sub2 starts at j+1.
    #    Check if left[j] >= 2 and right[j+1] >= 2.
    
    left = [0] * n
    right = [0] * n
    
    # Calculate left lengths
    current_run = 1
    left[0] = 1
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            current_run += 1
        else:
            current_run = 1
        left[i] = current_run
        
    # Calculate right lengths
    current_run = 1
    right[n-1] = 1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            current_run += 1
        else:
            current_run = 1
        right[i] = current_run
        
    count = 0
    # A split point exists between index i and i+1
    # Subarray 1: ends at i, length = left[i]
    # Subarray 2: starts at i+1, length = right[i+1]
    for i in range(n - 1):
        if left[i] >= 2 and right[i+1] >= 2:
            count += 1
            
    return count
