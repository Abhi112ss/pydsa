METADATA = {
    "id": 1024,
    "name": "Video Stitching",
    "slug": "video-stitching",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "intervals", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n log n) or O(n + T) depending on implementation",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of clips needed to cover a given time interval [0, T].",
}

def solve(clips: list[list[int]], time: int) -> int:
    """
    Finds the minimum number of clips required to cover the interval [0, time].

    Args:
        clips: A list of intervals where each interval is [start, end].
        time: The target end time.

    Returns:
        The minimum number of clips needed to cover [0, time], or -1 if impossible.

    Examples:
        >>> solve([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10)
        3
        >>> solve([[0,1],[1,2],[3,4]], 4)
        -1
    """
    # Sort clips by start time to process them in chronological order
    clips.sort()

    num_clips = 0
    current_end = 0
    furthest_reachable = 0
    i = 0
    n = len(clips)

    # We continue as long as the current covered range is less than the target time
    while current_end < time:
        # Look at all clips that start within the currently covered range [0, current_end]
        # and find the one that extends our reach the furthest.
        found_extension = False
        while i < n and clips[i][0] <= current_end:
            if clips[i][1] > furthest_reachable:
                furthest_reachable = clips[i][1]
                found_extension = True
            i += 1

        # If we couldn't find any clip that starts within our current range 
        # and extends beyond our current end, it's impossible to proceed.
        if furthest_reachable <= current_end:
            return -1

        # Greedily pick the clip that gave us the furthest reach
        current_end = furthest_reachable
        num_clips += 1

    return num_clips
