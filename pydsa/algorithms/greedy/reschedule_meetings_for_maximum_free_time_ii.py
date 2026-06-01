METADATA = {
    "id": 3440,
    "name": "Reschedule Meetings for Maximum Free Time II",
    "slug": "reschedule-meetings-for-maximum-free-time-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array", "intervals"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if it is possible to reschedule at most one meeting to any other gap to maximize the continuous free time.",
}

def solve(eventTime: int, meetings: list[list[int]]) -> bool:
    """
    Determines if we can reschedule at most one meeting to create a larger continuous gap.

    Args:
        eventTime: The total duration of the day.
        meetings: A list of meetings where meetings[i] = [start_i, end_i].

    Returns:
        True if we can achieve a continuous free time greater than the current maximum, False otherwise.

    Examples:
        >>> solve(5, [[1, 2], [3, 4]])
        True
        >>> solve(5, [[1, 2], [3, 4]])
        False
    """
    n = len(meetings)
    
    # Calculate gaps between meetings
    # Gap 0 is before the first meeting, Gap n is after the last meeting
    gaps = []
    gaps.append(meetings[0][0])
    for i in range(1, n):
        gaps.append(meetings[i][0] - meetings[i-1][1])
    gaps.append(eventTime - meetings[-1][1])
    
    # Precompute prefix and suffix maximums of gaps to check if a meeting 
    # can fit into any gap other than its immediate neighbors.
    prefix_max = [0] * (n + 1)
    suffix_max = [0] * (n + 1)
    
    current_max = 0
    for i in range(n + 1):
        current_max = max(current_max, gaps[i])
        prefix_max[i] = current_max
        
    current_max = 0
    for i in range(n, -1, -1):
        current_max = max(current_max, gaps[i])
        suffix_max[i] = current_max

    max_free_time = 0
    for i in range(n + 1):
        max_free_time = max(max_free_time, gaps[i])
    
    # The current maximum free time is the largest existing gap.
    # However, if we move a meeting, we merge two adjacent gaps.
    # Let's check if moving meeting 'i' (which is between gap i and gap i+1)
    # can result in a larger gap.
    
    for i in range(n):
        # If we move meeting i, the new gap formed by merging its neighbors is:
        # gaps[i] + duration_of_meeting_i + gaps[i+1]
        # But wait, the problem asks for the maximum *continuous* free time.
        # If we move meeting i, the two gaps adjacent to it merge:
        combined_gap = gaps[i] + gaps[i+1] + (meetings[i][1] - meetings[i][0])
        # Wait, that's not right. If we move meeting i, the gap becomes:
        # gaps[i] + duration_of_meeting_i + gaps[i+1] is the space occupied by the meeting and its gaps.
        # The actual continuous free time created by removing meeting i is gaps[i] + duration + gaps[i+1]? No.
        # If we remove meeting i, the new gap is gaps[i] + (meeting_i_duration) + gaps[i+1].
        # BUT, we can only do this if the meeting i can fit into SOME OTHER gap.
        
        meeting_duration = meetings[i][1] - meetings[i][0]
        new_gap_if_moved = gaps[i] + gaps[i+1] + meeting_duration
        # Actually, the question is: can we move meeting i to another gap?
        # If we move meeting i, the gap at its old position becomes gaps[i] + meeting_duration + gaps[i+1].
        # No, the gap becomes gaps[i] + meeting_duration + gaps[i+1] ONLY if we move it.
        # The gap created is gaps[i] + meeting_duration + gaps[i+1].
        # Wait, the gap is the space between meetings. 
        # If we remove meeting i, the space between meeting i-1 and i+1 is:
        # (start of i+1) - (end of i-1) = (start of i+1 - end of i) + (end of i - start of i) + (start of i - end of i-1)
        # = gaps[i+1] + duration_i + gaps[i].
        
        # Let's re-evaluate:
        # If we move meeting i, the new gap at its old location is gaps[i] + meeting_duration + gaps[i+1].
        # But we can only do this if meeting i fits into some OTHER gap j (where j != i and j != i+1).
        
        # Find the largest gap available that is not gaps[i] or gaps[i+1]
        best_other_gap = 0
        if i > 0:
            best_other_gap = max(best_other_gap, prefix_max[i-1])
        if i + 2 <= n:
            best_other_gap = max(best_other_gap, suffix_max[i+2])
            
        # Case 1: We move meeting i to another gap.
        # The new gap at the old position is gaps[i] + meeting_duration + gaps[i+1].
        # This is only possible if meeting_duration <= best_other_gap.
        if best_other_gap >= meeting_duration:
            max_free_time = max(max_free_time, gaps[i] + meeting_duration + gaps[i+1])
        else:
            # If we can't move it to a completely different gap, we can still 
            # just "slide" it within its own combined gap (gaps[i] + duration + gaps[i+1])
            # but that doesn't increase the continuous free time beyond gaps[i] + gaps[i+1].
            # Actually, if we can't move it elsewhere, the best we can do is 
            # merge the two gaps by sliding the meeting to one side.
            max_free_time = max(max_free_time, gaps[i] + gaps[i+1])

    # The logic above is slightly flawed. Let's refine:
    # A meeting i is between gap i and gap i+1.
    # If we move meeting i, the new gap is gaps[i] + meeting_duration + gaps[i+1].
    # This is only possible if meeting_duration <= some gap j (j != i and j != i+1).
    # If we can't move it elsewhere, the best we can do is move it to the edge of its 
    # current combined gap, resulting in a single gap of size (gaps[i] + gaps[i+1]).
    
    # Let's re-calculate max_free_time correctly.
    # The current max_free_time is the max of all gaps.
    # We want to see if we can get a gap > current_max.
    
    current_max_gap = max(gaps)
    possible_max = current_max_gap
    
    for i in range(n):
        meeting_duration = meetings[i][1] - meetings[i][0]
        # Option A: Move meeting i to another gap.
        # The gap at its old position becomes gaps[i] + meeting_duration + gaps[i+1].
        # This is only possible if meeting_duration <= max(gaps[j] for j != i, i+1).
        
        other_gap_max = 0
        if i > 0:
            other_gap_max = max(other_gap_max, prefix_max[i-1])
        if i + 2 <= n:
            other_gap_max = max(other_gap_max, suffix_max[i+2])
            
        if other_gap_max >= meeting_duration:
            possible_max = max(possible_max, gaps[i] + meeting_duration + gaps[i+1])
        else:
            # Option B: We can't move it to another gap, but we can slide it 
            # to merge gaps[i] and gaps[i+1].
            possible_max = max(possible_max, gaps[i] + gaps[i+1])
            
    return possible_max > current_max_gap

# The logic above is still a bit messy. Let's write the clean version.

def solve_final(eventTime: int, meetings: list[list[int]]) -> bool:
    """
    Correct implementation of the logic.
    """
    n = len(meetings)
    gaps = []
    gaps.append(meetings[0][0])
    for i in range(1, n):
        gaps.append(meetings[i][0] - meetings[i-1][1])
    gaps.append(eventTime - meetings[-1][1])
    
    prefix_max = [0] * (n + 1)
    suffix_max = [0] * (n + 1)
    
    curr = 0
    for i in range(n + 1):
        curr = max(curr, gaps[i])
        prefix_max[i] = curr
        
    curr = 0
    for i in range(n, -1, -1):
        curr = max(curr, gaps[i])
        suffix_max[i] = curr
        
    max_gap = max(gaps)
    
    for i in range(n):
        duration = meetings[i][1] - meetings[i][0]
        # The gap created by removing meeting i is gaps[i] + duration + gaps[i+1]
        # BUT this is only if we can place 'duration' somewhere else.
        # If we can't, the best we can do is merge gaps[i] and gaps[i+1] 
        # by sliding the meeting to one side, resulting in gaps[i] + gaps[i+1].
        
        # Check if meeting i can fit in any other gap
        other_max_gap = 0
        if i > 0:
            other_max_gap = max(other_max_gap, prefix_max[i-1])
        if i + 2 <= n:
            other_max_gap = max(other_max_gap, suffix_max[i+2])
            
        if other_max_gap >= duration:
            # We can move it elsewhere, so the new gap is the combined space
            if gaps[i] + duration + gaps[i+1] > max_gap:
                return True
        else:
            # We can only slide it, so the new gap is just the two gaps merged
            if gaps[i] + gaps[i+1] > max_gap:
                return True
                
    return False

# Re-assigning to solve for the final structure
solve = solve_final