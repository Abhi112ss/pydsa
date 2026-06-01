METADATA = {
    "id": 1723,
    "name": "Find Minimum Time to Finish All Jobs",
    "slug": "find-minimum-time-to-finish-all-jobs",
    "category": "Hard",
    "aliases": [],
    "tags": ["backtracking", "binary_search", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(k^n * log(sum(jobs)))",
    "space_complexity": "O(n)",
    "description": "Find the minimum maximum load assigned to any worker when distributing jobs.",
}

def solve(jobs: list[int], k: int) -> int:
    """
    Finds the minimum possible maximum load assigned to any worker.

    Args:
        jobs: A list of integers representing the time required for each job.
        k: The number of workers available.

    Returns:
        The minimum maximum load among all workers.

    Examples:
        >>> solve([3, 2, 3], 3)
        3
        >>> solve([1, 2, 4, 7, 8], 2)
        11
    """
    # Sort jobs in descending order to improve pruning efficiency in backtracking
    jobs.sort(reverse=True)
    n = len(jobs)
    worker_loads = [0] * k

    def can_finish(job_idx: int, max_load: int) -> bool:
        """
        Backtracking function to check if jobs can be distributed such that
        no worker exceeds the max_load.
        """
        if job_idx == n:
            return True

        current_job_weight = jobs[job_idx]

        for i in range(k):
            # If adding this job doesn't exceed the limit
            if worker_loads[i] + current_job_weight <= max_load:
                worker_loads[i] += current_job_weight
                if can_finish(job_idx + 1, max_load):
                    return True
                worker_loads[i] -= current_job_weight

            # Pruning 1: If this worker has 0 load and we couldn't fit the job,
            # then trying other empty workers won't help (symmetry breaking).
            if worker_loads[i] == 0:
                break
            
            # Pruning 2: If the job exactly fills the worker to the limit and 
            # it failed, there's no point trying to distribute it differently 
            # for this specific job at this level.
            if worker_loads[i] + current_job_weight == max_load:
                break

        return False

    # Binary search range: 
    # Low: the largest single job (a worker must at least take this)
    # High: the sum of all jobs (one worker takes everything)
    low = max(jobs)
    high = sum(jobs)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        # Reset worker loads for each feasibility check
        worker_loads = [0] * k
        if can_finish(0, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
