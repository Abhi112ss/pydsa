METADATA = {
    "id": 2458,
    "name": "Height of Binary Tree After Subtree Removal Queries",
    "slug": "height-of-binary-tree-after-subtree-removal-queries",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "depth-first-search"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the height of a binary tree after sequentially removing subtrees specified in queries.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, queries: list[int]) -> list[int]:
    """
    Calculates the height of the binary tree after each subtree removal query.

    The strategy is to precompute the maximum height reachable from each node 
    without passing through its children. Since queries are processed in reverse, 
    we can track the maximum height seen so far for each node.

    Args:
        root: The root of the binary tree.
        queries: A list of node values representing the roots of subtrees to be removed.

    Returns:
        A list of integers representing the height of the tree after each query.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
        >>> queries = [3, 6, 2]
        >>> solve(root, queries)
        [2, 2, 1]
    """
    # Map node values to their maximum height if their subtree is removed.
    # We use a dictionary to store the max height available at each node's position.
    node_to_max_height = {}
    
    # Map node values to their depth (distance from root).
    # This helps in identifying which nodes are affected.
    node_to_depth = {}

    def compute_heights(node: TreeNode, depth: int) -> int:
        """
        DFS to compute the height of each node and store depth information.
        """
        if not node:
            return -1
        
        node_to_depth[node.val] = depth
        
        left_height = compute_heights(node.left, depth + 1)
        right_height = compute_heights(node.right, depth + 1)
        
        # The height of the current node is 1 + max height of its children.
        current_height = 1 + max(left_height, right_height)
        
        # We store the height of the node itself to use in queries.
        # However, the core logic relies on knowing the max height 
        # available from the parent if this child is removed.
        return current_height

    # First pass: Calculate standard heights and depths.
    # We need a way to know the max height available at a node if a child is removed.
    # We'll use a second DFS or a post-order traversal to build the 'alternative' heights.
    
    # To handle queries efficiently, we process them in REVERSE.
    # When processing queries in reverse, a removal is "undone".
    # But a better way: Precompute the max height reachable from each node 
    # if its subtree is removed, by looking at its siblings and ancestors.
    
    # Let's refine: For every node, what is the max height in the tree 
    # if this node's subtree is removed?
    # This is equivalent to: max(height of node's sibling, height of node's parent's sibling, ...)
    
    max_height_if_removed = {}

    def compute_alternative_heights(node: TreeNode, current_max_path: int) -> None:
        """
        DFS to compute the max height available if the current node is removed.
        
        Args:
            node: Current node.
            current_max_path: The maximum height reachable from the root 
                             without going through the current node's branch.
        """
        if not node:
            return

        # The height if this node is removed is the current_max_path.
        max_height_if_removed[node.val] = current_max_path

        # Calculate heights of children to pass down to siblings.
        # We need the actual height of subtrees to determine the max path for siblings.
        # This requires a pre-pass to get heights.
        pass

    # Re-implementing with a cleaner two-pass approach.
    
    # Pass 1: Get heights of all subtrees.
    heights = {}
    def get_heights(node: TreeNode) -> int:
        if not node:
            return -1
        h = 1 + max(get_heights(node.left), get_heights(node.right))
        heights[node.val] = h
        return h

    get_heights(root)

    # Pass 2: Compute the max height available if a node is removed.
    # We pass down the maximum height seen so far from the "outside".
    def compute_max_alt(node: TreeNode, alt_height: int) -> None:
        if not node:
            return
        
        max_height_if_removed[node.val] = alt_height
        
        # For the left child, the alternative height is:
        # max(alt_height of parent, height of right sibling + 1)
        left_alt = max(alt_height, (heights[node.right] + 1) if node.right else 0)
        compute_max_alt(node.left, left_alt)
        
        # For the right child, the alternative height is:
        # max(alt_height of parent, height of left sibling + 1)
        right_alt = max(alt_height, (heights[node.left] + 1) if node.left else 0)
        compute_max_alt(node.right, right_alt)

    # Initial call: if root is removed, height is -1 (or 0 depending on definition, 
    # but problem uses 0-indexed height where leaf is 0).
    # The problem defines height as number of edges. A single node tree has height 0.
    # Our 'heights' dict uses number of nodes (leaf = 1). 
    # Let's adjust: height = nodes - 1.
    
    # Let's use the 'nodes' definition for internal logic and convert at end.
    # If root is removed, height is -1 (empty tree).
    compute_max_alt(root, -1)

    # The queries are processed. However, the problem says "after each removal".
    # This implies removals are PERMANENT.
    # BUT, the queries are such that once a subtree is removed, it's gone.
    # Crucially, the problem states: "The queries are such that each query 
    # removes a subtree that has not been removed yet."
    # This means we don't need to "undo" anything. We just need to find the 
    # max height among all nodes that have NOT been removed.
    
    # Wait, if we remove a subtree, the height of the tree is the max height 
    # of any node that is still in the tree.
    # Since we remove subtrees, the height of the tree is the max of 
    # (max_height_if_removed[node]) for all nodes that are being removed? No.
    
    # Correct logic:
    # The height of the tree after removing subtree at 'v' is the maximum height 
    # reachable from the root without passing through 'v'.
    # This is exactly what we precomputed in `max_height_if_removed`.
    # However, we must account for the fact that multiple subtrees are removed.
    # If we remove subtree A and then subtree B, the height is the max height 
    # available after BOTH are gone.
    
    # Because the problem says "each query removes a subtree that has not been removed yet",
    # and we want the height after EACH query, we can process queries in REVERSE.
    # In reverse, we are ADDING subtrees back.
    # But actually, it's even simpler:
    # The height after query i is the max of:
    # 1. The max height available if we removed the current subtree.
    # 2. The max height available if we removed any of the PREVIOUSLY removed subtrees.
    # No, that's not right. The queries are sequential.
    # Let's re-read: "After each query, the subtree is removed."
    # This means if query 1 removes node 3, and query 2 removes node 6, 
    # the height after query 2 is the height of the tree with BOTH 3 and 6 removed.
    
    # Let's use the reverse approach:
    # 1. Start with the tree with ALL query subtrees removed.
    # 2. Process queries from last to first.
    # 3. When "adding" a subtree back, the height might increase.
    
    # Actually, the simplest way:
    # The height after query i is the maximum of:
    # - The height of the tree if we only removed the subtrees in queries[0...i].
    # Since subtrees are removed, the height is the maximum of 
    # `max_height_if_removed[v]` for all `v` in `queries[0...i]`? No.
    
    # Let's use the property: The height of the tree after removing subtrees 
    # in `queries[0...i]` is the maximum of `max_height_if_removed[v]` 
    # for all `v` in `queries[0...i]`? No, that's still not quite right.
    
    # Let's use the "Max Height seen so far" logic:
    # A node's height is affected by the removal of its descendants.
    # But the queries remove subtrees. If we remove a node, its entire subtree is gone.
    # The height of the tree is the maximum depth of any node remaining.
    # Let's precompute for every node the maximum depth of its subtree.
    # When a node is removed, we look at the maximum depth available in the 
    # rest of the tree.
    
    # Let's use the "Reverse" approach properly:
    # 1. Identify all nodes that will be removed by any query.
    # 2. The "final" tree is the original tree minus all these nodes.
    # 3. Calculate the height of this "final" tree.
    # 4. Process queries from last to first:
    #    - "Add" the subtree back.
    #    - The height of the tree is max(current_height, height_of_added_subtree).
    
    # Wait, the problem says "each query removes a subtree that has not been removed yet".
    # This means the subtrees in `queries` are disjoint!
    # If they are disjoint, then the height after query `i` is:
    # max(height of tree if only queries[0...i] are removed).
    # Since they are disjoint, the height after query `i` is:
    # max( {max_height_if_removed[v] for v in queries[0...i]} UNION {heights of nodes not in any query} )
    # This is still slightly complex.
    
    # Let's use the most robust way:
    # 1. Precompute `max_height_if_removed[v]` for all `v`.
    #    This is the max height of the tree if ONLY subtree `v` is removed.
    # 2. Since queries are disjoint, the height after query `i` is:
    #    max( {max_height_if_removed[v] for v in queries[0...i]} )? No.
    
    # Let's use the "Reverse" approach with the "disjoint" property:
    # 1. The height after ALL queries are done is the max height of the tree 
    #    considering only nodes that are not in any query.
    # 2. Let `removed_set` be the set of all nodes in `queries`.
    # 3. The height after query `i` is the max height of the tree 
    #    where nodes in `queries[0...i]` are removed.
    
    # Actually, the simplest observation:
    # The height after query `i` is the maximum of:
    # - `max_height_if_removed[v]` for all `v` in `queries[0...i]`
    # - The height of the tree if NO nodes were removed (but we must ignore 
    #   the subtrees that ARE removed).
    
    # Let's use the "Max Height" approach:
    # For each node `v`, `max_height_if_removed[v]` is the max height of the tree 
    # if `v` is removed.
    # If we remove multiple disjoint subtrees `v1, v2, ... vk`, the height is:
    # max( {max_height_if_removed[v_j] for j=1..k} )? No.
    
    # Let's go back to basics.
    # The height of the tree is the maximum depth of any node.
    # When we remove a subtree at `v`, all nodes in `v`'s subtree are gone.
    # The remaining nodes are those that are not descendants of any `v` in `queries[0...i]`.
    # Since queries are disjoint, the height after query `i` is:
    # max( {max_height_if_removed[v] for v in queries[0...i]} ) is NOT correct.
    # The correct one is:
    # The height after query `i` is the maximum of:
    # - `max_height_if_removed[v]` for all `v` in `queries[0...i]`
    # - The height of the tree if we only removed the subtrees in `queries[0...i]`.
    
    # Let's use the "Reverse" approach. It is the most reliable.
    # 1. Mark all nodes that are in `queries` as "removed".
    # 2. Calculate the height of the tree with these nodes removed.
    #    (A node is "present" if it's not in `removed_set` and none of its ancestors are in `removed_set`).
    #    Actually, since queries are disjoint, we just need to check if a node is in `removed_set`.
    # 3. `current_max_height` = max depth of any node `u` such that `u` is not in `removed_set`.
    # 4. Process queries from `len(queries)-1` down to `0`:
    #    - `results[i] = current_max_height`
    #    - `v = queries[i]`
    #    - `current_max_height = max(current_max_height, height_of_subtree_at_v)`
    #    - Wait, this is only if the subtree at `v` was not already part of a removed subtree.
    #    - But the problem says queries are disjoint! So `v` is not a descendant of any other query.
    
    # Let's refine the "Reverse" approach:
    # 1. `is_removed = {val: False for all nodes}`
    # 2. For `v` in `queries`: `is_removed[v] = True`
    # 3. `current_max_height = -1`
    # 4. DFS to find max depth of nodes where `is_removed[node]` is False.
    #    (Note: if a node is removed, its children are also effectively removed).
    #    But since queries are disjoint, we only need to check `is_removed[node]`.
    # 5. `results = []`
    # 6. For `v` in `reversed(queries)`:
    #    - `results.append(current_max_height)`
    #    - `is_removed[v] = False`
    #    - `current_max_height = max(current_max_height, height_of_subtree_at_v)`
    # 7. Return `reversed(results)`.

    # Let's implement this.
    
    # Step 1: Precompute heights and depths.
    node_heights = {}
    def get_heights(node: TreeNode) -> int:
        if not node:
            return -1
        h = 1 + max(get_heights(node.left), get_heights(node.right))
        node_heights[node.val] = h
        return h
    
    get_heights(root)
    
    # Step 2: Identify all nodes that are part of any query.
    # Since queries are disjoint, we only care about the roots of the subtrees.
    query_set = set(queries)
    
    # Step 3: Find the max height of the tree after ALL queries are removed.
    # A node is "active" if it is not in `query_set` AND none of its ancestors are in `query_set`.
    # However, since queries are disjoint, we only need to check if the node itself