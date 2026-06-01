METADATA = {
    "id": 3660,
    "name": "Jump Game IX",
    "slug": "jump-game-ix",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "monotonic_stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of jumps to reach the last index given specific jump constraints based on element values.",
}

def solve(nums: list[int]) -> int:
    """
    Args:
        nums: A list of integers representing the jump constraints.

    Returns:
        The minimum number of jumps required to reach the last index.
    """
    n = len(nums)
    if n <= 1:
        return 0

    next_greater_index = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            next_greater_index[index] = i
        stack.append(i)

    next_smaller_index = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            index = stack.pop()
            next_smaller_index[index] = i
        stack.append(i)

    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(n):
        if dp[i] == float('inf'):
            continue

        next_greater = next_greater_index[i]
        if next_greater != -1:
            dp[next_greater] = min(dp[next_greater], dp[i] + 1)

        next_smaller = next_smaller_index[i]
        if next_smaller != -1:
            dp[next_smaller] = min(dp[next_smaller], dp[i] + 1)

    return int(dp[n - 1])