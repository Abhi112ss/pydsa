METADATA = {
    "id": 3879,
    "name": "Maximum Distinct Path Sum in a Binary Tree",
    "slug": "maximum_distinct_path_sum_in_a_binary_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a path in a binary tree where all node values in the path are distinct.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Finds the maximum sum of a path in a binary tree where all node values 
    in the path are distinct.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum sum of a path with distinct node values. Returns 0 if tree is empty.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(2))
        >>> solve(root)
        3
        >>> root = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(3))
        >>> solve(root)
        6
    """
    if not root:
        return 0

    max_path_sum = float('-inf')

    def dfs(node: TreeNode | None, visited_values: set[int]) -> int:
        """
        Helper function to find the maximum path sum starting from 'node' 
        going downwards, ensuring all values are distinct.
        """
        nonlocal max_path_sum
        if not node:
            return 0

        # If the current node's value is already in the path, this branch is invalid
        if node.val in visited_values:
            return float('-inf')

        # Add current value to the set to maintain distinctness for children
        visited_values.add(node.val)

        # Explore left and right subtrees
        left_sum = dfs(node.left, visited_values)
        right_sum = dfs(node.right, visited_values)

        # A path can be: just the node, node + left, node + right, or node + left + right
        # However, the problem asks for a path (usually defined as a sequence of connected nodes).
        # In standard LeetCode "path sum" problems, a path can go from a node down to a leaf.
        # If the path can "bend" (like diameter), we handle it by updating the global max.
        
        # Case 1: Path goes through node and potentially branches into both sides
        # Note: This is only valid if both sides return valid (non -inf) sums.
        current_branch_sum = node.val
        
        # We calculate the max sum of a path that "bends" at this node
        # We only consider positive contributions from children to maximize the sum
        left_contribution = max(0, left_sum) if left_sum != float('-inf') else 0
        right_contribution = max(0, right_sum) if right_sum != float('-inf') else 0
        
        # Update the global maximum with the path that bends at this node
        # We check if the path is valid (node.val is distinct, which is guaranteed by the set)
        max_path_sum = max(max_path_sum, node.val + left_contribution + right_contribution)

        # Backtrack: remove the current node's value so other branches can use it
        visited_values.remove(node.val)

        # Return the maximum sum of a single downward path starting from this node
        return node.val + max(0, left_sum, right_sum) if max(left_sum, right_sum) != float('-inf') else node.val

    # We need to handle the case where the path doesn't necessarily start at the root
    # The DFS above explores all paths by treating every node as a potential "highest" node in a path.
    # However, the 'visited_values' logic in the current DFS structure is designed for 
    # paths starting from a specific ancestor. To find ANY distinct path, we must 
    # ensure that for every node, we check the max path where that node is the highest point.
    
    # To correctly implement "any path with distinct values", we use a slightly different approach:
    # For every node, we find the max sum of a path where this node is the highest point.
    # A path is distinct if all nodes in it are unique.
    
    def find_max_distinct_path(node: TreeNode | None) -> int:
        nonlocal max_path_sum
        if not node:
            return 0
        
        # This is a standard tree traversal. For each node, we find the max distinct 
        # downward path from left and right.
        # But "distinct" is tricky because a path can't reuse a value from its own ancestors.
        # Since we want the maximum sum of ANY path, we can iterate through all nodes
        # and for each node, perform a DFS to find the max sum path starting there.
        # Given the O(n^2) constraint, this is acceptable.
        return 0

    # Re-implementing with the O(n^2) approach: 
    # For each node, find the max sum of a path starting at that node and going downwards.
    # Then, for each node, find the max sum of a path that "bends" at that node.
    
    def get_max_downward_path(u: TreeNode | None, seen: set[int]) -> int:
        if not u or u.val in seen:
            return float('-inf')
        
        seen.add(u.val)
        l = get_max_downward_path(u.left, seen)
        r = get_max_downward_path(u.right, seen)
        seen.remove(u.val)
        
        res = u.val
        best_child = max(l, r)
        if best_child != float('-inf'):
            res += max(0, best_child)
        return res

    # To find the max path that "bends" at node 'u', we need to find two 
    # downward paths from 'u' that are collectively distinct.
    # This is complex. Let's simplify: A path is a sequence of nodes.
    # A path is distinct if all values are unique.
    
    # Correct O(n^2) approach:
    # For every node 'u', find the max sum of a path where 'u' is the highest node.
    # This path consists of 'u' and two downward paths (one left, one right).
    # The union of nodes in these two paths must have distinct values.
    
    def get_all_paths(u: TreeNode | None, seen: set[int], current_sum: int, path_vals: set[int]):
        """Helper to collect all possible downward paths from a node."""
        if not u or u.val in seen:
            return
        
        seen.add(u.val)
        path_vals.add(u.val)
        current_sum += u.val
        
        # Store the result (sum, set_of_values)
        # But we only need the max sum for a specific set of values to avoid O(2^n)
        # Actually, for a fixed 'u', we can just DFS to find all valid downward paths.
        
        # This is getting complicated. Let's use the simplest O(n^2) interpretation:
        # For every node, start a DFS to find the max sum path starting at that node.
        # Then, for every node, try to combine two paths.
        pass

    # Final attempt at logic:
    # For each node in the tree, treat it as the "root" of a potential path.
    # A path can go from some node A up to some node B and down to some node C.
    # But in a tree, a path is uniquely defined by its two endpoints.
    # For every pair of nodes (u, v), check if the path is distinct and calculate sum.
    # This is O(n^2).
    
    nodes = []
    def collect_nodes(curr: TreeNode | None):
        if not curr: return
        nodes.append(curr)
        collect_nodes(curr.left)
        collect_nodes(curr.right)
    
    collect_nodes(root)
    
    # Precompute parent pointers to find paths between any two nodes
    parent = {root: None}
    def build_parents(curr: TreeNode | None):
        if not curr: return
        if curr.left:
            parent[curr.left] = curr
            build_parents(curr.left)
        if curr.right:
            parent[curr.right] = curr
            build_parents(curr.right)
    build_parents(root)

    def get_path(u: TreeNode, v: TreeNode) -> list[int]:
        # Find path using LCA logic or simple climbing
        path_u = []
        curr = u
        while curr:
            path_u.append(curr)
            curr = parent[curr]
        
        path_v = []
        curr = v
        while curr:
            path_v.append(curr)
            curr = parent[curr]
            
        # Find LCA
        i = len(path_u) - 1
        j = len(path_v) - 1
        lca = None
        while i >= 0 and j >= 0 and path_u[i] == path_v[j]:
            lca = path_u[i]
            i -= 1
            j -= 1
        
        # Path is u -> LCA -> v
        final_path = []
        # u to LCA
        curr = u
        while curr != lca:
            final_path.append(curr.val)
            curr = parent[curr]
        final_path.append(lca.val)
        # LCA to v (reverse of v to LCA)
        temp_v = []
        curr = v
        while curr != lca:
            temp_v.append(curr.val)
            curr = parent[curr]
        final_path.extend(reversed(temp_v))
        return final_path

    ans = float('-inf')
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            path_vals = get_path(nodes[i], nodes[j])
            if len(path_vals) == len(set(path_vals)):
                ans = max(ans, sum(path_vals))
                
    return int(ans) if ans != float('-inf') else 0

# Note: The O(n^2) implementation above is a conceptual brute force.
# A more efficient O(n^2) uses DFS from each node to find all valid paths.

def solve_optimized(root: TreeNode | None) -> int:
    if not root:
        return 0

    max_sum = float('-inf')

    def dfs_from_node(u: TreeNode | None, current_sum: int, visited: set[int]):
        nonlocal max_sum
        if not u or u.val in visited:
            return
        
        new_sum = current_sum + u.val
        max_sum = max(max_sum, new_sum)
        
        visited.add(u.val)
        dfs_from_node(u.left, new_sum, visited)
        dfs_from_node(u.right, new_sum, visited)
        visited.remove(u.val)

    # To find any path (not just downward), we can observe that any path 
    # has a "highest" node (the LCA of the endpoints).
    # For every node 'u', we want to find two downward paths starting from 'u'
    # such that all nodes in the combined path are distinct.
    
    def get_downward_paths(u: TreeNode | None, visited: set[int]) -> list[tuple[int, set[int]]]:
        """Returns a list of (sum, set_of_values) for all valid downward paths."""
        if not u or u.val in visited:
            return []
        
        visited.add(u.val)
        # Base case: the path containing only the node itself
        results = [(u.val, {u.val})]
        
        # Get paths from children
        left_paths = get_downward_paths(u.left, visited)
        right_paths = get_downward_paths(u.right, visited)
        
        for l_sum, l_set in left_paths:
            results.append((u.val + l_sum, l_set | {u.val}))
        for r_sum, r_set in right_paths:
            results.append((u.val + r_sum, r_set | {u.val}))
            
        visited.remove(u.val)
        return results

    # The actual optimal O(n^2) for "any path" is:
    # For each node 'u', find all valid downward paths. 
    # Then try to combine a left-downward path and a right-downward path.
    
    def find_all_downward(u: TreeNode | None, visited: set[int]) -> list[tuple[int, set[int]]]:
        if not u or u.val in visited:
            return []
        
        visited.add(u.val)
        # A path can be just the node
        paths = [(u.val, {u.val})]
        
        # Or node + path from left
        for l_sum, l_set in find_all_downward(u.left, visited):
            paths.append((u.val + l_sum, l_set | {u.val}))
            
        # Or node + path from right
        for r_sum, r_set in find_all_downward(u.right, visited):
            paths.append((u.val + r_sum, r_set | {u.val}))
            
        visited.remove(u.val)
        return paths

    # Let's use the most robust O(n^2) approach:
    # For every node, perform a DFS to find all possible paths starting at that node.
    # Since a path is just a sequence of nodes, and we want to find the max sum,
    # we can just start a DFS from every single node.
    # A path starting at 'u' can go to any node 'v' in the tree.
    # But wait, a path in a tree is a simple path. 
    # If we start a DFS from 'u', we can explore all paths starting at 'u'.
    # To cover all paths, we just need to start a DFS from every node.
    
    def dfs_all_paths(u: TreeNode | None, current_sum: int, visited: set[int]):
        nonlocal max_sum
        if not u or u.val in visited:
            return
        
        new_sum = current_sum + u.val
        max_sum = max(max_sum, new_sum)
        
        visited.add(u.val)
        # In a tree, from node 'u', a path can go to its parent or its children.
        # If we start a DFS from every node and only move to neighbors (parent/child),
        # we will cover all possible simple paths.
        
        # To avoid infinite loops and ensure we only move along simple paths,
        # we use the 'visited' set.
        
        # We need access to parents.
        # Let's build an adjacency list.
        pass

    # Final implementation strategy:
    # 1. Build adjacency list (node -> [children, parent])
    # 2. For each node, run a DFS to find the max sum path starting at that node.
    # 3. Use a 'visited' set to ensure the path is simple and values are distinct.
    
    adj = {}
    def build_adj(u: TreeNode | None, p: TreeNode | None):
        if not u: return
        if u not in adj: adj[u] = []
        if p: adj[u].append(p)
        if u.left:
            adj[u].append(u.left)
            build_adj(u.left, u)
        if u.right:
            adj[u].append(u.right)
            build_adj(u.right, u)

    build_adj(root, None)
    
    all_nodes = []
    def collect(u: TreeNode | None):
        if not u: return
        all_nodes.append(u)
        collect(u.left)
        collect(u.right)
    collect(root)

    final_max = float('-inf')

    for start_node in all_nodes:
        # DFS to find all simple paths starting at start_node
        stack = [(start_node, start_node.val, {start_node.val})]
        # Using a stack for iterative DFS to avoid recursion depth issues
        # stack element: (current_node, current_sum, visited_values_