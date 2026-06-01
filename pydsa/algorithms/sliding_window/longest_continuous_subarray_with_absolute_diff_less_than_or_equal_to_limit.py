METADATA = {
    "id": 1438,
    "name": "Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit",
    "slug": "longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "monotonic_queue", "deque"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to the given limit.",
}

from collections import deque

def solve(nums: list[int], limit: int) -> int:
    """
    Finds the length of the longest subarray where the difference between 
    the maximum and minimum elements is within the specified limit.

    Args:
        nums: A list of integers.
        limit: The maximum allowed absolute difference between any two elements.

    Returns:
        The length of the longest valid continuous subarray.

    Examples:
        >>> solve([8, 2, 4, 7], 4)
        2
        >>> solve([10, 1, 2, 4, 7, 2], 5)
        4
    """
    # max_deque stores indices of elements in decreasing order to track the maximum
    max_deque: deque[int] = deque()
    # min_deque stores indices of elements in increasing order to track the minimum
    min_deque: deque[int] = deque()
    
    left_pointer = 0
    max_length = 0

    for right_pointer in range(len(nums)):
        current_val = nums[right_pointer]

        # Maintain max_deque: remove elements smaller than current_val from the back
        while max_deque and nums[max_deque[-1]] <= current_val:
            max_deque.pop()
        max_deque.append(right_pointer)

        # Maintain min_deque: remove elements larger than current_val from the back
        while min_deque and nums[min_deque[-1]] >= current_val:
            min_deque.pop()
        min_deque.append(right_pointer)

        # If the current window violates the limit, shrink the window from the left
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            left_pointer += 1
            # Remove indices from deques if they are no longer within the window
            if max_deque[0] < left_pointer:
                max_deque.popleft()
            if min_deque[0] < left_pointer:
                min_deque.popleft()

        # Update the maximum length found so far
        max_length = max(max_length, right_pointer - left_pointer + 1)

    return max_length
