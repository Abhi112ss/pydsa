METADATA = {
    "id": 2233,
    "name": "Maximum Product After K Increments",
    "slug": "maximum-product-after-k-increments",
    "category": "Greedy",
    "aliases": [],
    "tags": ["heap", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(k log n + n)",
    "space_complexity": "O(n)",
    "description": "Maximize the product of an array after performing k increments on any element.",
}

import heapq

def solve(nums: list[int], k: int) -> int:
    """
    Maximizes the product of elements in an array after k increments.
    
    The strategy is to always increment the smallest current element. 
    This is because increasing a smaller number provides a larger relative 
    increase to the total product compared to increasing a larger number.
    
    Args:
        nums: A list of positive integers.
        k: The number of increments to perform.
        
    Returns:
        The maximum product modulo 10^9 + 7.
        
    Examples:
        >>> solve([1, 3], 2)
        12
        >>> solve([6, 3, 3], 2)
        48
    """
    MOD = 1_000_000_007
    
    # Transform the list into a min-heap in-place.
    # This allows us to retrieve and update the smallest element in O(log n) time.
    heapq.heapify(nums)
    
    # Perform k increments. In each step, pop the smallest element,
    # increment it, and push it back into the heap.
    for _ in range(k):
        smallest = heapq.heappop(nums)
        heapq.heappush(nums, smallest + 1)
        
    # Calculate the final product of all elements in the heap.
    # We apply the modulo at each multiplication step to prevent integer overflow
    # (though Python handles large integers, it's good practice for performance/consistency).
    product = 1
    for num in nums:
        product = (product * num) % MOD
        
    return product
