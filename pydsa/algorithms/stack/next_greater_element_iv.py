METADATA = {
    "id": 2454,
    "name": "Next Greater Element IV",
    "slug": "next-greater-element-iv",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "segment_tree", "data_structures"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the index of the next greater element for each element in an array, where the next greater element is the first element to the right that is strictly greater than the current element.",
}

class SegmentTree:
    """A Segment Tree to perform range maximum queries on indices."""

    def __init__(self, size: int):
        self.size = size
        # Tree stores the maximum index for a given value range
        # Since values can be large, we use the index in the sorted unique values array
        self.tree = [-1] * (4 * size)

    def update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        """Updates the segment tree at a specific value index with a new array index."""
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        """Queries the maximum index in the range [l, r]."""
        if r < start or end < l:
            return -1
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self.query(2 * node, start, mid, l, r)
        p2 = self.query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)


def solve(nums: list[int]) -> list[int]:
    """
    Finds the index of the next greater element for each element in nums.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers where result[i] is the index of the next greater 
        element for nums[i], or -1 if none exists.

    Examples:
        >>> solve([1, 3, 4, 2])
        [-1, 2, -1, -1]
        >>> solve([1, 2, 3, 4, 5])
        [1, 2, 3, 4, -1]
    """
    n = len(nums)
    if n == 0:
        return []

    # Coordinate compression to handle large integer values in Segment Tree
    sorted_unique_elements = sorted(list(set(nums)))
    rank_map = {val: i for i, val in enumerate(sorted_unique_elements)}
    m = len(sorted_unique_elements)

    # Segment tree will store the latest (rightmost) index encountered for each value rank
    seg_tree = SegmentTree(m)
    result = [-1] * n

    # We iterate backwards to find the "next" (right-side) greater element
    for i in range(n - 1, -1, -1):
        current_val = nums[i]
        current_rank = rank_map[current_val]

        # Find the maximum index among all elements with rank > current_rank
        # This effectively finds the closest index to the right that is strictly greater
        if current_rank + 1 < m:
            next_greater_idx = seg_tree.query(1, 0, m - 1, current_rank + 1, m - 1)
            result[i] = next_greater_idx

        # Update the segment tree with the current element's index at its rank
        seg_tree.update(1, 0, m - 1, current_rank, i)

    return result
