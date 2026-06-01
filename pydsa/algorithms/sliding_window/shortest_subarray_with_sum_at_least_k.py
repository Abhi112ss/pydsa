METADATA = {
    "id": 862,
    "name": "Shortest Subarray with Sum at Least K",
    "slug": "shortest-subarray-with-sum-at-least-k",
    "category": "Array",
    "aliases": [],
    "tags": ["deque", "prefix_sum", "monotonic_queue", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the shortest non-empty subarray with a sum of at least k.",
}

from collections import deque

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the shortest non-empty subarray with a sum of at least k.

    Args:
        nums: A list of integers.
        k: The target minimum sum.

    Returns:
        The length of the shortest subarray, or -1 if no such subarray exists.

    Examples:
        >>> solve([2, -1, 2], 3)
        3
        >>> solve([1, 2], 4)
        -1
        >>> solve([2], 3)
        -1
    """
    n = len(nums)
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    min_length = float('inf')
    # monotonic_deque will store indices 'i' such that prefix_sums[i] is increasing
    monotonic_deque = deque()

    for i in range(n + 1):
        # 1. Check if we found a valid subarray: prefix_sums[i] - prefix_sums[left_index] >= k
        # We use a while loop to shrink the window from the left to find the shortest possible length
        while monotonic_deque and prefix_sums[i] - prefix_sums[monotonic_deque[0]] >= k:
            left_index = monotonic_deque.popleft()
            min_length = min(min_length, i - left_index)

        # 2. Maintain monotonicity: if current prefix_sum is smaller than the last one in deque,
        # the last one is useless because the current one is a "better" starting point 
        # (smaller sum and further to the right).
        while monotonic_deque and prefix_sums[i] <= prefix_sums[monotonic_deque[-1]]:
            monotonic_deque.pop()

        monotonic_deque.append(i)

    return int(min_length) if min_length != float('inf') else -1
