METADATA = {
    "id": 1651,
    "name": "Hopper Company Queries III",
    "slug": "hopper-company-queries-iii",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "lazy_propagation", "range_update", "range_query"],
    "difficulty": "hard",
    "time_complexity": "O(q log n)",
    "space_complexity": "O(n)",
    "description": "Perform range updates and range minimum queries on an array using a segment tree with lazy propagation.",
}

class SegmentTree:
    """A Segment Tree implementation with Lazy Propagation for range updates and range minimum queries."""

    def __init__(self, data: list[int]):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data: list[int], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def _push(self, node: int) -> None:
        """Propagate the lazy value to children."""
        if self.lazy[node] != 0:
            self.tree[2 * node] += self.lazy[node]
            self.lazy[2 * node] += self.lazy[node]
            self.tree[2 * node + 1] += self.lazy[node]
            self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(self, l: int, r: int, val: int) -> None:
        self._update(1, 0, self.n - 1, l, r, val)

    def _update(self, node: int, start: int, end: int, l: int, r: int, val: int) -> None:
        if start > end or start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] += val
            self.lazy[node] += val
            return
        
        self._push(node)
        mid = (start + end) // 2
        self._update(2 * node, start, mid, l, r, val)
        self._update(2 * node + 1, mid + 1, end, l, r, val)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l: int, r: int) -> int:
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if start > end or start > r or end < l:
            return float('inf')
        if start >= l and end <= r:
            return self.tree[node]
        
        self._push(node)
        mid = (start + end) // 2
        left_min = self._query(2 * node, start, mid, l, r)
        right_min = self._query(2 * node + 1, mid + 1, end, l, r)
        return min(left_min, right_min)


def solve(n: int, queries: list[list[int]]) -> list[int]:
    """
    Processes queries for range updates and range minimum queries.

    Args:
        n: The size of the initial array (all elements are 0).
        queries: A list of queries where:
            - queries[i] = [1, l, r, val] means add val to range [l, r].
            - queries[i] = [2, l, r] means find the minimum in range [l, r].

    Returns:
        A list of integers representing the results of type 2 queries.

    Examples:
        >>> solve(5, [[1, 0, 2, 3], [2, 0, 4], [1, 2, 4, -1], [2, 0, 4]])
        [0, -1]
    """
    # Initialize array with zeros as per problem context
    initial_array = [0] * n
    st = SegmentTree(initial_array)
    results = []

    for query in queries:
        query_type = query[0]
        
        if query_type == 1:
            # Range Update: [l, r] += val
            _, left, right, val = query
            st.update(left, right, val)
        else:
            # Range Minimum Query: min([l, r])
            _, left, right = query
            res = st.query(left, right)
            results.append(int(res))

    return results
