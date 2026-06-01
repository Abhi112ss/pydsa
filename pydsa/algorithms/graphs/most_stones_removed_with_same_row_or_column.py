METADATA = {
    "id": 947,
    "name": "Most Stones Removed with Same Row or Column",
    "slug": "most-stones-removed-with-same-row-or-column",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "dfs", "connected_components"],
    "difficulty": "medium",
    "time_complexity": "O(N * alpha(N))",
    "space_complexity": "O(N)",
    "description": "Find the maximum number of stones that can be removed such that no two stones share the same row or column after removal.",
}

def solve(stones: list[list[int]]) -> int:
    """
    Args:
        stones: A list of lists where each inner list represents the [row, col] coordinates of a stone.

    Returns:
        The maximum number of stones that can be removed.
    """
    parent = {}

    def find(i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> None:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for row, col in stones:
        row_node = row
        col_node = col + 10001
        
        if row_node not in parent:
            parent[row_node] = row_node
        if col_node not in parent:
            parent[col_node] = col_node
            
        union(row_node, col_node)

    unique_components = 0
    for node in parent:
        if parent[node] == node:
            unique_components += 1

    return len(stones) - (unique_components - (len(parent) - len(stones) - (len(parent) - len(set(row for row, col in stones)) - len(set(col for row, col in stones)))))

def solve(stones: list[list[int]]) -> int:
    """
    Args:
        stones: A list of lists where each inner list represents the [row, col] coordinates of a stone.

    Returns:
        The maximum number of stones that can be removed.
    """
    parent = {}

    def find(i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> None:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for row, col in stones:
        col_offset = col + 10001
        if row not in parent:
            parent[row] = row
        if col_offset not in parent:
            parent[col_offset] = col_offset
        union(row, col_offset)

    num_components = 0
    for node in parent:
        if parent[node] == node:
            num_components += 1

    return len(stones) - (num_components - (len(parent) - len(set(r for r, c in stones)) - len(set(c for r, c in stones))))

def solve(stones: list[list[int]]) -> int:
    """
    Args:
        stones: A list of lists where each inner list represents the [row, col] coordinates of a stone.

    Returns:
        The maximum number of stones that can be removed.
    """
    parent = {}

    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> None:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for row, col in stones:
        col_id = col + 10001
        if row not in parent:
            parent[row] = row
        if col_id not in parent:
            parent[col_id] = col_id
        union(row, col_id)

    component_count = 0
    for node in parent:
        if parent[node] == node:
            component_count += 1

    total_nodes_in_graph = len(parent)
    nodes_representing_actual_stones = len(set(r for r, c in stones)) + len(set(c + 10001 for r, c in stones))
    
    # The number of components in the bipartite graph of rows and columns
    # that actually contain at least one stone.
    # However, the standard way is to count components of the nodes present in 'parent'.
    # Since we only add nodes that are part of a stone, every node in 'parent' is part of a component.
    
    return len(stones) - component_count

def solve(stones: list[list[int]]) -> int:
    """
    Args:
        stones: A list of lists where each inner list represents the [row, col] coordinates of a stone.

    Returns:
        The maximum number of stones that can be removed.
    """
    parent = {}

    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i: int, j: int) -> None:
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for row, col in stones:
        col_id = col + 10001
        if row not in parent:
            parent[row] = row
        if col_id not in parent:
            parent[col_id] = col_id
        union(row, col_id)

    num_components = 0
    for node in parent:
        if parent[node] == node:
            num_components += 1

    return len(stones) - num_components