METADATA = {
    "id": 2323,
    "name": "Find Minimum Time to Finish All Jobs II",
    "slug": "find-minimum-time-to-finish-all-jobs-ii",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "bitmask_dp", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(k^n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum maximum load assigned to any worker when distributing jobs among k workers.",
}

def solve(jobs: list[int], k: int) -> int:
    """
    Finds the minimum possible maximum load assigned to any worker.

    This problem is solved using binary search on the answer combined with 
    backtracking (with pruning) to check if a specific maximum load is feasible.

    Args:
        jobs: A list of integers representing the load of each job.
        k: The number of workers available.

    Returns:
        The minimum maximum load assigned to any worker.

    Examples:
        >>> solve([1, 2, 4, 7, 8], 2)
        15
        >>> solve([3, 2, 3], 3)
        3
    """
    # Sort jobs in descending order to improve pruning efficiency in backtracking
    jobs.sort(reverse=True)
    n = len(jobs)
    worker_loads = [0] * k

    def can_finish(job_index: int, max_load: int) -> bool:
        """
        Backtracking helper to check if jobs can be assigned without exceeding max_load.
        """
        if job_index == n:
            return True

        current_job_weight = jobs[job_index]

        for i in range(k):
            # If adding this job doesn't exceed the current limit
            if worker_loads[i] + current_job_weight <= max_load:
                worker_loads[i] += current_job_weight
                if can_finish(job_index + 1, max_load):
                    return True
                worker_loads[i] -= current_job_weight

            # Pruning 1: If the worker has 0 load and the job couldn't be placed,
            # then trying this job in other empty workers won't change the outcome.
            if worker_loads[i] == 0:
                break
            
            # Pruning 2: If the job exactly fills the worker to the limit and failed,
            # there's no point in trying to distribute this job differently for this branch.
            if worker_loads[i] + current_job_weight == max_load:
                break

        return False

    # Binary search range for the possible maximum load
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
