METADATA = {
    "id": 2673,
    "name": "Make Costs of Paths Equal in a Binary Tree",
    "slug": "make-costs-of-paths-equal-in-a-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the minimum cost to make all path costs in a binary tree equal by reducing edge weights.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Calculates the minimum cost to make all path costs in a binary tree equal.
    
    The strategy is to use a post-order traversal. For each node, we determine 
    the maximum path cost from its children to the leaves. To make all paths 
    equal, we must reduce the edge weights of the 'heavier' child so that 
    both children provide the same path cost to the current node.

    Args:
        root: The root of the binary tree.

    Returns:
        int: The minimum total cost (sum of reductions) to equalize all paths.

    Examples:
        >>> root = TreeNode(1, TreeNode(1, TreeNode(3), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(3)))
        >>> solve(root)
        4
    """
    total_reduction_cost = 0

    def dfs(node: TreeNode) -> int:
        nonlocal total_reduction_cost
        
        if not node:
            return 0
        
        # Post-order traversal: process children first
        left_path_cost = dfs(node.left)
        right_path_cost = dfs(node.right)
        
        # If left child exists, we must ensure the path through the left edge 
        # matches the path through the right edge (or vice versa).
        # We greedily reduce the larger path to match the smaller one.
        if node.left:
            # The cost of the path through the left child is the edge weight (node.left.val)
            # plus the max path cost from that child downwards.
            # However, the problem defines the edge weight as the child's value.
            # So the path cost from current node through left is: node.left.val + left_path_cost
            # Wait, the problem says: "the cost of the edge between node and its child is child.val".
            # So the path cost from node through left is: node.left.val + left_path_cost.
            # But we can only reduce node.left.val.
            
            # Let's re-evaluate: 
            # The path cost from node through left child is: node.left.val + left_path_cost
            # The path cost from node through right child is: node.right.val + right_path_cost
            # Actually, the problem states the edge weight IS the child's value.
            # So the total path cost from node through left is: node.left.val + left_path_cost.
            # But we can only reduce node.left.val.
            # Let's simplify: the 'cost' contributed by a child to the parent is 
            # (child.val + max_path_from_child).
            pass

        # Correct logic:
        # Let f(node) be the max path cost from node to a leaf.
        # f(node) = max(node.left.val + f(node.left), node.right.val + f(node.right))
        # To equalize, we reduce the larger child's edge weight.
        
        left_val = node.left.val + left_path_cost if node.left else 0
        right_val = node.right.val + right_path_cost if node.right else 0
        
        if node.left and node.right:
            # If both children exist, reduce the larger one to match the smaller one
            diff = abs(left_val - right_val)
            total_reduction_cost += diff
            # The path cost from this node to leaves will be the minimum of the two
            return min(left_val, right_val)
        elif node.left:
            # Only left child exists, path cost is just the left path
            return left_val
        elif node.right:
            # Only right child exists, path cost is just the right path
            return right_val
        else:
            # Leaf node
            return 0

    # The problem defines path cost as sum of edge weights.
    # A leaf node itself doesn't have an edge weight below it.
    # The edge weight is the value of the child node.
    
    # Let's refine the DFS return value:
    # dfs(node) returns the maximum path cost from 'node' to any leaf in its subtree.
    # Note: The edge weight between 'node' and 'node.left' is 'node.left.val'.
    
    def get_max_path(curr: TreeNode) -> int:
        nonlocal total_reduction_cost
        if not curr:
            return 0
        
        left_max = get_max_path(curr.left)
        right_max = get_max_path(curr.right)
        
        # Path cost through left child: edge(curr, left) + max_path_from_left
        # edge(curr, left) is curr.left.val
        left_total = (curr.left.val + left_max) if curr.left else 0
        right_total = (curr.right.val + right_max) if curr.right else 0
        
        if curr.left and curr.right:
            # We must make left_total == right_total by reducing the larger edge
            total_reduction_cost += abs(left_total - right_total)
            return max(left_total, right_total) - abs(left_total - right_total) # which is min(left_total, right_total)
        
        # If only one child exists, the path cost is just that child's path
        # No reduction needed because there's no other path to compare it to
        return max(left_total, right_total)

    # Re-implementing the logic clearly
    total_reduction_cost = 0
    
    def dfs_final(node: TreeNode) -> int:
        nonlocal total_reduction_cost
        if not node:
            return 0
        
        # Get max path cost from children to leaves
        l_path = dfs_final(node.left)
        r_path = dfs_final(node.right)
        
        # Total path cost from current node through left child
        l_cost = (node.left.val + l_path) if node.left else 0
        r_cost = (node.right.val + r_path) if node.right else 0
        
        if node.left and node.right:
            # Greedy step: reduce the heavier branch to match the lighter branch
            total_reduction_cost += abs(l_cost - r_cost)
            return min(l_cost, r_cost)
        
        # If only one child, the path cost is just that child's path
        return max(l_cost, r_cost)

    dfs_final(root)
    return total_reduction_cost
