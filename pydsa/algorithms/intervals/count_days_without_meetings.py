METADATA = {
    "id": 3169,
    "name": "Count Days Without Meetings",
    "slug": "count-days-without-meetings",
    "category": "Intervals",
    "aliases": [],
    "tags": ["intervals", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the number of days between 1 and n that do not fall within any given meeting intervals.",
}

def solve(n: int, meetings: list[list[int]]) -> int:
    """
    Calculates the number of days from 1 to n that are not covered by any meeting.

    Args:
        n (int): The total number of days.
        meetings (list[list[int]]): A list of intervals [start, end] representing meeting times.

    Returns:
        int: The count of days without meetings.

    Examples:
        >>> solve(10, [[2, 3], [5, 8]])
        4
        >>> solve(5, [[1, 5]])
        0
        >>> solve(10, [[1, 2], [2, 3], [4, 5]])
        5
    """
    if not meetings:
        return n

    # Sort meetings by start time to allow linear merging
    meetings.sort()

    total_meeting_days = 0
    
    # Initialize the current merged interval with the first meeting
    current_start = meetings[0][0]
    current_end = meetings[0][1]

    for i in range(1, len(meetings)):
        next_start, next_end = meetings[i]

        if next_start <= current_end:
            # Overlapping or adjacent intervals: extend the current end
            current_end = max(current_end, next_end)
        else:
            # No overlap: add the duration of the completed interval and start a new one
            total_meeting_days += (current_end - current_start + 1)
            current_start = next_start
            current_end = next_end

    # Add the final merged interval
    total_meeting_days += (current_end - current_start + 1)

    # The result is the total days minus the days covered by meetings
    return n - total_meeting_days
