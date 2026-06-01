METADATA = {
    "id": 431,
    "name": "Encode N-ary Tree to Binary Tree",
    "slug": "encode-n-ary-tree-to-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Convert an N-ary tree into a binary tree where the first child is the left child and siblings are connected via right child pointers.",
}

class Node:
    def __init__(self, val: int = None, children: list = None, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.children = children if children is not None else []
        self.left = left
        self.right = right

def solve(root: Node) -> Node:
    """
    Args:
        root: The root of the N-ary tree.

    Returns:
        The root of the converted binary tree.
    """
    if not root:
        return None

    def convert(current_node: Node) -> Node:
        if not current_node:
            return None

        binary_node = Node(val=current_node.val)
        
        if current_node.children:
            binary_node.left = convert(current_node.children[0])
            
            current_sibling = current_node.children[0]
            for i in range(1, len(current_node.children)):
                next_sibling = current_node.children[i]
                sibling_binary_node = convert(next_sibling)
                
                temp = binary_node.left
                while temp.right:
                    temp = temp.right
                temp.right = sibling_binary_node

        return binary_node

    def convert_optimized(current_node: Node) -> Node:
        if not current_node:
            return None

        new_node = Node(val=current_node.val)
        
        if current_node.children:
            new_node.left = convert_optimized(current_node.children[0])
            
            prev_sibling_binary = new_node.left
            for i in range(1, len(current_node.children)):
                current_sibling_binary = convert_optimized(current_node.children[i])
                prev_sibling_binary.right = current_sibling_binary
                prev_sibling_binary = current_sibling_binary
                
        return new_node

    return convert_optimized(root)