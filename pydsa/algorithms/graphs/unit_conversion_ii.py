METADATA = {
    "id": 3535,
    "name": "Unit Conversion II",
    "slug": "unit-conversion-ii",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "hash_map", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(N + Q)",
    "space_complexity": "O(N)",
    "description": "Find the conversion factor between two units using a graph-based approach where units are nodes and conversion factors are weighted edges.",
}

from collections import deque, defaultdict

def solve(conversions: list[list[float]], queries: list[list[str]]) -> list[float]:
    """
    Finds the conversion factor between two units based on a list of given conversions.

    Args:
        conversions: A list of lists where each sublist contains [from_unit, to_unit, factor].
            Example: [["m", "cm", 100.0], ["cm", "mm", 10.0]]
        queries: A list of queries where each query is [start_unit, end_unit].

    Returns:
        A list of floats representing the conversion factor for each query. 
        Returns -1.0 if no conversion path exists.

    Examples:
        >>> solve([["m", "cm", 100.0], ["cm", "mm", 10.0]], [["m", "mm"], ["m", "km"]])
        [1000.0, -1.0]
    """
    # Build an adjacency list representing the graph.
    # Each entry in graph[u] is a tuple (v, factor) meaning 1 unit of u = factor units of v.
    graph = defaultdict(list)
    for u, v, factor in conversions:
        graph[u].append((v, factor))
        # Also add the inverse relationship: 1 unit of v = (1/factor) units of u.
        graph[v].append((u, 1.0 / factor))

    results = []

    for start_unit, end_unit in queries:
        if start_unit == end_unit:
            results.append(1.0)
            continue
        
        # Use BFS to find the conversion factor from start_unit to end_unit.
        # We store (current_unit, cumulative_factor) in the queue.
        queue = deque([(start_unit, 1.0)])
        visited = {start_unit}
        found_factor = -1.0

        while queue:
            current_node, current_factor = queue.popleft()

            if current_node == end_unit:
                found_factor = current_factor
                break

            for neighbor, multiplier in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # The new factor is the current cumulative factor multiplied by the edge weight.
                    queue.append((neighbor, current_factor * multiplier))
            
            if found_factor != -1.0:
                break
        
        results.append(found_factor)

    return results
