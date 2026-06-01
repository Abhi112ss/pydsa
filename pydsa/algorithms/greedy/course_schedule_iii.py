METADATA = {
    "id": 630,
    "name": "Course Schedule III",
    "slug": "course-schedule-iii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "heap", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of courses you can take given their durations and deadlines.",
}

import heapq

def solve(time: list[int], deadline: list[int]) -> int:
    """
    Calculates the maximum number of courses that can be completed.

    The algorithm uses a greedy approach: sort courses by their deadlines. 
    As we iterate through the sorted courses, we keep track of the total 
    time spent. If adding a course exceeds its deadline, we remove the 
    course with the longest duration from our current selection to 
    make room for potentially more, shorter courses later.

    Args:
        time: A list of integers representing the duration of each course.
        deadline: A list of integers representing the deadline of each course.

    Returns:
        The maximum number of courses that can be completed.

    Examples:
        >>> solve([1, 3, 4, 5], [2, 4, 5, 6])
        2
        >>> solve([1, 1, 1], [2, 2, 2])
        3
    """
    # Combine time and deadline into pairs and sort by deadline
    # Sorting by deadline is crucial for the greedy strategy
    courses = sorted(zip(deadline, time))
    
    # Max-heap to store durations of courses we have currently "accepted"
    # Python's heapq is a min-heap, so we store negative values to simulate a max-heap
    accepted_durations_heap: list[int] = []
    current_total_time: int = 0
    
    for d, t in courses:
        # Add the current course to our schedule
        heapq.heappush(accepted_durations_heap, -t)
        current_total_time += t
        
        # If the current total time exceeds the deadline of the current course,
        # we must discard one course to stay within the deadline.
        # To maximize the count, we discard the course with the largest duration.
        if current_total_time > d:
            # Pop the largest duration (stored as negative)
            longest_duration = -heapq.heappop(accepted_durations_heap)
            current_total_time -= longest_duration
            
    return len(accepted_durations_heap)
