METADATA = {
    "id": 331,
    "name": "Verify Preorder Serialization of a Binary Tree",
    "slug": "verify-preorder-serialization-of-a-binary-tree",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given preorder serialization of a binary tree is valid.",
}

def solve(serialization: str) -> bool:
    """
    Verifies if the given preorder serialization represents a valid binary tree.
    
    The algorithm uses the concept of 'slots' or 'capacity'. 
    - Initially, there is 1 available slot (for the root).
    - Each non-null node ('#') consumes 1 slot and produces 2 new slots (for its children).
    - Each null node ('#') consumes 1 slot and produces 0 new slots.
    - If at any point slots become zero or negative before the end, or if slots 
      are not exactly zero at the end, the serialization is invalid.

    Args:
        serialization: A string representing the preorder traversal of a binary tree.

    Returns:
        True if the serialization is valid, False otherwise.

    Examples:
        >>> solve("9,3,4,#,#,1,#,#,2,#,6,#,#")
        True
        >>> solve("1,#")
        False
        >>> solve("#")
        True
    """
    # We start with 1 available slot for the root node
    slots = 1
    
    # Split the string by comma to iterate through nodes
    nodes = serialization.split(',')
    
    for node in nodes:
        # Every node (whether null or non-null) consumes exactly one slot
        slots -= 1
        
        # If slots become negative, it means we have more nodes than the tree structure allows
        if slots < 0:
            return False
        
        # If the node is not null, it creates two new slots for its children
        if node != "#":
            slots += 2
            
    # A valid serialization must consume all available slots exactly
    return slots == 0