METADATA = {
    "id": 1104,
    "name": "Path In Zigzag Labelled Binary Tree",
    "slug": "path-in-zigzag-labelled-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["math", "trees", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the path from the root to a given node in a zigzag labelled binary tree.",
}

def solve(start_value: int, end_value: int) -> list[int]:
    """
    Finds the path from the root to the end_value in a zigzag labelled binary tree.

    In a zigzag binary tree, the levels alternate direction:
    Level 1: 1 (Left to Right)
    Level 2: 3, 2 (Right to Left)
    Level 3: 4, 5, 6, 7 (Left to Right)
    ... and so on.

    Args:
        start_value: The value of the root node (always 1).
        end_value: The target node value to find the path to.

    Returns:
        A list of integers representing the path from root to end_value.

    Examples:
        >>> solve(1, 6)
        [1, 3, 6]
        >>> solve(1, 1)
        [1]
        >>> solve(1, 2)
        [1, 2]
    """
    path = []
    current_node = end_value

    while current_node > 0:
        path.append(current_node)
        
        # To find the parent in a zigzag tree, we need to find the 
        # 'mirrored' position of the current node within its level.
        
        # 1. Determine the level of the current node.
        # Level 1: [1, 1], Level 2: [2, 3], Level 3: [4, 7], Level 4: [8, 15]
        level = 0
        temp = current_node
        while temp > 0:
            temp >>= 1
            level += 1
        
        # 2. Calculate the range of values in this level.
        # The first value in level 'L' is 2^(L-1).
        # The last value in level 'L' is 2^L - 1.
        level_start = 1 << (level - 1)
        level_end = (1 << level) - 1
        
        # 3. Find the mirrored value.
        # In a zigzag tree, if the level is even, the values are reversed.
        # However, the mathematical trick is to realize that the parent 
        # of 'x' in a standard tree is x // 2. 
        # In a zigzag tree, the parent of 'x' is the value that would 
        # be x // 2 if the level were not reversed.
        # We can find this by mirroring the current node relative to the level range.
        # Mirrored value = level_start + level_end - current_node
        # The parent is then the mirrored value divided by 2.
        
        # We calculate the 'standard' position by mirroring the current node
        # within its level boundaries, then divide by 2 to move up.
        current_node = (level_start + level_end - current_node) // 2

    # The path was constructed from end to start, so reverse it.
    return path[::-1]
