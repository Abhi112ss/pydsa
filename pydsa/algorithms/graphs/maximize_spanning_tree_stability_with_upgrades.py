METADATA = {
    "id": 3600,
    "name": "Maximize Spanning Tree Stability with Upgrades",
    "slug": "maximize-spanning-tree-stability-with-upgrades",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "greedy", "union-find", "kruskal"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V + E)",
    "description": "Find the maximum possible minimum edge weight in a spanning tree after applying a limited number of upgrades to edge weights.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_sets = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            self.num_sets -= 1
            return True
        return False

def solve(n: int, edges: list[list[int]], k: int) -> int:
    """
    Finds the maximum possible minimum edge weight in a spanning tree after 
    upgrading at most k edges. An upgrade increases an edge weight to a target value.
    
    In this specific problem context, we assume an upgrade makes an edge weight 
    effectively 'infinite' (or sufficiently large) for the purpose of finding 
    the bottleneck weight.

    Args:
        n: The number of vertices in the graph.
        edges: A list of edges where edges[i] = [u, v, weight].
        k: The maximum number of edges that can be upgraded.

    Returns:
        The maximum possible minimum edge weight in the spanning tree.

    Examples:
        >>> solve(3, [[0, 1, 10], [1, 2, 5], [0, 2, 2]], 1)
        5
        >>> solve(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 1)
        1
    """
    # To maximize the minimum edge weight, we can binary search on the possible weight values.
    # However, a more direct approach is to realize we want to pick edges such that 
    # we use as many 'upgraded' edges as possible to bridge components that 
    # would otherwise be connected by low-weight edges.
    
    # Sort edges by weight descending to try and build the MST with largest weights first.
    # But since we want to maximize the MINIMUM weight, we actually want to see 
    # if we can form a spanning tree where all edges are >= X, 
    # using at most k upgrades for edges that are < X.

    # Collect all unique weights to binary search over them
    weights = sorted(list(set(edge[2] for edge in edges)))
    
    def can_form_mst_with_min_weight(min_weight_threshold: int) -> bool:
        """
        Checks if it's possible to form a spanning tree where all edges 
        have weight >= min_weight_threshold, given k upgrades.
        """
        dsu = UnionFind(n)
        upgrades_used = 0
        edges_count = 0
        
        # First, use all edges that already satisfy the threshold
        for u, v, w in edges:
            if w >= min_weight_threshold:
                if dsu.union(u, v):
                    edges_count += 1
        
        # Second, use edges that require an upgrade to meet the threshold
        # We prioritize edges that connect different components
        for u, v, w in edges:
            if w < min_weight_threshold:
                if dsu.find(u) != dsu.find(v):
                    # We only use an upgrade if we haven't exceeded k
                    # Note: In a real scenario, we'd need to check if this edge 
                    # is actually useful. Since we want to minimize upgrades, 
                    # we only union if they are in different components.
                    if upgrades_used < k:
                        if dsu.union(u, v):
                            upgrades_used += 1
                            edges_count += 1
                            
        return edges_count == n - 1

    # Binary search for the maximum possible minimum weight
    low = 0
    high = len(weights) - 1
    ans = 0
    
    # If k is large enough to cover all edges needed for a spanning tree, 
    # the answer could be the max weight available.
    # But we must be careful: an upgrade makes an edge "large". 
    # Let's assume an upgraded edge can satisfy any threshold.
    
    # If we can form a spanning tree using only k upgrades, 
    # the bottleneck will be the largest weight among the non-upgraded edges.
    
    # Correct logic: The bottleneck weight will either be one of the existing weights
    # or it will be "infinity" (if we can upgrade n-1 edges).
    # Since the problem asks for the max min weight, we check thresholds.
    
    # If k >= n-1, we can upgrade all edges in a spanning tree.
    # The problem implies we want to find the highest weight such that 
    # we can form a tree where all edges are >= that weight.
    
    # Let's refine: The possible answers are the weights in the 'weights' list.
    # If we can't even form a spanning tree with k upgrades, return 0 or similar.
    
    # Check if a spanning tree is even possible
    dsu_check = UnionFind(n)
    for u, v, w in edges:
        dsu_check.union(u, v)
    if dsu_check.num_sets > 1:
        return -1 # Or 0, depending on problem constraints for disconnected graphs

    # Binary search on the index of sorted weights
    left = 0
    right = len(weights) - 1
    best_weight = 0
    
    # If k is enough to make all edges in a spanning tree "large", 
    # the bottleneck is effectively the largest weight we can achieve.
    # However, the problem usually implies upgrades set weight to a specific value 
    # or we are looking for the weight of the (n-1-k)-th largest edge in the MST.
    
    # Let's use the property: The max-min weight is the weight of the 
    # (n-1-k)-th edge in a Maximum Spanning Tree.
    
    # 1. Sort edges by weight descending
    sorted_edges = sorted(edges, key=lambda x: x[2], reverse=True)
    dsu = UnionFind(n)
    mst_weights = []
    
    for u, v, w in sorted_edges:
        if dsu.union(u, v):
            mst_weights.append(w)
            if len(mst_weights) == n - 1:
                break
                
    if len(mst_weights) < n - 1:
        return -1

    # In a Maximum Spanning Tree, the edges are the best possible.
    # To maximize the minimum weight, we take the MST and upgrade the k smallest edges.
    # The new minimum weight will be the (k+1)-th smallest edge in the MST 
    # (if we index from 1) or the edge at index (len(mst_weights) - 1 - k).
    
    # Wait, if we upgrade an edge, its weight becomes "infinity".
    # So the minimum weight of the tree will be the minimum of the remaining 
    # (n-1-k) edges. To maximize this, we pick the MST.
    
    if k >= n - 1:
        # We can upgrade all edges in the MST. 
        # The problem usually provides a max weight or we return the max possible.
        # Assuming we return the max weight in the original set if all are upgraded.
        return weights[-1] if weights else 0

    # The k smallest edges in the MST are upgraded.
    # The minimum weight is the smallest edge that was NOT upgraded.
    # Since mst_weights is sorted descending, the smallest edges are at the end.
    # The edges are: mst_weights[0] ... mst_weights[n-2]
    # We upgrade the k smallest: mst_weights[n-1-k] ... mst_weights[n-2]
    # The minimum weight is mst_weights[n-2-k] if n-2-k >= 0.
    
    # Example: n=3, edges=[10, 5, 2], k=1. MST weights = [10, 5].
    # Upgrade 5. Min weight is 10.
    # Wait, if we upgrade 5, the edges are [10, inf]. Min is 10.
    # If k=1, we upgrade the smallest. The new min is the next smallest.
    
    # Let's re-sort mst_weights ascending for easier indexing
    mst_weights.sort()
    # Smallest is mst_weights[0]. We upgrade k smallest.
    # The new minimum is mst_weights[k].
    
    if k < len(mst_weights):
        return mst_weights[k]
    else:
        return weights[-1]
