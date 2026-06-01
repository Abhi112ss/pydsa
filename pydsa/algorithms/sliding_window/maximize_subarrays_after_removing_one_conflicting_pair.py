METADATA = {
    "id": 3480,
    "name": "Maximize Subarrays After Removing One Conflicting Pair",
    "slug": "maximize_subarrays_after_removing_one_conflicting_pair",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "sorting", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Maximize the number of valid subarrays by removing exactly one conflicting pair.",
}

def solve(n: int, conflicts: list[list[int]]) -> int:
    """
    Calculates the maximum number of valid subarrays possible after removing 
    exactly one conflicting pair. A subarray is valid if it contains no 
    conflicting pairs.

    Args:
        n: The number of elements in the array (1 to n).
        conflicts: A list of pairs [u, v] representing a conflict.

    Returns:
        The maximum number of valid subarrays after removing one pair.

    Examples:
        >>> solve(4, [[1, 2], [2, 3]])
        5
    """
    # Normalize conflicts so that u < v
    normalized_conflicts = []
    for u, v in conflicts:
        if u < v:
            normalized_conflicts.append((u, v))
        else:
            normalized_conflicts.append((v, u))

    # For each starting position i, we need to find the nearest conflict end.
    # Let min_end[i] be the smallest 'v' such that there is a conflict (u, v) with u >= i.
    # However, it's easier to track for each 'v', what is the largest 'u' that conflicts with it.
    # Let's define: for each index i, what is the nearest right-side conflict boundary?
    # boundary[i] = min(v) for all (u, v) where u >= i.
    
    # To handle "removing one pair", we need to know the first and second constraints.
    # For each index i, let:
    # first_constraint[i] = the smallest v such that there exists a conflict (u, v) with u >= i.
    # second_constraint[i] = the second smallest v such that there exists a conflict (u, v) with u >= i.
    
    # Pre-calculate the most restrictive conflict for each starting position.
    # We use a suffix approach.
    
    # max_u_for_v[v] stores the largest u such that (u, v) is a conflict.
    # But we actually need: for a fixed start i, what is the smallest v?
    # Let's map each index i to the smallest v that forms a conflict with some u >= i.
    
    # Let's use a different approach:
    # For each index i (from 1 to n), find the smallest v such that there is a conflict (u, v) with u >= i.
    # Actually, the condition is: a subarray [L, R] is valid if for all (u, v) in conflicts,
    # it is NOT the case that L <= u and v <= R.
    # This is equivalent to: for a fixed L, R must be < min(v) for all (u, v) where u >= L.
    
    # Let's find for each L, the smallest v such that there is a conflict (u, v) with u >= L.
    # Let this be limit1[L].
    # Let the second smallest be limit2[L].
    
    # To compute this efficiently:
    # For each conflict (u, v), it affects all L <= u.
    # We want to find the two smallest v's for each L.
    
    # Initialize limits with n + 1
    limit1 = [n + 1] * (n + 2)
    limit2 = [n + 1] * (n + 2)
    
    # We need to track which conflict provided the limit1 to allow "removal"
    # limit_idx[L] = index of the conflict that provides limit1[L]
    limit_idx = [-1] * (n + 2)

    # Sort conflicts by u descending to use a suffix-like update
    # Or simply: for each conflict (u, v), it is a candidate for all L in [1, u]
    # We can use a segment tree or simply process from n down to 1.
    
    # Let's store conflicts by their u value
    conflicts_by_u = [[] for _ in range(n + 1)]
    for idx, (u, v) in enumerate(normalized_conflicts):
        conflicts_by_u[u].append((v, idx))

    # current_min1 and current_min2 will track the two smallest v's seen so far
    # as we iterate L from n down to 1.
    # Because if a conflict (u, v) exists, it constrains all L <= u.
    # So as we go from n down to 1, we add conflicts where u == L.
    
    import heapq
    # We need the two smallest v's among all conflicts (u, v) where u >= L.
    # We can use a min-heap to keep track of all v's for u >= L.
    # But we only need the two smallest.
    
    # Actually, a simpler way:
    # For each L, the constraints are the set of all v such that there is a conflict (u, v) with u >= L.
    # As L decreases, the set of available conflicts grows.
    
    # We'll use a min-heap to keep track of the smallest v's.
    # Since we only care about the two smallest, we can maintain them.
    # However, we need to know WHICH conflict index produced the smallest v.
    
    # To handle the "remove one" part:
    # Total valid subarrays = sum_{L=1 to n} (limit1[L] - L)
    # If we remove conflict 'idx', the new limit for L becomes limit2[L] 
    # IF limit_idx[L] == idx, otherwise it stays limit1[L].
    
    # Let's refine the limits:
    # For each L, find the two smallest v's among all (u, v) where u >= L.
    # Let these be (v1, idx1) and (v2, idx2).
    
    # We can use a min-heap to store (v, idx) for all conflicts (u, v) where u >= L.
    # As L goes from n down to 1, we add all (v, idx) where u == L.
    # To keep only the two smallest, we can't just use a heap because we need to 
    # potentially access the 3rd, 4th... if the 1st or 2nd is removed? 
    # No, if we remove the 1st, the 2nd becomes the new 1st.
    
    # Wait, the "remove one" is global. We pick ONE conflict index and remove it.
    # If we remove conflict 'idx', for each L, the new limit is:
    #   - limit2[L] if limit_idx[L] == idx
    #   - limit1[L] if limit_idx[L] != idx
    
    # This is correct.
    
    # Step 1: Calculate limit1, limit2, and limit_idx for each L
    # We use a min-heap to keep track of the smallest v's. 
    # Since we only need the two smallest, and we are adding elements, 
    # we can just maintain a sorted list of the smallest elements.
    
    # But wait, the number of conflicts can be up to 10^5. 
    # A heap of all v's where u >= L is fine.
    
    current_v_heap = [] # stores (v, idx)
    
    # To make it O(N log N), we use a heap.
    # But we need to be careful: we need the two smallest v's for each L.
    # As L decreases, we add conflicts (u, v) where u == L.
    # The heap will contain all (v, idx) for all u >= L.
    # The two smallest are heap[0] and the next smallest.
    # But the next smallest might not be heap[1] if we don't use a proper heap.
    # Actually, we can just use a min-heap and peek.
    
    # To find the second smallest in a heap:
    # We can't easily. Let's use a different approach.
    # We only need the two smallest. Let's use a sorted list of size 2? 
    # No, because when we add a new v, it might be smaller than both.
    
    # Let's use a min-heap to store all (v, idx) for all u >= L.
    # For each L, the smallest is heap[0].
    # To find the second smallest, we can't just look at heap[1].
    # We need to find the smallest (v, idx) such that idx != heap[0].idx.
    
    # Correct approach:
    # For each L, we want:
    # min1 = min { v | (u, v) is conflict and u >= L }
    # min2 = min { v | (u, v) is conflict, u >= L, and idx != min1_idx }
    
    # We can use a Segment Tree or a Fenwick tree? No.
    # Let's use a Min-Heap and when we need the second smallest, 
    # we temporarily pop the first. But that's slow.
    
    # Better: Use a Segment Tree where each node stores the two smallest (v, idx) pairs.
    # Or, since we are iterating L from n down to 1, we are just adding elements.
    # We can use a simple min-heap and to find the second smallest, 
    # we can't just pop.
    
    # Let's use a specialized data structure: a min-heap that supports 
    # finding the two smallest elements. Actually, a simple min-heap 
    # works if we just want the absolute smallest. 
    # To get the second smallest, we can use a Segment Tree over the range of indices 
    # or just use the fact that we only add elements.
    
    # Let's use a Segment Tree on the range of possible v values [1, n].
    # Each node in the Segment Tree will store the two smallest (v, idx) pairs.
    # But v is the value itself. So we can use a Segment Tree over the index of conflicts? No.
    
    # Let's go back:
    # For each L, we need the two smallest v's among all conflicts with u >= L.
    # Let's collect all (v, idx) for all u >= L.
    # We can use a Segment Tree where the leaf at position 'u' stores all (v, idx) for that 'u'.
    # Then we query the range [L, n] for the two smallest (v, idx).
    
    # Wait, the number of conflicts is M.
    # We can build a Segment Tree over the range [1, n].
    # Each leaf i stores the smallest (v, idx) for all conflicts with u = i.
    # Each internal node stores the two smallest (v, idx) from its children.
    
    # 1. Initialize Segment Tree with (infinity, -1)
    # 2. For each conflict (u, v, idx), update leaf u with (v, idx).
    #    Note: a leaf u might have multiple conflicts. So leaf u should store 
    #    the two smallest (v, idx) for that specific u.
    # 3. Build the tree.
    # 4. For each L from 1 to n, query range [L, n] for the two smallest (v, idx).

    tree_size = 1
    while tree_size <= n:
        tree_size *= 2
    
    # Each node: [(v1, idx1), (v2, idx2)]
    tree = [[(n + 1, -1), (n + 1, -1)] for _ in range(2 * tree_size)]

    def merge(pair1, pair2):
        # Merges two lists of (v, idx) and returns the two smallest unique-idx pairs
        combined = sorted(pair1 + pair2)
        res = []
        seen_idx = set()
        for v, idx in combined:
            if idx != -1 and idx not in seen_idx:
                res.append((v, idx))
                seen_idx.add(idx)
                if len(res) == 2:
                    break
        while len(res) < 2:
            res.append((n + 1, -1))
        return res

    # Populate leaves
    for idx, (u, v) in enumerate(normalized_conflicts):
        # We need to update leaf u. Since multiple conflicts can have same u,
        # we first collect them.
        pass # handled below

    # Correct way to populate:
    leaf_data = [[] for _ in range(n + 1)]
    for idx, (u, v) in enumerate(normalized_conflicts):
        leaf_data[u].append((v, idx))
    
    for i in range(1, n + 1):
        if leaf_data[i]:
            # Sort and take top 2
            leaf_data[i].sort()
            top_two = []
            seen_idx = set()
            for v, idx in leaf_data[i]:
                if idx not in seen_idx:
                    top_two.append((v, idx))
                    seen_idx.add(idx)
                if len(top_two) == 2:
                    break
            while len(top_two) < 2:
                top_two.append((n + 1, -1))
            tree[tree_size + i] = top_two

    # Build tree
    for i in range(tree_size - 1, 0, -1):
        tree[i] = merge(tree[2 * i], tree[2 * i + 1])

    def query(l, r):
        res = [(n + 1, -1), (n + 1, -1)]
        l += tree_size
        r += tree_size
        while l <= r:
            if l % 2 == 1:
                res = merge(res, tree[l])
                l += 1
            if r % 2 == 0:
                res = merge(res, tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    # Step 2: Calculate base total and the gain for each conflict
    # base_total = sum_{L=1 to n} (limit1[L] - L)
    # gain[idx] = sum_{L where limit_idx[L] == idx} (limit2[L] - limit1[L])
    
    base_total = 0
    gain = [0] * len(normalized_conflicts)
    
    for L in range(1, n + 1):
        # Query range [L, n]
        res = query(L, n)
        v1, idx1 = res[0]
        v2, idx2 = res[1]
        
        # Valid subarrays starting at L are [L, L], [L, L+1], ..., [L, v1-1]
        # Number of such subarrays is (v1 - 1) - L + 1 = v1 - L
        # But if v1 is n+1, it's n - L + 1. 
        # Wait, if v1 = n+1, the max R is n. So count is n - L + 1.
        # If v1 is a conflict, the max R is v1 - 1. So count is (v1 - 1) - L + 1 = v1 - L.
        # This works if we treat v1 as n+1.
        
        count = v1 - L
        if count < 0: count = 0 # Should not happen as v1 >= L+1 or v1=n+1
        
        # If v1 is n+1, it means no conflict starts at or after L.
        # The number of subarrays is n - L + 1.
        if v1 > n:
            count = n - L + 1
            
        base_total += count
        
        # If we remove idx1, the new limit is v2.
        # The new count is v2 - L (or n - L + 1 if v2 > n).
        # The gain is (new_count - old_count).
        if idx1 != -1:
            new_count = v2 - L
            if v2 > n:
                new_count = n - L + 1
            
            gain[idx1] += (new_count - count)

    return base_total + max(gain) if gain else base_total

# The Segment Tree approach is O(M log N + N log N). 
# Given