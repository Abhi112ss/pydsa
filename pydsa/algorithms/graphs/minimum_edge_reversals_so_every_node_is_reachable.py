METADATA = {
    "id": 2858,
    "name": "Minimum Edge Reversals So Every Node Is Reachable",
    "slug": "minimum-edge-reversals-so-every-node-is-reachable",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "bfs"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of edge reversals needed so that every node in a tree is reachable from a chosen root.",
}

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Calculates the minimum edge reversals needed for each node to be a root 
    that can reach all other nodes.

    Args:
        n: The number of nodes in the tree.
        edges: A list of directed edges where edges[i] = [u, v] means u -> v.

    Returns:
        A list of integers where the i-th integer is the minimum reversals 
        needed if node i is the root.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        [0, 1, 2]
        >>> solve(3, [[0, 1], [2, 1]])
        [1, 2, 1]
    """
    # adjacency_list stores (neighbor, weight)
    # weight 0 means the edge exists in the original direction (u -> v)
    # weight 1 means the edge is a reversal (v -> u)
    adjacency_list: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    
    for u, v in edges:
        # Original edge u -> v costs 0 reversals if we move u to v
        adjacency_list[u].append((v, 0))
        # To move v to u, we must reverse the edge, costing 1 reversal
        adjacency_list[v].append((u, 1))

    reversals_needed: list[int] = [0] * n

    def compute_initial_root_cost(current_node: int, parent: int) -> int:
        """
        DFS to calculate the total reversals needed if node 0 is the root.
        """
        total_cost = 0
        for neighbor, cost in adjacency_list[current_node]:
            if neighbor != parent:
                # Add the cost of this edge + cost of the subtree
                total_cost += cost + compute_initial_root_cost(neighbor, current_node)
        return total_cost

    # Step 1: Calculate cost for node 0 using DFS
    reversals_needed[0] = compute_initial_root_cost(0, -1)

    # Step 2: Use Re-rooting DP (Tree DP) to calculate costs for all other nodes in O(n)
    # If we move the root from 'u' to its neighbor 'v':
    # - If the edge was u -> v (cost 0), moving root to v increases cost by 1 (v -> u)
    # - If the edge was v -> u (cost 1), moving root to v decreases cost by 1 (v -> u is now original)
    # More simply: new_cost = old_cost - (cost of u->v) + (cost of v->u)
    # Since cost(u->v) + cost(v->u) is always 1 in our weight scheme:
    # new_cost = old_cost - cost_uv + (1 - cost_uv) is not quite right.
    # Let's use: new_cost = old_cost + (1 if edge is u->v else -1)
    # Wait, if edge is u->v (cost 0), moving root to v means we now need to reverse v->u.
    # So cost increases by 1. If edge is v->u (cost 1), moving root to v means 
    # we no longer need to reverse v->u, so cost decreases by 1.
    
    stack = [(0, -1)]
    while stack:
        u, parent = stack.pop()
        for v, cost in adjacency_list[u]:
            if v != parent:
                # If cost is 0, edge is u -> v. Moving root to v requires reversing v -> u.
                # If cost is 1, edge is v -> u. Moving root to v uses the existing v -> u.
                if cost == 0:
                    reversals_needed[v] = reversals_needed[u] + 1
                else:
                    reversals_needed[v] = reversals_needed[u] - 1
                stack.append((v, u))

    return reversals_needed
