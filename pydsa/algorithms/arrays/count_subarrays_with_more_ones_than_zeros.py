METADATA = {
    "id": 2031,
    "name": "Count Subarrays With More Ones Than Zeros",
    "slug": "count-subarrays-with-more-ones-than-zeros",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "binary_indexed_tree", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays that contain more ones than zeros.",
}

class FenwickTree:
    """A standard implementation of a Binary Indexed Tree (Fenwick Tree)."""

    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at index."""
        index += 1  # 1-based indexing
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum up to index."""
        index += 1  # 1-based indexing
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays where the count of 1s is greater than the count of 0s.
    
    The problem is transformed by treating 0s as -1s. A subarray [i, j] has more 1s 
    than 0s if the sum of elements in that range is > 0.
    Let P[i] be the prefix sum up to index i. The condition becomes P[j] - P[i-1] > 0,
    or P[j] > P[i-1].

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The total count of subarrays with more 1s than 0s.

    Examples:
        >>> solve([0, 1, 1])
        2
        >>> solve([1, 1, 1])
        6
        >>> solve([0, 0, 0])
        0
    """
    n = len(nums)
    # Transform 0 to -1 and 1 to 1
    # Prefix sums can range from -n to n.
    # To use as indices in Fenwick Tree, we shift them by adding n.
    # Range of shifted prefix sums: [0, 2*n]
    offset = n
    bit = FenwickTree(2 * n + 1)
    
    current_prefix_sum = 0
    count = 0
    
    # Initial state: prefix sum 0 exists before any elements are processed.
    # Shifted index for 0 is 0 + offset.
    bit.update(current_prefix_sum + offset, 1)
    
    for num in nums:
        # Update current prefix sum: 1 adds 1, 0 adds -1
        current_prefix_sum += 1 if num == 1 else -1
        
        # We need to find how many previous prefix sums P_prev satisfy:
        # current_prefix_sum - P_prev > 0  =>  P_prev < current_prefix_sum
        # In terms of shifted indices: (P_prev + offset) < (current_prefix_sum + offset)
        # We query the BIT for the sum of frequencies in range [0, current_prefix_sum + offset - 1]
        
        # The index we query is (current_prefix_sum + offset - 1)
        # We must ensure the index is not negative (though with offset=n, it won't be)
        query_idx = current_prefix_sum + offset - 1
        if query_idx >= 0:
            count += bit.query(min(query_idx, 2 * n))
            
        # Add the current prefix sum to the BIT for future queries
        bit.update(current_prefix_sum + offset, 1)
        
    return count
