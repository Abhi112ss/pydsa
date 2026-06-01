METADATA = {
    "id": 3026,
    "name": "Maximum Good Subarray Sum",
    "slug": "maximum-good-subarray-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "fenwick_tree", "segment_tree"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a 'good' subarray where the distance between any two identical elements is greater than k.",
}

class FenwickTree:
    """A standard Fenwick Tree (Binary Indexed Tree) for prefix maximum queries."""
    
    def __init__(self, size: int):
        self.tree = [-float('inf')] * (size + 1)

    def update(self, index: int, value: float) -> None:
        """Updates the tree at a specific index with a new value (keeping the maximum)."""
        index += 1  # 1-based indexing
        while index < len(self.tree):
            if value > self.tree[index]:
                self.tree[index] = value
            else:
                # Since we only ever increase values in this specific problem context,
                # if the new value isn't larger, we can't optimize further.
                break
            index += index & (-index)

    def query(self, index: int) -> float:
        """Returns the maximum value in the range [0, index]."""
        index += 1
        res = -float('inf')
        while index > 0:
            if self.tree[index] > res:
                res = self.tree[index]
            index -= index & (-index)
        return res

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum of a 'good' subarray.
    
    A subarray is 'good' if for every element in the subarray, the distance 
    to its previous occurrence of the same value is greater than k.

    Args:
        nums: A list of integers.
        k: An integer representing the minimum distance requirement.

    Returns:
        The maximum sum of a good subarray.

    Examples:
        >>> solve([1, 2, 3, 1, 2, 3], 2)
        6
        >>> solve([-1, -2, -3], 1)
        -1
    """
    n = len(nums)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    # last_seen stores the most recent index of each number
    last_seen = {}
    # valid_left_boundary[i] is the smallest index L such that subarray [L, i] is 'good'
    valid_left_boundary = [0] * n
    current_left = 0
    
    for i in range(n):
        if nums[i] in last_seen:
            # If the distance to the previous occurrence is <= k, 
            # the subarray cannot start at or before the previous occurrence.
            prev_idx = last_seen[nums[i]]
            if i - prev_idx <= k:
                current_left = max(current_left, prev_idx + 1)
        
        valid_left_boundary[i] = current_left
        last_seen[nums[i]] = i

    # We want to maximize: prefix_sums[i+1] - prefix_sums[j]
    # where 0 <= j <= valid_left_boundary[i]
    # This is equivalent to: prefix_sums[i+1] - min(prefix_sums[j])
    # However, the constraint is on the 'goodness' of the subarray.
    # A subarray [j, i] is good if for all elements in [j, i], their previous 
    # occurrence is < j.
    # The valid_left_boundary[i] calculated above ensures that for the current i,
    # any j in [valid_left_boundary[i], i] makes the subarray [j, i] good 
    # relative to elements seen so far.
    
    # To handle the "good" condition correctly:
    # A subarray [j, i] is good if for all x in [j, i], last_occurrence(x) < j.
    # This is exactly what valid_left_boundary[i] tracks.
    
    # We use a Fenwick tree to store prefix_sums[j] and find the minimum.
    # Since Fenwick is usually for prefix sums or prefix max, we store -prefix_sums[j]
    # to find the maximum of (-prefix_sums[j]), which is the minimum of prefix_sums[j].
    
    # Actually, a simpler approach:
    # We need max(prefix_sums[i+1] - prefix_sums[j]) for 0 <= j <= valid_left_boundary[i].
    # This is prefix_sums[i+1] - min(prefix_sums[j] for 0 <= j <= valid_left_boundary[i]).
    
    # Let's use a Segment Tree or Fenwick Tree to maintain the minimum prefix_sum 
    # seen so far up to index 'valid_left_boundary[i]'.
    
    # Precompute prefix minimums for the range [0, valid_left_boundary[i]]
    # Since valid_left_boundary[i] is non-decreasing, we can use a pointer.
    
    min_prefix_at_boundary = [0.0] * (n + 1)
    current_min = float('inf')
    
    # We need to find min(prefix_sums[j]) for 0 <= j <= valid_left_boundary[i]
    # Because valid_left_boundary[i] is non-decreasing, we can use a simple 
    # running minimum.
    
    # Wait, is valid_left_boundary[i] non-decreasing?
    # Yes, because current_left only ever increases.
    
    ans = -float('inf')
    ptr = 0
    running_min_prefix = float('inf')
    
    for i in range(n):
        # Update running_min_prefix to include all prefix_sums up to valid_left_boundary[i]
        target_boundary = valid_left_boundary[i]
        while ptr <= target_boundary:
            if prefix_sums[ptr] < running_min_prefix:
                running_min_prefix = prefix_sums[ptr]
            ptr += 1
        
        current_sum = prefix_sums[i + 1] - running_min_prefix
        if current_sum > ans:
            ans = current_sum
            
    return int(ans)
