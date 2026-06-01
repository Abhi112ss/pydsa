METADATA = {
    "id": 971,
    "name": "Flip Binary Tree To Match Preorder Traversal",
    "slug": "flip-binary-tree-to-match-preorder-traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "binary tree", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if a binary tree can be flipped to match a given preorder traversal sequence.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, voyage: list[int]) -> bool:
    """
    Determines if a binary tree can be flipped to match a given preorder traversal.

    Args:
        root: The root of the binary tree.
        voyage: A list of integers representing the target preorder traversal.

    Returns:
        True if the tree can be flipped to match the voyage, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> voyage = [1, 3, 2]
        >>> solve(root, voyage)
        True
    """
    # Use an iterator to keep track of our current position in the voyage list
    # This allows us to consume elements linearly during the DFS traversal
    voyage_iter = iter(voyage)

    def dfs(node: TreeNode | None) -> bool:
        try:
            # Get the next expected value in the preorder sequence
            next_val = next(voyage_iter)
        except StopIteration:
            # If we run out of values in voyage but still have nodes, it's a mismatch
            return False

        # The current node's value must match the next value in the preorder sequence
        if not node or node.val != next_val:
            return False

        # If it's a leaf node, we've successfully matched this branch
        if not node.left and not node.right:
            return True

        # Try matching the left child first (standard preorder)
        # If the left child's value matches the next element in voyage, we proceed normally
        if node.left and node.left.val == next(voyage_iter, None):
            # Note: We need to handle the fact that next() was called. 
            # To avoid complex iterator management, we use a more robust approach:
            # We check the next value without consuming it or we re-structure the logic.
            pass

        # Re-implementing logic to avoid the 'next()' consumption issue in the check
        return False # Placeholder for the logic below

    # Refined DFS to handle the iterator correctly
    # We use a pointer/index or a list with a shared index to avoid 'next()' issues
    index = [0]

    def dfs_robust(node: TreeNode | None) -> bool:
        if not node:
            return True
        
        # Check if current node matches the current element in voyage
        if index[0] >= len(voyage) or node.val != voyage[index[0]]:
            return False
        
        index[0] += 1
        
        if not node.left and not node.right:
            return True

        # Check if the left child matches the next value in the voyage
        # If it does, we proceed with the left child first
        if node.left and index[0] < len(voyage) and node.left.val == voyage[index[0]]:
            return dfs_robust(node.left) and dfs_robust(node.right)
        
        # If the left child doesn't match, try the right child (the "flip" scenario)
        if node.right and index[0] < len(voyage) and node.right.val == voyage[index[0]]:
            return dfs_robust(node.right) and dfs_robust(node.left)
        
        return False

    # The actual logic:
    # 1. Match current node.
    # 2. If left child matches next voyage element, recurse left then right.
    # 3. Else if right child matches next voyage element, recurse right then left.
    # 4. Else return False.
    
    # We need to reset the index for the robust function
    index[0] = 0
    
    # Final implementation of the recursive logic
    def traverse(node: TreeNode | None) -> bool:
        if not node:
            return True
        
        if index[0] >= len(voyage) or node.val != voyage[index[0]]:
            return False
        
        index[0] += 1
        
        if not node.left and not node.right:
            return True
        
        # Check if left child matches the next value in the sequence
        # If it does, we don't flip.
        if node.left and index[0] < len(voyage) and node.left.val == voyage[index[0]]:
            return traverse(node.left) and traverse(node.right)
        
        # If left doesn't match, check if right child matches the next value
        # If it does, we "flip" by traversing right then left.
        if node.right and index[0] < len(voyage) and node.right.val == voyage[index[0]]:
            return traverse(node.right) and traverse(node.left)
        
        return False

    result = traverse(root)
    
    # If we matched the tree but didn't consume all elements in voyage, it's False
    return result and index[0] == len(voyage)