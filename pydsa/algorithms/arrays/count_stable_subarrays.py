METADATA = {
    "id": 3748,
    "name": "Count Stable Subarrays",
    "slug": "count_stable_subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays that satisfy a specific stability condition using a sliding window approach.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of stable subarrays in the given list.
    A subarray is considered stable if the difference between the maximum 
    and minimum elements within the window does not exceed k.

    Args:
        nums: A list of integers representing the input array.
        k: An integer representing the maximum allowed difference (stability threshold).

    Returns:
        The total count of stable subarrays.

    Examples:
        >>> solve([1, 2, 3], 1)
        5
        # Subarrays: [1], [2], [3], [1, 2], [2, 3]
        >>> solve([1, 5, 2], 2)
        3
        # Subarrays: [1], [5], [2]
    """
    # Note: Since the problem description provided in the prompt is a template 
    # for a generic "stable subarray" problem (max - min <= k), 
    # we implement the standard sliding window solution for that condition.
    # If the specific LeetCode 3748 definition differs, the logic remains 
    # a sliding window pattern.

    n = len(nums)
    if n == 0:
        return 0

    total_stable_subarrays = 0
    left = 0
    
    # We use two monotonic deques to track the indices of the maximum 
    # and minimum elements in the current window in O(1) amortized time.
    from collections import deque
    max_deque = deque()
    min_deque = deque()

    for right in range(n):
        # Maintain max_deque: descending order of values
        while max_deque and nums[max_deque[-1]] <= nums[right]:
            max_deque.pop()
        max_deque.append(right)

        # Maintain min_deque: ascending order of values
        while min_deque and nums[min_deque[-1]] >= nums[right]:
            min_deque.pop()
        min_deque.append(right)

        # If the stability condition (max - min <= k) is violated, 
        # shrink the window from the left.
        while nums[max_deque[0]] - nums[min_deque[0]] > k:
            left += 1
            # Remove indices that are no longer within the window
            if max_deque[0] < left:
                max_deque.popleft()
            if min_deque[0] < left:
                min_deque.popleft()

        # Every subarray ending at 'right' and starting from any index 
        # between 'left' and 'right' is stable.
        total_stable_subarrays += (right - left + 1)

    return total_stable_subarrays
