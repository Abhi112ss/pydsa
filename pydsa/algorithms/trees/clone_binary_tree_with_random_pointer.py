METADATA = {
    "id": 1485,
    "name": "Clone Binary Tree With Random Pointer",
    "slug": "clone_binary_tree_with_random_pointer",
    "category": "Trees",
    "aliases": [],
    "tags": ["hash_map", "trees", "depth-first-search", "breadth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Create a deep copy of a binary tree where each node contains an additional random pointer to any node in the tree or null.",
}

class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

def solve(root: Node | None) -> Node | None:
    """
    Creates a deep copy of a binary tree where each node has a random pointer.

    Args:
        root: The root node of the original binary tree.

    Returns:
        The root node of the cloned binary tree.

    Examples:
        >>> root = Node(1)
        >>> root.left = Node(2)
        >>> root.random = root.left
        >>> cloned = solve(root)
        >>> cloned.val == 1 and cloned.left.val == 2 and cloned.random == cloned.left
        True
    """
    if not root:
        return None

    # Map to store the relationship between original nodes and their clones
    # Key: Original Node, Value: Cloned Node
    visited_nodes: dict[Node, Node] = {}

    def get_clone(node: Node | None) -> Node | None:
        """Helper to retrieve or create a clone of a given node."""
        if not node:
            return None
        if node in visited_nodes:
            return visited_nodes[node]
        
        # Create a new node and immediately add to map to handle cycles/random pointers
        new_node = Node(node.val)
        visited_nodes[node] = new_node
        return new_node

    # We use a stack for an iterative DFS approach to traverse the tree
    # This ensures we visit every node and establish all connections
    stack: list[Node] = [root]
    
    # First pass: Create all nodes and map them
    # We can combine node creation and structural linking in one traversal
    # but to ensure random pointers are handled correctly regardless of order,
    # we use the visited_nodes map.
    
    # Standard DFS to traverse the tree structure
    traversal_stack: list[Node] = [root]
    visited_nodes[root] = Node(root.val)
    
    while traversal_stack:
        current = traversal_stack.pop()
        clone = visited_nodes[current]

        # Process left child
        if current.left:
            if current.left not in visited_nodes:
                visited_nodes[current.left] = Node(current.left.val)
                traversal_stack.append(current.left)
            clone.left = visited_nodes[current.left]

        # Process right child
        if current.right:
            if current.right not in visited_nodes:
                visited_nodes[current.right] = Node(current.right.val)
                traversal_stack.append(current.right)
            clone.right = visited_nodes[current.right]

        # Process random pointer
        if current.random:
            if current.random not in visited_nodes:
                # This case handles if random points to a node not yet in the tree structure
                visited_nodes[current.random] = Node(current.random.val)
                # Note: If the random node is not part of the tree structure, 
                # it won't be added to traversal_stack, but the problem 
                # implies random pointers point to nodes within the tree.
            clone.random = visited_nodes[current.random]

    # Since the problem implies random pointers point to nodes within the tree,
    # a single DFS traversal is sufficient to map all nodes.
    # However, to be robust, we perform a second pass or ensure all nodes are visited.
    # Let's refine the logic: 
    # 1. Traverse tree to create all nodes and map them.
    # 2. Traverse tree again to link left, right, and random.

    # Re-implementing with a cleaner two-pass approach for production-grade clarity
    node_map: dict[Node, Node] = {}

    def create_nodes(node: Node | None):
        if not node or node in node_map:
            return
        node_map[node] = Node(node.val)
        create_nodes(node.left)
        create_nodes(node.right)
        # We also need to ensure nodes pointed to by 'random' are in the map
        if node.random and node.random not in node_map:
            # This handles cases where random might point to a node not in the tree structure
            # though in standard LeetCode tree problems, random points to tree nodes.
            pass 

    # Iterative version of node creation to avoid recursion depth issues
    stack = [root]
    node_map[root] = Node(root.val)
    while stack:
        curr = stack.pop()
        for neighbor in [curr.left, curr.right, curr.random]:
            if neighbor and neighbor not in node_map:
                node_map[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
    
    # Second pass: Link the pointers
    stack = [root]
    visited_for_linking = set()
    while stack:
        curr = stack.pop()
        if curr in visited_for_linking:
            continue
        visited_for_linking.add(curr)
        
        clone = node_map[curr]
        clone.left = node_map.get(curr.left)
        clone.right = node_map.get(curr.right)
        clone.random = node_map.get(curr.random)
        
        if curr.left: stack.append(curr.left)
        if curr.right: stack.append(curr.right)
        if curr.random: stack.append(curr.random)

    return node_map[root] if root else None

# The above logic is slightly redundant due to the complexity of the problem constraints.
# Let's provide the most optimized, clean version.

def solve_optimized(root: Node | None) -> Node | None:
    """
    Optimized deep copy of a binary tree with random pointers.
    """
    if not root:
        return None

    # Map: Original Node -> Cloned Node
    old_to_new: dict[Node, Node] = {}

    # Step 1: Create all nodes and store in map
    # We use a simple BFS/DFS to ensure we find all nodes reachable via left, right, or random
    stack = [root]
    old_to_new[root] = Node(root.val)
    
    while stack:
        curr = stack.pop()
        
        # Check all three possible directions to ensure we capture all nodes
        for neighbor in [curr.left, curr.right, curr.random]:
            if neighbor and neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                stack.append(neighbor)
    
    # Step 2: Assign pointers for the clones
    # We iterate through the map to link the cloned nodes correctly
    for old_node, new_node in old_to_new.items():
        if old_node.left:
            new_node.left = old_to_new[old_node.left]
        if old_node.right:
            new_node.right = old_to_new[old_node.right]
        if old_node.random:
            new_node.random = old_to_new[old_node.random]
            
    return old_to_new[root]

# Assign the optimized version to solve
solve = solve_optimized