METADATA = {
    "id": 1354,
    "name": "Construct Target Array With Multiple Sums",
    "slug": "construct-target-array-with-multiple-sums",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heaps", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n log(max(target)))",
    "space_complexity": "O(n)",
    "description": "Construct a target array by reversing the process of adding an element to a sum of others using a max-heap and modulo arithmetic.",
}

import heapq

def solve(target: list[int]) -> bool:
    """
    Constructs the target array by working backwards from the sum of elements.

    The algorithm uses a max-heap to always identify the largest current element.
    Instead of subtracting the sum of other elements one by one, it uses 
    modulo arithmetic to jump multiple steps ahead, handling cases where 
    the largest element is significantly larger than the sum of others.

    Args:
        target: A list of integers representing the target array.

    Returns:
        True if the target array can be constructed, False otherwise.

    Examples:
        >>> solve([1, 2, 3])
        True
        >>> solve([1, 1, 1, 0])
        False
        >>> solve([1, 10, 1000000000])
        True
    """
    n = len(target)
    if n == 1:
        return target[0] == 1

    total_sum = sum(target)
    # Python's heapq is a min-heap, so we store negative values to simulate a max-heap
    max_heap = [-x for x in target]
    heapq.heapify(max_heap)

    while True:
        # Get the current largest element
        largest = -heapq.heappop(max_heap)
        
        # The sum of all other elements
        sum_others = total_sum - largest
        
        # Base case: if sum_others is 1, we can always reach the target (e.g., [1, 1, 1])
        if sum_others == 1:
            return True
        
        # If sum_others is 0 or largest is not greater than sum_others, it's impossible
        # (unless we already reached the base case above)
        if sum_others <= 1 or largest >= sum_others or sum_others == 0:
            # Special check: if the array is all 1s, we might have finished
            # But if we are here, it means we can't reduce further
            return False

        # Use modulo to handle cases where largest is much bigger than sum_others
        # We want to find 'largest % sum_others', but if the result is 0, 
        # it means the element becomes sum_others (the smallest possible valid value)
        new_largest = largest % sum_others
        if new_largest == 0:
            new_largest = sum_others
            
        # If the reduction doesn't change the value, we are stuck in a loop
        if new_largest == largest:
            return False

        # Update the total sum and push the new value back into the heap
        total_sum = total_sum - largest + new_largest
        heapq.heappush(max_heap, -new_largest)
