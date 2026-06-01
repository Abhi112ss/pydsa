METADATA = {
    "id": 2070,
    "name": "Most Beautiful Item for Each Query",
    "slug": "most-beautiful-item-for-each-query",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O((n + q) log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum beauty value of an item within a given index range for multiple queries.",
}

import bisect

def solve(beauty: list[int], queries: list[list[int]]) -> list[int]:
    """
    Finds the maximum beauty value for each query within the specified index range.

    Args:
        beauty: A list of integers representing the beauty of items at each index.
        queries: A list of queries, where each query is [left, right] representing 
                 the inclusive index range.

    Returns:
        A list of integers representing the maximum beauty for each query. 
        Returns -1 if no item exists in the range.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [[0, 2], [2, 4], [0, 4]])
        [3, 5, 5]
        >>> solve([10, 2, 5, 1], [[0, 1], [1, 3]])
        [10, 5]
    """
    n = len(beauty)
    # Create a list of (beauty_value, original_index) tuples
    # This allows us to sort by beauty while keeping track of where items were
    indexed_beauty = []
    for i in range(n):
        indexed_beauty.append((beauty[i], i))
    
    # Sort items by beauty in ascending order
    indexed_beauty.sort()
    
    # Extract sorted beauty values and sorted original indices for binary search
    sorted_values = [item[0] for item in indexed_beauty]
    sorted_indices = [item[1] for item in indexed_beauty]
    
    # To efficiently find the max beauty in a range, we need to know 
    # if any item with beauty >= X exists within [left, right].
    # However, the standard approach for "max in range" is Segment Tree/Sparse Table.
    # But the problem asks for the largest beauty value *available* in the range.
    # Since we want the *largest* beauty, we should check items from highest beauty to lowest.
    
    # Correct approach for this specific problem:
    # We want the largest beauty[i] such that left <= i <= right.
    # We can use a Segment Tree to find the maximum in a range.
    
    # Segment Tree Implementation
    tree_size = 1
    while tree_size < n:
        tree_size *= 2
    
    tree = [-1] * (2 * tree_size)
    
    # Build the segment tree with beauty values
    for i in range(n):
        tree[tree_size + i] = beauty[i]
    
    for i in range(tree_size - 1, 0, -1):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])
        
    def query_max(l: int, r: int) -> int:
        """Standard Segment Tree range maximum query."""
        res = -1
        l += tree_size
        r += tree_size
        while l <= r:
            if l % 2 == 1:
                res = max(res, tree[l])
                l += 1
            if r % 2 == 0:
                res = max(res, tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    results = []
    for left, right in queries:
        results.append(query_max(left, right))
        
    return results

# Note: The prompt suggested sorting + binary search. 
# While Segment Tree is O(Q log N), a sorting + binary search approach 
# would involve a Persistent Segment Tree or a Fenwick tree on sorted values 
# to find the largest beauty whose index is in [L, R].
# Given the constraints and the "Most Beautiful" requirement, 
# Segment Tree is the most direct production-grade solution for Range Maximum Query.
