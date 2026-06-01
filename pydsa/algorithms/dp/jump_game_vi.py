METADATA = {
    "id": 1696,
    "name": "Jump Game VI",
    "slug": "jump-game-vi",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "sliding_window_maximum", "monotonic_queue"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score you can get by jumping from the start to the end of an array, where each jump has a maximum distance k.",
}

from collections import deque

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum score achievable by jumping from index 0 to n-1.
    Each jump can be at most k steps forward.

    Args:
        nums: A list of integers representing the score at each index.
        k: The maximum number of steps allowed in a single jump.

    Returns:
        The maximum score possible to reach the last index.

    Examples:
        >>> solve([1, -1, -2, 4, -5, 6], 4)
        7
        >>> solve([1, -1], 1)
        0
    """
    n = len(nums)
    # dp[i] stores the maximum score to reach index i
    dp = [0] * n
    dp[0] = nums[0]

    # We use a monotonic queue to store indices of dp.
    # The queue will maintain indices such that dp[index] is in descending order.
    # This allows us to find the maximum dp value in the current window of size k in O(1).
    dq = deque([0])

    for i in range(1, n):
        # 1. Remove indices from the front that are out of the window range [i-k, i-1]
        if dq and dq[0] < i - k:
            dq.popleft()

        # 2. The maximum score to reach i is nums[i] + the best score in the window
        dp[i] = nums[i] + dp[dq[0]]

        # 3. Maintain the monotonic property: remove indices from the back whose 
        # dp values are less than or equal to the current dp[i]
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        
        dq.append(i)

    return dp[n - 1]
