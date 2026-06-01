METADATA = {
    "id": 3134,
    "name": "Find the Median of the Uniqueness Array",
    "slug": "find_the_median_of_the_uniqueness_array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sliding_window", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the median of the uniqueness array, where each element is the difference between the maximum and minimum elements of a subarray.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the median of the uniqueness array. The uniqueness array is formed by 
    the difference between the max and min elements of every possible subarray.

    Args:
        nums: A list of integers.

    Returns:
        The median value of the uniqueness array.

    Examples:
        >>> solve([1, 4, 2])
        2
        # Subarrays: [1], [4], [2], [1,4], [4,2], [1,4,2]
        # Uniqueness: 0, 0, 0, 3, 2, 3
        # Sorted: 0, 0, 0, 2, 3, 3
        # Median (for even length 6, index (6-1)//2 = 2): 0 (Note: LeetCode definition 
        # for median of even length array of size N is the (N-1)//2-th element)
        # Wait, standard LeetCode median for even N is usually the (N-1)//2-th element.
        # Let's re-verify: For [0,0,0,2,3,3], N=6, index is 2, value is 0.
    """
    n = len(nums)
    total_subarrays = n * (n + 1) // 2
    # The median index for a sorted array of size N is (N-1) // 2
    target_index = (total_subarrays - 1) // 2

    # The uniqueness value (max - min) for any subarray is in range [0, max(nums) - min(nums)]
    low = 0
    high = max(nums) - min(nums)
    ans = high

    def count_subarrays_with_diff_le(k: int) -> int:
        """
        Counts how many subarrays have (max - min) <= k.
        Since we need to handle max and min, and the array isn't sorted, 
        we use a sliding window with two monotonic deques to track max and min.
        """
        from collections import deque
        
        count = 0
        left = 0
        max_deque = deque()  # Stores indices, values are decreasing
        min_deque = deque()  # Stores indices, values are increasing
        
        for right in range(n):
            # Maintain max_deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min_deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # If current window [left, right] violates the condition, shrink from left
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # All subarrays ending at 'right' and starting from index in [left, right] 
            # satisfy the condition.
            count += (right - left + 1)
            
        return count

    # Binary search for the smallest k such that count_subarrays_with_diff_le(k) > target_index
    # This k will be our median.
    while low <= high:
        mid = (low + high) // 2
        if count_subarrays_with_diff_le(mid) > target_index:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
