METADATA = {
    "id": 2991,
    "name": "Top Three Wineries",
    "slug": "top-three-wineries",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "top-k"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the top three highest rated wineries from a given list of ratings.",
}

import heapq

def solve(ratings: list[int]) -> list[int]:
    """
    Finds the top three highest ratings from the provided list.

    Args:
        ratings: A list of integers representing winery ratings.

    Returns:
        A list of the top three highest ratings sorted in descending order.
        If there are fewer than three ratings, returns all available ratings 
        sorted in descending order.

    Examples:
        >>> solve([10, 20, 5, 30, 15])
        [30, 20, 15]
        >>> solve([5, 5, 5, 5])
        [5, 5, 5]
        >>> solve([10, 20])
        [20, 10]
    """
    # Use a min-heap to maintain only the top 3 elements seen so far.
    # This ensures O(n log 3) time complexity, which simplifies to O(n).
    min_heap = []
    
    for rating in ratings:
        if len(min_heap) < 3:
            heapq.heappush(min_heap, rating)
        else:
            # If current rating is larger than the smallest in our top 3, replace it.
            if rating > min_heap[0]:
                heapq.heapreplace(min_heap, rating)
                
    # The heap contains the top 3 elements, but they are in min-heap order.
    # We sort them descending to meet the expected output format.
    result = sorted(min_heap, reverse=True)
    return result
