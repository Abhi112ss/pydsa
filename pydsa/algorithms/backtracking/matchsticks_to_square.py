METADATA = {
    "id": 473,
    "name": "Matchsticks to Square",
    "slug": "matchsticks-to-square",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "dfs", "bitmask", "partition"],
    "difficulty": "medium",
    "time_complexity": "O(4^n)",
    "space_complexity": "O(n)",
    "description": "Determine if a set of matchsticks can be arranged to form a square by partitioning them into four equal sides.",
}

def solve(matchsticks: list[int]) -> bool:
    """
    Determines if the given matchsticks can form a square.

    Args:
        matchsticks: A list of integers representing the lengths of matchsticks.

    Returns:
        True if a square can be formed, False otherwise.

    Examples:
        >>> solve([1,1,2,2,2])
        True
        >>> solve([3,3,3,3,4])
        False
    """
    total_sum = sum(matchsticks)
    n = len(matchsticks)

    # A square must have 4 equal sides, so total sum must be divisible by 4
    # and we must have at least 4 matchsticks.
    if total_sum % 4 != 0 or n < 4:
        return False

    target_side_length = total_sum // 4
    
    # Sort matchsticks in descending order to fail fast in the backtracking process.
    # Larger sticks are harder to fit, so placing them first prunes the search tree.
    matchsticks.sort(reverse=True)

    # If the largest stick is longer than the target side, a square is impossible.
    if matchsticks[0] > target_side_length:
        return False

    # sides[i] stores the current length of the i-th side of the square.
    sides = [0] * 4

    def backtrack(index: int) -> bool:
        """
        Recursive helper to assign each matchstick to one of the four sides.

        Args:
            index: The index of the current matchstick being processed.

        Returns:
            True if the current matchstick can lead to a valid square.
        """
        # Base case: All matchsticks have been successfully assigned.
        if index == n:
            return True

        current_stick = matchsticks[index]

        for i in range(4):
            # Try placing the current stick in side i if it doesn't exceed the target.
            if sides[i] + current_stick <= target_side_length:
                sides[i] += current_stick
                
                if backtrack(index + 1):
                    return True
                
                # Backtrack: remove the stick to try the next side.
                sides[i] -= current_stick

            # Optimization 1: If the side is empty (0), and the stick didn't work,
            # there's no point trying this stick in other empty sides because
            # they are functionally identical.
            if sides[i] == 0:
                break
            
            # Optimization 2: If adding the stick makes the side exactly the target,
            # and it failed later, trying it in another side won't help either.
            if sides[i] + current_stick == target_side_length:
                break

        return False

    return backtrack(0)
