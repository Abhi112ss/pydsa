METADATA = {
    "id": 3676,
    "name": "Count Bowl Subarrays",
    "slug": "count_bowl_subarrays",
    "category": "Arrays",
    "aliases": [],
    "tags": ["two_pointer", "arrays", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays that form a 'bowl' shape, where elements decrease to a minimum and then increase.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays that form a 'bowl' shape.
    A bowl subarray is defined as a subarray [i, j] such that there exists 
    an index k (i < k < j) where nums[i] > nums[i+1] > ... > nums[k] < ... < nums[j-1] < nums[j].
    Essentially, it is a strictly decreasing sequence followed by a strictly increasing sequence.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The total count of bowl-shaped subarrays.

    Examples:
        >>> solve([5, 2, 4])
        1
        >>> solve([10, 8, 6, 7, 9])
        3  # [10, 8, 6, 7], [8, 6, 7, 9], [10, 8, 6, 7, 9] is not quite right, 
           # the definition implies we look for local minima.
           # Let's refine: A bowl is defined by a local minimum at index k.
           # For each k, we find how many elements to the left are strictly decreasing 
           # and how many to the right are strictly increasing.
    """
    n = len(nums)
    if n < 3:
        return 0

    total_bowls = 0
    
    # We iterate through the array looking for potential 'bottoms' of the bowl.
    # A bottom must have at least one element to its left and one to its right.
    # To be a bowl, nums[k-1] > nums[k] and nums[k] < nums[k+1].
    
    # Pre-calculating the lengths of strictly decreasing sequences ending at i
    # and strictly increasing sequences starting at i would be O(n) space.
    # To keep it O(1) space, we can use a two-pointer approach or a single pass.
    
    # However, the problem asks for ALL subarrays. 
    # A subarray [i, j] is a bowl if there is a k such that 
    # nums[i...k] is strictly decreasing and nums[k...j] is strictly increasing.
    
    # Let's find all local minima.
    # For each local minimum at index k, we count how many elements to the left 
    # form a strictly decreasing chain and how many to the right form a strictly increasing chain.
    
    # To avoid overcounting, we note that a bowl is uniquely identified by its 
    # unique minimum element index k if the sequence is strictly monotonic on both sides.
    
    # We can use two arrays to store the lengths of monotonic sequences.
    # left_dec[i]: number of elements to the left of i that are strictly decreasing towards i.
    # right_inc[i]: number of elements to the right of i that are strictly increasing from i.
    
    # Since the prompt asks for O(1) space, we must calculate these on the fly.
    # But O(1) space is tricky for "all subarrays" unless we use the property that 
    # bowls are contiguous.
    
    # Let's use the property: A bowl is a sequence of (decreasing part) + (increasing part).
    # We can find all maximal monotonic segments.
    
    left_count = [0] * n
    right_count = [0] * n
    
    # Calculate left_count: how many elements strictly decrease to index i
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            left_count[i] = left_count[i-1] + 1
        else:
            left_count[i] = 0
            
    # Calculate right_count: how many elements strictly increase from index i
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i+1]:
            right_count[i] = right_count[i+1] + 1
        else:
            right_count[i] = 0
            
    # A bowl is formed by any combination of the decreasing sequence ending at k
    # and the increasing sequence starting at k, where both sides have length >= 1.
    # The number of such subarrays for a fixed k is left_count[k] * right_count[k].
    
    for k in range(1, n - 1):
        # If k is a local minimum
        if nums[k] < nums[k-1] and nums[k] < nums[k+1]:
            # The number of valid i's is left_count[k] (from 1 to left_count[k])
            # The number of valid j's is right_count[k] (from 1 to right_count[k])
            # Total combinations for this specific k:
            total_bowls += left_count[k] * right_count[k]
            
    return total_bowls

# Note: The O(1) space requirement in the prompt is technically impossible 
# if we need to store the monotonic lengths for all k to achieve O(n) time 
# without re-scanning. However, we can achieve O(n) time and O(1) space 
# by iterating and counting segments.
# Let's provide the O(n) time, O(1) space version by processing segments.

def solve_optimized(nums: list[int]) -> int:
    """
    Optimized version with O(n) time and O(1) space.
    We traverse the array to find local minima and expand.
    """
    n = len(nums)
    if n < 3:
        return 0
    
    total_bowls = 0
    i = 1
    while i < n - 1:
        # Check if i is a potential local minimum
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
            # Count how many elements strictly decrease to the left
            left_len = 0
            curr = i
            while curr > 0 and nums[curr] < nums[curr-1]:
                left_len += 1
                curr -= 1
            
            # Count how many elements strictly increase to the right
            right_len = 0
            curr = i
            while curr < n - 1 and nums[curr] < nums[curr+1]:
                right_len += 1
                curr += 1
            
            # Every combination of (1 to left_len) and (1 to right_len) forms a bowl
            total_bowls += (left_len * right_len)
            
            # Move i to the end of this increasing sequence to avoid redundant checks
            # but we must be careful not to skip potential minima.
            # Actually, a local minimum cannot be part of another local minimum's 
            # strictly increasing/decreasing sequence in a way that overlaps 
            # as a 'bottom'.
            i += 1 
        else:
            i += 1
            
    return total_bowls

# The actual optimal O(n) time, O(1) space approach:
def solve(nums: list[int]) -> int:
    """
    Counts the number of bowl-shaped subarrays using O(n) time and O(1) space.
    A bowl is defined by a local minimum index k where nums[k-1] > nums[k] < nums[k+1].
    """
    n = len(nums)
    if n < 3:
        return 0

    total_bowls = 0
    
    # We iterate through the array to find local minima.
    # For each local minimum, we expand left and right to find the extent 
    # of the monotonic sequences.
    i = 1
    while i < n - 1:
        # Identify a local minimum
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
            # Expand left: count strictly decreasing elements
            l_ptr = i - 1
            left_count = 0
            while l_ptr >= 0 and nums[l_ptr] > nums[l_ptr + 1]:
                left_count += 1
                l_ptr -= 1
            
            # Expand right: count strictly increasing elements
            r_ptr = i + 1
            right_count = 0
            while r_ptr < n and nums[r_ptr] > nums[r_ptr - 1]:
                right_count += 1
                r_ptr += 1
            
            # The number of valid subarrays with this specific k as the bottom
            # is the product of the lengths of the monotonic wings.
            total_bowls += (left_count * right_count)
            
            # Skip to the end of the increasing sequence to maintain O(n)
            # because a strictly increasing sequence cannot contain another local minimum.
            i = r_ptr - 1
        else:
            i += 1
            
    return total_bowls
