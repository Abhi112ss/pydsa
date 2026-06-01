METADATA = {
    "id": 826,
    "name": "Most Profit Assigning Work",
    "slug": "most-profit-assigning-work",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["sorting", "two_pointer", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n + m log m)",
    "space_complexity": "O(n)",
    "description": "Assign jobs to workers to maximize total profit where each worker can take at most one job and job difficulty must be less than or equal to worker ability.",
}

def solve(difficulty: list[int], profit: list[int], ability: list[int]) -> int:
    """
    Calculates the maximum total profit that can be assigned to workers.

    Args:
        difficulty: A list of integers representing the difficulty of each job.
        profit: A list of integers representing the profit of each job.
        ability: A list of integers representing the ability of each worker.

    Returns:
        The maximum total profit that can be assigned to the workers.

    Examples:
        >>> solve([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
        110
        >>> solve([1, 2, 3, 4, 5], [30, 20, 10, 50, 40], [1, 2, 3, 4, 5])
        150
    """
    # Combine difficulty and profit into pairs and sort by difficulty
    # This allows us to process jobs in increasing order of difficulty
    jobs = sorted(zip(difficulty, profit))
    
    # Sort workers by ability to use a two-pointer approach
    # This allows us to maintain a running maximum profit for the current ability level
    sorted_abilities = sorted(ability)
    
    total_profit = 0
    max_profit_so_far = 0
    job_index = 0
    num_jobs = len(jobs)

    # Iterate through each worker in increasing order of ability
    for worker_ability in sorted_abilities:
        # For the current worker, check all jobs they can perform
        # Since workers are sorted, we don't need to re-check jobs for the next worker
        while job_index < num_jobs and jobs[job_index][0] <= worker_ability:
            # Update the maximum profit available for any job with difficulty <= current ability
            max_profit_so_far = max(max_profit_so_far, jobs[job_index][1])
            job_index += 1
        
        # Add the best possible profit found so far for this worker's ability
        total_profit += max_profit_so_far

    return total_profit
