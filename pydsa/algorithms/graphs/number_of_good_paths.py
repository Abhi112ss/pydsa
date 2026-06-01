METADATA = {
    "id": 2421,
    "name": "Number of Good Paths",
    "slug": "number-of-good-paths",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "union_find", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of paths in a tree where the starting and ending nodes have the same value and all intermediate nodes have values less than or equal to them.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

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
            return True
        return False

def solve(edges: list[list[int]], vals: list[int]) -> int:
    """
    Calculates the number of good paths in a tree using a greedy Union-Find approach.
    
    A path is 'good' if the start and end nodes have the same value and all 
    intermediate nodes have values <= the start/end value.

    Args:
        edges: A list of undirected edges where edges[i] = [u, v].
        vals: A list of integers representing the value of each node.

    Returns:
        The total number of good paths.

    Examples:
        >>> solve([[1, 3], [2, 3, 4, 5]], [1, 1, 1, 1, 1]) # Simplified representation
        # Actual LeetCode input format:
        >>> solve([[1, 3], [2, 3], [3, 4], [3, 5]], [1, 1, 1, 1, 1])
        5
    """
    n = len(vals)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Group node indices by their values to process them in increasing order
    val_to_nodes = {}
    for i, val in enumerate(vals):
        if val not in val_to_nodes:
            val_to_nodes[val] = []
        val_to_nodes[val].append(i)

    # Sort unique values to process nodes from smallest to largest
    sorted_unique_vals = sorted(val_to_nodes.keys())
    
    dsu = UnionFind(n)
    # track_count[root] stores how many nodes of the CURRENT value are in this component
    track_count = [0] * n
    total_good_paths = n  # Every single node is a good path of length 0

    for val in sorted_unique_vals:
        nodes_with_val = val_to_nodes[val]
        
        # Step 1: For each node of the current value, connect it to neighbors 
        # that have already been processed (i.e., neighbors with value <= current val)
        for node in nodes_with_val:
            for neighbor in adj[node]:
                if vals[neighbor] <= val:
                    dsu.union(node, neighbor)
        
        # Step 2: Count how many nodes of the current value exist in each component.
        # If a component has 'k' nodes of the current value, they can form 
        # k * (k - 1) / 2 additional paths.
        # We use a temporary dictionary to avoid resetting the whole track_count array.
        component_val_counts = {}
        for node in nodes_with_val:
            root = dsu.find(node)
            component_val_counts[root] = component_val_counts.get(root, 0) + 1
            
        for root_count in component_val_counts.values():
            if root_count > 1:
                # Combination formula: nC2 = n*(n-1)/2
                total_good_paths += (root_count * (root_count - 1)) // 2

    return total_good_paths
