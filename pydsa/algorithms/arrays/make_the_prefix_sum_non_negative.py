METADATA = {
    "id": 2599,
    "name": "Make the Prefix Sum Non-negative",
    "slug": "make-the-prefix-sum-non-negative",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the number of elements kept in an array such that all prefix sums remain non-negative.",
}

import heapq

def solve(nums: list[int]) -> int:
    """
    Maximizes the number of elements kept in the array such that all prefix sums are non-negative.

    The algorithm uses a greedy approach with a min-priority queue. We iterate through 
    the array, adding elements to a running prefix sum. If the sum becomes negative, 
    we greedily remove the smallest (most negative) element we have encountered 
    so far to restore the non-negative property with minimal impact on the count.

    Args:
        nums: A list of integers representing the original array.

    Returns:
        The maximum number of elements that can be kept such that all prefix sums are non-negative.

    Examples:
        >>> solve([5, -3, 5])
        3
        >>> solve([-1, -2, -3])
        0
        >>> solve([10, -10, -10, 5, 5])
        4
    """
    current_prefix_sum = 0
    # Min-heap to store the negative numbers we have included in our prefix sum
    # so far, allowing us to identify the most "damaging" element to remove.
    negative_elements_heap = []
    elements_kept_count = 0

    for num in nums:
        current_prefix_sum += num
        elements_kept_count += 1
        
        # If the current number is negative, track it in the heap
        if num < 0:
            heapq.heappush(negative_elements_heap, num)
        
        # If the prefix sum drops below zero, we must remove an element.
        # To maximize the count, we greedily remove the smallest (most negative) 
        # element encountered so far to increase the prefix sum as much as possible.
        if current_prefix_sum < 0:
            if negative_elements_heap:
                smallest_negative = heapq.heappop(negative_elements_heap)
                # Subtracting the negative value is equivalent to adding its absolute value
                current_prefix_sum -= smallest_negative
                elements_kept_count -= 1
            else:
                # This case handles if the current number itself is negative 
                # and makes the sum negative, but we haven't added it to the heap.
                # However, the logic above adds 'num' to the heap first, 
                # so this branch is technically unreachable with the current flow.
                pass

    return elements_kept_count
