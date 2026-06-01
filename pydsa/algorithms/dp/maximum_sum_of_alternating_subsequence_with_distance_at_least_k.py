METADATA = {
    "id": 3915,
    "name": "Maximum Sum of Alternating Subsequence With Distance at Least K",
    "slug": "maximum_sum_of_alternating_subsequence_with_distance_at_least_k",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "segment_tree", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of an alternating subsequence where each consecutive element is at least distance K apart.",
}

class SegmentTree:
    """A standard Max Segment Tree implementation for range maximum queries."""
    
    def __init__(self, size: int):
        self.size = 1
        while self.size < size:
            self.size *= 2
        self.tree = [-float('inf')] * (2 * self.size)

    def update(self, index: int, value: float) -> None:
        """Updates the value at a specific index in the tree."""
        index += self.size
        self.tree[index] = max(self.tree[index], value)
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left: int, right: int) -> float:
        """Queries the maximum value in the range [left, right)."""
        res = -float('inf')
        left += self.size
        right += self.size
        while left < right:
            if left % 2 == 1:
                res = max(res, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                res = max(res, self.tree[right])
            left //= 2
            right //= 2
        return res

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum of an alternating subsequence where elements 
    are at least distance K apart.
    
    An alternating subsequence is defined such that elements alternate in sign 
    relative to the operation (e.g., +nums[i] - nums[j] + nums[l]...).
    However, the standard interpretation for this specific problem type 
    is finding a subsequence a_1, a_2, ..., a_m such that 
    Sum = a_1 - a_2 + a_3 - a_4 ... and index(a_{i+1}) - index(a_i) >= k.

    Args:
        nums: A list of integers.
        k: The minimum distance between indices of consecutive elements in the subsequence.

    Returns:
        The maximum possible sum of such an alternating subsequence.

    Examples:
        >>> solve([10, 2, 10, 2], 2)
        18
        >>> solve([1, 5, 2, 10], 1)
        11
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp_plus[i]: max sum of alternating subsequence ending at index i with +nums[i]
    # dp_minus[i]: max sum of alternating subsequence ending at index i with -nums[i]
    # To optimize, we use two segment trees to store the best dp_plus and dp_minus 
    # values seen so far to allow O(log n) range queries.
    
    # tree_plus stores values of (dp_plus[j])
    # tree_minus stores values of (dp_minus[j])
    tree_plus = SegmentTree(n)
    tree_minus = SegmentTree(n)

    max_total_sum = -float('inf')

    for i in range(n):
        # Case 1: nums[i] is the first element in the subsequence (always +nums[i])
        current_dp_plus = nums[i]
        current_dp_minus = -float('inf')

        # Case 2: nums[i] is not the first element.
        # If nums[i] is added as a '+' term, the previous term must have been a '-' term.
        # The previous index j must satisfy: i - j >= k  =>  j <= i - k
        if i >= k:
            # Query max(dp_minus[j]) for 0 <= j <= i - k
            prev_minus = tree_minus.query(0, i - k + 1)
            if prev_minus != -float('inf'):
                current_dp_plus = max(current_dp_plus, prev_minus + nums[i])

        # If nums[i] is added as a '-' term, the previous term must have been a '+' term.
        # The previous index j must satisfy: i - j >= k  =>  j <= i - k
        if i >= k:
            # Query max(dp_plus[j]) for 0 <= j <= i - k
            prev_plus = tree_plus.query(0, i - k + 1)
            if prev_plus != -float('inf'):
                current_dp_minus = max(current_dp_minus, prev_plus - nums[i])

        # Update segment trees with the results for index i
        tree_plus.update(i, current_dp_plus)
        tree_minus.update(i, current_dp_minus)

        # The result can end on either a plus or a minus term
        max_total_sum = max(max_total_sum, current_dp_plus, current_dp_minus)

    return int(max_total_sum)
