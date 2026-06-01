METADATA = {
    "id": 2762,
    "name": "Continuous Subarrays",
    "slug": "continuous_subarrays",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "monotonic_queue", "deque"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of continuous subarrays where the difference between the maximum and minimum elements is at most 1.",
}

from collections import deque

def solve(nums: list[int], limit: int) -> int:
    """
    Calculates the number of continuous subarrays where the difference 
    between the maximum and minimum elements is at most the given limit.

    Args:
        nums: A list of integers representing the array.
        limit: The maximum allowed difference between max and min in a subarray.

    Returns:
        The total count of valid continuous subarrays.

    Examples:
        >>> solve([8, 2, 4, 7], 4)
        3
        >>> solve([10, 1, 2, 4, 7, 2], 5)
        4
    """
    # max_deque stores indices of elements in decreasing order to track maximums
    # min_deque stores indices of elements in increasing order to track minimums
    max_deque: deque[int] = deque()
    min_deque: deque[int] = deque()
    
    left_pointer = 0
    total_subarrays = 0
    
    for right_pointer in range(len(nums)):
        current_val = nums[right_pointer]
        
        # Maintain max_deque: remove elements smaller than current_val
        while max_deque and nums[max_deque[-1]] <= current_val:
            max_deque.pop()
        max_deque.append(right_pointer)
        
        # Maintain min_deque: remove elements larger than current_val
        while min_deque and nums[min_deque[-1]] >= current_val:
            min_deque.pop()
        min_deque.append(right_pointer)
        
        # If the current window violates the limit, shrink from the left
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left_pointer += 1
            # Remove indices that are no longer within the window
            if max_deque[0] < left_pointer:
                max_deque.popleft()
            if min_deque[0] < left_pointer:
                min_deque.popleft()
        
        # The number of valid subarrays ending at right_pointer is (right - left + 1)
        total_subarrays += (right_pointer - left_pointer + 1)
        
    return total_subarrays
