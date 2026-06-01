METADATA = {
    "id": 1514,
    "name": "Path with Maximum Probability",
    "slug": "path-with-maximum-probability",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "heap", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the maximum probability of reaching a destination node from a source node in a weighted graph.",
}

import heapq
from collections import defaultdict

def solve(n: int, edges: list[list[int]], succ_prob: list[float], start_node: int, end_node: int) -> float:
    """
    Finds the maximum probability of reaching the end_node from the start_node using Dijkstra's algorithm.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v].
        succ_prob: A list of probabilities where succ_prob[i] is the probability of success 
                   of the edge edges[i].
        start_node: The starting node index.
        end_node: The destination node index.

    Returns:
        The maximum probability of reaching end_node from start_node. Returns 0.0 if unreachable.

    Examples:
        >>> solve(3, [[0,1],[1,2],[0,2]], [0.5, 0.5, 0.2], 0, 2)
        0.25
        >>> solve(3, [[0,1],[1,2],[0,2]], [0.5, 0.5, 0.2], 0, 0)
        1.0
    """
    # Build adjacency list: graph[u] = [(v, probability), ...]
    graph = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        prob = succ_prob[i]
        graph[u].append((v, prob))
        graph[v].append((u, prob))

    # max_probs[i] stores the maximum probability found so far to reach node i
    max_probs = [0.0] * n
    max_probs[start_node] = 1.0

    # Max-heap to store (-probability, node). 
    # Python's heapq is a min-heap, so we negate probabilities to simulate a max-heap.
    priority_queue = [(-1.0, start_node)]

    while priority_queue:
        current_prob_neg, current_node = heapq.heappop(priority_queue)
        current_prob = -current_prob_neg

        # If we reached the destination, this is the maximum probability due to Dijkstra's property
        if current_node == end_node:
            return current_prob

        # If we found a better path to this node already, skip processing
        if current_prob < max_probs[current_node]:
            continue

        for neighbor, edge_prob in graph[current_node]:
            # Calculate the probability of reaching the neighbor via the current node
            new_prob = current_prob * edge_prob
            
            # If the new path offers a higher probability, update and push to heap
            if new_prob > max_probs[neighbor]:
                max_probs[neighbor] = new_prob
                heapq.heappush(priority_queue, (-new_prob, neighbor))

    return 0.0
