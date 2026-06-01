METADATA = {
    "id": 3373,
    "name": "Maximize the Number of Target Nodes After Connecting Trees II",
    "slug": "maximize-the-number-of-target-nodes-after-connecting-trees-ii",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "tree", "dp", "centroid_decomposition"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the number of target nodes in a forest by adding a single edge between two trees.",
}

from typing import List, Dict, Tuple

class Solver:
    """
    Solver for LeetCode 3373.
    
    The problem asks to connect two trees from a forest by adding one edge 
    to maximize the number of target nodes in the resulting connected component.
    Since we can only add one edge, we are essentially picking two trees 
    and merging them. To maximize target nodes, we should pick the two trees 
    that have the highest number of target nodes.
    """

    def solve(self, n: int, edges: List[List[int]], target_nodes: List[int]) -> int:
        """
        Calculates the maximum number of target nodes after connecting two trees.

        Args:
            n: The number of nodes in the forest.
            edges: A list of edges where edges[i] = [u, v].
            target_nodes: A list of nodes that are considered target nodes.

        Returns:
            The maximum number of target nodes in the largest connected component.

        Examples:
            >>> solver = Solver()
            >>> solver.solve(5, [[0, 1], [2, 3]], [0, 2, 4])
            3
        """
        # Build adjacency list
        adj: Dict[int, List[int]] = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        is_target = [False] * n
        for node in target_nodes:
            is_target[node] = True

        visited = [False] * n
        tree_target_counts: List[int] = []

        # Traverse each connected component (tree) to count its target nodes
        for i in range(n):
            if not visited[i]:
                current_tree_targets = 0
                stack = [i]
                visited[i] = True
                
                while stack:
                    u = stack.pop()
                    if is_target[u]:
                        current_tree_targets += 1
                    
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            stack.append(v)
                
                tree_target_counts.append(current_tree_targets)

        # If there is only one tree, we can't connect it to another tree.
        # However, the problem implies we add an edge between two trees.
        # If there's only one tree, the answer is just its target count.
        if len(tree_target_counts) < 2:
            return tree_target_counts[0] if tree_target_counts else 0

        # To maximize the target nodes in the new component, 
        # we pick the two trees with the largest number of target nodes.
        tree_target_counts.sort(reverse=True)
        
        # The result is the sum of the two largest target counts.
        # Note: If we have more than 2 trees, we only connect two.
        # The question asks for the max target nodes in the resulting component.
        return tree_target_counts[0] + tree_target_counts[1]

def solve(n: int, edges: List[List[int]], target_nodes: List[int]) -> int:
    """
    Entry point for the solver.
    """
    return Solver().solve(n, edges, target_nodes)
