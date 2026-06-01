METADATA = {
    "id": 3323,
    "name": "Minimize Connected Groups by Inserting Interval",
    "slug": "minimize_connected_groups_by_inserting_interval",
    "category": "Intervals",
    "aliases": [],
    "tags": ["intervals", "greedy", "sweep-line"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum reduction in the number of connected components (disjoint intervals) possible by adding a single interval of a fixed length.",
}

def solve(intervals: list[list[int]], k: int) -> int:
    """
    Calculates the maximum number of connected components that can be merged 
    into one by inserting a single interval of length k.

    The problem asks to minimize the number of connected groups. This is 
    equivalent to maximizing the number of existing disjoint groups that 
    the new interval can bridge.

    Args:
        intervals: A list of intervals where intervals[i] = [start_i, end_i].
        k: The length of the interval to be inserted.

    Returns:
        The minimum number of connected groups remaining after inserting the interval.

    Examples:
        >>> solve([[1, 2], [4, 5], [7, 8]], 2)
        1
        >>> solve([[1, 2], [4, 5], [7, 8]], 0)
        2
    """
    if not intervals:
        return 0

    # Step 1: Merge overlapping intervals to find the initial disjoint groups
    intervals.sort()
    merged = []
    if intervals:
        curr_start, curr_end = intervals[0]
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if next_start <= curr_end:
                curr_end = max(curr_end, next_end)
            else:
                merged.append([curr_start, curr_end])
                curr_start, curr_end = next_start, next_end
        merged.append([curr_start, curr_end])

    num_groups = len(merged)
    if num_groups <= 1:
        return num_groups

    # Step 2: Use a sliding window/two-pointer approach to find the maximum 
    # number of groups a single interval of length k can bridge.
    # A new interval [S, S+k] bridges groups if it touches or overlaps them.
    # To bridge 'm' groups, the interval must cover the gaps between them.
    
    # We want to find a range [S, S+k] that covers as many merged intervals as possible.
    # Specifically, if we pick a range that starts at the end of group i and 
    # ends at the start of group j, it bridges (j - i + 1) groups.
    # The condition is: merged[j].start - merged[i].end <= k
    
    max_bridged = 0
    left = 0
    
    # The interval [S, S+k] can bridge groups from index 'left' to 'right'
    # if the distance from the end of group 'left' to the start of group 'right'
    # is at most k. Note: The interval itself has length k, so its span is k.
    # However, the problem implies the interval is [x, x+k].
    # To bridge group i and group j, we need x <= merged[i].end (to touch i)
    # and x+k >= merged[j].start (to touch j).
    # Wait, the logic is: the interval [x, x+k] bridges groups if it 
    # intersects the intervals.
    # To bridge groups from index 'left' to 'right', we need:
    # merged[right].start - merged[left].end <= k
    
    for right in range(num_groups):
        # Shrink window from left if the gap between merged[left] and merged[right]
        # is greater than k.
        # The gap is the distance between the end of the first group and start of the last.
        while merged[right][0] - merged[left][1] > k:
            left += 1
        
        # Number of groups bridged is (right - left + 1)
        # But we only care if we actually bridge more than 1 group.
        # If we bridge 'm' groups, the total count reduces by (m - 1).
        # However, the question asks for the minimum number of groups.
        # If we bridge m groups, we replace m groups with 1 group.
        # New count = original_count - m + 1
        max_bridged = max(max_bridged, right - left + 1)

    # If max_bridged is 1, it means we didn't bridge any existing groups, 
    # we just added a new one (or overlapped one). 
    # But the problem asks to minimize groups. If we add an interval that 
    # overlaps an existing group, the count stays num_groups.
    # If we add an interval that bridges m groups, count becomes num_groups - m + 1.
    # If m=1, count = num_groups.
    # If m=0 (not possible here), count = num_groups + 1.
    
    # The maximum reduction is (max_bridged - 1) if max_bridged > 0.
    # But we must ensure we don't reduce below 1 if we actually bridge.
    # If max_bridged is 0, it means we just add a new group, but we want to MINIMIZE.
    # So we'd rather overlap an existing group.
    
    # If max_bridged is 1, we can just overlap an existing group, count remains num_groups.
    # If max_bridged > 1, we reduce the count.
    
    if max_bridged <= 1:
        # If we can't bridge, we can at least overlap an existing group to not increase count
        return num_groups
    
    return num_groups - (max_bridged - 1)
