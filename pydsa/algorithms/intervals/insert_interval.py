METADATA = {
    "id": 57,
    "name": "Insert Interval",
    "slug": "insert-interval",
    "category": "Intervals",
    "aliases": [],
    "tags": ["array", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Insert a new interval into a sorted list of non-overlapping intervals and merge if necessary.",
}

def solve(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    Inserts a new interval into a sorted list of non-overlapping intervals.

    Args:
        intervals: A list of non-overlapping intervals sorted by start time.
        new_interval: The interval to be inserted.

    Returns:
        A new list of non-overlapping intervals after insertion and merging.

    Examples:
        >>> solve([[1,3],[6,9]], [2,5])
        [[1, 5], [6, 9]]
        >>> solve([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
        [[1, 2], [3, 10], [12, 16]]
    """
    result: list[list[int]] = []
    n = len(intervals)
    index = 0

    # 1. Add all intervals that end before the new interval starts
    while index < n and intervals[index][1] < new_interval[0]:
        result.append(intervals[index])
        index += 1

    # 2. Merge all overlapping intervals with the new interval
    # An interval overlaps if its start is less than or equal to the new interval's end
    while index < n and intervals[index][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[index][0])
        new_interval[1] = max(new_interval[1], intervals[index][1])
        index += 1
    
    # Add the merged (or single) new interval
    result.append(new_interval)

    # 3. Add the remaining intervals that start after the new interval ends
    while index < n:
        result.append(intervals[index])
        index += 1

    return result
