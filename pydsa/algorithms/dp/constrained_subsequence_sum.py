METADATA = {
    "id": 1425,
    "name": "Constrained Subsequence Sum",
    "slug": "constrained-subsequence-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "monotonic_queue", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a non-empty subsequence such that the distance between any two consecutive elements in the subsequence is at most k.",
}

from collections import deque


def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum of a non-empty subsequence where the distance 
    between indices of consecutive elements is at most k.

    Args:
        nums: A list of integers representing the input array.
        k: The maximum allowed distance between indices of consecutive elements.

    Returns:
        The maximum possible subsequence sum.

    Examples:
        >>> solve([10, 2, -10, 5, 20], 2)
        37
        >>> solve([-1, -2, -3], 1)
        -1
    """
    n = len(nums)
    # dp[i] stores the maximum subsequence sum ending at index i
    dp = [0] * n
    
    # A monotonic queue to store indices. 
    # The queue will maintain indices such that dp[index] is in descending order.
    # This allows us to find the maximum dp value in the window [i-k, i-1] in O(1).
    max_queue = deque()

    for i in range(n):
        # 1. Remove indices from the front that are outside the sliding window of size k
        if max_queue and max_queue[0] < i - k:
            max_queue.popleft()

        # 2. Calculate dp[i]. 
        # If the max value in the window is positive, add it to nums[i].
        # Otherwise, the subsequence starts at index i.
        max_prev_dp = dp[max_queue[0]] if max_queue else 0
        dp[i] = nums[i] + max(0, max_prev_dp)

        # 3. Maintain the monotonic property: remove indices from the back 
        # whose dp values are less than or equal to the current dp[i].
        while max_queue and dp[max_queue[-1]] <= dp[i]:
            max_queue.pop()
            
        max_queue.append(i)

    return max(dp)
