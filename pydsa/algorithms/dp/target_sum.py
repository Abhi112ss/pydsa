METADATA = {
    "id": 494,
    "name": "Target Sum",
    "slug": "target-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "backtracking", "memoization", "subset_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Find the number of ways to assign +/- signs to elements in an array to reach a target sum.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of ways to assign '+' or '-' signs to each integer 
    in nums such that their sum equals target.

    The problem is transformed into a subset sum problem:
    Let P be the set of numbers with '+' and N be the set of numbers with '-'.
    sum(P) - sum(N) = target
    sum(P) + sum(N) = sum(nums)
    Adding the equations: 2 * sum(P) = target + sum(nums)
    sum(P) = (target + sum(nums)) / 2

    Args:
        nums: A list of integers.
        target: The target sum to achieve.

    Returns:
        The number of ways to reach the target sum.

    Examples:
        >>> solve([1, 1, 1, 1, 1], 3)
        5
        >>> solve([1], 1)
        1
    """
    total_sum = sum(nums)

    # If target is unreachable due to parity or magnitude
    if abs(target) > total_sum or (target + total_sum) % 2 != 0:
        return 0

    # The problem reduces to finding a subset that sums to subset_target
    subset_target = (target + total_sum) // 2

    # dp[i] stores the number of ways to reach sum 'i'
    dp = [0] * (subset_target + 1)
    dp[0] = 1  # Base case: one way to make sum 0 (empty subset)

    for num in nums:
        # Iterate backwards to ensure each number is used only once per subset
        # and to avoid using the updated value from the current iteration.
        for current_sum in range(subset_target, num - 1, -1):
            dp[current_sum] += dp[current_sum - num]

    return dp[subset_target]
