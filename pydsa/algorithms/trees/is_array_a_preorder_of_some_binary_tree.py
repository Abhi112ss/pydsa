METADATA = {
    "id": 2764,
    "name": "Is Array a Preorder of Some Binary Tree",
    "slug": "is-array-a-preorder-of-some-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["stack", "trees", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a given array can represent the preorder traversal of a binary search tree.",
}

def solve(preorder: list[int]) -> bool:
    """
    Determines if the given array can be a preorder traversal of a Binary Search Tree (BST).
    
    In a preorder traversal (Root, Left, Right), once we encounter a value larger than 
    the current node, we have entered the right subtree. In a BST, all nodes in the 
    right subtree must be greater than the parent node. We use a stack to keep track 
    of ancestors and a 'lower_bound' to ensure no node violates the BST property.

    Args:
        preorder: A list of integers representing the traversal.

    Returns:
        True if the array is a valid preorder traversal of a BST, False otherwise.

    Examples:
        >>> solve([1, 3, 2])
        True
        >>> solve([1, 3, 0])
        False
    """
    # lower_bound tracks the minimum value that any subsequent element must exceed.
    # This represents the value of a parent node whose right subtree we are currently in.
    lower_bound = float('-inf')
    stack: list[int] = []

    for value in preorder:
        # If we encounter a value smaller than the current lower_bound, 
        # it violates the BST property (it's in a right subtree but smaller than the ancestor).
        if value < lower_bound:
            return False

        # If the current value is greater than the top of the stack, it means we are 
        # moving into a right subtree. We pop elements to find the immediate parent 
        # of this right child.
        while stack and value > stack[-1]:
            lower_bound = stack.pop()

        # Push the current value onto the stack to act as a potential parent for future nodes.
        stack.append(value)

    return True
