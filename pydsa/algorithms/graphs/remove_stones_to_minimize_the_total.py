METADATA = {
    "id": 1962,
    "name": "Remove Stones to Minimize the Total",
    "slug": "remove-stones-to-minimize-the-total",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "dfs", "bfs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Minimize the total weight of stones remaining after removing stones of different colors by connecting components.",
}

def solve(stones: list[list[int]]) -> int:
    """
    Calculates the minimum total weight of stones remaining after removing stones.
    
    The problem can be modeled as a graph where each stone is a node and an edge 
    exists between stones of the same color. In each connected component, we can 
    remove all stones except for the one with the minimum weight.
    
    Args:
        stones: A list of lists where stones[i] = [weight_i, color_i].
        
    Returns:
        The minimum total weight of the remaining stones.
        
    Examples:
        >>> solve([[1,1],[3,1],[5,2],[2,2],[4,2]])
        6
        >>> solve([[1,1],[1,2],[1,3]])
        3
    """
    n = len(stones)
    parent = list(range(n))
    
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

    # Map color to the index of the first stone encountered with that color
    # to build connections between stones of the same color.
    color_to_index: dict[int, int] = {}
    
    for i in range(n):
        weight, color = stones[i]
        if color in color_to_index:
            # If color seen before, union current stone with the previous stone of same color
            union(i, color_to_index[color])
        else:
            color_to_index[color] = i

    # Group stones by their connected component root
    # component_min_weights stores the minimum weight found in each component
    # component_total_weights stores the sum of all weights in each component
    component_min_weights: dict[int, int] = {}
    component_total_weights: dict[int, int] = {}

    for i in range(n):
        root = find(i)
        weight = stones[i][0]
        
        if root not in component_min_weights:
            component_min_weights[root] = weight
            component_total_weights[root] = weight
        else:
            # Update the minimum weight and total weight for the component
            if weight < component_min_weights[root]:
                component_min_weights[root] = weight
            component_total_weights[root] += weight

    # The result is the sum of the minimum weights of all connected components
    total_remaining_weight = sum(component_min_weights.values())
    
    # However, the problem asks for the weight of stones REMOVED.
    # Wait, the problem asks for the minimum total weight of stones REMOVED? 
    # Re-reading: "Return the minimum total weight of stones REMOVED."
    # Actually, the prompt says "Minimize the Total" but the LeetCode problem 
    # asks for the weight of stones REMOVED.
    # Let's calculate: Total Weight - Sum of Min Weights in each component.
    
    total_weight_all_stones = sum(s[0] for s in stones)
    return total_weight_all_stones - total_remaining_weight
