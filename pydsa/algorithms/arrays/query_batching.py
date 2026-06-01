METADATA = {
    "id": 2756,
    "name": "Query Batching",
    "slug": "query_batching",
    "category": "Simulation",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Minimize the number of execution calls by grouping consecutive queries with identical properties.",
}

def solve(queries: list[list[int]]) -> int:
    """
    Calculates the minimum number of execution calls required to process a sequence of queries.
    A batch can be formed if consecutive queries have the same parameters.

    Args:
        queries: A list of queries where each query is a list of integers [param1, param2, ..., paramK].

    Returns:
        The total number of execution calls (batches) required.

    Examples:
        >>> solve([[1, 2], [1, 2], [3, 4], [1, 2]])
        3
        >>> solve([[1], [1], [1]])
        1
        >>> solve([[1, 2], [3, 4], [5, 6]])
        3
    """
    if not queries:
        return 0

    # Initialize count to 1 because the first query always starts the first batch
    batch_count = 1
    
    # The number of parameters in each query is assumed to be consistent
    num_params = len(queries[0])

    for i in range(1, len(queries)):
        # Compare the current query with the previous one
        # If any parameter differs, the current batch must end and a new one starts
        is_same_batch = True
        for j in range(num_params):
            if queries[i][j] != queries[i - 1][j]:
                is_same_batch = False
                break
        
        if not is_same_batch:
            batch_count += 1

    return batch_count
