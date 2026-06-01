METADATA = {
    "id": 851,
    "name": "Loud and Rich",
    "slug": "loud-and-rich",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "topological_sort", "graph", "memoization"],
    "difficulty": "medium",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n)",
    "description": "Find the quietest person among those who are richer than or equal to each person.",
}

def solve(richer: list[list[int]], quiet: list[int]) -> list[int]:
    """
    Finds the quietest person among those who are richer than or equal to each person.

    Args:
        richer: A list of pairs [a, b] where person a is richer than person b.
        quiet: A list where quiet[i] is the quietness level of person i.

    Returns:
        A list where result[i] is the index of the quietest person among those 
        who are richer than or equal to person i.

    Examples:
        >>> solve([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 8])
        [1, 1, 2, 4, 4, 4, 4, 7]
    """
    n = len(quiet)
    # Build an adjacency list where adj[i] contains people who are richer than i
    # Note: The input [a, b] means a -> b (a is richer). 
    # To find people richer than i, we need to traverse the graph in reverse: b -> a.
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in richer:
        adj[v].append(u)

    # memo[i] stores the index of the quietest person found so far in the richer hierarchy of i
    memo: list[int] = [-1] * n

    def dfs(person: int) -> int:
        """Performs DFS with memoization to find the quietest person in the richer chain."""
        if memo[person] != -1:
            return memo[person]

        # Start by assuming the person themselves is the quietest
        quietest_person = person

        # Explore all people who are directly richer than the current person
        for richer_person in adj[person]:
            candidate = dfs(richer_person)
            # Update if the candidate found via recursion is quieter
            if quiet[candidate] < quiet[quietest_person]:
                quietest_person = candidate

        memo[person] = quietest_person
        return quietest_person

    # Compute the result for every person
    results: list[int] = []
    for i in range(n):
        results.append(dfs(i))

    return results
