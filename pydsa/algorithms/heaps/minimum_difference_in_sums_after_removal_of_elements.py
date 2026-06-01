METADATA = {
    "id": 2163,
    "name": "Minimum Difference in Sums After Removal of Elements",
    "slug": "minimum-difference-in-sums-after-removal-of-elements",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "priority_queue", "prefix_suffix"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum difference between the sum of the first n elements and the sum of the last n elements after removing n elements from an array of 3n elements.",
}

import heapq

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum difference between the sum of the first n elements 
    and the sum of the last n elements after removing n elements from a 3n array.

    Args:
        nums: A list of integers of length 3n.

    Returns:
        The minimum possible value of (sum(first_n) - sum(last_n)).

    Examples:
        >>> solve([7, 9, 5, 8, 1, 3])
        1
        >>> solve([1, 2, 3, 4, 5, 6])
        -3
    """
    n = len(nums) // 3
    
    # prefix_min_sums[i] will store the minimum sum of n elements 
    # chosen from the first (i + n) elements of the array.
    prefix_min_sums = [0] * (3 * n)
    
    # We use a max-heap to keep track of the smallest n elements seen so far.
    # In Python, heapq is a min-heap, so we store negative values to simulate a max-heap.
    max_heap_prefix = []
    current_prefix_sum = 0
    
    for i in range(2 * n):
        heapq.heappush(max_heap_prefix, -nums[i])
        current_prefix_sum += nums[i]
        
        # If we have more than n elements, remove the largest element to keep the sum minimal.
        if len(max_heap_prefix) > n:
            largest_val = -heapq.heappop(max_heap_prefix)
            current_prefix_sum -= largest_val
            
        # We can only start recording valid prefix sums once we have at least n elements.
        if len(max_heap_prefix) == n:
            prefix_min_sums[i] = current_prefix_sum

    # suffix_max_sums[i] will store the maximum sum of n elements 
    # chosen from the last (3n - i) elements of the array.
    suffix_max_sums = [0] * (3 * n)
    
    # We use a min-heap to keep track of the largest n elements seen so far.
    min_heap_suffix = []
    current_suffix_sum = 0
    
    # Iterate backwards from the end of the array.
    for i in range(3 * n - 1, n - 1, -1):
        heapq.heappush(min_heap_suffix, nums[i])
        current_suffix_sum += nums[i]
        
        # If we have more than n elements, remove the smallest element to keep the sum maximal.
        if len(min_heap_suffix) > n:
            smallest_val = heapq.heappop(min_heap_suffix)
            current_suffix_sum -= smallest_val
            
        if len(min_heap_suffix) == n:
            suffix_max_sums[i] = current_suffix_sum

    # The split point 'i' can range from index n-1 to 2n-1.
    # The first part uses elements from [0...i] and the second part from [i+1...3n-1].
    # We want to minimize (prefix_min_sum[i] - suffix_max_sum[i+1]).
    min_diff = float('inf')
    for i in range(n - 1, 2 * n):
        # prefix_min_sums[i] is the min sum of n elements in nums[0...i]
        # suffix_max_sums[i+1] is the max sum of n elements in nums[i+1...3n-1]
        diff = prefix_min_sums[i] - suffix_max_sums[i + 1]
        if diff < min_diff:
            min_diff = diff
            
    return int(min_diff)
