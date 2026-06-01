METADATA = {
    "id": 2392,
    "name": "Build a Matrix With Conditions",
    "slug": "build-a-matrix-with-conditions",
    "category": "Graph",
    "aliases": [],
    "tags": ["topological_sort", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(n + m + k)",
    "space_complexity": "O(n + m + k)",
    "description": "Construct a matrix of size n x m such that specific row and column precedence constraints are satisfied.",
}

def solve(n: int, m: int, relations: list[list[int]]) -> list[list[int]]:
    """
    Args:
        n: The number of rows in the matrix.
        m: The number of columns in the matrix.
        relations: A list of lists where relations[i] = [a, b, c] means 
                   if c == 1, row a must come before row b.
                   if c == 2, column a must come before column b.

    Returns:
        A matrix of size n x m satisfying the conditions, or an empty list if impossible.
    """
    row_adj = [[] for _ in range(n + 1)]
    row_in_degree = [0] * (n + 1)
    col_adj = [[] for _ in range(m + 1)]
    col_in_degree = [0] * (m + 1)

    for u, v, type_id in relations:
        if type_id == 1:
            row_adj[u].append(v)
            row_in_degree[v] += 1
        else:
            col_adj[u].append(v)
            col_in_degree[v] += 1

    def get_topological_order(size: int, adj: list[list[int]], in_degree: list[int]) -> list[int]:
        queue = []
        for i in range(1, size + 1):
            if in_degree[i] == 0:
                queue.append(i)
        
        order = []
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            order.append(curr)
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != size:
            return []
        return order

    row_order = get_topological_order(n, row_adj, row_in_degree)
    if not row_order:
        return []

    col_order = get_topological_order(m, col_adj, col_in_degree)
    if not col_order:
        return []

    row_map = {val: i for i, val in enumerate(row_order)}
    col_map = {val: j for j, val in enumerate(col_order)}

    result = [[0] * m for _ in range(n)]
    for r_idx, r_val in enumerate(row_order):
        for c_idx, c_val in enumerate(col_order):
            result[r_idx][c_idx] = r_val * 1000 + c_val

    return result