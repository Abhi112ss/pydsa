METADATA = {
    "id": 2015,
    "name": "Average Height of Buildings in Each Segment",
    "slug": "average-height-of-buildings-in-each-segment",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "prefix_sum", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the average height of buildings within specific segments defined by height thresholds.",
}

from bisect import bisect_left

def solve(heights: list[int], queries: list[list[int]]) -> list[float]:
    """
    Calculates the average height of buildings in segments defined by height ranges.

    The problem asks for the average height of buildings whose height is within 
    the range [queries[i][0], queries[i][1]].

    Args:
        heights: A list of integers representing building heights.
        queries: A list of queries, where each query is [min_height, max_height].

    Returns:
        A list of floats representing the average height for each query.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [[2, 4]])
        [3.0]
        >>> solve([10, 20, 30], [[15, 35]])
        [25.0]
    """
    # Sort heights to enable binary search and prefix sum calculation
    sorted_heights = sorted(heights)
    n = len(sorted_heights)
    
    # Precompute prefix sums to allow O(1) range sum queries
    prefix_sums = [0.0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + sorted_heights[i]
        
    results = []
    for min_h, max_h in queries:
        # Find the range of indices in the sorted list that fall within [min_h, max_h]
        # left_idx is the first index where sorted_heights[i] >= min_h
        left_idx = bisect_left(sorted_heights, min_h)
        
        # right_idx is the first index where sorted_heights[i] > max_h
        # We use bisect_left on (max_h + 1) or bisect_right on max_h
        # To find the upper bound of the range
        import bisect
        right_idx = bisect.bisect_right(sorted_heights, max_h)
        
        # Number of buildings in the range
        count = right_idx - left_idx
        
        if count == 0:
            results.append(0.0)
        else:
            # Calculate sum using the precomputed prefix sums
            total_sum = prefix_sums[right_idx] - prefix_sums[left_idx]
            results.append(total_sum / count)
            
    return results

# Note: The problem description provided in the prompt "Average Height of Buildings 
# in Each Segment" with tags "segment_tree" and "prefix_sum" usually refers to 
# a variation of range queries. The implementation above uses the most efficient 
# approach for static height arrays: Sorting + Prefix Sums + Binary Search.
# This achieves O(N log N) for sorting and O(Q log N) for queries.