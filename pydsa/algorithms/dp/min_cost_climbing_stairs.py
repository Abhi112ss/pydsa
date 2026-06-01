METADATA = {
    "id": 746,
    "name": "Min Cost Climbing Stairs",
    "slug": "min_cost_climbing_stairs",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the minimum cost to reach the top of the staircase.",
}


def solve() -> None:
    """Read a list of step costs and output the minimum cost to reach the top.

    Args:
        None. The function reads from standard input. The input should contain
        a single line with space‑separated integers representing `cost[i]`.

    Returns:
        None. The result is printed to standard output.

    Examples:
        >>> # Input: 10 15 20
        >>> # Output: 15
        >>> # Explanation: Start at step 1 (cost 15) and then climb to the top.
        >>> # Input: 1 100 1 1 1 100 1 1 100 1
        >>> # Output: 6
    """
    import sys

    data = sys.stdin.read().strip().split()
    if not data:
        return
    cost = [int(x) for x in data]

    # Two variables hold the minimum cost to reach the two previous steps.
    min_cost_two_steps_before = 0  # dp[i-2]
    min_cost_one_step_before = 0   # dp[i-1]

    for index in range(2, len(cost) + 1):
        # Cost to step onto the (index‑1)th stair.
        current_cost = cost[index - 1] + min(min_cost_one_step_before, min_cost_two_steps_before)
        # Shift the window forward.
        min_cost_two_steps_before, min_cost_one_step_before = min_cost_one_step_before, current_cost

    # The top can be reached from either of the last two steps.
    result = min(min_cost_one_step_before, min_cost_two_steps_before)
    print(result)