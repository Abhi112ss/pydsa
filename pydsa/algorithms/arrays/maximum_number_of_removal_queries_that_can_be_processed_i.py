METADATA = {
    "id": 3018,
    "name": "Maximum Number of Removal Queries That Can Be Processed I",
    "slug": "maximum-number-of-removal-queries-that-can-be-processed-i",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of queries that can be processed such that each query removes a non-empty set of elements that are contiguous in the original array.",
}

def solve(n: int, queries: list[list[int]]) -> int:
    """
    Calculates the maximum number of queries that can be processed.
    
    The problem asks to process queries in order, but a query can only be 
    processed if the elements it removes are contiguous in the *current* 
    state of the array. A key insight is to process queries in reverse: 
    instead of removing elements, we add them back. A query is valid in 
    reverse if the elements being added form a contiguous block in the 
    current set of active elements.

    Args:
        n: The number of elements in the original array.
        queries: A list of queries where each query is [left, right].

    Returns:
        The maximum number of queries that can be processed.

    Examples:
        >>> solve(5, [[0, 2], [3, 4], [0, 4]])
        2
        >>> solve(4, [[0, 1], [2, 3], [0, 3]])
        3
    """
    # To process in reverse, we first identify which queries are "valid" 
    # if we were to add elements back. However, the problem states we 
    # must process queries in the given order. 
    # A query [L, R] is valid if all elements in [L, R] are currently 
    # present and they form a single contiguous block.
    
    # Actually, the condition "contiguous in the current array" means 
    # that if we remove [L, R], the remaining elements must have been 
    # contiguous before this removal.
    # A better way: A query [L, R] is valid if all elements in [L, R] 
    # have NOT been removed by a *previous* query in the sequence.
    # Wait, the rule is: "the elements being removed are contiguous".
    # This means if we have elements {0, 1, 2, 3, 4} and we remove {1, 2},
    # the remaining are {0, 3, 4}. If the next query is {0, 3}, it's 
    # NOT contiguous because 1 and 2 are gone.
    
    # Correct logic: A query [L, R] is valid if all elements in [L, R] 
    # are currently present AND they form a contiguous segment.
    # This is equivalent to saying that in the original array, 
    # all elements in [L, R] must be present, and no element 
    # outside [L, R] that was between elements of [L, R] can be missing.
    # Since we only remove, the "contiguous" requirement means that 
    # for a query [L, R] to be valid, all elements in [L, R] must 
    # still exist, and they must have been contiguous in the 
    # *original* array (which they are) and no elements *inside* 
    # the range [L, R] can have been removed by a *previous* query.
    
    # Wait, the problem says: "the elements being removed are contiguous 
    # in the current array". This means if we remove [L, R], 
    # all elements in [L, R] must be present.
    
    # Let's use the reverse approach:
    # Start with an empty set of elements. Add queries from last to first.
    # A query [L, R] can be "undone" (added) if the elements [L, R] 
    # form a contiguous block in the current set of elements.
    # This is true if the number of elements currently in the set 
    # that fall within [L, R] is exactly (R - L + 1), AND 
    # these elements are contiguous.
    
    # Actually, the simplest way to check if [L, R] is valid in the 
    # forward direction is: A query [L, R] is valid if no element 
    # in [L, R] has been removed by a previous query.
    # If any element in [L, R] was already removed, the elements 
    # in [L, R] are no longer contiguous (or some are missing).
    
    # Let's re-read: "the elements being removed are contiguous in the 
    # current array". If we remove [0, 2] from [0, 1, 2, 3, 4], 
    # we are left with [3, 4]. These are contiguous.
    # If the next query is [3, 4], we are left with [].
    # If the next query was [0, 4], it would be invalid because 
    # 0, 1, 2 are already gone.
    
    # So, a query [L, R] is valid if and only if all elements 
    # in the range [L, R] are still present.
    
    # Let's track which elements are present using a Fenwick tree 
    # or a simple boolean array. But we need to check if ALL 
    # elements in [L, R] are present.
    
    # Let's use a Disjoint Set Union (DSU) or a Segment Tree? 
    # Actually, we can just track the number of elements removed.
    # A query [L, R] is valid if (number of elements removed in [L, R]) == 0.
    
    # We can use a Fenwick tree to count how many elements in [L, R] 
    # have been removed.
    
    bit = [0] * (n + 1)

    def update(idx: int, val: int):
        idx += 1  # 1-based indexing
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)

    def query_sum(idx: int) -> int:
        idx += 1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    def query_range(l: int, r: int) -> int:
        return query_sum(r) - query_sum(l - 1)

    processed_count = 0
    # We need to track which elements are removed to ensure 
    # we don't remove the same element twice (though the problem 
    # implies queries are valid if they can be processed).
    # Actually, the problem says "the elements being removed are 
    # contiguous in the current array". This means all elements 
    # in [L, R] must be present.
    
    # We also need to handle the case where a query might 
    # overlap with a previously removed range.
    # If a query [L, R] is processed, all elements in [L, R] 
    # are removed.
    
    # To efficiently check if all elements in [L, R] are present:
    # 1. Check if any element in [L, R] has been removed.
    # 2. If not, mark all elements in [L, R] as removed.
    
    # To mark elements as removed efficiently, we can use a DSU 
    # to skip already removed elements.
    
    parent = list(range(n + 1))
    def find(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    # We need to check if any element in [L, R] is already removed.
    # We can use a Fenwick tree to store 1 if an element is removed, 0 otherwise.
    # A query [L, R] is valid if query_range(L, R) == 0.
    
    # However, there's a catch: if we remove [0, 2], and then 
    # the next query is [1, 3], the elements [1, 3] are NOT 
    # contiguous because 1 and 2 are gone.
    # So the condition is: query_range(L, R) must be 0.
    
    # Wait, if query_range(L, R) == 0, it means no element in [L, R] 
    # has been removed. This implies all elements in [L, R] are 
    # still there, and since they were contiguous originally, 
    # they are still contiguous.
    
    # Let's refine:
    # 1. For each query [L, R]:
    # 2. Check if any element in [L, R] is already removed.
    #    (Using Fenwick tree: query_range(L, R) == 0)
    # 3. If yes, this query cannot be processed.
    # 4. If no, this query IS processed. Increment count.
    #    Mark all elements in [L, R] as removed in Fenwick tree.
    #    To avoid O(N^2), use DSU to find the next unremoved element.

    removed = [False] * n
    # DSU to find the next element that is NOT removed.
    # parent[i] will point to the next index >= i that is not removed.
    # Actually, it's easier to have parent[i] point to the next 
    # index that might be unremoved.
    
    # Let's use a simpler DSU: parent[i] is the next index to check.
    # When i is removed, parent[i] = find(i + 1).
    
    parent = list(range(n + 1))
    def find_next(i: int) -> int:
        if parent[i] == i:
            return i
        parent[i] = find_next(parent[i])
        return parent[i]

    for l, r in queries:
        # Check if any element in [l, r] is already removed
        if query_range(l, r) == 0:
            processed_count += 1
            # Mark all elements in [l, r] as removed
            curr = find_next(l)
            while curr <= r:
                update(curr, 1)
                removed[curr] = True
                # Union this element with the next one
                parent[curr] = find_next(curr + 1)
                curr = find_next(curr)
                
    return processed_count

# The DSU approach above is slightly flawed because find_next(l) 
# might skip elements if we aren't careful. 
# Let's rewrite the solve function with a cleaner implementation.

def solve_final(n: int, queries: list[list[int]]) -> int:
    """
    Optimal implementation using Fenwick Tree and DSU.
    """
    bit = [0] * (n + 1)

    def update(idx: int, val: int):
        idx += 1
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)

    def query_sum(idx: int) -> int:
        idx += 1
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    def query_range(l: int, r: int) -> int:
        return query_sum(r) - query_sum(l - 1)

    # parent[i] points to the next index >= i that is NOT removed.
    parent = list(range(n + 1))
    def find(i: int) -> int:
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != root:
            next_i = parent[i]
            parent[i] = root
            i = next_i
        return root

    processed_count = 0
    for l, r in queries:
        # A query is valid if no element in [l, r] has been removed.
        if query_range(l, r) == 0:
            processed_count += 1
            # Mark all elements in [l, r] as removed.
            # We use DSU to jump over already removed elements.
            curr = find(l)
            while curr <= r:
                update(curr, 1)
                # Mark as removed by pointing to the next index
                parent[curr] = find(curr + 1)
                curr = find(curr)
                
    return processed_count

# Re-assigning to the required function name
solve = solve_final
