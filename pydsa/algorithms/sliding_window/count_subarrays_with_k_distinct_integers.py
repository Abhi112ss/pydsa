METADATA = {
    "id": 3859,
    "name": "Count Subarrays With K Distinct Integers",
    "slug": "count-subarrays-with-k-distinct-integers",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays that contain exactly K distinct integers using the sliding window technique.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays containing exactly k distinct integers.

    The problem is solved by using the property:
    Exactly(K) = AtMost(K) - AtMost(K - 1)

    Args:
        nums: A list of integers.
        k: The target number of distinct integers.

    Returns:
        The total count of subarrays with exactly k distinct integers.

    Examples:
        >>> solve([1, 2, 1, 2, 3], 2)
        7
        >>> solve([1, 2, 1, 3, 4], 3)
        3
    """

    def count_at_most(target_k: int) -> int:
        """Helper function to count subarrays with at most target_k distinct elements."""
        if target_k <= 0:
            return 0
        
        count = 0
        left = 0
        distinct_map = {}
        
        for right in range(len(nums)):
            # Add the current element to the frequency map
            val = nums[right]
            distinct_map[val] = distinct_map.get(val, 0) + 1
            
            # If distinct elements exceed target_k, shrink the window from the left
            while len(distinct_map) > target_k:
                left_val = nums[left]
                distinct_map[left_val] -= 1
                if distinct_map[left_val] == 0:
                    del distinct_map[left_val]
                left += 1
            
            # The number of subarrays ending at 'right' with at most target_k 
            # distinct elements is equal to the current window size.
            count += (right - left + 1)
            
        return count

    # Exactly K is the difference between AtMost(K) and AtMost(K-1)
    return count_at_most(k) - count_at_most(k - 1)
