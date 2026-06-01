METADATA = {
    "id": 45,
    "name": "Jump Game II",
    "slug": "jump-game-ii",
    "category": "Dynamic Programming / Greedy",
    "aliases": [],
    "tags": ["greedy", "array", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of jumps to reach the last index of an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of jumps required to reach the last index.

    Args:
        nums: A list of non-negative integers where each element represents 
              the maximum jump length from that position.

    Returns:
        The minimum number of jumps needed to reach the last index.

    Examples:
        >>> solve([2, 3, 1, 1, 4])
        1
        >>> solve([2, 3, 0, 1, 4])
        2
    """
    n = len(nums)
    if n <= 1:
        return 0

    jumps = 0
    current_jump_end = 0
    farthest_reach = 0

    # We iterate up to n - 1 because once we reach or can reach 
    # the last index, we don't need to jump from it.
    for i in range(n - 1):
        # Update the farthest index we can reach from the current position
        farthest_reach = max(farthest_reach, i + nums[i])

        # If we have reached the end of the range of the current jump,
        # we must make another jump to proceed further.
        if i == current_jump_end:
            jumps += 1
            current_jump_end = farthest_reach
            
            # Optimization: if the current range already reaches the end, we can stop
            if current_jump_end >= n - 1:
                break

    return jumps
