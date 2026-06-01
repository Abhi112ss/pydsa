METADATA = {
    "id": 1824,
    "name": "Minimum Sideway Jumps",
    "slug": "minimum-sideway-jumps",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of sideway jumps to reach the end of a track given obstacles in three lanes.",
}

def solve(lines: list[list[int]], max_jump_distance: int) -> int:
    """
    Calculates the minimum number of sideway jumps required to reach the end.

    Args:
        lines: A 2D list where lines[i][j] is 1 if there is an obstacle 
               at lane i, position j, and 0 otherwise.
        max_jump_distance: The maximum distance one can jump forward.

    Returns:
        The minimum number of sideway jumps needed.

    Examples:
        >>> solve([[0,0,0,0,0],[0,1,0,1,0],[0,0,0,0,0]], 1)
        0
        >>> solve([[0,1,0,0,0],[0,0,0,1,0],[0,0,0,0,0]], 1)
        1
    """
    # dp[i] represents the minimum sideway jumps to reach the current position in lane i.
    # We initialize with 0 for the starting lane (lane 0) and 1 for others 
    # because we must jump into lanes 1 and 2 to start there.
    dp = [0, 1, 1]
    n = len(lines[0])

    for pos in range(1, n):
        # Step 1: Update lanes that have an obstacle at the current position.
        # If a lane has an obstacle, it's impossible to be in that lane at this position.
        # We use infinity to represent an invalid state.
        for lane in range(3):
            if lines[lane][pos] == 1:
                dp[lane] = float('inf')

        # Step 2: Calculate the minimum jumps needed for lanes without obstacles.
        # A lane's value is either its current value (staying in the lane)
        # or the minimum jumps needed to jump from another valid lane.
        # We perform two passes (or a single pass with min logic) to ensure 
        # we account for jumping from lane A -> B -> C or B -> A.
        
        # First pass: check if jumping from a previous lane (left to right) is better
        # Second pass: check if jumping from a subsequent lane (right to left) is better
        # However, since sideway jumps are instantaneous at the same position, 
        # we can simply find the minimum of the valid lanes and update.
        
        min_val = min(dp)
        
        for lane in range(3):
            if lines[lane][pos] == 0:
                # If the current lane is not an obstacle, we can either stay in it
                # or jump from the best available lane at this position.
                # Jumping from another lane adds 1 to the min_val.
                dp[lane] = min(dp[lane], min_val + 1)

    # The answer is the value in the starting lane (lane 0) at the last position.
    # Since we are guaranteed to reach the end, dp[0] will hold the result.
    return int(dp[0])
