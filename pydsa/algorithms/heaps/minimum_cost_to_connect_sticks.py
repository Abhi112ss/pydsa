METADATA = {
    "id": 1167,
    "name": "Minimum Cost to Connect Sticks",
    "slug": "minimum-cost-to-connect-sticks",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "priority_queue", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to connect all sticks into one, where the cost of connecting two sticks is the sum of their lengths.",
}

import heapq

def solve(sticks: list[int]) -> int:
    """
    Calculates the minimum cost to connect all sticks into one single stick.
    
    The cost of connecting two sticks is the sum of their lengths. To minimize 
    the total cost, we always pick the two shortest available sticks to merge 
    using a greedy approach facilitated by a min-priority queue.

    Args:
        sticks: A list of integers representing the lengths of the sticks.

    Returns:
        The minimum total cost to connect all sticks. Returns 0 if there is 
        only one stick or no sticks.

    Examples:
        >>> solve([2, 4, 3])
        14
        >>> solve([1, 8, 3, 5])
        30
        >>> solve([5])
        0
    """
    if len(sticks) <= 1:
        return 0

    # Initialize a min-heap from the sticks list.
    # This allows us to extract the smallest elements in O(log n) time.
    heapq.heapify(sticks)
    
    total_cost = 0

    # Continue merging until only one stick remains in the heap.
    while len(sticks) > 1:
        # Extract the two smallest sticks.
        first_smallest = heapq.heappop(sticks)
        second_smallest = heapq.heappop(sticks)
        
        # The cost to connect these two is their sum.
        current_merge_cost = first_smallest + second_smallest
        total_cost += current_merge_cost
        
        # Push the resulting new stick back into the heap.
        heapq.heappush(sticks, current_merge_cost)

    return total_cost
