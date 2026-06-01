METADATA = {
    "id": 3768,
    "name": "Minimum Inversion Count in Subarrays of Fixed Length",
    "slug": "minimum_inversion_count_in_subarrays_of_fixed_length",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "fenwick_tree", "data_structures"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of inversions in any subarray of a fixed length k using a sliding window and a Fenwick tree.",
}

class FenwickTree:
    """A standard Fenwick Tree (Binary Indexed Tree) implementation."""
    
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def update(self, i: int, delta: int) -> None:
        """Adds delta to the element at index i (1-based)."""
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i: int) -> int:
        """Returns the prefix sum up to index i (1-based)."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum inversion count among all subarrays of length k.

    Args:
        nums: A list of integers.
        k: The fixed length of the subarrays.

    Returns:
        The minimum number of inversions found in any subarray of length k.

    Examples:
        >>> solve([3, 1, 2, 4], 3)
        1
        >>> solve([1, 2, 3], 2)
        0
    """
    n = len(nums)
    if k <= 1:
        return 0

    # Coordinate compression to handle large integer values in Fenwick Tree
    sorted_unique = sorted(list(set(nums)))
    rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
    compressed_nums = [rank_map[x] for x in nums]
    max_rank = len(sorted_unique)

    bit = FenwickTree(max_rank)
    current_inversions = 0
    
    # Initialize the first window of size k
    for i in range(k):
        # Inversions added by nums[i] are the count of elements already in BIT 
        # that are strictly greater than nums[i]
        current_inversions += i - bit.query(compressed_nums[i])
        bit.update(compressed_nums[i], 1)

    min_inversions = current_inversions

    # Slide the window from index 1 to n-k
    for i in range(k, n):
        # Element leaving the window: nums[i - k]
        leaving_val = compressed_nums[i - k]
        # Subtract inversions where leaving_val was the 'greater' element
        # This is the count of elements in the current window smaller than leaving_val
        current_inversions -= bit.query(leaving_val - 1)
        bit.update(leaving_val, -1)

        # Element entering the window: nums[i]
        entering_val = compressed_nums[i]
        # Add inversions where entering_val is the 'smaller' element
        # This is the count of elements currently in BIT that are greater than entering_val
        # Total elements in BIT is (k-1), so greater = (k-1) - bit.query(entering_val)
        # However, we must account for the fact that bit.query(entering_val) includes 
        # elements equal to entering_val. The formula for strictly greater is:
        # (current_window_size) - bit.query(entering_val)
        # Since we just removed one element, current window size in BIT is k-1.
        current_inversions += (k - 1) - bit.query(entering_val)
        bit.update(entering_val, 1)

        if current_inversions < min_inversions:
            min_inversions = current_inversions

    return min_inversions
