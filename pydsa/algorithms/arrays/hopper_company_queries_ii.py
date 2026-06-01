METADATA = {
    "id": 1645,
    "name": "Hopper Company Queries II",
    "slug": "hopper-company-queries-ii",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "fenwick_tree", "range_query", "point_update"],
    "difficulty": "hard",
    "time_complexity": "O(Q log N)",
    "space_complexity": "O(N)",
    "description": "Efficiently handle point updates and range sum queries using a Fenwick Tree or Segment Tree.",
}

class FenwickTree:
    """A Fenwick Tree (Binary Indexed Tree) implementation for prefix sums."""

    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at the given 1-based index."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum from 1 to the given 1-based index."""
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total

    def query_range(self, left: int, right: int) -> int:
        """Returns the sum in the range [left, right] inclusive."""
        if left > right:
            return 0
        return self.query(right) - self.query(left - 1)


def solve(n: int, initial_values: list[int], queries: list[list[int]]) -> list[int]:
    """
    Processes a series of queries involving point updates and range sum queries.

    Args:
        n: The number of elements in the array.
        initial_values: The starting values of the array.
        queries: A list of queries where:
            - query[0] == 1: Update (type 1), query[1] is index (0-indexed), query[2] is new value.
            - query[0] == 2: Sum (type 2), query[1] is left index (0-indexed), query[2] is right index (0-indexed).

    Returns:
        A list of integers representing the results of the type 2 queries.

    Examples:
        >>> solve(5, [1, 2, 3, 4, 5], [[2, 0, 2], [1, 1, 10], [2, 0, 2]])
        [6, 14]
    """
    # Initialize Fenwick Tree with 1-based indexing
    bit = FenwickTree(n)
    
    # current_arr tracks the current state to calculate the delta for updates
    current_arr = [0] * n
    
    for i in range(n):
        val = initial_values[i]
        current_arr[i] = val
        bit.update(i + 1, val)

    results = []
    for query in queries:
        query_type = query[0]
        
        if query_type == 1:
            # Update operation: index is query[1], new_val is query[2]
            idx = query[1]
            new_val = query[2]
            
            # Calculate the difference needed to change current_arr[idx] to new_val
            delta = new_val - current_arr[idx]
            current_arr[idx] = new_val
            
            # Apply the delta to the Fenwick Tree
            bit.update(idx + 1, delta)
            
        elif query_type == 2:
            # Range Sum operation: left is query[1], right is query[2]
            left = query[1]
            right = query[2]
            
            # Perform range sum query using the BIT
            results.append(bit.query_range(left + 1, right + 1))
            
    return results
