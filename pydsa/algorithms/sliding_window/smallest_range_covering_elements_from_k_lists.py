METADATA = {
    "id": 632,
    "name": "Smallest Range Covering Elements from K Lists",
    "slug": "smallest-range-covering-elements-from-k-lists",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sliding_window", "greedy", "priority_queue"],
    "difficulty": "hard",
    "time_complexity": "O(N log K)",
    "space_complexity": "O(K)",
    "description": "Find the smallest range that includes at least one number from each of the k lists.",
}

import heapq

def solve(nums: list[list[int]]) -> list[int]:
    """
    Finds the smallest range that includes at least one number from each of the k lists.

    The algorithm uses a min-heap to keep track of the smallest element currently 
    being considered from each list. By maintaining the maximum value among the 
    elements in the heap, we can calculate the range at every step.

    Args:
        nums: A list of k sorted integer lists.

    Returns:
        A list of two integers representing the smallest range [start, end].

    Examples:
        >>> solve([[4,10,15,24,26], [0,9,12,28,31], [5,18,22,30,35]])
        [24, 26]
        >>> solve([[1,2,3],[1,2,3],[1,2,3]])
        [1, 1]
    """
    # min_heap will store tuples: (value, list_index, element_index_within_list)
    min_heap = []
    current_max = float('-inf')
    
    # Initialize the heap with the first element from each list
    for list_idx in range(len(nums)):
        val = nums[list_idx][0]
        heapq.heappush(min_heap, (val, list_idx, 0))
        # Track the maximum value currently in our "window"
        if val > current_max:
            current_max = val
            
    # Initialize result range with a very large interval
    range_start, range_end = float('-inf'), float('inf')
    
    while len(min_heap) == len(nums):
        current_min, list_idx, element_idx = heapq.heappop(min_heap)
        
        # Update the best range found so far if the current range is smaller
        if current_max - current_min < range_end - range_start:
            range_start, range_end = current_min, current_max
            
        # If there's a next element in the list we just popped from, add it to the heap
        if element_idx + 1 < len(nums[list_idx]):
            next_val = nums[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))
            # Update current_max to reflect the new element added to the window
            if next_val > current_max:
                current_max = next_val
        else:
            # If any list is exhausted, we can no longer form a range containing all lists
            break
            
    return [int(range_start), int(range_end)]
