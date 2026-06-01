METADATA = {
    "id": 644,
    "name": "Maximum Average Subarray II",
    "slug": "maximum-average-subarray-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sliding_window", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(range / epsilon))",
    "space_complexity": "O(1)",
    "description": "Find the maximum average value of a contiguous subarray of length at least k.",
}

def solve(nums: list[float], k: int) -> float:
    """
    Finds the maximum average value of a contiguous subarray with length at least k.

    Args:
        nums: A list of floating point numbers.
        k: The minimum length of the subarray.

    Returns:
        The maximum average value found.

    Examples:
        >>> solve([1, 12, -5, -6, 50, 3], 4)
        12.75
        >>> solve([1], 1)
        1.0
    """
    n = len(nums)
    
    # We use binary search on the possible value of the average.
    # If there exists a subarray of length >= k with average >= target,
    # then sum(subarray) / length >= target  =>  sum(subarray) - length * target >= 0.
    # This is equivalent to checking if sum(nums[i] - target) for a subarray of length >= k is >= 0.
    
    def can_find_average_greater_than(target: float) -> bool:
        # Transform the problem: subtract target from every element.
        # We need to find if there's a subarray of length >= k with sum >= 0.
        current_sum = 0.0
        for i in range(k):
            current_sum += nums[i] - target
        
        if current_sum >= 0:
            return True
        
        # To handle length >= k, we track the minimum prefix sum seen so far
        # that allows for a subarray of length at least k.
        prev_sum = 0.0
        min_prev_sum = 0.0
        
        # We use a sliding window approach to maintain the sum of the first k elements
        # and track the minimum prefix sum encountered before the current window.
        for i in range(k, n):
            current_sum += nums[i] - target
            prev_sum += nums[i - k] - target
            # min_prev_sum tracks the smallest prefix sum seen before the current window
            # to maximize (current_sum - min_prev_sum).
            min_prev_sum = min(min_prev_sum, prev_sum)
            
            if current_sum - min_prev_sum >= 0:
                return True
                
        return False

    # Define the search range for the binary search.
    left = min(nums)
    right = max(nums)
    
    # Perform binary search for a fixed number of iterations to ensure precision.
    # 100 iterations provide precision roughly 2^-100, which is sufficient for float.
    for _ in range(100):
        mid = (left + right) / 2
        if can_find_average_greater_than(mid):
            left = mid
        else:
            right = mid
            
    return left
