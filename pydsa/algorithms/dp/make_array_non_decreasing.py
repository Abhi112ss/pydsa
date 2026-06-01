METADATA = {
    "id": 3523,
    "name": "Make Array Non-decreasing",
    "slug": "make_array_non_decreasing",
    "category": "Greedy",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "priority_queue"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Transform an array into a non-decreasing sequence with minimum total cost using a priority queue.",
}

import heapq

def solve(nums: list[int]) -> int:
    """
    Transforms the input array into a non-decreasing sequence with minimum total cost.
    The cost is defined as the sum of absolute differences between original and new elements.
    This is a classic application of the 'Slope Trick' algorithm.

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The minimum total cost (sum of absolute differences) to make the array non-decreasing.

    Examples:
        >>> solve([3, 2, 1])
        4
        >>> solve([1, 5, 2, 3])
        3
    """
    if not nums:
        return 0

    total_cost = 0
    # We use a max-heap to keep track of the 'turning points' of the convex cost function.
    # In Python, heapq is a min-heap, so we store negative values to simulate a max-heap.
    max_heap = []

    for x in nums:
        # For each element, we conceptually add a function |x - target| to our cumulative cost function.
        # If the current element is smaller than the largest element seen so far (the top of our max-heap),
        # it violates the non-decreasing property.
        if max_heap and -max_heap[0] > x:
            # The cost to fix this violation is the difference between the current max and x.
            # This is equivalent to moving the previous peak down to x or x up to the peak.
            diff = -max_heap[0] - x
            total_cost += diff
            
            # We pop the old peak and push the current element twice.
            # One push represents the new 'slope' change, and the other maintains the heap size
            # to correctly track the optimal value for the next element.
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -x)
            heapq.heappush(max_heap, -x)
        else:
            # If the element is already non-decreasing relative to the current optimal state,
            # we just add it to the heap to track potential future violations.
            heapq.heappush(max_heap, -x)

    return total_cost
