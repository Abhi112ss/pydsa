METADATA = {
    "id": 3439,
    "name": "Reschedule Meetings for Maximum Free Time I",
    "slug": "reschedule-meetings-for-maximum-free-time-i",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum continuous free time possible by rescheduling at most one meeting within a given time frame.",
}

def solve(eventTime: int, meetings: list[list[int]]) -> int:
    """
    Calculates the maximum continuous free time possible by rescheduling at most one meeting.

    The strategy is to identify all gaps between meetings (including gaps at the start 
    and end of the day). Since we can move one meeting, we can merge two adjacent 
    gaps if the meeting between them can be moved to some other available gap. 
    However, the problem constraints for version I allow us to simply move a meeting 
    to any other position, effectively allowing us to combine two adjacent gaps 
    into one, provided we don't exceed the total available space. 
    Actually, for version I, the rule is simpler: we can move one meeting to 
    anywhere else, which means we can combine two adjacent gaps by shifting the 
    meeting between them.

    Args:
        eventTime: The total duration of the day.
        meetings: A list of [start, end] intervals representing meetings.

    Returns:
        The maximum continuous free time available.

    Examples:
        >>> solve(5, [[1, 2], [3, 4]])
        2
        >>> solve(10, [[1, 2], [3, 4], [5, 6]])
        3
    """
    # Sort meetings by start time to ensure we process intervals in order
    meetings.sort()
    
    n = len(meetings)
    gaps = []
    
    # 1. Calculate all gaps between meetings
    # Gap before the first meeting
    gaps.append(meetings[0][0])
    
    # Gaps between consecutive meetings
    for i in range(1, n):
        gap = meetings[i][0] - meetings[i-1][1]
        gaps.append(gap)
        
    # Gap after the last meeting
    gaps.append(eventTime - meetings[-1][1])
    
    # 2. The core logic for version I:
    # We can move one meeting to any other location. 
    # Moving a meeting between two gaps effectively merges those two gaps 
    # and the meeting's duration is no longer a barrier.
    # However, the meeting itself must still fit somewhere.
    # In version I, the constraint is simply that we can combine two adjacent 
    # gaps by moving the meeting that separates them.
    
    max_free_time = 0
    
    # Check the maximum of any single gap
    for gap in gaps:
        if gap > max_free_time:
            max_free_time = gap
            
    # Check the maximum of any two adjacent gaps combined
    # Because we can move the meeting between them to any other gap 
    # (or just push it to the side), the two gaps become one continuous block.
    for i in range(len(gaps) - 1):
        combined_gap = gaps[i] + gaps[i+1]
        if combined_gap > max_free_time:
            max_free_time = combined_gap
            
    return max_free_time
