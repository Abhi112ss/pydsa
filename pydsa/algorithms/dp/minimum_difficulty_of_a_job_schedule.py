METADATA = {
    "id": 1335,
    "name": "Minimum Difficulty of a Job Schedule",
    "slug": "minimum-difficulty-of-a-job-schedule",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 * d)",
    "space_complexity": "O(n * d)",
    "description": "Find the minimum difficulty to complete all jobs within a given number of days by partitioning the jobs array.",
}

def solve(job_difficulty: list[int], d: int) -> int:
    """
    Calculates the minimum difficulty to complete all jobs in d days.

    The difficulty of a day is the maximum difficulty of any job performed that day.
    The total difficulty is the sum of difficulties of all days.

    Args:
        job_difficulty: A list of integers representing the difficulty of each job.
        d: The number of days available to complete the jobs.

    Returns:
        The minimum total difficulty, or -1 if it is impossible to schedule.

    Examples:
        >>> solve([6, 5, 4, 3, 2, 1], 2)
        7
        >>> solve([6, 5, 4, 3, 2, 1], 3)
        9
        >>> solve([1, 1, 1], 3)
        3
        >>> solve([1, 1, 1], 4)
        -1
    """
    n = len(job_difficulty)

    # If there are fewer jobs than days, it's impossible to assign at least one job per day.
    if n < d:
        return -1

    # dp[i][j] represents the minimum difficulty to complete the first j jobs in i days.
    # Initialize with infinity.
    inf = float('inf')
    dp = [[inf] * (n + 1) for _ in range(d + 1)]

    # Base case: 0 days, 0 jobs has 0 difficulty.
    dp[0][0] = 0

    # Iterate through each day from 1 to d.
    for day in range(1, d + 1):
        # Iterate through each possible end job index for the current day.
        # A day must have at least one job, and we need enough jobs left for remaining days.
        for end_job in range(day, n + 1):
            current_max_difficulty = 0
            
            # Try all possible split points for the current day.
            # The current day starts from 'start_job' and ends at 'end_job - 1'.
            # We iterate backwards to update the max difficulty of the current day efficiently.
            for start_job in range(end_job, day - 1, -1):
                # Update the max difficulty encountered in the current day's partition.
                current_max_difficulty = max(current_max_difficulty, job_difficulty[start_job - 1])
                
                # If the previous days (day - 1) could successfully complete (start_job - 1) jobs,
                # update the DP state for the current day and end_job.
                if dp[day - 1][start_job - 1] != inf:
                    dp[day][end_job] = min(
                        dp[day][end_job], 
                        dp[day - 1][start_job - 1] + current_max_difficulty
                    )

    return int(dp[d][n]) if dp[d][n] != inf else -1
