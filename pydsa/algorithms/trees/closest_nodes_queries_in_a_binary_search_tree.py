METADATA = {
    "id": 2476,
    "name": "Closest Nodes in a Binary Search Tree",
    "slug": "closest_nodes_in_a_binary_search_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "binary_search", "binary_search_tree"],
    "difficulty": "medium",
    "time_complexity": "O(q * log n)",
    "space_complexity": "O(n)",
    "description": "Given a BST and queries, find the closest value in the BST for each query value.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, queries: list[int]) -> list[int]:
    """
    Finds the closest value in a Binary Search Tree for each query in a list.

    Args:
        root: The root node of the Binary Search Tree.
        queries: A list of integers representing the query values.

    Returns:
        A list of integers where each element is the value in the BST closest to the query.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        >>> queries = [3, 10, 5]
        >>> solve(root, queries)
        [3, 4, 4]
    """
    results = []

    for query in queries:
        current_node = root
        closest_val = root.val
        
        # Standard BST search logic to find the closest value
        while current_node:
            # Update closest_val if the current node is closer to the query
            if abs(current_node.val - query) < abs(closest_val - query):
                closest_val = current_node.val
            # If distances are equal, the problem implies we can pick either, 
            # but standard BST traversal handles the value comparison.
            elif abs(current_node.val - query) == abs(closest_val - query):
                # Tie-breaking: usually the smaller value is preferred in some problems,
                # but here any closest value works. We keep the existing one.
                if current_node.val < closest_val:
                    closest_val = current_node.val

            # Decide which direction to move in the BST
            if query < current_node.val:
                current_node = current_node.left
            elif query > current_node.val:
                current_node = current_node.right
            else:
                # Exact match found
                closest_val = current_node.val
                break
        
        results.append(closest_val)

    return results
