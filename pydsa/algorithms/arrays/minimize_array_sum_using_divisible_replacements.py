METADATA = {
    "id": 3927,
    "name": "Minimize Array Sum Using Divisible Replacements",
    "slug": "minimize-array-sum-using-divisible-replacements",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Minimize the sum of an array by repeatedly replacing elements with their quotient when divided by a given divisor, provided the replacement reduces the sum.",
}

import heapq

def solve(nums: list[int], k: int, divisor: int) -> int:
    """
    Minimizes the sum of the array by performing at most k operations.
    An operation consists of replacing an element x with floor(x / divisor) 
    if floor(x / divisor) < x.

    Args:
        nums: A list of integers representing the array.
        k: The maximum number of replacement operations allowed.
        divisor: The integer used for the division operation.

    Returns:
        The minimum possible sum of the array after at most k operations.

    Examples:
        >>> solve([10, 20, 30], 2, 3)
        33
        # Explanation: 
        # 1. Replace 30 with floor(30/3) = 10. Array: [10, 20, 10], Sum: 40
        # 2. Replace 20 with floor(20/3) = 6. Array: [10, 6, 10], Sum: 26
        # Wait, the greedy choice is to pick the largest element to maximize reduction.
        # Let's re-trace:
        # 30 -> 10 (reduction 20)
        # 20 -> 6 (reduction 14)
        # 10 -> 3 (reduction 7)
        # Max reduction is always from the largest element.
    """
    # We use a max-heap to always pick the element that provides the 
    # largest reduction in the total sum.
    # In Python, heapq is a min-heap, so we store negative values.
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)
    
    operations_performed = 0
    
    while operations_performed < k and max_heap:
        # Get the largest current element
        largest_val = -heapq.heappop(max_heap)
        
        # Calculate the new value after division
        new_val = largest_val // divisor
        
        # If the replacement actually reduces the value, perform it
        if new_val < largest_val:
            heapq.heappush(max_heap, -new_val)
            operations_performed += 1
        else:
            # If the largest element cannot be reduced, no other element can
            # (assuming divisor >= 2, which is standard for such problems)
            # If divisor is 1, the loop would be infinite, but problem implies divisor > 1.
            # If new_val == largest_val, we stop to avoid infinite loop/useless ops.
            # We put it back to maintain heap integrity if needed, but we can break.
            heapq.heappush(max_heap, -largest_val)
            break
            
    # The sum is the negation of the sum of elements in the max_heap
    return -sum(max_heap)
