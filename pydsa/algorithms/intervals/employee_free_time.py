METADATA = {
    "id": 759,
    "name": "Employee Free Time",
    "slug": "employee-free-time",
    "category": "Hard",
    "aliases": [],
    "tags": ["heap", "sorting", "intervals"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the free time intervals that are common to all employees.",
}

from typing import Optional


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def solve(schedule: list[list[Interval]]) -> list[Interval]:
    """
    Finds the common free time intervals for all employees.

    The algorithm flattens all busy intervals, sorts them by start time,
    and merges overlapping intervals. The gaps between these merged 
    busy intervals represent the common free time.

    Args:
        schedule: A list of lists, where each sublist contains the busy 
            intervals of a single employee.

    Returns:
        A list of Interval objects representing the common free time.

    Examples:
        >>> schedule = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
        >>> result = solve(schedule)
        >>> [ (r.start, r.end) for r in result ]
        [(5, 6), (7, 9)]
    """
    # Flatten all intervals into a single list
    all_intervals: list[Interval] = []
    for employee_schedule in schedule:
        for interval in employee_schedule:
            all_intervals.append(interval)

    if not all_intervals:
        return []

    # Sort intervals by start time to allow linear merging
    all_intervals.sort(key=lambda x: x.start)

    free_time: list[Interval] = []
    
    # Initialize the current merged busy period with the first interval
    current_end = all_intervals[0].end

    for i in range(1, len(all_intervals)):
        next_interval = all_intervals[i]

        # If the next interval starts after the current merged end, 
        # there is a gap (free time) between them.
        if next_interval.start > current_end:
            free_time.append(Interval(current_end, next_interval.start))
            current_end = next_interval.end
        else:
            # Otherwise, extend the current merged busy period if necessary
            current_end = max(current_end, next_interval.end)

    return free_time
