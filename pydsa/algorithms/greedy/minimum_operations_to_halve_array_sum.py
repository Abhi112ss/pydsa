METADATA = {
    "id": 2208,
    "name": "Minimum Operations to Halve Array Sum",
    "slug": "minimum-operations-to-halve-array-sum",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to reduce the sum of an array by half, where an operation consists of halving an element.",
}

import heapq

def solve(nums: list[float], target: float) -> int:
    """
    Calculates the minimum number of operations to make the sum of the array 
    less than or equal to the target. Each operation halves an element.

    Args:
        nums: A list of positive integers representing the array.
        target: The target sum that the array sum must be less than or equal to.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([5, 4, 3, 2, 1], 11)
        3
        >>> solve([1, 10, 100, 1000], 500)
        1
    """
    current_sum = sum(nums)
    
    # If the current sum is already within the target, no operations needed
    if current_sum <= target:
        return 0

    # Python's heapq is a min-heap. To simulate a max-heap, we store negative values.
    # We store the values as floats to handle the division accurately.
    max_heap = [-float(num) for num in nums]
    heapq.heapify(max_heap)

    operations = 0
    
    while current_sum > target:
        # Extract the largest element (remember to negate back to positive)
        largest_val = -heapq.heappop(max_heap)
        
        # Calculate the reduction amount (half of the current value)
        reduction = largest_val / 2.0
        
        # Update the total sum and the count of operations
        current_sum -= reduction
        operations += 1
        
        # Push the halved value back into the heap
        # We negate it to maintain the max-heap property using heapq
        heapq.heappush(max_heap, -reduction)

    return operations
