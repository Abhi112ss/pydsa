METADATA = {
    "id": 2874,
    "name": "Maximum Value of an Ordered Triplet II",
    "slug": "maximum-value-of-an-ordered-triplet-ii",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "segment_tree", "prefix_max"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value of (nums[i] - nums[j]) * nums[k] where i < j < k and nums[i] > nums[j].",
}

class SegmentTree:
    """A standard Segment Tree implementation for range maximum queries."""
    
    def __init__(self, data: list[int]):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data: list[int], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if r < start or end < l:
            return float('-inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_max = self.query(2 * node, start, mid, l, r)
        right_max = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(left_max, right_max)

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of (nums[i] - nums[j]) * nums[k] for i < j < k and nums[i] > nums[j].

    Args:
        nums: A list of integers.

    Returns:
        The maximum value of the triplet expression, or 0 if no such triplet exists.

    Examples:
        >>> solve([4, 2, 5, 3])
        6
        >>> solve([1, 2, 3, 4])
        0
    """
    n = len(nums)
    if n < 3:
        return 0

    # We need to maximize (nums[i] - nums[j]) * nums[k]
    # For a fixed j, we want the largest nums[i] where i < j and nums[i] > nums[j]
    # and the largest nums[k] where k > j.
    
    # Precompute suffix maximums for nums[k]
    suffix_max = [0] * n
    suffix_max[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(nums[i], suffix_max[i + 1])

    # To handle the condition nums[i] > nums[j] efficiently, we can use a 
    # Segment Tree to store values of nums[i] seen so far and query 
    # the maximum value in a specific range. 
    # However, since we only care about i < j, we can use a Fenwick tree 
    # or Segment Tree on the *values* of nums if they were small, 
    # but here values are up to 10^5.
    
    # A more efficient approach for "i < j and nums[i] > nums[j]" is to use 
    # a Segment Tree where the indices of the tree represent the sorted unique values 
    # of nums. This allows us to query the max nums[i] in the range (nums[j], max_val].

    # Coordinate Compression
    sorted_unique_elements = sorted(list(set(nums)))
    rank_map = {val: i for i, val in enumerate(sorted_unique_elements)}
    m = len(sorted_unique_elements)
    
    # Segment Tree to store the maximum nums[i] encountered so far, 
    # indexed by their rank in the sorted unique elements.
    tree_size = 1
    while tree_size < m:
        tree_size *= 2
    max_tree = [float('-inf')] * (2 * tree_size)

    def update(idx: int, val: int) -> None:
        idx += tree_size
        max_tree[idx] = max(max_tree[idx], val)
        while idx > 1:
            idx //= 2
            max_tree[idx] = max(max_tree[2 * idx], max_tree[2 * idx + 1])

    def query_max(l: int, r: int) -> float:
        res = float('-inf')
        l += tree_size
        r += tree_size
        while l <= r:
            if l % 2 == 1:
                res = max(res, max_tree[l])
                l += 1
            if r % 2 == 0:
                res = max(res, max_tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    max_triplet_val = 0

    for j in range(n):
        # 1. Check if we can form a triplet with current nums[j] as the middle element
        # We need max nums[i] where i < j and nums[i] > nums[j]
        current_val = nums[j]
        current_rank = rank_map[current_val]
        
        # Query the segment tree for the maximum value in range [rank_of_next_larger, m-1]
        if current_rank + 1 < m:
            best_i = query_max(current_rank + 1, m - 1)
            if best_i > current_val:
                # 2. If we found a valid i, multiply (nums[i] - nums[j]) by the max nums[k] where k > j
                if j + 1 < n:
                    best_k = suffix_max[j + 1]
                    max_triplet_val = max(max_triplet_val, (best_i - current_val) * best_k)

        # 3. Update the segment tree with the current nums[j] to be used as a potential nums[i] for future j's
        update(current_rank, current_val)

    return max_triplet_val
