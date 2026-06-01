METADATA = {
    "id": 2415,
    "name": "Reverse Odd Levels of Binary Tree",
    "slug": "reverse-odd-levels-of-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bfs", "level-order-traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse the values of nodes at all odd levels of a perfect binary tree.",
}

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Reverses the values of nodes at all odd levels of a perfect binary tree.

    Args:
        root: The root of a perfect binary tree.

    Returns:
        The root of the modified binary tree.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        >>> solve(root).val
        1
        >>> solve(root).left.val
        3
        >>> solve(root).right.val
        2
    """
    if not root:
        return None

    # Use a queue for level-order traversal (BFS)
    queue: list[TreeNode] = [root]
    level_index = 0

    while queue:
        level_size = len(queue)
        
        # If the current level is odd, we need to reverse the values
        if level_index % 2 == 1:
            left_ptr = 0
            right_ptr = level_size - 1
            
            # Extract values to swap them using two pointers
            # We swap the values of the nodes themselves
            while left_ptr < right_ptr:
                queue[left_ptr].val, queue[right_ptr].val = queue[right_ptr].val, queue[left_ptr].val
                left_ptr += 1
                right_ptr -= 1
        
        # Prepare the next level
        next_level = []
        for node in queue:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        # If no children were added, we have reached the leaf level
        if not next_level:
            break
            
        queue = next_level
        level_index += 1

    return root
