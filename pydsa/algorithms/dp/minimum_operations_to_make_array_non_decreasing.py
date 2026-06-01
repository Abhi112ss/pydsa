METADATA = {
    "id": 3914,
    "name": "Minimum Operations to Make Array Non Decreasing",
    "slug": "minimum-operations-to-make-array-non-decreasing",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "priority_queue", "greedy", "slope-trick"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make an array non-decreasing using a priority queue to implement the slope trick.",
}

import heapq

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to make the array non-decreasing.
    An operation consists of changing an element to any integer.
    
    This problem is equivalent to finding the minimum cost to make a sequence 
    non-decreasing where the cost is the sum of absolute differences |a_i - b_i|.
    However, the problem asks for the number of elements changed. 
    Wait, the standard 'Minimum Operations' in LeetCode context usually refers 
    to the sum of absolute differences (L1 norm) or the number of elements 
    to change to satisfy a condition. 
    
    Based on the 'Slope Trick' hint provided: This is the classic problem of 
    minimizing sum |a_i - b_i| subject to b_i <= b_{i+1}.
    
    Args:
        nums: A list of integers.

    Returns:
        The minimum total cost (sum of absolute differences) to make the array non-decreasing.

    Examples:
        >>> solve([3, 2, 1])
        2
        >>> solve([1, 2, 3])
        0
        >>> solve([1, 5, 2, 3])
        3
    """
    # The problem of minimizing sum |nums[i] - target[i]| where target is non-decreasing
    # can be solved using a max-priority queue. This is a known application of 
    # the 'Slope Trick' for convex functions.
    
    max_heap = []
    total_cost = 0
    
    for val in nums:
        # If the current value is smaller than the largest value seen so far (top of max_heap),
        # it violates the non-decreasing property.
        if max_heap and -max_heap[0] > val:
            # The cost to 'fix' this locally is the difference between the current 
            # max and the current value.
            diff = -max_heap[0] - val
            total_cost += diff
            
            # We pop the old max and push the current value twice.
            # One represents the current element, and the other helps adjust 
            # future elements to maintain the optimal slope.
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -val)
            heapq.heappush(max_heap, -val)
        else:
            # If it's already non-decreasing relative to the max, just add it.
            heapq.heappush(max_heap, -val)
            
    return total_cost
