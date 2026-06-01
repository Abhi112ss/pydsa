METADATA = {
    "id": 3479,
    "name": "Fruits Into Baskets III",
    "slug": "fruits-into-baskets-iii",
    "category": "Segment Tree",
    "aliases": [],
    "tags": ["segment_tree", "greedy", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of fruits that can be placed into baskets such that each fruit goes into the first available basket with sufficient capacity.",
}

class SegmentTree:
    """A Segment Tree to maintain the maximum value in ranges for efficient searching."""
    
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

    def update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def find_first_greater_or_equal(self, node: int, start: int, end: int, target: int) -> int:
        """Finds the leftmost index in the range [start, end] where tree[node] >= target."""
        if self.tree[node] < target:
            return -1
        if start == end:
            return start
        
        mid = (start + end) // 2
        # Check left child first to ensure we find the smallest index (greedy)
        res = self.find_first_greater_or_equal(2 * node, start, mid, target)
        if res == -1:
            res = self.find_first_greater_or_equal(2 * node + 1, mid + 1, end, target)
        return res

def solve(fruits: list[int], baskets: list[int]) -> int:
    """
    Calculates the maximum number of fruits that can be placed into baskets.
    Each fruit is placed in the first available basket that can hold it.

    Args:
        fruits: A list of integers representing the size of each fruit.
        baskets: A list of integers representing the capacity of each basket.

    Returns:
        The total count of fruits successfully placed in baskets.

    Examples:
        >>> solve([4, 2, 5], [3, 5, 4])
        2
        >>> solve([1, 2, 3], [1, 1, 1])
        1
    """
    n = len(baskets)
    st = SegmentTree(baskets)
    placed_count = 0

    for fruit_size in fruits:
        # Use the segment tree to find the leftmost index i such that baskets[i] >= fruit_size
        # This is an O(log n) operation
        basket_idx = st.find_first_greater_or_equal(1, 0, n - 1, fruit_size)
        
        if basket_idx != -1:
            placed_count += 1
            # Once a basket is used, its capacity effectively becomes 0 for future fruits
            # Update the segment tree to reflect the used basket
            st.update(1, 0, n - 1, basket_idx, 0)
            
    return placed_count
