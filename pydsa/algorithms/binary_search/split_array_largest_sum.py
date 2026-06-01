METADATA = {
    "id": 410,
    "name": "Split Array Largest Sum",
    "slug": "split-array-largest-sum",
    "category": "Dynamic Programming / Binary Search",
    "aliases": [],
    "tags": ["binary_search", "greedy", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(sum(nums)))",
    "space_complexity": "O(1)",
    "description": "Split an array into m non-empty continuous subarrays such that the largest sum among these m subarrays is minimized.",
}

def solve(nums: list[int], m: int) -> int:
    """
    Finds the minimum possible value of the largest sum of m continuous subarrays.

    Args:
        nums: A list of non-negative integers.
        m: The number of subarrays to split the array into.

    Returns:
        The minimum largest sum possible.

    Examples:
        >>> solve([7, 2, 5, 10, 8], 2)
        18
        >>> solve([1, 2, 3, 4, 5], 2)
        9
    """
    
    def can_split_with_max_sum(max_allowed_sum: int) -> bool:
        """
        Checks if it is possible to split the array into at most m subarrays
        such that no subarray sum exceeds max_allowed_sum.
        """
        current_subarray_sum = 0
        required_subarrays = 1
        
        for num in nums:
            # If a single element is larger than the limit, this limit is impossible
            if current_subarray_sum + num > max_allowed_sum:
                # Start a new subarray
                required_subarrays += 1
                current_subarray_sum = num
                # If we exceed the allowed number of subarrays, return False
                if required_subarrays > m:
                    return False
            else:
                current_subarray_sum += num
        
        return True

    # The lower bound is the maximum single element (a subarray must contain at least one element)
    # The upper bound is the sum of all elements (one single subarray containing everything)
    low = max(nums)
    high = sum(nums)
    ans = high

    # Binary search on the answer space [max(nums), sum(nums)]
    while low <= high:
        mid = (low + high) // 2
        
        # If it's possible to split with 'mid' as the max sum, try a smaller max sum
        if can_split_with_max_sum(mid):
            ans = mid
            high = mid - 1
        else:
            # Otherwise, we need a larger max sum to accommodate the elements
            low = mid + 1
            
    return ans
