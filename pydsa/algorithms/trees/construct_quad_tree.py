METADATA = {
    "id": 427,
    "name": "Construct Quad Tree",
    "slug": "construct-quad-tree",
    "category": "Divide and Conquer",
    "aliases": [],
    "tags": ["divide_and_conquer", "recursion", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(log n)",
    "description": "Construct a quad tree from a given n x n grid where each node represents a quadrant of the grid.",
}

class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft: 'Node' = None, topRight: 'Node' = None, bottomLeft: 'Node' = None, bottomRight: 'Node' = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def solve(grid: list[list[int]]) -> Node:
    """
    Args:
        grid: A 2D list of integers representing the n x n grid.

    Returns:
        The root node of the constructed quad tree.
    """
    def build_quadtree(row_start: int, col_start: int, size: int) -> Node:
        if size == 1:
            return Node(val=bool(grid[row_start][col_start]), isLeaf=True)

        half_size = size // 2
        top_left_node = build_quadtree(row_start, col_start, half_size)
        top_right_node = build_quadtree(row_start, col_start + half_size, half_size)
        bottom_left_node = build_quadtree(row_start + half_size, col_start, half_size)
        bottom_right_node = build_quadtree(row_start + half_size, col_start + half_size, half_size)

        is_leaf = (
            top_left_node.isLeaf and
            top_right_node.isLeaf and
            bottom_left_node.isLeaf and
            bottom_right_node.isLeaf and
            top_left_node.val == top_right_node.val == bottom_left_node.val == bottom_right_node.val
        )

        if is_leaf:
            return Node(val=top_left_node.val, isLeaf=True)
        
        return Node(
            val=False,
            isLeaf=False,
            topLeft=top_left_node,
            topRight=top_right_node,
            bottomLeft=bottom_left_node,
            bottomRight=bottom_right_node
        )

    return build_quadtree(0, 0, len(grid))