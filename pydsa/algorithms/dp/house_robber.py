METADATA = {
    "id": 198,
    "name": "House Robber",
    "slug": "house_robber",
    "category": "Dynamic Programming",
    "aliases": ["house_robber", "house_robber_dp"],
    "tags": ["dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given an integer array representing money in each house, return the maximum amount you can rob without robbing two adjacent houses.",
}

def solve(nums: list[int]) -> int:
    """Return the maximum amount of money you can rob without robbing adjacent houses.

    Args:
        nums: A list of non-negative integers representing money in each house.

    Returns:
        The maximum amount of money you can rob.

    Examples:
        >>> solve([1, 2, 3, 1])
        4
        >>> solve([2, 7, 9, 3, 1])
        12
        >>> solve([0])
        0
    """
    if not nums:
        return 0

    # prev_prev tracks the max profit up to two houses back, prev tracks max profit up to the previous house
    prev_prev = 0
    prev = 0

    for amount in nums:
        # At each house, choose to either rob it (add to prev_prev) or skip it (keep prev)
        current = max(prev, prev_prev + amount)
        prev_prev = prev
        prev = current

    return prev