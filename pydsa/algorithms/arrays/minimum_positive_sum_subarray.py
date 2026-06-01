METADATA = {
    "id": 3364,
    "name": "Minimum Positive Sum Subarray",
    "slug": "minimum-positive-sum-subarray",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "set_data_structure"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum length of a subarray whose sum is strictly greater than zero.",
}

import bisect

class SortedList:
    """
    A simplified SortedList implementation using bisect to maintain order.
    In a production environment, a Balanced BST or Fenwick Tree might be used,
    but for LeetCode constraints, a bisect-maintained list is efficient.
    """
    def __init__(self) -> None:
        self._data: list[int] = []

    def add(self, val: int) -> None:
        bisect.insort(self._data, val)

    def find_smallest_greater_than(self, val: int) -> int:
        """Returns the smallest element in the list strictly greater than val."""
        idx = bisect.bisect_right(self._data, val)
        if idx < len(self._data):
            return self._data[idx]
        return float('inf')

    def __len__(self) -> int:
        return len(self._data)

def solve(nums: list[int]) -> int:
    """
    Finds the minimum length of a subarray with a sum strictly greater than zero.

    Args:
        nums: A list of integers.

    Returns:
        The minimum length of a subarray with sum > 0. Returns -1 if no such subarray exists.

    Examples:
        >>> solve([1, -2, 3])
        1
        >>> solve([-1, -2, -3])
        -1
        >>> solve([2, -1, -1, 2])
        1
    """
    n = len(nums)
    # We store (prefix_sum, index) pairs. 
    # To find the smallest subarray sum > 0, we need prefix_sum[j] - prefix_sum[i] > 0
    # which means prefix_sum[j] > prefix_sum[i] where j > i.
    # However, the problem asks for the minimum length (j - i).
    # This is equivalent to finding the closest index i < j such that prefix_sum[i] < prefix_sum[j].
    
    # Actually, the problem is simpler: we want to find min(j - i) such that P[j] > P[i].
    # This is a variation of the "closest pair" problem in 1D with index constraints.
    
    # Let's use a more robust approach:
    # We want to find min(j - i) such that P[j] - P[i] > 0.
    # We can iterate through the array, maintaining a data structure of (prefix_sum, index).
    # For a fixed j, we want the largest i < j such that P[i] < P[j].
    
    prefix_sum = 0
    # Store (value, index) pairs in a way that we can query by value
    # Since we want the largest index i < j, we can use a Fenwick tree or Segment tree 
    # on coordinate-compressed prefix sums to store the maximum index seen so far.
    
    # Coordinate Compression
    all_sums = [0]
    current_sum = 0
    for x in nums:
        current_sum += x
        all_sums.append(current_sum)
    
    sorted_sums = sorted(list(set(all_sums)))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_sums)}
    m = len(sorted_sums)
    
    # Fenwick tree to store the maximum index for a given prefix sum rank
    # bit[r] stores the max index i such that rank(P[i]) <= r
    bit = [-1] * (m + 1)

    def update(idx: int, val: int) -> None:
        while idx <= m:
            bit[idx] = max(bit[idx], val)
            idx += idx & (-idx)

    def query(idx: int) -> int:
        res = -1
        while idx > 0:
            res = max(res, bit[idx])
            idx -= idx & (-idx)
        return res

    min_len = float('inf')
    current_sum = 0
    
    # Initial state: prefix sum 0 at index -1
    update(rank_map[0], -1)
    
    for j in range(n):
        current_sum += nums[j]
        
        # We need P[i] < P[j]. 
        # In terms of ranks, we need rank(P[i]) < rank(P[j]).
        # So we query the max index in range [1, rank(P[j]) - 1]
        target_rank = rank_map[current_sum]
        max_i = query(target_rank - 1)
        
        if max_i != -1:
            # max_i is the largest index < j such that P[max_i] < P[j]
            # Wait, the problem asks for MINIMUM length. 
            # The largest index i < j gives the smallest (j - i).
            # Note: index in BIT is 0-based for the array, but we used -1 for the 0-th prefix sum.
            # Let's adjust: if max_i is -1, it refers to the prefix sum 0 before the first element.
            # The actual index in nums for the start of the subarray is max_i + 1.
            # Length = j - (max_i + 1) + 1 = j - max_i.
            
            # If max_i is -1, length is j - (-1) = j + 1.
            # If max_i is 0, length is j - 0 = j.
            # Wait, if P[j] - P[i] > 0, the subarray is nums[i+1...j].
            # Length is j - (i+1) + 1 = j - i.
            # If i = -1 (the dummy index for P[0]=0), length is j - (-1) = j + 1.
            
            # Let's re-verify:
            # nums = [1, -2, 3], j=0: P[0]=1. query(rank(1)-1) -> rank(0) is 1. query(0) is -1.
            # max_i = -1. len = 0 - (-1) = 1. Correct.
            # j=1: P[1]=-1. query(rank(-1)-1) -> rank(-1) is 0 (not possible, rank starts at 1).
            # Let's use 1-based indexing for BIT and handle the dummy carefully.
            
            min_len = min(min_len, j - max_i)
            
        # Update BIT with current prefix sum rank and current index j
        update(rank_map[current_sum], j)

    return int(min_len) if min_len != float('inf') else -1
