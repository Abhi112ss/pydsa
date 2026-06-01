METADATA = {
    "id": 1918,
    "name": "Kth Smallest Subarray Sum",
    "slug": "kth-smallest-subarray-sum",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sliding_window", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(n * log(total_sum))",
    "space_complexity": "O(1)",
    "description": "Find the kth smallest subarray sum using binary search on the answer range and a sliding window to count valid subarrays.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the kth smallest subarray sum in the given array.

    Args:
        nums: A list of positive integers.
        k: The rank of the subarray sum to find.

    Returns:
        The kth smallest subarray sum.

    Examples:
        >>> solve([1, 2, 3], 2)
        2
        >>> solve([1, 2, 3], 4)
        3
    """
    
    def count_subarrays_with_sum_at_most(target_sum: int) -> int:
        """
        Counts how many subarrays have a sum less than or equal to target_sum
        using a sliding window approach.
        """
        count = 0
        current_window_sum = 0
        left_pointer = 0
        
        for right_pointer in range(len(nums)):
            current_window_sum += nums[right_pointer]
            
            # Shrink the window from the left if the sum exceeds the target
            while current_window_sum > target_sum and left_pointer <= right_pointer:
                current_window_sum -= nums[left_pointer]
                left_pointer += 1
            
            # All subarrays ending at right_pointer and starting from 
            # any index between left_pointer and right_pointer are valid.
            count += (right_pointer - left_pointer + 1)
            
        return count

    # The range for binary search: 
    # Minimum possible sum is the smallest element (or 0 if empty, but nums are positive)
    # Maximum possible sum is the sum of all elements.
    low = min(nums)
    high = sum(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        
        # If the number of subarrays with sum <= mid is at least k,
        # then the kth smallest sum is mid or something smaller.
        if count_subarrays_with_sum_at_most(mid) >= k:
            ans = mid
            high = mid - 1
        else:
            # Otherwise, the kth smallest sum must be larger than mid.
            low = mid + 1
            
    return ans
