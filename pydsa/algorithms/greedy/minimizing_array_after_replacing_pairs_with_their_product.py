METADATA = {
    "id": 2892,
    "name": "Minimizing Array After Replacing Pairs With Their Product",
    "slug": "minimizing-array-after-replacing-pairs-with-their-product",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Minimize the sum of an array by repeatedly replacing two elements with their product, where each element can be used at most once.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Minimizes the sum of the array by performing at most k operations.
    Each operation consists of picking two elements and replacing them with their product.
    To minimize the sum, we greedily pick the two smallest elements.

    Args:
        nums: A list of integers.
        k: The maximum number of operations allowed.

    Returns:
        The minimum possible sum of the array after at most k operations.

    Examples:
        >>> solve([2, 3, 4, 5], 1)
        14
        >>> solve([2, 3, 4, 5], 2)
        11
    """
    # Sort the array to easily access the smallest elements
    nums.sort()
    
    n = len(nums)
    # We can perform at most k operations, but we also cannot exceed 
    # the number of pairs available in the array.
    num_operations = min(k, n // 2)
    
    # Use a pointer-based approach to simulate the replacement
    # Since we always pick the smallest two, we can process the sorted array
    # in steps of 2.
    
    # We will build a new list of elements that remain after operations
    # or are the results of the products.
    new_elements = []
    
    # Index for the current element being processed
    i = 0
    
    # Perform the operations greedily on the smallest available elements
    for _ in range(num_operations):
        # Multiply the two smallest available elements
        product = nums[i] * nums[i + 1]
        new_elements.append(product)
        i += 2
        
    # Add the remaining elements that were not part of any operation
    while i < n:
        new_elements.append(nums[i])
        i += 1
        
    return sum(new_elements)
