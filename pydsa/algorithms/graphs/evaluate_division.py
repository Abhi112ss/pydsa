METADATA = {
    "id": 399,
    "name": "Evaluate Division",
    "slug": "evaluate-division",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph", "union-find"],
    "difficulty": "medium",
    "time_complexity": "O(Q * (V + E))",
    "space_complexity": "O(V + E)",
    "description": "Given equations representing division, evaluate the result of new division queries using a graph-based approach.",
}

from collections import defaultdict

def solve(equations: list[list[float]], values: list[float], queries: list[list[float]]) -> list[float]:
    """
    Evaluates division queries based on given equations and values using a graph approach.

    Args:
        equations: A list of pairs [A, B] representing the equation A / B.
        values: A list of values where values[i] is the result of equations[i][0] / equations[i][1].
        queries: A list of pairs [C, D] representing the query C / D.

    Returns:
        A list of floats representing the results of the queries. Returns -1.0 if a query is invalid.

    Examples:
        >>> solve([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["x", "x"]])
        [6.0, 0.5, -1.0, -1.0]
    """
    # Build an adjacency list where graph[u] = [(v, weight), ...]
    # weight represents the ratio u / v
    graph = defaultdict(dict)

    for (dividend, divisor), value in zip(equations, values):
        graph[dividend][divisor] = value
        graph[divisor][dividend] = 1.0 / value

    def dfs(current_node: str, target_node: str, visited: set[str]) -> float:
        """Performs a Depth First Search to find the product of weights from start to target."""
        # If the node doesn't exist in our graph, the division is impossible
        if current_node not in graph or target_node not in graph:
            return -1.0
        
        # Base case: target found
        if current_node == target_node:
            return 1.0

        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                result = dfs(neighbor, target_node, visited)
                # If a valid path is found through this neighbor, return the product
                if result != -1.0:
                    return weight * result

        return -1.0

    results = []
    for start, end in queries:
        # For each query, perform a fresh DFS search
        # Note: If start == end and start exists in graph, result is 1.0
        if start == end and start in graph:
            results.append(1.0)
        else:
            results.append(dfs(start, end, set()))

    return results
