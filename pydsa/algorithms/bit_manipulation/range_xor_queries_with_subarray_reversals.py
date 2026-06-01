METADATA = {
    "id": 3526,
    "name": "Range XOR Queries with Subarray Reversals",
    "slug": "range_xor_queries_with_subarray_reversals",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "bit_manipulation", "treap", "splay_tree"],
    "difficulty": "hard",
    "time_complexity": "O(q log n)",
    "space_complexity": "O(n)",
    "description": "Perform range XOR queries and range subarray reversals on an array using a balanced binary search tree.",
}

import random

class TreapNode:
    """A node in a Treap used to represent an implicit key sequence."""
    def __init__(self, value: int):
        self.value = value
        self.priority = random.random()
        self.left: TreapNode | None = None
        self.right: TreapNode | None = None
        self.size = 1
        self.xor_sum = value
        self.reverse_flag = False

    def push_up(self) -> None:
        """Recalculate size and XOR sum based on children."""
        self.size = 1
        self.xor_sum = self.value
        if self.left:
            self.size += self.left.size
            self.xor_sum ^= self.left.xor_sum
        if self.right:
            self.size += self.right.size
            self.xor_sum ^= self.right.xor_sum

    def push_down(self) -> None:
        """Propagate the reversal flag to children."""
        if self.reverse_flag:
            if self.left:
                self.left.reverse_flag = not self.left.reverse_flag
                self.left.left, self.left.right = self.left.right, self.left.left
            if self.right:
                self.right.reverse_flag = not self.right.reverse_flag
                self.right.left, self.right.right = self.right.right, self.right.left
            self.reverse_flag = False

class Treap:
    """Implicit Treap implementation for range operations."""
    def __init__(self, arr: list[int]):
        self.root: TreapNode | None = None
        for x in arr:
            self.root = self._merge(self.root, TreapNode(x))

    def _get_size(self, node: TreapNode | None) -> int:
        return node.size if node else 0

    def _split(self, node: TreapNode | None, k: int) -> tuple[TreapNode | None, TreapNode | None]:
        """Splits the treap into two: one with k elements, one with the rest."""
        if not node:
            return None, None
        
        node.push_down()
        left_size = self._get_size(node.left)
        
        if left_size < k:
            node.right, right_part = self._split(node.right, k - left_size - 1)
            node.push_up()
            return node, right_part
        else:
            left_part, node.left = self._split(node.left, k)
            node.push_up()
            return left_part, node

    def _merge(self, left: TreapNode | None, right: TreapNode | None) -> TreapNode | None:
        """Merges two treaps."""
        if not left or not right:
            return left or right
        
        left.push_down()
        right.push_down()
        
        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            left.push_up()
            return left
        else:
            right.left = self._merge(left, right.left)
            right.push_up()
            return right

    def reverse(self, l: int, r: int) -> None:
        """Reverses the subarray from index l to r (0-indexed)."""
        # Split into [0, l), [l, r], (r, n-1]
        t1, t23 = self._split(self.root, l)
        t2, t3 = self._split(t23, r - l + 1)
        
        if t2:
            t2.reverse_flag = not t2.reverse_flag
            t2.left, t2.right = t2.right, t2.left
            
        self.root = self._merge(t1, self._merge(t2, t3))

    def query_xor(self, l: int, r: int) -> int:
        """Returns the XOR sum of the subarray from index l to r (0-indexed)."""
        t1, t23 = self._split(self.root, l)
        t2, t3 = self._split(t23, r - l + 1)
        
        res = t2.xor_sum if t2 else 0
        
        # Re-merge to restore the tree
        self.root = self._merge(t1, self._merge(t2, t3))
        return res

def solve(n: int, arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    Solves the range XOR queries with subarray reversals problem.

    Args:
        n: The size of the array.
        arr: The initial array of integers.
        queries: A list of queries where:
            - query[0] == 1: Reverse subarray [l, r] (1-indexed).
            - query[0] == 2: XOR sum of subarray [l, r] (1-indexed).

    Returns:
        A list of results for all type 2 queries.

    Examples:
        >>> solve(5, [1, 2, 3, 4, 5], [[2, 1, 3], [1, 1, 3], [2, 1, 3]])
        [0, 6]
    """
    treap = Treap(arr)
    results = []

    for query in queries:
        q_type = query[0]
        # Convert 1-indexed to 0-indexed
        l, r = query[1] - 1, query[2] - 1
        
        if q_type == 1:
            treap.reverse(l, r)
        else:
            results.append(treap.query_xor(l, r))
            
    return results
