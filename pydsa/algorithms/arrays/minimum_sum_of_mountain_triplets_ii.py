METADATA = {
    "id": 2909,
    "name": "Minimum Sum of Mountain Triplets II",
    "slug": "minimum-sum-of-mountain-triplets-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum", "monotonic_stack"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum sum of a mountain triplet (i, j, k) such that i < j < k and nums[i] < nums[j] > nums[k].",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum sum of a mountain triplet (nums[i] + nums[j] + nums[k])
    where i < j < k and nums[i] < nums[j] and nums[k] < nums[j].

    Args:
        nums: A list of integers representing the mountain elements.

    Returns:
        The minimum sum of a mountain triplet, or -1 if no such triplet exists.

    Examples:
        >>> solve([1, 3, 2])
        6
        >>> solve([5, 2, 4, 3, 1])
        8
        >>> solve([1, 2, 3])
        -1
    """
    n = len(nums)
    if n < 3:
        return -1

    # left_min[j] will store the minimum value nums[i] such that i < j and nums[i] < nums[j]
    left_min = [float('inf')] * n
    # right_min[j] will store the minimum value nums[k] such that k > j and nums[k] < nums[j]
    right_min = [float('inf')] * n

    # To find the minimum nums[i] < nums[j] for each j, we can use a monotonic stack
    # or simply observe that we need the smallest element seen so far that is less than nums[j].
    # However, a simple prefix minimum doesn't work because the condition is nums[i] < nums[j].
    # Actually, for a fixed j, we want the smallest nums[i] in the range [0, j-1] such that nums[i] < nums[j].
    # Since we want to MINIMIZE the sum, we want the absolute smallest element to the left of j.
    # If the absolute smallest element to the left is NOT less than nums[j], then no element is.
    
    # Correct approach for O(n):
    # For each j, we need min(nums[i]) for i < j and nums[i] < nums[j].
    # We can use a Segment Tree or Fenwick Tree to find the minimum in range [0, nums[j]-1],
    # but since we only care about the value, we can use a Fenwick tree on coordinate-compressed values.
    # Alternatively, since we want the minimum value, we can use a monotonic approach or a simple 
    # data structure. Let's use a Fenwick tree (Binary Indexed Tree) to store the minimum value 
    # encountered for each value seen so far.

    def get_min_elements(arr: list[int]) -> list[float]:
        """Helper to find min element to the left/right satisfying the condition."""
        size = len(arr)
        res = [float('inf')] * size
        
        # Coordinate compression to handle large values in Fenwick Tree
        sorted_unique = sorted(list(set(arr)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        m = len(sorted_unique)
        
        # bit[r] stores the minimum value seen so far for rank r
        bit = [float('inf')] * (m + 1)

        def update(r: int, val: int):
            while r <= m:
                if val < bit[r]:
                    bit[r] = val
                else:
                    break # Optimization: if current val isn't smaller, higher ranks won't be updated by this
                r += r & (-r)
        
        # Standard BIT update for prefix minimum
        def update_standard(r: int, val: int):
            while r <= m:
                bit[r] = min(bit[r], val)
                r += r & (-r)

        def query(r: int) -> float:
            m_val = float('inf')
            while r > 0:
                m_val = min(m_val, bit[r])
                r -= r & (-r)
            return m_val

        for idx in range(size):
            # Query minimum value among elements with rank < current rank
            current_rank = rank_map[arr[idx]]
            res[idx] = query(current_rank - 1)
            # Update BIT with current value
            update_standard(current_rank, arr[idx])
        return res

    # Compute left minimums
    left_min = get_min_elements(nums)
    
    # Compute right minimums by reversing the array
    reversed_nums = nums[::-1]
    right_min_rev = get_min_elements(reversed_nums)
    right_min = right_min_rev[::-1]

    min_sum = float('inf')
    found = False

    # Iterate through each element treating it as the peak 'j'
    for j in range(n):
        # A valid mountain triplet exists if both left and right minimums are valid
        if left_min[j] != float('inf') and right_min[j] != float('inf'):
            current_sum = left_min[j] + nums[j] + right_min[j]
            if current_sum < min_sum:
                min_sum = current_sum
                found = True

    return int(min_sum) if found else -1
