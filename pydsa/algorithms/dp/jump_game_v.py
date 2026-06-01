METADATA = {
    "id": 1340,
    "name": "Jump Game V",
    "slug": "jump-game-v",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "memoization", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of jumps you can make starting from any index, moving only to strictly lower heights.",
}

def solve(height: list[int]) -> int:
    """
    Calculates the maximum number of jumps possible starting from any index.
    A jump is valid if the target index is within bounds and has a strictly lower height.

    Args:
        height: A list of integers representing the heights of the terrain.

    Returns:
        The maximum number of jumps that can be made.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        0
        >>> solve([5, 4, 3, 2, 1])
        4
        >>> solve([0, 4, 2, 1, 0])
        3
    """
    n = len(height)
    # memo[i] stores the maximum jumps possible starting from index i
    memo: list[int] = [-1] * n

    def get_max_jumps(current_index: int) -> int:
        """Recursive helper with memoization to find max jumps from a specific index."""
        if memo[current_index] != -1:
            return memo[current_index]

        max_jumps_from_here = 0

        # Check all possible jumps to the left
        for left in range(current_index - 1, -1, -1):
            if height[left] < height[current_index]:
                # If valid, the path length is 1 + the max jumps from the target index
                max_jumps_from_here = max(max_jumps_from_here, 1 + get_max_jumps(left))
            else:
                # Since we are looking for strictly lower, we can't stop early 
                # because a further index might be lower.
                pass

        # Check all possible jumps to the right
        for right in range(current_index + 1, n):
            if height[right] < height[current_index]:
                max_jumps_from_here = max(max_jumps_from_here, 1 + get_max_jumps(right))
            else:
                pass

        memo[current_index] = max_jumps_from_here
        return max_jumps_from_here

    # We must try starting from every possible index to find the global maximum
    overall_max_jumps = 0
    for i in range(n):
        overall_max_jumps = max(overall_max_jumps, get_max_jumps(i))

    return overall_max_jumps
