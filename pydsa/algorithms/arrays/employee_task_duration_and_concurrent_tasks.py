METADATA = {
    "id": 3156,
    "name": "Employee Task Duration and Concurrent Tasks",
    "slug": "employee-task-duration-and-concurrent-tasks",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "sorting", "sweep-line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum number of concurrent tasks being performed by employees using a sweep-line algorithm.",
}

def solve(tasks: list[list[int]]) -> int:
    """
    Calculates the maximum number of tasks occurring simultaneously.

    Args:
        tasks: A list of tasks, where each task is represented as [start_time, end_time].
               The end_time is inclusive for the duration of the task.

    Returns:
        The maximum number of overlapping tasks at any point in time.

    Examples:
        >>> solve([[1, 5], [2, 3], [4, 6]])
        2
        >>> solve([[1, 10], [2, 3], [4, 5], [6, 7]])
        2
        >>> solve([[1, 2], [2, 3], [3, 4]])
        2
    """
    if not tasks:
        return 0

    # To handle inclusive end times, we treat the task as active from 
    # start_time to end_time. In a sweep-line, an event at 'time' 
    # that starts a task should be processed before an event that 
    # ends a task if they occur at the same time, OR we treat 
    # the end as occurring slightly after the time.
    # Standard approach for inclusive intervals: 
    # Start event: (time, +1), End event: (time, -1)
    # However, if a task ends at 5 and another starts at 5, they overlap.
    # To ensure they overlap, we process '+1' events before '-1' events 
    # for the same timestamp.
    
    events = []
    for start, end in tasks:
        # Use -1 for start and 1 for end to sort start before end 
        # when using a simple sort, but it's clearer to use explicit types.
        # We want to process 'start' events before 'end' events at the same time.
        events.append((start, -1)) 
        events.append((end, 1))

    # Sort by time. If times are equal, the second element (-1) 
    # ensures the 'start' event comes before the 'end' event.
    events.sort()

    max_concurrent = 0
    current_concurrent = 0

    for _, type_flag in events:
        if type_flag == -1:
            # It's a start event
            current_concurrent += 1
        else:
            # It's an end event
            # Note: Because we want to count the end time as inclusive,
            # we only decrement AFTER checking the max if we were 
            # processing strictly. But with the -1/1 trick, 
            # the 'start' at time T is processed, then 'end' at time T.
            # Wait, if task is [1, 2] and [2, 3], they overlap at 2.
            # Events: (1, -1), (2, 1), (2, -1), (3, 1)
            # Sorted: (1, -1), (2, -1), (2, 1), (3, 1)
            # This correctly counts 2 at time 2.
            current_concurrent -= 1
        
        # Update the global maximum
        if current_concurrent > max_concurrent:
            max_concurrent = current_concurrent

    # Re-evaluating the logic for inclusive intervals:
    # If task is [1, 2], it exists at time 1 and time 2.
    # If we use (start, -1) and (end, 1), and sort:
    # [1, 2] -> (1, -1), (2, 1)
    # [2, 3] -> (2, -1), (3, 1)
    # Sorted: (1, -1), (2, -1), (2, 1), (3, 1)
    # Process (1, -1): curr=1, max=1
    # Process (2, -1): curr=2, max=2
    # Process (2, 1):  curr=1, max=2
    # Process (3, 1):  curr=0, max=2
    # This works perfectly for inclusive intervals.

    # Let's refine the loop to be more robust.
    # The logic above is actually correct. Let's rewrite the loop 
    # slightly to be cleaner.
    
    max_concurrent = 0
    current_concurrent = 0
    
    # Re-sorting with explicit logic:
    # We want to process all starts at time T before all ends at time T
    # to capture the maximum overlap at that instant.
    events.sort(key=lambda x: (x[0], x[1]))

    for _, type_flag in events:
        if type_flag == -1:
            current_concurrent += 1
        else:
            # We must check max_concurrent BEFORE decrementing if 
            # we want to count the end time as part of the overlap.
            # Actually, the current_concurrent already includes the 
            # task that is about to end.
            pass
        
        # If we use the -1/1 trick, the 'start' increments current,
        # then we check max, then the 'end' decrements.
        # But if multiple tasks start/end at the same time, 
        # we want to see the peak.
        
        # Correct Sweep-line for inclusive:
        # 1. Add all starts at time T
        # 2. Update Max
        # 3. Subtract all ends at time T
        # This is achieved by sorting starts (-1) before ends (1).
        
        if type_flag == -1:
            # Start event
            current_concurrent += 1
            if current_concurrent > max_concurrent:
                max_concurrent = current_concurrent
        else:
            # End event
            # We don't update max here because the peak was 
            # already captured when the task was active.
            current_concurrent -= 1
            
    return max_concurrent
