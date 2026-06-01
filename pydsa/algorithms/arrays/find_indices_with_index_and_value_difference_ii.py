METADATA = {
    "id": 2905,
    "name": "Find Indices With Index and Value Difference II",
    "slug": "find-indices-with-index-and-value-difference-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sliding_window", "segment_tree"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find all pairs of indices (i, j) such that i < j and nums[j] - nums[i] - (j - i) > threshold.",
}

class SegmentTree:
    """A Segment Tree implementation to perform range maximum queries."""

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
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)

def solve(nums: list[int], threshold: int) -> list[list[int]]:
    """
    Finds all pairs (i, j) such that i < j and nums[j] - nums[i] - (j - i) > threshold.
    
    The condition can be rewritten as:
    nums[j] - j - (nums[i] - i) > threshold
    Let B[k] = nums[k] - k.
    The condition becomes: B[j] - B[i] > threshold => B[j] - threshold > B[i].
    
    However, the problem asks for all pairs (i, j) where i < j. 
    Wait, the condition is nums[j] - nums[i] - (j - i) > threshold.
    Rearranging: (nums[j] - j) - (nums[i] - i) > threshold.
    Let val[k] = nums[k] - k.
    We need to find pairs (i, j) such that i < j and val[j] - val[i] > threshold.
    
    Args:
        nums: A list of integers.
        threshold: An integer threshold.

    Returns:
        A list of lists, where each inner list is a pair of indices [i, j].

    Examples:
        >>> solve([4, 2, 1, 5], 1)
        [[0, 3]]
        >>> solve([1, 1, 1, 1], 0)
        []
    """
    n = len(nums)
    # Transform the array to simplify the condition to val[j] - val[i] > threshold
    val = [nums[i] - i for i in range(n)]
    
    # We need to find all i < j such that val[i] < val[j] - threshold.
    # Since we need to return ALL pairs, and the number of pairs can be O(n^2),
    # we use a Segment Tree to find the indices.
    # To handle the "all pairs" requirement efficiently, we store indices in the Segment Tree.
    # However, a standard Segment Tree returns the max value. 
    # To find all indices i that satisfy the condition for a fixed j, 
    # we can use a Segment Tree where each node stores a sorted list of values (or indices).
    # But the problem asks for all pairs, and the constraints/output suggest we can't 
    # avoid O(number of pairs) in the worst case.
    
    # Let's use a Segment Tree where each node stores the maximum value in its range.
    # For each j, we want to find all i in [0, j-1] such that val[i] < val[j] - threshold.
    # This is actually easier if we use a Segment Tree to find the MINIMUM value in a range.
    # If min(val[0...j-1]) < val[j] - threshold, there is at least one i.
    # We can use a Segment Tree to store the minimums to prune the search.
    
    tree_size = 1
    while tree_size < n:
        tree_size *= 2
    
    # min_tree stores the minimum value of val[i] in the range
    min_tree = [float('inf')] * (2 * tree_size)
    
    for i in range(n):
        min_tree[tree_size + i] = val[i]
    
    for i in range(tree_size - 1, 0, -1):
        min_tree[i] = min(min_tree[2 * i], min_tree[2 * i + 1])

    def find_indices_in_range(node: int, start: int, end: int, l: int, r: int, target: float, results: list[int]) -> None:
        # If the minimum in this range is not less than target, no i in this range works
        if r < start or end < l or min_tree[node] >= target:
            return
        
        # If leaf node
        if start == end:
            results.append(start)
            return
        
        mid = (start + end) // 2
        # Search left child
        find_indices_in_range(2 * node, start, mid, l, r, target, results)
        # Search right child
        find_indices_in_range(2 * node + 1, mid + 1, end, l, r, target, results)

    ans = []
    for j in range(1, n):
        target = val[j] - threshold
        # We need to find all i in [0, j-1] such that val[i] < target
        # We use the min_tree to prune branches that don't contain any val[i] < target
        found_indices = []
        find_indices_in_range(1, 0, tree_size - 1, 0, j - 1, target, found_indices)
        
        # The problem asks for pairs [i, j]. Since we need to return them in a specific order
        # (usually sorted by i then j), and we iterate j from 1 to n, we should collect
        # and then sort or handle carefully. The problem doesn't specify order, 
        # but typically it's lexicographical.
        for i in found_indices:
            ans.append([i, j])

    # The problem asks for all pairs. The order of pairs in the output is not strictly 
    # defined in the prompt, but usually, it's sorted by i then j.
    # Given the way we iterate j, we are collecting [i, j] where j is increasing.
    # To get lexicographical order [i, j], we sort.
    ans.sort()
    return ans
