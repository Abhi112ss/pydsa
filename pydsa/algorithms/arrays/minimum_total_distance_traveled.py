METADATA = {
    "id": 2463,
    "name": "Minimum Total Distance Traveled",
    "slug": "minimum-total-distance-traveled",
    "category": "Math",
    "aliases": [],
    "tags": ["prefix_sum", "two_pointer", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum total distance traveled by two robots to meet at a single point on a 1D line.",
}

def solve(robots: list[int], meeting_point: int) -> int:
    """
    Calculates the total distance traveled by two robots to reach a specific meeting point.

    Args:
        robots: A list of integers representing the positions of the robots.
        meeting_point: The coordinate where the robots meet.

    Returns:
        The total distance traveled by all robots.

    Examples:
        >>> solve([1, 5, 10], 5)
        9
        >>> solve([1, 2, 3], 2)
        2
    """
    total_distance = 0
    for position in robots:
        total_distance += abs(position - meeting_point)
    return total_distance

def min_total_distance(robots: list[int], meeting_point: int) -> int:
    """
    Finds the minimum total distance traveled by two robots to meet at a single point.
    
    The problem asks for the minimum distance to meet at a point 'x' such that 
    x is within the range [meeting_point, max(robots)]. However, the problem 
    actually implies we want to find a point 'x' that minimizes the sum of 
    distances, subject to the constraint that the robots can only move 
    towards or away from the meeting_point in a specific way.
    
    Actually, the problem asks for the minimum distance to meet at a point 'x' 
    where x >= meeting_point. The optimal 'x' is the median of the robots' 
    positions, but we must also satisfy x >= meeting_point.
    
    Args:
        robots: A list of integers representing the positions of the robots.
        meeting_point: The coordinate where the robots must meet or pass.

    Returns:
        The minimum total distance traveled.

    Examples:
        >>> min_total_distance([1, 5, 10], 2)
        9
        >>> min_total_distance([1, 2, 3], 2)
        2
    """
    n = len(robots)
    # Sort robots to use prefix sums and median properties
    # Note: The problem constraints usually imply robots are already sorted or 
    # we need to sort them to find the median.
    sorted_robots = sorted(robots)
    
    # Precompute prefix sums to calculate range sums in O(1)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + sorted_robots[i]
        
    def get_sum(left: int, right: int) -> int:
        """Returns the sum of elements in sorted_robots from index left to right inclusive."""
        if left > right:
            return 0
        return prefix_sums[right + 1] - prefix_sums[left]

    # The optimal meeting point 'x' must be >= meeting_point.
    # The function f(x) = sum|robots[i] - x| is convex.
    # The global minimum is at the median. 
    # If meeting_point <= median, the answer is the distance to the median.
    # If meeting_point > median, the answer is the distance to meeting_point.
    
    # Find the index of the first robot position that is >= meeting_point
    # using binary search (or just find where meeting_point fits in the sorted list)
    import bisect
    idx = bisect.bisect_left(sorted_robots, meeting_point)
    
    # The optimal x is max(meeting_point, median)
    # However, the problem is slightly different: we need to find x >= meeting_point
    # that minimizes sum|robots[i] - x|.
    # Since f(x) is convex, if meeting_point is to the left of the median, 
    # the minimum is at the median. If meeting_point is to the right of the median,
    # the minimum is at meeting_point.
    
    # Let's find the median index
    median_idx = (n - 1) // 2
    median_val = sorted_robots[median_idx]
    
    # The optimal x is max(meeting_point, median_val)
    # But wait, the problem says "the robots can only move to the right" 
    # or "the meeting point must be >= meeting_point".
    # Actually, the optimal x is the median of the set of robots, 
    # but we are constrained to x >= meeting_point.
    # Because f(x) is non-increasing until the median and non-decreasing after,
    # the minimum in the range [meeting_point, infinity) is:
    # 1. The median, if median >= meeting_point
    # 2. meeting_point, if meeting_point > median
    
    # However, there is a catch: the problem asks for the minimum distance 
    # where the meeting point x is such that x >= meeting_point.
    # Let's re-evaluate: the optimal x is max(meeting_point, median_of_robots).
    # But the median of robots is not necessarily a single value if n is even.
    # For even n, any value in [sorted_robots[n//2 - 1], sorted_robots[n//2]] is a median.
    # We want the smallest such value that is >= meeting_point.
    
    # Correct logic:
    # The function f(x) = sum |robots[i] - x| is minimized at the median.
    # If meeting_point <= median, the minimum is f(median).
    # If meeting_point > median, the minimum is f(meeting_point).
    
    # Let's find the median. For a sorted list, the median is at index (n-1)//2 
    # (or any value between (n-1)//2 and n//2).
    # Let's pick the smallest median: sorted_robots[(n-1)//2]
    
    # Wait, the problem is actually: find x >= meeting_point to minimize sum|robots[i] - x|.
    # Let's find the index 'k' such that sorted_robots[k] is the first element >= meeting_point.
    # If meeting_point is very large, x = meeting_point.
    # If meeting_point is very small, x = median.
    
    # Let's find the median index.
    # If n is odd, median is at n // 2.
    # If n is even, any value in [robots[n//2 - 1], robots[n//2]] is a median.
    
    # Let's find the optimal x.
    # We can use binary search on the value of x, but since f(x) is convex, 
    # we can just check the median and the meeting_point.
    
    # Let's find the median value. To be safe with even n, 
    # the median is any value in [sorted_robots[n//2 - 1], sorted_robots[n//2]].
    # We want to find x in [meeting_point, inf) that minimizes f(x).
    
    # Case 1: meeting_point <= sorted_robots[n//2 - 1] (if n even) or sorted_robots[n//2] (if n odd)
    # The minimum is at the median.
    # Case 2: meeting_point > median.
    # The minimum is at meeting_point.
    
    # Let's refine: The median is the value that minimizes sum|r_i - x|.
    # For sorted robots, any x in [sorted_robots[(n-1)//2], sorted_robots[n//2]] works.
    # We want the smallest x in this range that is >= meeting_point.
    # If meeting_point <= sorted_robots[(n-1)//2], then x = sorted_robots[(n-1)//2] is optimal.
    # If sorted_robots[(n-1)//2] < meeting_point <= sorted_robots[n//2], then x = meeting_point is optimal.
    # If meeting_point > sorted_robots[n//2], then x = meeting_point is optimal.
    
    # Actually, it's simpler:
    # The optimal x is max(meeting_point, sorted_robots[(n-1)//2] if we want the smallest median)
    # Wait, if n=2, robots=[1, 10], median is any x in [1, 10].
    # If meeting_point = 5, x=5 is a median, f(5) = |1-5| + |10-5| = 4+5=9.
    # If meeting_point = 0, x=1 is a median, f(1) = |1-1| + |10-1| = 9.
    # If meeting_point = 11, x=11 is the best, f(11) = |1-11| + |10-11| = 10+1=11.
    
    # So the optimal x is:
    # If meeting_point <= sorted_robots[(n-1)//2], x = sorted_robots[(n-1)//2] (or any median)
    # If meeting_point > sorted_robots[(n-1)//2], x = meeting_point is NOT necessarily optimal.
    # If meeting_point is within the median range [sorted_robots[(n-1)//2], sorted_robots[n//2]],
    # then meeting_point is itself a median, so f(meeting_point) is the minimum.
    # If meeting_point > sorted_robots[n//2], then meeting_point is to the right of the median,
    # so f(meeting_point) is the minimum.
    
    # Conclusion: The optimal x is max(meeting_point, sorted_robots[(n-1)//2]) is WRONG.
    # The optimal x is:
    # If meeting_point <= sorted_robots[(n-1)//2], x = sorted_robots[(n-1)//2]
    # If meeting_point > sorted_robots[(n-1)//2], x = meeting_point
    # Wait, let's re-check: if n=2, robots=[1, 10], meeting_point=5.
    # (n-1)//2 = 0. sorted_robots[0] = 1.
    # meeting_point (5) > 1, so x = 5. f(5) = 9. Correct.
    # If meeting_point = 0. 0 <= 1, so x = 1. f(1) = 9. Correct.
    # If meeting_point = 11. 11 > 1, so x = 11. f(11) = 11. Correct.
    
    # Let's try n=3, robots=[1, 5, 10], meeting_point=2.
    # (n-1)//2 = 1. sorted_robots[1] = 5.
    # meeting_point (2) <= 5, so x = 5. f(5) = |1-5| + |5-5| + |10-5| = 4+0+5 = 9. Correct.
    
    # Final logic:
    # target_x = max(meeting_point, sorted_robots[(n-1)//2]) is not quite right.
    # If meeting_point is 2 and median is 5, we want x=5.
    # If meeting_point is 6 and median is 5, we want x=6.
    # So target_x = max(meeting_point, sorted_robots[(n-1)//2]) is actually correct?
    # Let's re-verify:
    # If meeting_point = 2, median = 5 -> max(2, 5) = 5.
    # If meeting_point = 6, median = 5 -> max(6, 5) = 6.
    # Yes.
    
    # Wait, one more check. n=2, robots=[1, 10], meeting_point=5.
    # (n-1)//2 = 0. sorted_robots[0] = 1.
    # max(5, 1) = 5. Correct.
    
    # One more: n=4, robots=[1, 2, 10, 11], meeting_point=5.
    # (n-1)//2 = 1. sorted_robots[1] = 2.
    # max(5, 2) = 5.
    # f(5) = |1-5| + |2-5| + |10-5| + |11-5| = 4 + 3 + 5 + 6 = 18.
    # Is there a better x >= 5?
    # f(6) = 5 + 4 + 4 + 5 = 18.
    # f(10) = 9 + 8 + 0 + 1 = 18.
    # f(11) = 10 + 9 + 1 + 0 = 20.
    # So x=5 is indeed optimal.
    
    # Wait, what if meeting_point is 1?
    # max(1, 2) = 2. f(2) = 1 + 0 + 8 + 9 = 18.
    # f(1) = 0 + 1 + 9 + 10 = 20.
    # So x=2 is better.
    
    # The logic seems to be:
    # The function f(x) = sum |r_i - x| is minimized at any x in [sorted_robots[(n-1)//2], sorted_robots[n//2]].
    # We want to find x in [meeting_point, infinity) that minimizes f(x).
    # If meeting_point is within the median range, any x in [meeting_point, sorted_robots[n//2]] is optimal.
    # If meeting_point is to the left of the median range, the median range is available, so pick any x in the range.
    # If meeting_point is to the right of the median range, the best x is meeting_point.
    
    # So:
    # If meeting_point <= sorted_robots[(n-1)//2]:
    #    x = sorted_robots[(n-1)//2]
    # Else:
    #    x = meeting_point
    
    # This is exactly: target_x = max(meeting_point, sorted_robots[(n-1)//2])
    # Wait, let's re-check n=4, robots=[1, 2, 10, 11], meeting_point=5.
    # (n-1)//2 = 1. sorted_robots[1] = 2.
    # max(5, 2) = 5. Correct.
    
    # Let's re-check n=4, robots=[1, 2, 10, 11], meeting_point=1.
    # (n-1)//2 = 1. sorted_robots[1] = 2.
    # max(1, 2) = 2. Correct.
    
    # Wait, there's a slight edge case. If n=4, the median range is [2, 10].
    # If meeting_point = 5, it is inside [2, 10].
    # Any x in [5, 10] should give the same minimum distance.
    # Let's check x=5: f(5) = 4+3+5+6 = 18.
    # Let's check x=10: f(10) = 9+8+0+1 = 18.
    # Yes!
    
    # So the target_x is:
    # if meeting_point <= sorted_robots[(n-1)//2]:
    #     target_x = sorted_robots[(n-1)//2]
    # else:
    #     target_x = meeting_point
    
    # This is simply: target_x = max(meeting_point, sorted_robots[(n-1)//2])
    # Wait, let's check n=4, robots=[1, 2, 10, 11], meeting_point=15.
    # max(15, 2) = 15. f(15) = 14+13+5+4 = 36.
    # f(11) = 10+9+1+0 = 20.
    # Since 15 > 11, 15 is the best we can do. Correct.

    # Implementation using prefix sums for O(1) distance calculation
    # to ensure O(n