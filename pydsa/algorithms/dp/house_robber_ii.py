METADATA = {
    "id": 213,
    "name": "House Robber II",
    "slug": "house_robber_ii",
    "category": "Dynamic Programming",
    "aliases": ["house_robber_2"],
    "tags": ["dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a circular array of house values, find the maximum amount you can rob without alerting the police.",
}

from typing import Optional

def solve(nums: list[int]) -> int:
    """
    Determine the maximum amount of money you can rob from houses arranged in a circle without robbing adjacent houses.

    Args:
        nums: A list of non-negative integers representing the amount of money in each house.

    Returns:
        The maximum amount of money that can be robbed without triggering the alarm.

    Examples:
        >>> solve([2, 3, 2])
        3
        >>> solve([1, 2, 3, 1])
        4
        >>> solve([0])
        0
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    def rob_linear(houses: list[int]) -> int:
        prev_prev = 0
        prev = 0
        for house in houses:
            current = max(prev, prev_prev + house)
            prev_prev = prev
            prev = current
        return prev
    
    # Case 1: Exclude the last house (rob from index 0 to n-2)
    case1 = rob_linear(nums[:-1])
    
    # Case 2: Exclude the first house (rob from index 1 to n-1)
    case2 = rob_linear(nums[1:])
    
    return max(case1, case2)