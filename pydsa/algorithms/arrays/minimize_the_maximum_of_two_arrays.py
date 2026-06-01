METADATA = {
    "id": 2513,
    "name": "Minimize the Maximum of Two Arrays",
    "slug": "minimize-the-maximum-of-two-arrays",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Minimize the maximum value of two arrays after performing at most k operations where each operation decreases an element in one array by 1.",
}

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    """
    Minimizes the maximum value of two arrays by performing at most k operations.
    Each operation consists of decreasing an element in either array by 1.

    Args:
        nums1: A list of integers representing the first array.
        nums2: A list of integers representing the second array.
        k: The maximum number of operations allowed.

    Returns:
        The minimum possible value of the maximum element across both arrays.

    Examples:
        >>> solve([4, 3, 2, 1], [1, 2, 3, 4], 3)
        3
        >>> solve([1, 1, 1], [1, 1, 1], 0)
        1
    """
    
    def can_achieve_max(target: int) -> bool:
        """
        Checks if it is possible to make all elements in both arrays <= target
        using at most k operations.
        """
        operations_needed = 0
        for val in nums1:
            if val > target:
                operations_needed += val - target
        
        for val in nums2:
            if val > target:
                operations_needed += val - target
                
        return operations_needed <= k

    # The range for binary search is between 1 and the current maximum value
    low = 1
    high = max(max(nums1), max(nums2))
    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        # If we can make all elements <= mid, try a smaller target
        if can_achieve_max(mid):
            ans = mid
            high = mid - 1
        else:
            # Otherwise, we need a larger target
            low = mid + 1
            
    return ans
