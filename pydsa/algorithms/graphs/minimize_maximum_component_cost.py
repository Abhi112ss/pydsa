METADATA = {
    "id": 3613,
    "name": "Minimize Maximum Component Cost",
    "slug": "minimize-maximum-component-cost",
    "category": "Graph",
    "aliases": [],
    "tags": ["binary_search", "disjoint_set", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(E log E * alpha(V))",
    "space_complexity": "O(V)",
    "description": "Find the minimum possible value of the maximum component cost by selecting edges such that no component exceeds a certain cost threshold.",
}

class DisjointSetUnion:
    """Standard Disjoint Set Union (DSU) with path compression and union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.component_cost = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int, edge_weight: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by rank to keep tree flat
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            
            self.parent[root_j] = root_i
            self.component_cost[root_i] += self.component_cost[root_j] + edge_weight
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            return True
        else:
            # If already in same component, adding edge increases cost of that component
            self.component_cost[root_i] += edge_weight
            return False

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the minimum possible value of the maximum component cost.
    
    Args:
        n: Number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, weight].
        
    Returns:
        The minimum maximum component cost.
        
    Examples:
        >>> solve(3, [[0, 1, 10], [1, 2, 20]])
        30
        >>> solve(4, [[0, 1, 5], [2, 3, 5], [1, 2, 10]])
        20
    """
    # Sort edges by weight to facilitate greedy selection or binary search logic
    # However, the problem asks to minimize the maximum component cost.
    # A component's cost is the sum of weights of edges within it + sum of node weights?
    # Standard interpretation: Cost of component = sum of weights of edges in it.
    # If nodes have weights, they should be included. Assuming nodes have weight 0 for this template.
    
    # Sort edges by weight to process them in a specific order if needed
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    def can_achieve(max_allowed_cost: int) -> bool:
        """Checks if it's possible to have all components <= max_allowed_cost."""
        dsu = DisjointSetUnion(n)
        # Initialize component costs with node weights if applicable. 
        # Here we assume node weights are 0.
        
        for u, v, w in sorted_edges:
            root_u = dsu.find(u)
            root_v = dsu.find(v)
            
            if root_u == root_v:
                # Adding this edge to an existing component
                if dsu.component_cost[root_u] + w <= max_allowed_cost:
                    dsu.component_cost[root_u] += w
                else:
                    # This edge would violate the constraint if we include it
                    # In a 'minimize max' problem, we usually decide which edges to include.
                    # If the goal is to include ALL edges, the answer is just the sum of all edges in components.
                    # If the goal is to select a subset of edges to satisfy a property, the logic changes.
                    # Assuming the problem asks to partition edges into components such that max cost is minimized.
                    pass
            else:
                # Merging two components
                if dsu.component_cost[root_u] + dsu.component_cost[root_v] + w <= max_allowed_cost:
                    dsu.union(u, v, w)
                else:
                    # Cannot merge without exceeding max_allowed_cost
                    pass
        
        # Check if any component exceeds the limit
        for i in range(n):
            if dsu.parent[i] == i and dsu.component_cost[i] > max_allowed_cost:
                return False
        return True

    # Binary search range: [0, sum of all edge weights]
    low = 0
    high = sum(edge[2] for edge in edges)
    ans = high

    # Note: The logic above depends on whether we MUST include all edges or can pick a subset.
    # If we must include all edges, the answer is simply the cost of the components 
    # formed by all edges. If we want to minimize the max cost by partitioning, 
    # it's a different problem. 
    # Given the prompt "Minimize Maximum Component Cost", it usually implies 
    # we are looking for a way to group edges.
    
    # Correct approach for "Minimize Maximum Component Cost" where we must include all edges:
    # The components are fixed by the connectivity. The cost is the sum of weights in each component.
    # The answer is max(component_costs).
    
    dsu = DisjointSetUnion(n)
    for u, v, w in edges:
        dsu.union(u, v, w)
    
    max_cost = 0
    for i in range(n):
        if dsu.parent[i] == i:
            max_cost = max(max_cost, dsu.component_cost[i])
            
    return max_cost
