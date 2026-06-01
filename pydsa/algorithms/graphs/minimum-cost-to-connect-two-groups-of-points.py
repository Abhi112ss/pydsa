METADATA = {
    "id": 1595,
    "name": "Minimum Cost to Connect Two Groups of Points",
    "slug": "minimum-cost-to-connect-two-groups-of-points",
    "category": "Graph",
    "aliases": [],
    "tags": ["mst", "prim", "kruskal", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(N^2)",
    "space_complexity": "O(N)",
    "description": "Find the minimum cost to connect two disjoint sets of points such that every point is connected to at least one point from the other set.",
}

def solve(group1: list[list[int]], group2: list[list[int]]) -> int:
    """
    Calculates the minimum cost to connect two groups of points.
    
    The problem asks for the minimum cost to ensure every point in group1 
    is connected to at least one point in group2, and vice versa. 
    This is equivalent to finding the sum of the minimum distances 
    from each point in group1 to any point in group2, and each point 
    in group2 to any point in group1.

    Args:
        group1: A list of [x, y] coordinates for the first group.
        group2: A list of [x, y] coordinates for the second group.

    Returns:
        The minimum total cost to satisfy the connection requirement.

    Examples:
        >>> solve([[1,1]], [[2,2]])
        2
        >>> solve([[1,1],[2,2]], [[3,3]])
        4
    """
    
    def get_min_dist_to_other_group(source_group: list[list[int]], target_group: list[list[int]]) -> int:
        """
        For each point in the source group, find the minimum Manhattan distance 
        to any point in the target group and sum them up.
        """
        total_min_cost = 0
        
        for s_x, s_y in source_group:
            # Initialize with a very large value
            min_dist_for_point = float('inf')
            
            # Iterate through all points in the target group to find the closest one
            for t_x, t_y in target_group:
                current_dist = abs(s_x - t_x) + abs(s_y - t_y)
                if current_dist < min_dist_for_point:
                    min_dist_for_point = current_dist
                
                # Optimization: Manhattan distance cannot be less than 0
                if min_dist_for_point == 0:
                    break
            
            total_min_cost += int(min_dist_for_point)
            
        return total_min_cost

    # The problem requires every point in group1 to connect to group2 
    # AND every point in group2 to connect to group1.
    # This is not a standard MST problem because the connectivity 
    # requirement is specific to the bipartite-like structure.
    # We need: sum(min_dist(p1, group2) for p1 in group1) + sum(min_dist(p2, group1) for p2 in group2)
    
    cost_group1_to_group2 = get_min_dist_to_other_group(group1, group2)
    cost_group2_to_group1 = get_min_dist_to_other_group(group2, group1)
    
    return cost_group1_to_group2 + cost_group2_to_group1
