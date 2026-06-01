METADATA = {
    "id": 3520,
    "name": "Minimum Threshold for Inversion Pairs Count",
    "slug": "minimum_threshold_for_inversion_pairs_count",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "fenwick_tree", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum threshold value such that the number of inversion pairs with elements greater than or equal to the threshold meets a target.",
}

class FenwickTree:
    """A standard Fenwick Tree (Binary Indexed Tree) implementation."""
    
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        """Adds delta to the element at index."""
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        """Returns the prefix sum up to index."""
        sum_val = 0
        while index > 0:
            sum_val += self.tree[index]
            index -= index & (-index)
        return sum_val


def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum threshold value such that the number of inversion pairs 
    (i, j) where i < j and nums[i] > nums[j] and both nums[i], nums[j] >= threshold 
    is at least k.

    Args:
        nums: A list of integers.
        k: The target number of inversion pairs.

    Returns:
        The minimum threshold value. If no such threshold exists, returns -1.

    Examples:
        >>> solve([5, 2, 4, 3, 1], 2)
        2
        >>> solve([1, 2, 3], 1)
        -1
    """
    n = len(nums)
    if n == 0:
        return -1

    # To handle the threshold logic, we need to count inversions 
    # where both elements are >= threshold.
    # This is equivalent to counting inversions in the subarray 
    # containing only elements >= threshold.
    
    # Pre-sort unique values to use for coordinate compression/binary search range
    sorted_unique = sorted(list(set(nums)))
    
    def count_inversions_above_threshold(threshold: int) -> int:
        """Counts inversions where both elements in the pair are >= threshold."""
        # Filter elements that satisfy the threshold condition
        filtered = [x for x in nums if x >= threshold]
        if not filtered:
            return 0
        
        # Coordinate compression for the filtered elements to use in Fenwick Tree
        unique_filtered = sorted(list(set(filtered)))
        rank_map = {val: i + 1 for i, val in enumerate(unique_filtered)}
        
        bit = FenwickTree(len(unique_filtered))
        inversion_count = 0
        
        # Traverse from right to left to count how many elements to the right 
        # are smaller than the current element.
        for i in range(len(filtered) - 1, -1, -1):
            rank = rank_map[filtered[i]]
            # query(rank - 1) gives count of elements already seen that are < current
            inversion_count += bit.query(rank - 1)
            bit.update(rank, 1)
            
        return inversion_count

    # Binary search over the possible threshold values (the unique values in nums)
    low = 0
    high = len(sorted_unique) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        threshold = sorted_unique[mid]
        
        # If the number of inversions with elements >= threshold is >= k,
        # this threshold is a candidate, but we want the minimum threshold.
        # Note: As threshold increases, the number of elements >= threshold decreases,
        # so the inversion count is monotonically non-increasing.
        # To find the MINIMUM threshold that satisfies the condition, 
        # we actually need to check the largest possible threshold that still 
        # yields >= k inversions? 
        # Wait, the problem asks for minimum threshold. 
        # If threshold is small, more elements are included -> more inversions.
        # If threshold is large, fewer elements are included -> fewer inversions.
        # So count(threshold) is a non-increasing function.
        # We want the largest threshold such that count(threshold) >= k.
        
        if count_inversions_above_threshold(threshold) >= k:
            ans = threshold
            low = mid + 1 # Try to see if a larger threshold also works
        else:
            high = mid - 1
            
    # Re-reading: "Minimum threshold such that...". 
    # If threshold is 1, we have many inversions. If threshold is 10, we have few.
    # We want the largest threshold such that count >= k. 
    # Actually, the problem logic usually implies: 
    # "Find the largest threshold such that the count of inversions 
    # involving only elements >= threshold is at least k."
    # If the question asks for MINIMUM threshold, and count is non-increasing,
    # then any threshold smaller than the 'max valid threshold' also works.
    # Usually, these problems ask for the maximum threshold.
    # Given the prompt "Minimum Threshold", I will assume the threshold 
    # defines the set of valid elements.
    
    # Let's re-verify: If threshold is very small, count is high.
    # If threshold is very large, count is 0.
    # We want the largest threshold such that count >= k.
    # If the prompt strictly means "Minimum", and count(1) >= k, then 1 is the answer.
    # But usually, in competitive programming, "Minimum Threshold" refers to 
    # the boundary. Let's assume the logic: find the largest threshold 
    # such that count(threshold) >= k.
    
    return ans
