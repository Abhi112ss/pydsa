METADATA = {
    "id": 239,
    "name": "Sliding Window Maximum",
    "slug": "sliding_window_maximum",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "deque", "monotonic_queue"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Given an array and a window size k, return the maximum element in every sliding window of size k.",
}

from collections import deque

def solve(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in every sliding window of size k using a monotonic deque.

    Args:
        nums: A list of integers representing the input array.
        k: An integer representing the size of the sliding window.

    Returns:
        A list of integers containing the maximum value for each window position.

    Examples:
        >>> solve([1, 3, -1, -3, 5, 3, 6, 7], 3)
        [3, 3, 5, 5, 6, 7]
        >>> solve([1], 1)
        [1]
    """
    if not nums or k == 0:
        return []
    
    # The deque will store indices of elements in nums.
    # We maintain the deque such that the values at these indices are in strictly decreasing order.
    # This ensures the element at the front of the deque is always the maximum for the current window.
    monotonic_deque: deque[int] = deque()
    result: list[int] = []

    for i in range(len(nums)):
        # 1. Remove indices that are out of the current window's range.
        # The window covers indices from (i - k + 1) to i.
        if monotonic_deque and monotonic_deque[0] <= i - k:
            monotonic_deque.popleft()

        # 2. Maintain the monotonic property:
        # Before adding the current element, remove all indices from the back whose 
        # corresponding values are less than or equal to the current element.
        # They can never be the maximum for any future window.
        while monotonic_deque and nums[monotonic_deque[-1]] <= nums[i]:
            monotonic_deque.pop()

        monotonic_deque.append(i)

        # 3. Once the first window is fully formed (i >= k - 1), 
        # the front of the deque is the maximum for the current window.
        if i >= k - 1:
            result.append(nums[monotonic_deque[0]])

    return result
