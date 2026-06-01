METADATA = {
    "id": 1203,
    "name": "Sort Items by Groups Respecting Dependencies",
    "slug": "sort-items-by-groups-respecting-dependencies",
    "category": "Hard",
    "aliases": [],
    "tags": ["topological_sort", "graphs", "dfs"],
    "difficulty": "hard",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Sort items such that group dependencies and item dependencies are both respected.",
}

def solve(n: int, group: list[int], dependencies: list[list[int]]) -> list[int]:
    """
    Sorts items by groups respecting both item-level and group-level dependencies.

    Args:
        n: The total number of items.
        group: A list where group[i] is the group ID of item i. 
               If group[i] == -1, the item belongs to no group.
        dependencies: A list of pairs [a, b] where item a must come before item b.

    Returns:
        A list of sorted item indices, or an empty list if no valid ordering exists.

    Examples:
        >>> solve(3, [-1, -1, -1], [[0, 1], [1, 2]])
        [0, 1, 2]
        >>> solve(3, [0, 0, 1], [[0, 2], [1, 2]])
        [0, 1, 2]
    """

    # Assign unique group IDs to items that don't belong to any group (-1)
    # This allows us to treat them as individual groups for the group-level topo sort.
    group_id_counter = 0
    for i in range(n):
        if group[i] == -1:
            group[i] = group_id_counter
            group_id_counter += 1
    
    # Total number of groups is the max group ID + 1
    num_groups = max(group) + 1

    # Build adjacency lists for both item-level and group-level dependencies
    item_adj: list[list[int]] = [[] for _ in range(n)]
    group_adj: list[list[int]] = [[] for _ in range(num_groups)]
    
    for u, v in dependencies:
        item_adj[u].append(v)
        # If items belong to different groups, there is a dependency between groups
        if group[u] != group[v]:
            group_adj[group[u]].append(group[v])

    def topological_sort(nodes: list[int], adj: list[list[int]]) -> list[int]:
        """Standard Kahn's algorithm for topological sorting."""
        in_degree = {node: 0 for node in nodes}
        for u in nodes:
            for v in adj[u]:
                if v in in_degree:
                    in_degree[v] += 1
        
        queue = [node for node in nodes if in_degree[node] == 0]
        result = []
        
        # Use a simple pointer as a queue to avoid O(n) pop(0)
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            result.append(u)
            for v in adj[u]:
                if v in in_degree:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
        
        return result if len(result) == len(nodes) else []

    # 1. Sort the groups themselves
    sorted_groups = topological_sort(list(range(num_groups)), group_adj)
    if not sorted_groups:
        return []

    # 2. Sort items within each group
    # We group items by their group ID to process them together
    items_by_group: dict[int, list[int]] = {}
    for i in range(n):
        g_id = group[i]
        if g_id not in items_by_group:
            items_by_group[g_id] = []
        items_by_group[g_id].append(i)

    # Pre-calculate sorted items for every group
    sorted_items_in_group: dict[int, list[int]] = {}
    for g_id, items in items_by_group.items():
        # Note: item_adj is used here, but we only care about dependencies within the same group
        # because group-level dependencies are handled by the group-level topo sort.
        # However, the problem implies item dependencies must be respected regardless.
        # If item a -> item b and they are in different groups, it's handled by group_adj.
        # If they are in the same group, it must be handled by item_adj.
        res = topological_sort(items, item_adj)
        if not res:
            return []
        sorted_items_in_group[g_id] = res

    # 3. Combine: Iterate through sorted groups and append their sorted items
    final_order = []
    for g_id in sorted_groups:
        if g_id in sorted_items_in_group:
            final_order.extend(sorted_items_in_group[g_id])
            
    return final_order if len(final_order) == n else []
