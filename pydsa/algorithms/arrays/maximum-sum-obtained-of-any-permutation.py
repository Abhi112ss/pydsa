METADATA = {
    "id": 1589,
    "name": "Maximum Sum Obtained of Any Permutation",
    "slug": "maximum-sum-obtained-of-any-permutation",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the sum of products of elements from two arrays by finding an optimal permutation.",
}

def solve(nums: list[int], perm: list[int]) -> int:
    """
    Calculates the maximum sum of products of elements from nums and perm.
    
    The problem asks to find a permutation of 'perm' such that the sum of 
    nums[i] * perm[i] is maximized. According to the Rearrangement Inequality, 
    the sum is maximized when both sequences are sorted in the same order.

    Args:
        nums: A list of integers representing the first array.
        perm: A list of integers representing the second array (to be permuted).

    Returns:
        The maximum possible sum of products.

    Examples:
        >>> solve([2, 1, 3], [3, 1, 2])
        11
        >>> solve([1, 4, 3, 2], [3, 1, 2, 4])
        25
    """
    # To maximize the sum of products (a[i] * b[i]), we pair the smallest 
    # with the smallest and the largest with the largest.
    # This is a direct application of the Rearrangement Inequality.
    
    sorted_nums = sorted(nums)
    sorted_perm = sorted(perm)
    
    total_sum = 0
    # Iterate through the sorted arrays and accumulate the products
    for i in range(len(sorted_nums)):
        total_sum += sorted_nums[i] * sorted_perm[i]
        
    return total_sum
