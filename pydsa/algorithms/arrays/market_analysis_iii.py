METADATA = {
    "id": 2922,
    "name": "Market Analysis III",
    "slug": "market_analysis_iii",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "coordinate_compression", "query_processing"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum stock price within specific time intervals using coordinate compression and a segment tree.",
}

class SegmentTree:
    """A Segment Tree implementation for Range Maximum Queries."""

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (4 * size)

    def update(self, index: int, value: int, node: int, start: int, end: int) -> None:
        """Updates the value at a specific index in the segment tree."""
        if start == end:
            self.tree[node] = max(self.tree[node], value)
            return
        
        mid = (start + end) // 2
        if index <= mid:
            self.update(index, value, 2 * node, start, mid)
        else:
            self.update(index, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l: int, r: int, node: int, start: int, end: int) -> int:
        """Queries the maximum value in the range [l, r]."""
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_max = self.query(l, r, 2 * node, start, mid)
        right_max = self.query(l, r, 2 * node + 1, mid + 1, end)
        return max(left_max, right_max)


def solve(prices: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Solves the Market Analysis III problem using coordinate compression and a Segment Tree.

    Args:
        prices: A list of lists where prices[i] = [timestamp_i, price_i].
        queries: A list of lists where queries[j] = [start_j, end_j].

    Returns:
        A list of integers representing the maximum price for each query interval.

    Examples:
        >>> solve([[1, 10], [2, 20], [3, 15]], [[1, 2], [2, 3], [1, 3]])
        [20, 20, 20]
    """
    # 1. Coordinate Compression: Collect all unique timestamps to map them to a continuous range
    # This allows us to use a Segment Tree even if timestamps are very large or sparse.
    all_timestamps = sorted(list(set(p[0] for p in prices)))
    timestamp_map = {ts: i for i, ts in enumerate(all_timestamps)}
    num_unique_ts = len(all_timestamps)

    if not all_timestamps:
        return [0] * len(queries)

    # 2. Build the Segment Tree
    # The tree will store the maximum price at each compressed timestamp index.
    st = SegmentTree(num_unique_ts)
    for ts, price in prices:
        st.update(timestamp_map[ts], price, 1, 0, num_unique_ts - 1)

    import bisect
    results = []
    for start_time, end_time in queries:
        # 3. Find the range of indices in the compressed array that fall within [start_time, end_time]
        # bisect_left finds the first index where timestamp >= start_time
        # bisect_right finds the first index where timestamp > end_time
        idx_start = bisect.bisect_left(all_timestamps, start_time)
        idx_end = bisect.bisect_right(all_timestamps, end_time) - 1

        if idx_start > idx_end:
            # No timestamps fall within the query range
            results.append(0)
        else:
            # Perform Range Maximum Query on the Segment Tree
            results.append(st.query(idx_start, idx_end, 1, 0, num_unique_ts - 1))

    return results
