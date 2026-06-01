METADATA = {
    "id": 646,
    "name": "Maximum Length of Pair Chain",
    "slug": "maximum-length-of-pair-chain",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["greedy", "dynamic_programming", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a chain of pairs where each pair (a, b) is followed by (c, d) such that b < c.",
}

def solve(pairs: list[list[int]]) -> int:
    """
    Calculates the maximum length of a chain of pairs using a greedy approach.

    The problem is equivalent to the Interval Scheduling Maximization Problem.
    To maximize the number of non-overlapping intervals, we should always
    pick the interval that finishes earliest. This leaves the most room
    for subsequent intervals.

    Args:
        pairs: A list of pairs where each pair is a list of two integers [start, end].

    Returns:
        The maximum length of the pair chain.

    Examples:
        >>> solve([[1, 2], [7, 8], [4, 5]])
        2
        >>> solve([[1, 2], [2, 3], [3, 4]])
        2
    """
    if not pairs:
        return 0

    # Sort pairs by their end values (the second element of each pair).
    # This is the greedy choice: finishing earlier allows more room for others.
    pairs.sort(key=lambda pair: pair[1])

    chain_length = 0
    current_end_time = float('-inf')

    for start, end in pairs:
        # If the current pair starts after the previous pair ended,
        # we can add this pair to our chain.
        if start > current_end_time:
            chain_length += 1
            current_end_time = end

    return chain_length
