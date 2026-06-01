METADATA = {
    "id": 1847,
    "name": "Closest Room",
    "slug": "closest-room",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the closest node to a target node in a tree structure where each node has a weight representing its distance to a specific room.",
}

def solve(rooms: list[list[int]], target: int) -> int:
    """
    Args:
        rooms: A list of lists where rooms[i] contains the children of node i and the weight of node i.
        target: The index of the target node.

    Returns:
        The index of the node closest to the target node based on the given weights.
    """
    n = len(rooms)
    parent = [-1] * n
    weights = [0] * n
    for node_index, data in enumerate(rooms):
        weights[node_index] = data[0]
        for child in data[1:]:
            parent[child] = node_index

    path_to_target = []
    current = target
    while current != -1:
        path_to_target.append(current)
        current = parent[current]

    best_node = target
    min_distance = weights[target]

    for node in path_to_target:
        if weights[node] < min_distance:
            min_distance = weights[node]
            best_node = node
        elif weights[node] == min_distance:
            if node < best_node:
                best_node = node

    def find_closest_in_subtree(start_node: int, target_node: int) -> tuple[int, int]:
        stack = [(start_node, 0)]
        local_best_node = -1
        local_min_dist = float('inf')

        while stack:
            curr, dist = stack.pop()
            if weights[curr] < local_min_dist:
                local_min_dist = weights[curr]
                local_best_node = curr
            elif weights[curr] == local_min_dist:
                if curr < local_best_node:
                    local_best_node = curr
            
            for child in rooms[curr][1:]:
                if child != target_node:
                    stack.append((child, dist + 1))
        
        return local_best_node, local_min_dist

    for i in range(len(path_to_target) - 1):
        ancestor = path_to_target[i + 1]
        child_on_path = path_to_target[i]
        
        subtree_node, subtree_dist = find_closest_in_subtree(child_on_path, ancestor)
        
        total_dist = subtree_dist + (i + 1)
        
        if total_dist < min_distance:
            min_distance = total_dist
            best_node = subtree_node
        elif total_dist == min_distance:
            if subtree_node < best_node:
                best_node = subtree_node

    return best_node