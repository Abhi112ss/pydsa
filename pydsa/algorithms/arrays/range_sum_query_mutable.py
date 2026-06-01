METADATA = {
    "id": 307,
    "name": "Range Sum Query - Mutable",
    "slug": "range-sum-query-mutable",
    "category": "Data Structures",
    "aliases": [],
    "tags": ["segment_tree", "binary_indexed_tree", "array"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Implement a data structure that supports updating elements and calculating range sums in logarithmic time.",
}

class NumArray:
    """
    A data structure that supports point updates and range sum queries
    using a Binary Indexed Tree (Fenwick Tree).
    """

    def __init__(self, nums: list[int]):
        """
        Initializes the Fenwick Tree with the given array.

        Args:
            nums: A list of integers.
        """
        self.n = len(nums)
        self.nums = [0] * self.n
        # Fenwick tree is 1-indexed, so size is n + 1
        self.tree = [0] * (self.n + 1)
        
        # Build the tree by treating each initial element as an update
        for i, val in enumerate(nums):
            self.update(i, val)

    def update(self, index: int, val: int) -> None:
        """
        Updates the value at the given index to the new value.

        Args:
            index: The zero-based index to update.
            val: The new value to be placed at the index.
        """
        # Calculate the difference between the new value and the current value
        delta = val - self.nums[index]
        self.nums[index] = val
        
        # Propagate the change through the Fenwick Tree
        # We use 1-based indexing for the tree traversal
        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            # Move to the next responsible node in the Fenwick Tree
            i += i & (-i)

    def sum_query(self, i: int) -> int:
        """
        Calculates the prefix sum from index 0 to i (inclusive).

        Args:
            i: The zero-based end index.

        Returns:
            The sum of elements from nums[0] to nums[i].
        """
        s = 0
        i += 1  # Convert to 1-based index
        while i > 0:
            s += self.tree[i]
            # Move to the parent node in the Fenwick Tree
            i -= i & (-i)
        return s

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculates the sum of elements in the range [left, right].

        Args:
            left: The zero-based start index.
            right: The zero-based end index.

        Returns:
            The sum of elements from nums[left] to nums[right].
        """
        # Range sum [L, R] is PrefixSum(R) - PrefixSum(L-1)
        if left == 0:
            return self.sum_query(right)
        return self.sum_query(right) - self.sum_query(left - 1)


def solve() -> None:
    """
    Example usage of the NumArray class.
    """
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    
    # Expected: 4 (0 + 3 + -5 + 2 + -1 = -1? No, 0+3-5+2-1 = -1. Let's re-check)
    # nums[0..2] = -2 + 0 + 3 = 1
    print(f"Sum range 0 to 2: {obj.sumRange(0, 2)}") 
    
    obj.update(0, 5) # nums becomes [5, 0, 3, -5, 2, -1]
    
    # Expected: 5 + 0 + 3 = 8
    print(f"Sum range 0 to 2 after update: {obj.sumRange(0, 2)}")
