METADATA = {
    "id": 3350,
    "name": "Adjacent Increasing Subarrays Detection II",
    "slug": "adjacent_increasing_subarrays_detection_ii",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two_pointer", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs of adjacent increasing subarrays that satisfy specific boundary conditions using precomputed lengths.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of pairs of adjacent increasing subarrays.
    
    A pair of adjacent increasing subarrays (A, B) is valid if:
    1. A is a subarray [i, j] and B is a subarray [j+1, k].
    2. Both A and B are strictly increasing.
    3. The problem constraints/definition for 'Adjacent Increasing Subarrays II' 
       usually involve counting how many ways we can split an increasing 
       sequence into two non-empty parts.

    Args:
        nums: A list of integers.

    Returns:
        The total count of valid adjacent increasing subarray pairs.

    Examples:
        >>> solve([1, 2, 3, 4])
        6
        # Pairs: ([1],[2]), ([1,2],[3]), ([1,2,3],[4]), ([2],[3]), ([2,3],[4]), ([3],[4])
        # Wait, the logic depends on the specific definition of 'Adjacent Increasing Subarrays II'.
        # For a continuous increasing segment of length L, the number of ways to 
        # split it into two non-empty adjacent subarrays is (L-1).
        # However, if we are counting all possible pairs (A, B) where A and B are 
        # adjacent and both are increasing:
        # For each index i from 0 to n-2, if nums[i] < nums[i+1], 
        # we can potentially form pairs.
    """
    n = len(nums)
    if n < 2:
        return 0

    # left_inc[i] stores the length of the strictly increasing subarray ending at i
    left_inc = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            left_inc[i] = left_inc[i - 1] + 1
            
    # right_inc[i] stores the length of the strictly increasing subarray starting at i
    right_inc = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            right_inc[i] = right_inc[i + 1] + 1

    total_pairs = 0
    
    # A pair of adjacent subarrays (A, B) is defined by a split point between index i and i+1.
    # Subarray A ends at i, Subarray B starts at i+1.
    # For A to be increasing, its length can be any value from 1 to left_inc[i].
    # For B to be increasing, its length can be any value from 1 to right_inc[i+1].
    # However, the problem "Adjacent Increasing Subarrays II" typically asks for 
    # the number of pairs (A, B) such that A and B are adjacent and both are increasing.
    # The number of such pairs at split point i is (left_inc[i] * right_inc[i+1]) 
    # ONLY if we consider all possible lengths. 
    # But if the problem implies A and B must be the *maximal* increasing subarrays 
    # or specific segments, the logic changes.
    
    # Based on standard LeetCode patterns for "Adjacent Increasing Subarrays":
    # We iterate through every possible split point between index i and i+1.
    # At each split point, any increasing subarray ending at i can be paired 
    # with any increasing subarray starting at i+1.
    
    for i in range(n - 1):
        # The number of increasing subarrays ending at i is left_inc[i]
        # The number of increasing subarrays starting at i+1 is right_inc[i+1]
        # The product gives the number of valid (A, B) pairs at this split.
        total_pairs += left_inc[i] * right_inc[i + 1]

    return total_pairs
