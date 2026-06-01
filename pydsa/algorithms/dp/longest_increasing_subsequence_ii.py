METADATA = {
    "id": 2407,
    "name": "Longest Increasing Subsequence II",
    "slug": "longest-increasing-subsequence-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "segment_tree", "binary_search"],
    "difficulty": "hard",
    "time_complexity": "O(n log m) where m is max(nums)",
    "space_complexity": "O(m) where m is max(nums)",
    "description": "Find the length of the longest subsequence such that the difference between adjacent elements is at most k.",
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

    def query(self, left: int, right: int, node: int, start: int, end: int) -> int:
        """Queries the maximum value in the range [left, right]."""
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        p1 = self.query(left, right, 2 * node, start, mid)
        p2 = self.query(left, right, 2 * node + 1, mid + 1, end)
        return max(p1, p2)


def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest subsequence where the difference between 
    adjacent elements is at most k.

    Args:
        nums: A list of integers representing the sequence.
        k: The maximum allowed difference between adjacent elements.

    Returns:
        The length of the longest valid subsequence.

    Examples:
        >>> solve([4, 2, 1, 4, 3, 4, 5, 8, 12], 3)
        5
        >>> solve([1, 2, 3, 4, 5], 1)
        5
    """
    if not nums:
        return 0

    # The range of values in nums determines the size of our Segment Tree.
    # We use the values themselves as indices in the Segment Tree.
    max_val = max(nums)
    segment_tree = SegmentTree(max_val + 1)

    max_length = 0

    for num in nums:
        # Define the search range [num - k, num + k] clamped to valid indices.
        # This ensures the difference between the current element and the 
        # previous element in the subsequence is at most k.
        lower_bound = max(0, num - k)
        upper_bound = min(max_val, num + k)

        # Query the segment tree for the maximum DP value in the valid range.
        # dp[v] stores the length of the longest subsequence ending with value v.
        current_max_prev = segment_tree.query(lower_bound, upper_bound, 1, 0, max_val)
        
        # The new length for the current number is the best previous length + 1.
        current_len = current_max_prev + 1
        
        # Update the segment tree with the new length for the current value.
        segment_tree.update(num, current_len, 1, 0, max_val)
        
        # Track the global maximum length found so far.
        if current_len > max_length:
            max_length = current_len

    return max_length
