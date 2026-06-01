METADATA = {
    "id": 1892,
    "name": "Page Recommendations II",
    "slug": "page-recommendations-ii",
    "category": "Heap",
    "aliases": [],
    "tags": ["hash_map", "heap", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n * k log k)",
    "space_complexity": "O(n)",
    "description": "Given a sequence of page views, return the top k most frequent pages in the last 7 days, sorted by frequency and then lexicographically.",
}

import heapq
from collections import Counter, deque

def solve(pages: list[int], k: int) -> list[list[int]]:
    """
    Finds the top k most frequent pages in a sliding window of the last 7 days.

    Args:
        pages: A list of integers representing page IDs visited each day.
        k: The number of recommendations to return.

    Returns:
        A list of lists, where each inner list contains up to k recommended page IDs.

    Examples:
        >>> solve([1, 2, 3, 1, 2, 1, 2, 3], 2)
        [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]
    """
    n = len(pages)
    results = []
    # Frequency map for the current sliding window
    frequency_map = Counter()
    # Queue to track the history of the last 7 days
    window_history = deque()

    for i in range(n):
        # Add current page to window
        current_page = pages[i]
        frequency_map[current_page] += 1
        window_history.append(current_page)

        # Maintain sliding window of size 7
        if len(window_history) > 7:
            old_page = window_history.popleft()
            frequency_map[old_page] -= 1
            if frequency_map[old_page] == 0:
                del frequency_map[old_page]

        # To find top k, we use a min-heap.
        # To handle the tie-breaking (higher frequency first, then smaller ID),
        # we store (-frequency, page_id) in a max-heap or (frequency, -page_id) in a min-heap.
        # However, since we need the top k, a min-heap of size k is standard.
        # For tie-breaking: we want higher frequency, then smaller ID.
        # In a min-heap, we want to discard the "smallest" elements.
        # "Smallest" in our context means: lower frequency, or same frequency but larger ID.
        # So we store (frequency, -page_id) in the min-heap.
        
        min_heap = []
        for page, freq in frequency_map.items():
            # We use -page to make the min-heap treat larger IDs as "smaller" 
            # so they are popped first when frequencies are equal.
            heapq.heappush(min_heap, (freq, -page))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract from heap and sort for the final output
        # The heap contains the top k elements, but they are in min-heap order.
        # We need them sorted by freq DESC, then page_id ASC.
        current_recommendations = []
        while min_heap:
            freq, neg_page = heapq.heappop(min_heap)
            current_recommendations.append((-neg_page, freq))
        
        # Sort: primary key frequency (descending), secondary key page_id (ascending)
        current_recommendations.sort(key=lambda x: (-x[1], x[0]))
        results.append([item[0] for item in current_recommendations])

    return results
