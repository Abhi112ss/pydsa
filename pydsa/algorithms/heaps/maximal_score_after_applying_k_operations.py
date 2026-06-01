METADATA = {
    "id": 2530,
    "name": "Maximal Score After Applying K Operations",
    "slug": "maximal-score-after-applying-k-operations",
    "category": "Heap",
    "aliases": [],
    "tags": ["heaps", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n + k log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximal score by repeatedly picking the largest element and adding its difference with the second largest to the total score.",
}

import heapq

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximal score after applying k operations.
    
    In each operation, we pick the largest element and the second largest element,
    add their difference to the score, and then update the largest element to 
    be the difference.

    Args:
        nums: A list of integers representing the initial elements.
        k: The number of operations to perform.

    Returns:
        The total maximal score accumulated after k operations.

    Examples:
        >>> solve([4, 1, 2], 3)
        6
        >>> solve([2, 4, 1], 4)
        6
    """
    # Python's heapq is a min-heap. To simulate a max-heap, 
    # we negate all numbers.
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    total_score = 0
    
    for _ in range(k):
        # Extract the largest element
        first_max = -heapq.heappop(max_heap)
        
        # If there is no second element, we cannot perform the operation
        if not max_heap:
            break
            
        # Extract the second largest element
        second_max = -heapq.heappop(max_heap)
        
        # Calculate the difference (score)
        diff = first_max - second_max
        total_score += diff
        
        # Push the second largest back into the heap
        heapq.heappush(max_heap, -second_max)
        
        # Push the new difference back into the heap
        heapq.heappush(max_heap, -diff)
        
    return total_score
