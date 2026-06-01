METADATA = {
    "id": 2097,
    "name": "Valid Arrangement of Pairs",
    "slug": "valid-arrangement-of-pairs",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "eulerian_path", "hierholzer"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find a valid arrangement of pairs such that each pair's second element is the first element of the next pair, forming an Eulerian path.",
}

import collections

def solve(pairs: list[list[int]]) -> list[int]:
    """
    Finds a valid arrangement of pairs using Hierholzer's algorithm to find an Eulerian path.

    Args:
        pairs: A list of pairs where each pair is [u, v].

    Returns:
        A list of integers representing the valid arrangement.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 1]])
        [1, 2, 3, 1]
        >>> solve([[1, 2], [2, 1], [1, 3]])
        [2, 1, 3, 1, 2] (or other valid permutations)
    """
    # Build adjacency list and track in-degrees and out-degrees
    adj = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)
    out_degree = collections.defaultdict(int)
    nodes = set()

    for u, v in pairs:
        adj[u].append(v)
        out_degree[u] += 1
        in_degree[v] += 1
        nodes.add(u)
        nodes.add(v)

    # An Eulerian path exists if:
    # 1. All nodes with non-zero degree belong to a single connected component.
    # 2. For all nodes, in_degree == out_degree, OR
    #    exactly one node has out_degree - in_degree = 1 (start)
    #    and exactly one node has in_degree - out_degree = 1 (end).
    start_node = next(iter(nodes))
    for node in nodes:
        if out_degree[node] - in_degree[node] == 1:
            start_node = node
            break

    path = []
    stack = [start_node]

    # Hierholzer's algorithm to find the Eulerian path
    while stack:
        curr = stack[-1]
        if adj[curr]:
            # If the current node has outgoing edges, traverse one
            next_node = adj[curr].pop()
            stack.append(next_node)
        else:
            # If no more outgoing edges, backtrack and add to path
            path.append(stack.pop())

    # The path is constructed in reverse order
    result = path[::-1]
    return result
