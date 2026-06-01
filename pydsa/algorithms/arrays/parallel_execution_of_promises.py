METADATA = {
    "id": 2795,
    "name": "Parallel Execution of Promises for Individual Results Retrieval",
    "slug": "parallel-execution-of-promises-for-individual-results-retrieval",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Simulate the execution of promises and return the order in which their results are retrieved based on their resolution times.",
}

def solve(execution_times: list[int], resolution_times: list[int]) -> list[int]:
    """
    Simulates the parallel execution of promises and returns the order of result retrieval.

    Each promise starts at time 0. A promise i finishes its execution at 
    execution_times[i] and then takes resolution_times[i] to resolve.
    The result is retrieved at time: execution_times[i] + resolution_times[i].

    Args:
        execution_times: A list of integers representing the time taken to execute each promise.
        resolution_times: A list of integers representing the time taken to resolve each promise.

    Returns:
        A list of integers representing the 1-indexed IDs of the promises in the order 
        they are resolved. If two promises resolve at the same time, the one with the 
        smaller ID comes first.

    Examples:
        >>> solve([1, 2, 3], [1, 1, 1])
        [1, 2, 3]
        >>> solve([3, 2, 1], [1, 1, 1])
        [3, 2, 1]
        >>> solve([1, 1, 1], [2, 1, 3])
        [2, 1, 3]
    """
    # The total time for a promise to be retrieved is the sum of its 
    # execution time and its resolution time.
    # We store tuples of (total_time, promise_id) to handle sorting.
    # promise_id is 1-indexed as per problem requirements.
    
    retrieval_events = []
    
    for i in range(len(execution_times)):
        total_time = execution_times[i] + resolution_times[i]
        promise_id = i + 1
        retrieval_events.append((total_time, promise_id))
    
    # Sort the events. Python's sort is stable and handles tuples by 
    # comparing the first element, then the second. 
    # This naturally handles the tie-breaking rule: if total_time is equal, 
    # the smaller promise_id comes first.
    retrieval_events.sort()
    
    # Extract the sorted IDs into the final result list.
    return [event[1] for event in retrieval_events]
