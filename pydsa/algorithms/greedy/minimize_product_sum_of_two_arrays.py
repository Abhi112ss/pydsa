METADATA = {
    "id": 1874,
    "name": "Minimize Product Sum of Two Arrays",
    "slug": "minimize-product-sum-of-two-arrays",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Minimize the sum of products of elements from two arrays by pairing the smallest elements of one with the largest of the other.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum possible product sum of two arrays.

    The strategy is to use a greedy approach: sort one array in ascending order 
    and the other in descending order. This ensures that the largest values 
    from one array are multiplied by the smallest values from the other, 
    minimizing the total sum.

    Args:
        nums1: A list of integers.
        nums2: A list of integers.

    Returns:
        The minimum possible sum of products.

    Examples:
        >>> solve([4, 5, 2], [2, 3, 1])
        25
        >>> solve([3, 2, 1], [1, 4, 5])
        17
    """
    # Sort nums1 in ascending order
    nums1.sort()
    
    # Sort nums2 in descending order
    nums2.sort(reverse=True)
    
    product_sum = 0
    
    # Iterate through the arrays and accumulate the product of paired elements
    for i in range(len(nums1)):
        # Pair smallest of nums1 with largest of nums2
        product_sum += nums1[i] * nums2[i]
        
    return product_sum
