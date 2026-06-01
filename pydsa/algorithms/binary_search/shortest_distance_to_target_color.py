METADATA = {
    "id": 1182,
    "name": "Shortest Distance to Target Color",
    "slug": "shortest-distance-to-target-color",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "preprocessing", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n + q log n)",
    "space_complexity": "O(n)",
    "description": "Find the shortest distance from each query index to a target color in a given array.",
}

import bisect

def solve(colors: list[int], queries: list[int], target_color: int) -> list[int]:
    """
    Calculates the shortest distance from each query index to the nearest occurrence 
    of the target_color.

    Args:
        colors: A list of integers representing the colors of elements.
        queries: A list of indices to query.
        target_color: The specific color to find the distance to.

    Returns:
        A list of integers representing the shortest distance for each query.

    Examples:
        >>> solve([1, 2, 3, 4, 1], [0, 1, 2, 3, 4], 1)
        [0, 1, 2, 1, 0]
        >>> solve([1, 1, 1, 2, 2, 2], [3, 4, 5], 1)
        [3, 3, 3]
    """
    # Pre-process: Store all indices where the target_color appears in a sorted list
    target_indices = [i for i, color in enumerate(colors) if color == target_color]
    
    # If the target color doesn't exist in the array, return -1 for all queries
    if not target_indices:
        return [-1] * len(queries)
    
    results = []
    for query_idx in queries:
        # Use binary search to find the insertion point for the query index
        # bisect_left returns the leftmost index where query_idx could be inserted
        pos = bisect.bisect_left(target_indices, query_idx)
        
        min_dist = float('inf')
        
        # Check the element at the insertion point (the smallest index >= query_idx)
        if pos < len(target_indices):
            min_dist = min(min_dist, abs(target_indices[pos] - query_idx))
            
        # Check the element before the insertion point (the largest index < query_idx)
        if pos > 0:
            min_dist = min(min_dist, abs(target_indices[pos - 1] - query_idx))
            
        results.append(int(min_dist))
        
    return results
