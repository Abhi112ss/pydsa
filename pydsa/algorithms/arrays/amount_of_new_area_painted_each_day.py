METADATA = {
    "id": 2158,
    "name": "Amount of New Area Painted Each Day",
    "slug": "amount-of-new-area-painted-each-day",
    "category": "Segment Tree",
    "aliases": [],
    "tags": ["segment_tree", "intervals", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the amount of new area painted each day given a series of paint strokes on a line.",
}

class SegmentTree:
    """
    A Segment Tree implementation to manage range updates and queries.
    Specifically designed to track if a range is fully covered.
    """
    def __init__(self, n: int):
        self.n = n
        # tree[i] stores the number of painted units in the range covered by node i
        self.tree = [0] * (4 * n)
        # is_full[i] is True if the entire range covered by node i is painted
        self.is_full = [False] * (4 * n)

    def update(self, node: int, start: int, end: int, l: int, r: int) -> int:
        """
        Updates the range [l, r] to be painted and returns the count of newly painted units.
        """
        # If this range is already fully painted, no new area can be added
        if self.is_full[node]:
            return 0
        
        # If the current node range is completely within the target range [l, r]
        if l <= start and end <= r:
            # Calculate how many units in this range were not yet painted
            new_painted = (end - start + 1) - self.tree[node]
            # Mark this node and its entire range as fully painted
            self.tree[node] = end - start + 1
            self.is_full[node] = True
            return new_painted

        mid = (start + end) // 2
        new_area = 0
        
        # Standard segment tree range update logic
        if l <= mid:
            new_area += self.update(2 * node, start, mid, l, r)
        if r > mid:
            new_area += self.update(2 * node + 1, mid + 1, end, l, r)
            
        # Update current node based on children
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        # If both children are fully painted, this node is fully painted
        if self.is_full[2 * node] and self.is_full[2 * node + 1]:
            self.is_full[node] = True
            
        return new_area

def solve(n: int, in_range: list[list[int]]) -> list[int]:
    """
    Calculates the amount of new area painted each day.

    Args:
        n (int): The total length of the line (from 1 to n).
        in_range (list[list[int]]): A list of [start, end] pairs for each day.

    Returns:
        list[int]: A list where the i-th element is the new area painted on day i.

    Examples:
        >>> solve(5, [[1, 3], [2, 5]])
        [3, 2]
        >>> solve(10, [[1, 2], [5, 5], [2, 6]])
        [2, 1, 3]
    """
    # Segment tree handles range [1, n]
    # We use 1-based indexing for the segment tree logic internally
    st = SegmentTree(n + 1)
    results = []

    for start, end in in_range:
        # Update the segment tree with the new range and capture the increment
        # The update function returns only the 'newly' painted units
        new_area = st.update(1, 1, n, start, end)
        results.append(new_area)

    return results
