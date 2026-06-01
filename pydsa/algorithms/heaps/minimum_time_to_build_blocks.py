METADATA = {
    "id": 1199,
    "name": "Minimum Time to Build Blocks",
    "slug": "minimum-time-to-build-blocks",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "huffman"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum time to build blocks by merging them using a strategy similar to Huffman coding.",
}

import heapq

def solve(blocks: list[int]) -> int:
    """
    Calculates the minimum time to build blocks by merging them.
    
    The problem can be modeled as building a tree where each internal node 
    represents a merge operation. The cost of a merge is the sum of the 
    sizes of the two blocks being merged, plus the time taken to perform 
    the merge. However, the problem constraints imply a Huffman-like 
    greedy approach where we always merge the two smallest available 
    elements to minimize the cumulative cost.

    Args:
        blocks: A list of integers representing the sizes of the initial blocks.

    Returns:
        The minimum total time required to merge all blocks into one.

    Examples:
        >>> solve([1, 2, 3])
        9
        >>> solve([5, 5, 5, 5])
        40
    """
    if not blocks:
        return 0
    if len(blocks) == 1:
        return 0

    # Use a min-heap to always extract the two smallest current blocks.
    # This is the standard greedy approach for optimal merge patterns (Huffman).
    heapq.heapify(blocks)
    total_time = 0

    while len(blocks) > 1:
        # Extract the two smallest blocks
        first_smallest = heapq.heappop(blocks)
        second_smallest = heapq.heappop(blocks)
        
        # The cost of this merge is the sum of the two blocks.
        # In this specific problem variation, the 'time' is the sum of the 
        # resulting block size.
        merge_cost = first_smallest + second_smallest
        total_time += merge_cost
        
        # Push the newly formed block back into the heap
        heapq.heappush(blocks, merge_cost)

    return total_time
