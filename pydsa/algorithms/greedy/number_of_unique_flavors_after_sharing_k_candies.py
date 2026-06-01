METADATA = {
    "id": 2107,
    "name": "Number of Unique Flavors After Sharing K Candies",
    "slug": "number-of-unique-flavors-after-sharing-k-candies",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Minimize the number of unique candy flavors remaining after distributing k candies by greedily reducing the counts of the most frequent flavors.",
}

import heapq

def solve(flavors: list[int], k: int) -> int:
    """
    Calculates the minimum number of unique flavors remaining after sharing k candies.

    The strategy is to use a max-heap to always pick the flavor with the highest 
    count. By reducing the largest counts, we maximize the chance of completely 
    eliminating a flavor, thereby reducing the total count of unique flavors.

    Args:
        flavors: A list of integers representing the count of each candy flavor.
        k: The total number of candies that can be shared.

    Returns:
        The minimum number of unique flavors remaining.

    Examples:
        >>> solve([4, 8, 2, 4], 10)
        1
        >>> solve([2, 1, 1], 3)
        1
        >>> solve([1, 1, 1], 3)
        0
    """
    # Python's heapq is a min-heap. To use it as a max-heap, we negate the values.
    # We only care about flavors that have at least 1 candy.
    max_heap = [-count for count in flavors if count > 0]
    heapq.heapify(max_heap)
    
    remaining_k = k
    unique_flavors_count = len(max_heap)

    while remaining_k > 0 and max_heap:
        # Get the flavor with the highest count
        current_flavor_count = -heapq.heappop(max_heap)
        
        if remaining_k >= current_flavor_count:
            # We have enough candies to completely eliminate this flavor
            remaining_k -= current_flavor_count
            unique_flavors_count -= 1
        else:
            # We don't have enough candies to eliminate this flavor, 
            # but we can reduce its count. Since it won't reach 0, 
            # the number of unique flavors won't change further.
            # We can break early because any other flavor in the heap 
            # will also not be eliminated.
            remaining_k = 0
            
    return unique_flavors_count
