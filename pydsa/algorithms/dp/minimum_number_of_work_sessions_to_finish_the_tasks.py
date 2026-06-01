METADATA = {
    "id": 1986,
    "name": "Minimum Number of Work Sessions to Finish the Tasks",
    "slug": "minimum-number-of-work-sessions-to-finish-the-tasks",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "bitmask", "subset_sum"],
    "difficulty": "hard",
    "time_complexity": "O(3^n)",
    "space_complexity": "O(2^n)",
    "description": "Find the minimum number of work sessions required to complete all tasks given a maximum session time.",
}

def solve(sessions: int, tasks: list[int]) -> int:
    """
    Calculates the minimum number of work sessions required to complete all tasks.

    Args:
        sessions: The maximum time allowed for a single work session.
        tasks: A list of integers representing the time required for each task.

    Returns:
        The minimum number of work sessions needed to finish all tasks.

    Examples:
        >>> solve(10, [2, 3, 4, 5, 6])
        3
        >>> solve(5, [1, 2, 3, 4, 5])
        3
    """
    n = len(tasks)
    num_subsets = 1 << n
    
    # dp[mask] stores the minimum number of sessions needed for the subset of tasks in 'mask'
    # Initialize with a value larger than any possible answer (n + 1)
    dp = [n + 1] * num_subsets
    
    # last_session_time[mask] stores the minimum time used in the last session 
    # for the subset of tasks in 'mask', given the minimum number of sessions.
    last_session_time = [0] * num_subsets
    
    # Base case: 0 tasks require 1 session (or 0, but 1 is safer for the logic) 
    # and 0 time used in that session.
    dp[0] = 1
    last_session_time[0] = 0
    
    for mask in range(num_subsets):
        for i in range(n):
            # If the i-th task is not yet in the current mask
            if not (mask & (1 << i)):
                next_mask = mask | (1 << i)
                task_time = tasks[i]
                
                # Option 1: Add the task to the current last session
                if last_session_time[mask] + task_time <= sessions:
                    new_sessions = dp[mask]
                    new_last_time = last_session_time[mask] + task_time
                # Option 2: Start a new session for this task
                else:
                    new_sessions = dp[mask] + 1
                    new_last_time = task_time
                
                # Update the DP state if we found a better way (fewer sessions, 
                # or same sessions with less time used in the last session)
                if new_sessions < dp[next_mask]:
                    dp[next_mask] = new_sessions
                    last_session_time[next_mask] = new_last_time
                elif new_sessions == dp[next_mask]:
                    if new_last_time < last_session_time[next_mask]:
                        last_session_time[next_mask] = new_last_time
                        
    return dp[num_subsets - 1]
