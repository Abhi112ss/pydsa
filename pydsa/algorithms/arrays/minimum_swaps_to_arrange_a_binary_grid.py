METADATA = {
    "id": 1536,
    "name": "Minimum Swaps to Make Binary Grid Alternating",
    "slug": "minimum-swaps-to-make-binary-grid-alternating",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array", "bit-manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps to make a binary array alternating.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of swaps required to make a binary array alternating.
    
    An alternating array is one where no two adjacent elements are the same.
    For a binary array, there are only two possible alternating patterns:
    1. Starting with 0: [0, 1, 0, 1, ...]
    2. Starting with 1: [1, 0, 1, 0, ...]

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The minimum number of swaps required. Returns -1 if it is impossible.

    Examples:
        >>> solve([0, 1, 0, 1])
        0
        >>> solve([1, 1, 0, 0])
        1
        >>> solve([1, 1, 1, 0])
        -1
    """
    n = len(nums)
    count_zeros = nums.count(0)
    count_ones = n - count_zeros

    # An alternating array must have an equal number of 0s and 1s,
    # or a difference of at most 1 if the length is odd.
    if abs(count_zeros - count_ones) > 1:
        return -1

    def get_swaps(start_val: int) -> int:
        """
        Calculates swaps needed to match a pattern starting with start_val.
        A swap fixes two misplaced elements (one 0 and one 1).
        """
        mismatched_zeros = 0
        mismatched_ones = 0
        
        for i in range(n):
            # Expected value for an alternating pattern
            expected = (start_val + i) % 2
            if nums[i] != expected:
                if nums[i] == 0:
                    mismatched_zeros += 1
                else:
                    mismatched_ones += 1
        
        # If the number of misplaced 0s doesn't equal misplaced 1s, 
        # this pattern is impossible for the given counts.
        if mismatched_zeros != mismatched_ones:
            return float('inf')
        
        # Each swap corrects one misplaced 0 and one misplaced 1.
        return mismatched_zeros

    # Case 1: Pattern starts with 0 (0, 1, 0, 1...)
    # This is only possible if count_zeros >= count_ones
    res_start_zero = float('inf')
    if count_zeros >= count_ones and (n % 2 == 0 or count_zeros == count_ones + 1):
        res_start_zero = get_swaps(0)

    # Case 2: Pattern starts with 1 (1, 0, 1, 0...)
    # This is only possible if count_ones >= count_zeros
    res_start_one = float('inf')
    if count_ones >= count_zeros and (n % 2 == 0 or count_ones == count_zeros + 1):
        res_start_one = get_swaps(1)

    ans = min(res_start_zero, res_start_one)
    return int(ans) if ans != float('inf') else -1
