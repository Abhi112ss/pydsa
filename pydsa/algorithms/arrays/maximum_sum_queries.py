METADATA = {
    "id": 2736,
    "name": "Maximum Sum Queries",
    "slug": "maximum-sum-queries",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "segment_tree", "binary_search", "monotonic_stack"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of elements in a subset of queries where each query defines a range and a value to add.",
}

def solve(queries: list[list[int]]) -> list[int]:
    """
    Args:
        queries: A list of queries where each query is [left, right, value].

    Returns:
        A list of integers representing the maximum sum after each query.
    """
    n = len(queries)
    sorted_queries = []
    for i in range(n):
        sorted_queries.append(queries[i] + [i])

    sorted_queries.sort(key=lambda x: x[1])

    max_sums = [0] * n
    current_max_sum = 0
    
    import heapq
    
    active_queries = []
    
    query_idx = 0
    
    sorted_queries.sort(key=lambda x: x[1])
    
    results = [0] * n
    
    sorted_queries = []
    for i in range(n):
        sorted_queries.append({
            "left": queries[i][0],
            "right": queries[i][1],
            "val": queries[i][2],
            "id": i
        })
    
    sorted_queries.sort(key=lambda x: x["right"])
    
    import bisect
    
    stack = []
    
    current_total_sum = 0
    
    ans = [0] * n
    
    sorted_queries = []
    for i in range(n):
        sorted_queries.append((queries[i][0], queries[i][1], queries[i][2], i))
    
    sorted_queries.sort(key=lambda x: x[1])
    
    stack = []
    
    for left, right, val, original_idx in sorted_queries:
        current_val = val
        while stack and stack[-1][0] <= left:
            prev_left, prev_val = stack.pop()
            current_val += prev_val
        
        stack.append((left, current_val))
        
        total_sum = 0
        for s_left, s_val in stack:
            total_sum += s_val
            
        # The above logic is O(N^2) in worst case. 
        # Let's use the correct O(N log N) approach.
        pass

    # Correct O(N log N) implementation using a monotonic approach
    # We need to track the maximum sum possible at any point.
    # A query (l, r, v) contributes 'v' to all indices in [l, r].
    # We want to find max sum for each query i after queries 0...i are applied.
    
    # Re-evaluating: The problem asks for the max sum after EACH query is added.
    # This is equivalent to: for each query i, find max_{indices j} (sum of values of queries k <= i where j in [l_k, r_k]).
    
    # Let's use a Segment Tree to maintain the current sums of all indices.
    # Since indices can be up to 10^9, we must coordinate compress or use a dynamic segment tree.
    # However, the number of queries is only 5*10^4. The relevant coordinates are the 'left' and 'right' boundaries.
    
    coords = set()
    for l, r, v in queries:
        coords.add(l)
        coords.add(r)
    
    sorted_coords = sorted(list(coords))
    coord_map = {val: i for i, val in enumerate(sorted_coords)}
    m = len(sorted_coords)
    
    tree_size = 1
    while tree_size < m:
        tree_size *= 2
    
    tree = [0] * (2 * tree_size)
    lazy = [0] * (2 * tree_size)
    
    def update(l, r, val, node, node_l, node_r):
        if l <= node_l and node_r <= r:
            tree[node] += val
            lazy[node] += val
            return
        
        mid = (node_l + node_r) // 2
        if lazy[node] != 0:
            tree[2 * node] += lazy[node]
            lazy[2 * node] += lazy[node]
            tree[2 * node + 1] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
            lazy[node] = 0
            
        if l <= mid:
            update(l, r, val, 2 * node, node_l, mid)
        if r > mid:
            update(l, r, val, 2 * node + 1, mid + 1, node_r)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

    results = []
    for l, r, v in queries:
        update(coord_map[l], coord_map[r], v, 1, 0, tree_size - 1)
        results.append(tree[1])
        
    return results

# The segment tree approach above is correct but the implementation needs to be iterative or 
# carefully written to avoid recursion depth issues in Python.
# Let's rewrite the solve function with an iterative segment tree for production grade.

def solve(queries: list[list[int]]) -> list[int]:
    """
    Args:
        queries: A list of queries where each query is [left, right, value].

    Returns:
        A list of integers representing the maximum sum after each query.
    """
    coords = set()
    for l, r, v in queries:
        coords.add(l)
        coords.add(r)
    
    sorted_coords = sorted(list(coords))
    coord_map = {val: i for i, val in enumerate(sorted_coords)}
    m = len(sorted_coords)
    
    n = 1
    while n < m:
        n *= 2
    
    tree = [0] * (2 * n)
    lazy = [0] * (2 * n)
    
    def apply(idx, val):
        tree[idx] += val
        if idx < n:
            lazy[idx] += val

    def build(idx):
        while idx > 1:
            idx //= 2
            tree[idx] = max(tree[2 * idx], tree[2 * idx + 1]) + lazy[idx]

    def push(idx):
        for s in range(idx.bit_length() - 1, 0, -1):
            i = idx >> s
            if lazy[i] != 0:
                apply(2 * i, lazy[i])
                apply(2 * i + 1, lazy[i])
                lazy[i] = 0

    def update_range(l, r, val):
        l += n
        r += n
        l0, r0 = l, r
        while l <= r:
            if l % 2 == 1:
                apply(l, val)
                l += 1
            if r % 2 == 0:
                apply(r, val)
                r -= 1
            l //= 2
            r //= 2
        build(l0)
        build(r0)

    ans = []
    for l, r, v in queries:
        update_range(coord_map[l], coord_map[r], v)
        ans.append(tree[1])
    
    return ans