METADATA = {
    "id": 3264,
    "name": "Final Array State After K Multiplication Operations I",
    "slug": "final-array-state-after-k-multiplication-operations-i",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "priority_queue", "heap"],
    "difficulty": "easy",
    "time_complexity": "O(k log n)",
    "space_complexity": "O(n)",
    "description": "Perform k operations where the smallest element in an array is multiplied by a given multiplier, returning the final array.",
}

import heapq

def solve(nums: list[int], k: int, multiplier: int) -> list[int]:
    """
    Performs k operations where the smallest element in the array is multiplied 
    by the given multiplier.

    Args:
        nums: A list of integers representing the initial state of the array.
        k: The number of multiplication operations to perform.
        multiplier: The integer value to multiply the smallest element by.

    Returns:
        The final state of the array after k operations.

    Examples:
        >>> solve([4, 5, 2, 6], 3, 2)
        [4, 5, 16, 6]
        >>> solve([1, 3, 5], 2, 2)
        [4, 3, 5]
    """
    # We use a min-heap to efficiently find and extract the smallest element.
    # Since we need to return the array in its original order, we store 
    # tuples of (value, original_index) in the heap.
    min_heap = []
    for index, value in enumerate(nums):
        heapq.heappush(min_heap, (value, index))

    for _ in range(k):
        # Extract the smallest element and its original index
        current_value, original_index = heapq.heappop(min_heap)
        
        # Perform the multiplication
        new_value = current_value * multiplier
        
        # Update the original array to reflect the change
        nums[original_index] = new_value
        
        # Push the updated value back into the heap to maintain order
        heapq.heappush(min_heap, (new_value, original_index))

    return nums
