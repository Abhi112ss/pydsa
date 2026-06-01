METADATA = {
    "id": 2212,
    "name": "Maximum Points in an Archery Competition",
    "slug": "maximum-points-in-an-archery-competition",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum points achievable by selecting non-overlapping intervals of targets, where each interval must contain at least one target and all targets in an interval must be in the same direction.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the maximum points achievable in an archery competition.

    The problem is solved using dynamic programming. We first group targets by 
    direction and sort them by position. We then use a DP approach where 
    dp[i] represents the maximum points achievable using a subset of the 
    first i targets.

    Args:
        points: A list of [position, direction, points] for each target.

    Returns:
        The maximum total points possible.

    Examples:
        >>> solve([[1,1,1],[2,2,1],[3,3,1]])
        3
        >>> solve([[1,1,1],[2,2,1],[3,1,1]])
        2
    """
    # Sort points by position to ensure we process them in spatial order
    points.sort()
    n = len(points)
    
    # dp[i] will store the maximum points using targets from index 0 to i-1
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # Option 1: Do not include the i-th target in any interval
        dp[i] = dp[i - 1]
        
        current_pos, current_dir, current_pts = points[i - 1]
        
        # Option 2: The i-th target is the LAST target in an interval
        # We look backwards to find all possible starting points 'j' for this interval
        # An interval [j, i-1] is valid if all targets in it have the same direction
        # and we pick at least one target from it.
        
        # To maximize points in an interval [j, i-1], we must pick all targets 
        # in that range that have the same direction as the current target.
        
        # However, the problem states we pick an interval and all targets in it 
        # must be in the same direction. This implies we pick a range [j, i-1] 
        # such that we only count points for targets with current_dir.
        # But the constraint is actually: "all targets in the chosen interval 
        # must be in the same direction". This means for a chosen range [j, i-1],
        # every target k where j <= k <= i-1 must have points[k].direction == current_dir.
        
        # Wait, re-reading: "Each interval must contain at least one target, 
        # and all targets in the interval must be in the same direction."
        # This means if we pick an interval [j, i-1], then for all k in [j, i-1],
        # points[k].direction must be the same.
        
        # Let's refine: We are looking for a contiguous subsegment of the sorted 
        # points where all elements have the same direction.
        
        # Let's find the largest possible contiguous block ending at i-1 
        # that has the same direction.
        
        running_sum = 0
        for j in range(i - 1, -1, -1):
            pos_j, dir_j, pts_j = points[j]
            
            # If the direction changes, this interval is no longer valid 
            # according to the "all targets in the interval must be in the same direction" rule.
            if dir_j != current_dir:
                break
            
            # Add points of the current target in the valid direction block
            running_sum += pts_j
            
            # dp[i] = max(dp[i], dp[j] + running_sum)
            # where dp[j] is the max points from targets before this interval
            if dp[j] + running_sum > dp[i]:
                dp[i] = dp[j] + running_sum

    return dp[n]
