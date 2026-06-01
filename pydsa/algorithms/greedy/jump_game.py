METADATA = {
    "id": 55,
    "name": "Jump Game",
    "slug": "jump-game",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if you can reach the last index of an array given the maximum jump length at each position.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the last index of the array is reachable starting from the first index.

    Args:
        nums: A list of non-negative integers where each element represents 
              the maximum jump length from that position.

    Returns:
        True if the last index is reachable, False otherwise.

    Examples:
        >>> solve([2, 3, 1, 1, 4])
        True
        >>> solve([3, 2, 1, 0, 4])
        False
    """
    # The furthest index we can currently reach
    max_reachable_index = 0
    target_index = len(nums) - 1

    for current_index, max_jump in enumerate(nums):
        # If the current index is greater than the furthest index we can reach,
        # it means we have hit a gap (like a 0) that we cannot cross.
        if current_index > max_reachable_index:
            return False

        # Update the furthest reachable index by comparing the current max
        # with the potential reach from the current position.
        max_reachable_index = max(max_reachable_index, current_index + max_jump)

        # Optimization: If we can already reach or exceed the target, return True.
        if max_reachable_index >= target_index:
            return True

    return max_reachable_index >= target_index
