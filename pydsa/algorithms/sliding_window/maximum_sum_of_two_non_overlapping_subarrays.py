METADATA = {
    "id": 1031,
    "name": "Maximum Sum of Two Non-Overlapping Subarrays",
    "slug": "maximum-sum-of-two-non-overlapping-subarrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of two non-overlapping subarrays of lengths firstLen and secondLen.",
}

def solve(nums: list[int], firstLen: int, secondLen: int) -> int:
    """
    Calculates the maximum sum of two non-overlapping subarrays with given lengths.

    Args:
        nums: A list of integers.
        firstLen: The length of the first subarray.
        secondLen: The length of the second subarray.

    Returns:
        The maximum sum possible from two non-overlapping subarrays.

    Examples:
        >>> solve([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)
        20
        >>> solve([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2)
        29
    """

    def helper(length_a: int, length_b: int) -> int:
        """
        Finds max sum where subarray A comes before subarray B.
        """
        max_sum_a = 0
        current_sum_a = 0
        current_sum_b = 0
        max_total = 0
        
        # Calculate initial window sums for the first possible positions
        for i in range(length_a):
            current_sum_a += nums[i]
        
        # We start the second window (B) immediately after the first window (A) ends
        # The first possible B window ends at index (length_a + length_b - 1)
        for i in range(length_a, length_a + length_b):
            current_sum_b += nums[i]
            
        max_sum_a = current_sum_a
        max_total = max_sum_a + current_sum_b
        
        # Slide both windows across the array
        # i represents the end index of the second window (B)
        for i in range(length_a + length_b, len(nums)):
            # Slide window A: add new element, remove oldest element
            # The element being added to A is at index (i - length_b)
            # The element being removed from A is at index (i - length_b - length_a)
            current_sum_a += nums[i - length_b] - nums[i - length_b - length_a]
            max_sum_a = max(max_sum_a, current_sum_a)
            
            # Slide window B: add new element, remove oldest element
            current_sum_b += nums[i] - nums[i - length_b]
            
            # Update global max for this configuration
            max_total = max(max_total, max_sum_a + current_sum_b)
            
        return max_total

    # The problem asks for two non-overlapping subarrays. 
    # Either the firstLen subarray can come before the secondLen subarray, or vice versa.
    return max(helper(firstLen, secondLen), helper(secondLen, firstLen))
