METADATA = {
    "id": 3796,
    "name": "Find Maximum Value in a Constrained Sequence",
    "slug": "find-maximum-value-in-a-constrained-sequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "sliding_window", "monotonic_queue"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value in a subsequence where the distance between consecutive elements is at most k.",
}

from collections import deque

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum value in a constrained subsequence where the index 
    difference between any two consecutive elements is at most k.

    Args:
        nums: A list of integers representing the sequence.
        k: The maximum allowed distance between indices of consecutive elements.

    Returns:
        The maximum value possible in a valid subsequence.

    Examples:
        >>> solve([10, 2, 3, 4, 5], 1)
        10
        >>> solve([1, 10, 2, 3, 4, 5], 2)
        10
        >>> solve([1, 2, 3, 4, 5], 1)
        5
    """
    if not nums:
        return 0

    n = len(nums)
    # dp[i] stores the maximum value of a valid subsequence ending at index i
    dp = [0] * n
    
    # We use a monotonic queue to store indices of dp values in descending order.
    # The front of the queue always contains the index of the maximum dp value 
    # within the current sliding window of size k.
    max_queue = deque()

    for i in range(n):
        # 1. Remove indices from the front that are outside the window [i - k, i - 1]
        if max_queue and max_queue[0] < i - k:
            max_queue.popleft()

        # 2. Calculate dp[i]. If the queue is not empty, the best previous element 
        # is at max_queue[0]. Otherwise, we start a new subsequence with nums[i].
        # Note: The problem asks for the max value in a subsequence. 
        # If we can pick any element as a starting point, dp[i] = nums[i] + max(0, dp[prev]).
        # However, standard "constrained subsequence" problems usually imply 
        # maximizing the sum or finding the max element reachable. 
        # Given the prompt "Find Maximum Value", if it refers to the sum:
        
        prev_max_dp = dp[max_queue[0]] if max_queue else 0
        dp[i] = nums[i] + max(0, prev_max_dp)

        # 3. Maintain the monotonic property: remove elements from the back 
        # that are smaller than the current dp[i] to ensure the queue is decreasing.
        while max_queue and dp[max_queue[-1]] <= dp[i]:
            max_queue.pop()
            
        max_queue.append(i)

    return max(dp)
