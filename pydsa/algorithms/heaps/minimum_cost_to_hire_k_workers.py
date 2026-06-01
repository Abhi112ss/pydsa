METADATA = {
    "id": 857,
    "name": "Minimum Cost to Hire K Workers",
    "slug": "minimum-cost-to-hire-k-workers",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "heap"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the minimum cost to hire K workers such that every worker's pay is proportional to their quality and satisfies their minimum wage requirement.",
}

import heapq

def solve(quality: list[int], wage: list[int], k: int) -> float:
    """
    Calculates the minimum cost to hire K workers based on quality and wage constraints.

    The strategy is to sort workers by their wage-to-quality ratio. As we iterate 
    through the sorted workers, we maintain a max-heap of the qualities of the 
    K workers seen so far. This allows us to minimize the total quality sum 
    for a given ratio, which in turn minimizes the total cost.

    Args:
        quality: A list of integers representing the quality of each worker.
        wage: A list of integers representing the minimum wage of each worker.
        k: The number of workers to hire.

    Returns:
        The minimum cost to hire K workers as a float.

    Examples:
        >>> solve([10, 20, 70], [10, 100, 200], 2)
        240.0
        >>> solve([1, 2, 3], [10, 10, 10], 3)
        60.0
    """
    n = len(quality)
    # Create worker tuples: (ratio, quality)
    # ratio = wage / quality
    workers = []
    for i in range(n):
        workers.append((wage[i] / quality[i], quality[i]))

    # Sort workers by their wage-to-quality ratio
    workers.sort()

    min_cost = float('inf')
    current_quality_sum = 0
    # Max-heap to store the qualities of the K workers selected so far.
    # Python's heapq is a min-heap, so we store negative values to simulate a max-heap.
    max_heap_qualities = []

    for ratio, q in workers:
        heapq.heappush(max_heap_qualities, -q)
        current_quality_sum += q

        # If we have more than K workers, remove the one with the highest quality
        # to keep the total quality sum (and thus the cost) as low as possible.
        if len(max_heap_qualities) > k:
            highest_quality = -heapq.heappop(max_heap_qualities)
            current_quality_sum -= highest_quality

        # Once we have exactly K workers, calculate the cost using the current ratio.
        # The current ratio is the highest ratio seen so far in our sorted iteration,
        # ensuring all K workers meet their minimum wage requirements.
        if len(max_heap_qualities) == k:
            min_cost = min(min_cost, current_quality_sum * ratio)

    return float(min_cost)
