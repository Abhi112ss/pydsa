METADATA = {
    "id": 255,
    "name": "Verify Preorder Sequence in Binary Search Tree",
    "slug": "verify-preorder-sequence-in-binary-search-tree",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "binary_search_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a given sequence can represent the preorder traversal of a valid Binary Search Tree.",
}

def solve(preorder: list[int]) -> bool:
    """
    Verifies if the given sequence is a valid preorder traversal of a BST.

    The algorithm uses a monotonic decreasing stack to simulate the traversal.
    As we encounter elements, we maintain a 'lower_bound' which represents 
    the value of the parent node whose right subtree we are currently exploring.
    In a valid BST preorder, once we move to a right child, all subsequent 
    elements must be greater than the parent node.

    Args:
        preorder: A list of integers representing the preorder traversal.

    Returns:
        True if the sequence is a valid preorder traversal of a BST, False otherwise.

    Examples:
        >>> solve([3, 1, 4, 5])
        True
        >>> solve([3, 1, 4, 2])
        False
    """
    # This variable tracks the minimum value allowed for any subsequent element.
    # Once we pop a node from the stack, it means we have found a right child,
    # and all future nodes must be greater than the popped node.
    lower_bound = float('-inf')
    stack: list[int] = []

    for current_value in preorder:
        # If we encounter a value smaller than the current lower bound,
        # it violates the BST property for the current subtree.
        if current_value < lower_bound:
            return False

        # While the current value is greater than the top of the stack,
        # it means we are moving into a right subtree.
        # We pop elements to find the parent of this right subtree.
        while stack and current_value > stack[-1]:
            lower_bound = stack.pop()

        # Push the current value onto the stack to represent the current path.
        stack.append(current_value)

    return True
