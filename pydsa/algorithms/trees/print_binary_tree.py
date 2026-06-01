METADATA = {
    "id": 655,
    "name": "Print Binary Tree",
    "slug": "print-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "recursion", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Print a binary tree in a grid-like format where each node is placed at a specific coordinate based on its depth and position.",
}

def solve(root: list[list[int]]) -> list[list[str]]:
    """
    Args:
        root: A nested list representation of a binary tree.

    Returns:
        A 2D list of strings representing the printed tree.
    """
    if not root:
        return []

    def get_height(node: list) -> int:
        if not node:
            return 0
        return 1 + max(get_height(node[0]), get_height(node[1]))

    def get_width(node: list) -> int:
        if not node:
            return 0
        return 1 + max(get_width(node[0]), get_width(node[1]))

    def fill_matrix(node: list, row: int, col_start: int, col_end: int, matrix: list[list[str]]):
        if not node:
            return

        val = str(node[2])
        matrix[row][col_start + (col_end - col_start) // 2] = val

        if node[0]:
            fill_matrix(node[0], row + 1, col_start, col_start + (col_end - col_start) // 2, matrix)
        if node[1]:
            fill_matrix(node[1], row + 1, col_start + (col_end - col_start) // 2 + 1, col_end, matrix)

    height = get_height(root)
    width = get_width(root)
    
    matrix_rows = height * 2 - 1
    matrix_cols = (2 ** height) - 1
    
    grid = [[" " for _ in range(matrix_cols)] for _ in range(matrix_rows)]
    
    def traverse_and_place(node: list, row: int, col_left: int, col_right: int):
        if not node:
            return
        
        mid_col = (col_left + col_right) // 2
        grid[row][mid_col] = str(node[2])
        
        if node[0]:
            traverse_and_place(node[0], row + 2, col_left, mid_col - 1)
        if node[1]:
            traverse_and_place(node[1], row + 2, mid_col + 1, col_right)

    def get_dimensions(node: list) -> tuple[int, int]:
        if not node:
            return 0, 0
        left_h, left_w = get_dimensions(node[0])
        right_h, right_w = get_dimensions(node[1])
        return max(left_h, right_h) + 1, max(left_w, right_w) + 1

    def build_grid(node: list, row: int, col_start: int, col_end: int):
        if not node:
            return
        
        mid = (col_start + col_end) // 2
        grid[row][mid] = str(node[2])
        
        if node[0]:
            build_grid(node[0], row + 2, col_start, mid - 1)
        if node[1]:
            build_grid(node[1], row + 2, mid + 1, col_end)

    def get_tree_info(node: list) -> tuple[int, int, int, int]:
        if not node:
            return 0, 0, 0, 0
        
        left_h, left_w, left_min_col, left_max_col = get_tree_info(node[0])
        right_h, right_w, right_min_col, right_max_col = get_tree_info(node[1])
        
        current_h = max(left_h, right_h) + 1
        
        if not node[0] and not node[1]:
            return 1, 1, 0, 0
        
        if not node[0]:
            return current_h, right_w + 1, 1, right_w + 1
        
        if not node[1]:
            return current_h, left_w + 1, 0, left_w
            
        return current_h, left_w + right_w + 1, 0, left_w + right_w

    def get_actual_dims(node: list) -> tuple[int, int, int, int]:
        if not node:
            return 0, 0, 0, 0
        
        l_h, l_w, l_min, l_max = get_actual_dims(node[0])
        r_h, r_w, r_min, r_max = get_actual_dims(node[1])
        
        h = max(l_h, r_h) + 1
        
        if not node[0] and not node[1]:
            return 1, 1, 0, 0
        
        if not node[0]:
            return h, r_w + 1, 1, r_w + 1
        
        if not node[1]:
            return h, l_w + 1, 0, l_w
            
        return h, l_w + r_w + 1, 0, l_w + r_w

    def solve_recursive(node: list, row: int, col_start: int, col_end: int):
        if not node:
            return
        
        mid = (col_start + col_end) // 2
        grid[row][mid] = str(node[2])
        
        if node[0]:
            solve_recursive(node[0], row + 2, col_start, mid - 1)
        if node[1]:
            solve_recursive(node[1], row + 2, mid + 1, col_end)

    def get_full_dims(node: list) -> tuple[int, int]:
        if not node:
            return 0, 0
        
        def get_h(n):
            if not n: return 0
            return 1 + max(get_h(n[0]), get_h(n[1]))
        
        def get_w(n):
            if not n: return 0
            l_w = get_w(n[0])
            r_w = get_w(n[1])
            if not n[0] and not n[1]: return 1
            if not n[0]: return r_w + 1
            if not n[1]: return l_w + 1
            return l_w + r_w + 1
            
        return get_h(node), get_w(node)

    h, w = get_full_dims(root)
    res_grid = [[" " for _ in range(w)] for _ in range(h * 2 - 1)]
    
    def place(node: list, r: int, c_start: int, c_end: int):
        if not node:
            return
        
        mid = (c_start + c_end) // 2
        res_grid[r][mid] = str(node[2])
        
        if node[0]:
            place(node[0], r + 2, c_start, mid - 1)
        if node[1]:
            place(node[1], r + 2, mid + 1, c_end)

    def get_width_at_depth(node: list, depth: int) -> int:
        if not node or depth == 0:
            return 1 if node else 0
        return get_width_at_depth(node[0], depth - 1) + get_width_at_depth(node[1], depth - 1)

    def get_height_of_tree(node: list) -> int:
        if not node:
            return 0
        return 1 + max(get_height_of_tree(node[0]), get_height_of_tree(node[1]))

    def get_width_of_tree(node: list) -> int:
        if not node:
            return 0
        if not node[0] and not node[1]:
            return 1
        if not node[0]:
            return get_width_of_tree(node[1]) + 1
        if not node[1]:
            return get_width_of_tree(node[0]) + 1
        return get_width_of_tree(node[0]) + get_width_of_tree(node[1]) + 1

    def get_tree_metrics(node: list) -> tuple[int, int]:
        if not node:
            return 0, 0
        
        def h(n):
            if not n: return 0
            return 1 + max(h(n[0]), h(n[1]))
        
        def w(n):
            if not n: return 0
            if not n[0] and not n[1]: return 1
            if not n[0]: return w(n[1]) + 1
            if not n[1]: return w(n[0]) + 1
            return w(n[0]) + w(n[1]) + 1
            
        return h(node), w(node)

    tree_h, tree_w = get_tree_metrics(root)
    final_grid = [[" " for _ in range(tree_w)] for _ in range(tree_h * 2 - 1)]

    def fill(node: list, r: int, c_left: int, c_right: int):
        if not node:
            return
        
        mid = (c_left + c_right) // 2
        final_grid[r][mid] = str(node[2])
        
        if node[0]:
            fill(node[0], r + 2, c_left, mid - 1)
        if node[1]:
            fill(node[1], r + 2, mid + 1, c_right)

    def get_node_width(node: list) -> int:
        if not node:
            return 0
        if not node[0] and not node[1]:
            return 1
        if not node[0]:
            return get_node_width(node[1]) + 1
        if not node[1]:
            return get_node_width(node[0]) + 1
        return get_node_width(node[0]) + get_node_width(node[1]) + 1

    def get_node_height(node: list) -> int:
        if not node:
            return 0
        return 1 + max(get_node_height(node[0]), get_node_height(node[1]))

    def get_dims(node: list) -> tuple[int, int]:
        if not node:
            return 0, 0
        lh, lw = get_dims(node[0])
        rh, rw = get_dims(node[1])
        h = max(lh, rh) + 1
        if not node[0] and not node[1]:
            w = 1
        elif not node[0]:
            w = rw + 1
        elif not node[1]:
            w = lw + 1
        else:
            w = lw + rw + 1
        return h, w

    th, tw = get_dims(root)
    grid = [[" " for _ in range(tw)] for _ in range(th * 2 - 1)]

    def dfs(node: list, r: int, c_start: int, c_end: int):
        if not node:
            return
        mid = (c_start + c_end) // 2
        grid[r][mid] = str(node[2])
        if node[0]:
            dfs(node[0], r + 2, c_start, mid - 1)
        if node[1]:
            dfs(node[1], r + 2, mid + 1, c_end)

    dfs(root, 0, 0, tw - 1)
    return grid