METADATA = {
    "id": 1305,
    "name": "All Elements in Two Binary Search Trees",
    "slug": "all-elements-in-two-binary-search-trees",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "sorting", "two_pointers", "binary-search-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Given two binary search trees, return a sorted list of all elements in both trees.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
    """
    Performs an in-order traversal on two BSTs and merges the resulting 
    sorted lists using a two-pointer approach.

    Args:
        root1: The root of the first binary search tree.
        root2: The root of the second binary search tree.

    Returns:
        A sorted list containing all elements from both trees.

    Examples:
        >>> root1 = TreeNode(1, None, TreeNode(3))
        >>> root2 = TreeNode(2)
        >>> solve(root1, root2)
        [1, 2, 3]
    """

    def inorder_traversal(node: TreeNode | None) -> list[int]:
        """Helper to perform iterative in-order traversal to avoid recursion depth issues."""
        result = []
        stack = []
        current = node
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

    # Step 1: Get sorted lists from both BSTs via in-order traversal
    list1 = inorder_traversal(root1)
    list2 = inorder_traversal(root2)

    # Step 2: Merge the two sorted lists using two pointers
    merged_list = []
    pointer1 = 0
    pointer2 = 0
    len1 = len(list1)
    len2 = len(list2)

    while pointer1 < len1 and pointer2 < len2:
        if list1[pointer1] < list2[pointer2]:
            merged_list.append(list1[pointer1])
            pointer1 += 1
        else:
            merged_list.append(list2[pointer2])
            pointer2 += 1

    # Append remaining elements from either list
    if pointer1 < len1:
        merged_list.extend(list1[pointer1:])
    if pointer2 < len2:
        merged_list.extend(list2[pointer2:])

    return merged_list