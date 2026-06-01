METADATA = {
    "id": 2335,
    "name": "Minimum Amount of Time to Fill Cups",
    "slug": "minimum-amount-of-time-to-fill-cups",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum time to fill all cups given a limit on how many cups can be filled simultaneously.",
    "solution_type": "Greedy with Max-Heap"
}

import heapq

def solve(amount: list[int], limit: int) -> int:
    """
    Calculates the minimum time required to fill all cups.
    
    In each time step, we can fill up to 'limit' cups. To minimize the total 
    time, we should always prioritize the cups that have the most remaining 
    amount to be filled (Greedy approach).

    Args:
        amount: A list of integers representing the amount needed for each cup.
        limit: The maximum number of cups that can be filled in one time step.

    Returns:
        The minimum number of time steps required to fill all cups.

    Examples:
        >>> solve([10, 10, 10], 3)
        10
        >>> solve([1, 2, 3, 4, 5], 2)
        5
    """
    # Python's heapq is a min-heap. To use it as a max-heap, 
    # we store the negative of the values.
    max_heap = [-a for a in amount if a > 0]
    heapq.heapify(max_heap)
    
    total_time = 0
    
    while max_heap:
        total_time += 1
        # We can pick up to 'limit' cups to fill in this time step.
        # We extract the largest elements currently in the heap.
        to_refill = []
        for _ in range(limit):
            if not max_heap:
                break
            # Pop the cup with the largest remaining amount
            current_val = -heapq.heappop(max_heap)
            # Reduce the amount by 1 (since we fill 1 unit per time step)
            if current_val > 1:
                to_refill.append(-(current_val - 1))
        
        # Push the cups that still need more filling back into the heap
        for remaining in to_refill:
            heapq.heappush(max_heap, remaining)
            
    return total_time
