METADATA = {
    "id": 795,
    "name": "Number of Subarrays with Bounded Maximum",
    "slug": "number-of-subarrays-with-bounded-maximum",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "two_pointer", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays where the maximum element falls within a given range [left, right].",
}

def solve(arr: list[int], left: int, right: int) -> int:
    """
    Calculates the number of subarrays where the maximum element is between left and right inclusive.

    The logic uses the principle of inclusion-exclusion:
    Count(max in [left, right]) = Count(max <= right) - Count(max < left).
    A subarray has max <= K if and only if all its elements are <= K.

    Args:
        arr: A list of integers.
        left: The lower bound of the maximum value.
        right: The upper bound of the maximum value.

    Returns:
        The total number of subarrays whose maximum element is in [left, right].

    Examples:
        >>> solve([2, 1, 4, 3], 2, 3)
        3
        >>> solve([2, 1, 4, 3], 3, 3)
        1
    """

    def count_subarrays_with_max_le(limit: int) -> int:
        """
        Helper function to count subarrays where all elements are <= limit.
        """
        total_count = 0
        current_streak = 0
        
        for num in arr:
            if num <= limit:
                # If the current number is within the limit, it extends 
                # all existing subarrays ending at the previous index.
                current_streak += 1
                total_count += current_streak
            else:
                # If the number exceeds the limit, the streak of valid 
                # subarrays is broken.
                current_streak = 0
        return total_count

    # The number of subarrays with max in [left, right] is the number of 
    # subarrays where all elements are <= right, minus those where 
    # all elements are <= left - 1.
    return count_subarrays_with_max_le(right) - count_subarrays_with_max_le(left - 1)
