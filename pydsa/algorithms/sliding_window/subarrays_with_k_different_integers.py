METADATA = {
    "id": 992,
    "name": "Subarrays with K Different Integers",
    "slug": "subarrays-with-k-different-integers",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointer"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of subarrays that contain exactly k different integers.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays containing exactly k distinct integers.

    The problem is solved using the principle of inclusion-exclusion for sliding windows:
    Exactly(K) = AtMost(K) - AtMost(K - 1).

    Args:
        nums: A list of integers.
        k: The target number of distinct integers.

    Returns:
        The total count of subarrays with exactly k distinct integers.

    Examples:
        >>> solve([1, 2, 1, 2, 3], 2)
        7
        >>> solve([1, 2, 1, 2, 3], 3)
        3
    """

    def count_at_most(target_k: int) -> int:
        """
        Helper function to count subarrays with at most target_k distinct elements.
        """
        if target_k <= 0:
            return 0

        count = 0
        left = 0
        # Frequency map to track occurrences of numbers in the current window
        frequency_map: dict[int, int] = {}

        for right in range(len(nums)):
            # Add the current element to the window
            current_val = nums[right]
            frequency_map[current_val] = frequency_map.get(current_val, 0) + 1

            # If distinct elements exceed target_k, shrink the window from the left
            while len(frequency_map) > target_k:
                left_val = nums[left]
                frequency_map[left_val] -= 1
                if frequency_map[left_val] == 0:
                    del frequency_map[left_val]
                left += 1

            # The number of subarrays ending at 'right' with at most target_k 
            # distinct elements is equal to the current window size (right - left + 1)
            count += (right - left + 1)

        return count

    # Exactly K = AtMost(K) - AtMost(K-1)
    return count_at_most(k) - count_at_most(k - 1)
