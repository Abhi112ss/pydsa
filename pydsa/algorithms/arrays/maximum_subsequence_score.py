METADATA = {
    "id": 2542,
    "name": "Maximum Subsequence Score",
    "slug": "maximum-subsequence-score",
    "category": "Heap",
    "aliases": [],
    "tags": ["heap", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score of a subsequence of length k, where score is the sum of elements multiplied by the minimum element in the subsequence.",
}

import heapq

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum possible score of a subsequence of length k.
    The score is defined as the sum of the elements in the subsequence 
    multiplied by the minimum element in that subsequence.

    Args:
        nums: A list of integers representing the available numbers.
        k: The required size of the subsequence.

    Returns:
        The maximum score possible.

    Examples:
        >>> solve([1, 3, 3, 2], 3)
        8
        >>> solve([2, 4, 3, 5], 3)
        24
    """
    # Pair each number with its index to maintain the relationship 
    # between value and its original position (though here we only need values).
    # We sort by value descending so that as we iterate, the current 
    # element is always the minimum of the elements seen so far.
    indexed_nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
    
    # We need to pick k elements. To maximize the sum while the current 
    # element is the minimum, we should pick the k-1 largest elements 
    # encountered so far.
    min_heap = []
    current_sum = 0
    max_score = 0
    
    for index, value in indexed_nums:
        # Add the current value to our potential subsequence sum
        heapq.heappush(min_heap, value)
        current_sum += value
        
        # If we have more than k elements, remove the smallest one 
        # to keep the sum as large as possible for the current minimum.
        if len(min_heap) > k:
            smallest_val = heapq.heappop(min_heap)
            current_sum -= smallest_val
            
        # Once we have exactly k elements, calculate the score.
        # Since we sorted descending, 'value' is the minimum of the 
        # k elements currently in the heap.
        if len(min_heap) == k:
            max_score = max(max_score, current_sum * value)
            
    return max_score
