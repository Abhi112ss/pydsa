METADATA = {
    "id": 1229,
    "name": "Meeting Scheduler",
    "slug": "meeting-scheduler",
    "category": "Intervals",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "intervals"],
    "difficulty": "medium",
    "time_complexity": "O(n log n + m log m)",
    "space_complexity": "O(1)",
    "description": "Find the earliest time slot of a given duration that is available in both provided schedules.",
}

def solve(scheduler1: list[list[int]], scheduler2: list[list[int]], duration: int) -> list[int]:
    """
    Args:
        scheduler1: A list of intervals representing available time slots in the first person's schedule.
        scheduler2: A list of intervals representing available time slots in the second person's schedule.
        duration: The required length of the meeting.

    Returns:
        The earliest available time slot [start, end] that satisfies the duration, or [-1, -1] if none exists.
    """
    scheduler1.sort()
    scheduler2.sort()

    index1 = 0
    index2 = 0

    while index1 < len(scheduler1) and index2 < len(scheduler2):
        start1, end1 = scheduler1[index1]
        start2, end2 = scheduler2[index2]

        overlap_start = max(start1, start2)
        overlap_end = min(end1, end2)

        if overlap_end - overlap_start >= duration:
            return [overlap_start, overlap_start + duration]

        if end1 < end2:
            index1 += 1
        else:
            index2 += 1

    return [-1, -1]