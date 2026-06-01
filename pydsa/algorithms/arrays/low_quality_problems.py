METADATA = {
    "id": 2026,
    "name": "Low-Quality Problems",
    "slug": "low-quality-problems",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(k)",
    "description": "Find the number of problems with low quality among the top k problems with the highest rating.",
}

import heapq

def solve(rating: list[int], quality: list[int], k: int) -> int:
    """
    Finds the number of low-quality problems among the top k highest-rated problems.
    
    A problem is considered low-quality if its quality is less than the average 
    quality of the top k highest-rated problems.

    Args:
        rating: A list of integers representing the rating of each problem.
        quality: A list of integers representing the quality of each problem.
        k: The number of top-rated problems to consider.

    Returns:
        The count of low-quality problems among the top k highest-rated problems.

    Examples:
        >>> solve([2,5,1,3,4], [1,2,3,4,5], 3)
        1
        >>> solve([1,2,3,4,5], [5,4,3,2,1], 2)
        0
    """
    n = len(rating)
    # We want the top k highest ratings. 
    # To find the top k elements efficiently, we use a min-heap of size k.
    # The min-heap will store tuples of (rating, quality).
    # The smallest rating in the heap will be at the root, allowing us to 
    # replace it if we find a larger rating.
    top_k_heap: list[tuple[int, int]] = []

    for i in range(n):
        current_rating = rating[i]
        current_quality = quality[i]
        
        if len(top_k_heap) < k:
            heapq.heappush(top_k_heap, (current_rating, current_quality))
        else:
            # If current rating is higher than the smallest rating in our top k,
            # replace the smallest one.
            if current_rating > top_k_heap[0][0]:
                heapq.heapreplace(top_k_heap, (current_rating, current_quality))

    # Calculate the sum of qualities of the top k problems
    total_quality_sum = sum(item[1] for item in top_k_heap)
    average_quality = total_quality_sum / k

    # Count how many of these top k problems have quality < average_quality
    low_quality_count = 0
    for _, prob_quality in top_k_heap:
        if prob_quality < average_quality:
            low_quality_count += 1

    return low_quality_count
