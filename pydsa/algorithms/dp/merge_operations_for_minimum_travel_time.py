METADATA = {
    "id": 3538,
    "name": "Merge Operations for Minimum Travel Time",
    "slug": "merge-operations-for-minimum-travel-time",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heaps", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum total cost to merge all elements into one, where the cost of merging two elements is their sum.",
}

import heapq

def solve(costs: list[int]) -> int:
    """
    Calculates the minimum total cost to merge all elements in the list into a single element.
    The cost of merging two elements is the sum of their values.

    This is a classic application of the Huffman Coding / Optimal Merge Pattern algorithm.
    By always merging the two smallest current elements, we ensure that larger values 
    are involved in fewer merge operations, thus minimizing the total sum.

    Args:
        costs: A list of integers representing the initial values of the elements.

    Returns:
        The minimum total cost to merge all elements.

    Examples:
        >>> solve([1, 2, 3])
        9
        # (1+2) = 3; (3+3) = 6; Total = 3 + 6 = 9
        >>> solve([4, 3, 2, 6])
        29
        # (2+3) = 5; (5+4) = 9; (9+6) = 15; Total = 5 + 9 + 15 = 29
    """
    if not costs:
        return 0
    if len(costs) == 1:
        return 0

    # Initialize a min-priority queue to always extract the smallest elements
    min_heap = costs[:]
    heapq.heapify(min_heap)
    
    total_merge_cost = 0

    # Continue merging until only one element remains in the heap
    while len(min_heap) > 1:
        # Extract the two smallest elements
        first_smallest = heapq.heappop(min_heap)
        second_smallest = heapq.heappop(min_heap)
        
        # The cost of this specific merge operation
        current_merge_cost = first_smallest + second_smallest
        total_merge_cost += current_merge_cost
        
        # Push the resulting merged element back into the heap
        heapq.heappush(min_heap, current_merge_cost)

    return total_merge_cost
