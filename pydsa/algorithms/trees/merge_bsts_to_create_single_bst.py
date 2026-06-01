METADATA = {
    "id": 1932,
    "name": "Merge BSTs to Create Single BST",
    "slug": "merge-bsts-to-create-single-bst",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "sorting", "binary search tree"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Merge multiple Binary Search Trees into a single valid Binary Search Tree containing all elements.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(trees: list[TreeNode | None]) -> TreeNode | None:
    """
    Merges multiple Binary Search Trees into a single valid Binary Search Tree.

    The algorithm follows three main steps:
    1. Perform in-order traversal on each tree to extract sorted elements.
    2. Merge all sorted lists into one single sorted list.
    3. Construct a balanced BST from the merged sorted list.

    Args:
        trees: A list of root nodes of Binary Search Trees.

    Returns:
        The root of the newly created merged Binary Search Tree.

    Examples:
        >>> tree1 = TreeNode(1, None, TreeNode(3))
        >>> tree2 = TreeNode(2)
        >>> root = solve([tree1, tree2])
        >>> # root represents a BST containing [1, 2, 3]
    """
    
    def get_inorder(node: TreeNode | None, result: list[int]) -> None:
        """Standard in-order traversal to get sorted elements."""
        if not node:
            return
        get_inorder(node.left, result)
        result.append(node.val)
        get_inorder(node.right, result)

    def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
        """Merges multiple sorted lists into one using a min-heap approach (simulated via sorting for simplicity, 
        though a heap is O(N log K)). Given the constraints, a global sort is O(N log N)."""
        merged = []
        for lst in lists:
            merged.extend(lst)
        # Sorting the combined list ensures we have a single sorted sequence
        merged.sort()
        return merged

    def build_balanced_bst(sorted_elements: list[int], start: int, end: int) -> TreeNode | None:
        """Recursively builds a balanced BST from a sorted array."""
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = TreeNode(sorted_elements[mid])
        node.left = build_balanced_bst(sorted_elements, start, mid - 1)
        node.right = build_balanced_bst(sorted_elements, mid + 1, end)
        return node

    # Step 1: Extract sorted elements from all trees
    all_sorted_lists = []
    for root in trees:
        current_list = []
        get_inorder(root, current_list)
        if current_list:
            all_sorted_lists.append(current_list)

    if not all_sorted_lists:
        return None

    # Step 2: Combine all elements into one sorted list
    combined_sorted_elements = merge_sorted_lists(all_sorted_lists)

    # Step 3: Reconstruct the BST from the sorted list
    return build_balanced_bst(combined_sorted_elements, 0, len(combined_sorted_elements) - 1)