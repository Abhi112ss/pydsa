METADATA = {
    "id": 2925,
    "name": "Maximum Score After Applying Operations on a Tree",
    "slug": "maximum-score-after-applying-operations-on-a-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree", "greedy", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum score by choosing an optimal set of edges to remove such that each component contains exactly one node with a value of 1.",
}

def solve(n: int, edges: list[list[int]], values: list[int]) -> int:
    """
    Calculates the maximum score after applying operations on a tree.
    
    The score is defined as the number of edges removed. We want to remove 
    edges such that every resulting connected component contains exactly one 
    node with value 1.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges where edges[i] = [u, v].
        values: A list where values[i] is 1 if node i has a 1, and 0 otherwise.

    Returns:
        The maximum number of edges that can be removed. Returns -1 if no 
        such configuration exists.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [1, 0, 1])
        1
        >>> solve(3, [[0, 1], [1, 2]], [1, 1, 1])
        -1
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # total_ones tracks how many nodes have value 1 in the entire tree
    total_ones = sum(values)
    
    # If there are no 1s, it's impossible to satisfy the condition
    if total_ones == 0:
        return -1

    removed_edges = 0
    possible = True

    def dfs(node: int, parent: int) -> int:
        """
        Post-order traversal to determine if a subtree can be detached.
        
        Returns:
            The number of 1s found in the subtree rooted at 'node'.
        """
        nonlocal removed_edges, possible
        
        # Base case: current node's contribution
        ones_in_subtree = values[node]
        
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            
            # Recursive call to process children
            subtree_ones = dfs(neighbor, node)
            
            # If a subtree contains exactly one '1', we can cut the edge 
            # connecting it to the current node.
            if subtree_ones == 1:
                removed_edges += 1
            # If a subtree contains more than one '1', it's invalid 
            # unless we can cut it into valid components (handled by recursion).
            # However, if a subtree has 0 ones, it must be merged upwards.
            elif subtree_ones == 0:
                # This subtree has no 1s, so it must be part of the parent's component
                pass
            else:
                # If subtree_ones > 1, it means the 1s in that subtree 
                # couldn't be isolated, which is only okay if they are 
                # eventually part of a valid component. 
                # But in a tree, if a subtree has > 1 ones and we can't 
                # cut them, the whole tree is invalid.
                # Actually, the logic is: if subtree_ones > 1, we can't 
                # cut this edge, and we must pass all those 1s up.
                pass
            
            ones_in_subtree += subtree_ones

        return ones_in_subtree

    # Start DFS from node 0
    root_ones = dfs(0, -1)

    # After DFS, the root component must also contain exactly one '1' 
    # if we consider the entire tree. However, the problem states 
    # every component must have exactly one 1. 
    # If the total number of 1s in the tree is not equal to the number 
    # of components we've identified, it's impossible.
    # A simpler check: if the root component has more than one '1', 
    # it's impossible. But since we only cut when subtree_ones == 1, 
    # the root_ones will naturally be the total_ones.
    
    # The condition for success is that we must be able to partition 
    # the tree such that every component has exactly one 1.
    # This is only possible if the number of components created (removed_edges + 1)
    # is equal to the total number of 1s.
    if removed_edges + 1 != total_ones:
        return -1

    return removed_edges
