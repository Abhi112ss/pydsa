METADATA = {
    "id": 1248,
    "name": "Count Number of Nice Subarrays",
    "slug": "count-number-of-nice-subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays that contain exactly k odd numbers.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of subarrays containing exactly k odd numbers using a sliding window.

    The problem is equivalent to finding subarrays with a sum of k if we 
    transform odd numbers to 1 and even numbers to 0. To handle the "exactly k" 
    constraint efficiently with a single pass, we use a helper function to 
    calculate the number of subarrays with "at most k" odd numbers.
    The result is then: at_most(k) - at_most(k - 1).

    Args:
        nums: A list of integers.
        k: The target number of odd integers.

    Returns:
        The total count of nice subarrays.

    Examples:
        >>> solve([1, 1, 2, 1, 1], 3)
        3
        >>> solve([2, 4, 6], 1)
        0
        >>> solve([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2)
        16
    """

    def count_at_most(target_k: int) -> int:
        """Helper to count subarrays with at most target_k odd numbers."""
        if target_k < 0:
            return 0
        
        count = 0
        left = 0
        current_odd_count = 0
        
        for right in range(len(nums)):
            # If the current number is odd, increment our window's odd count
            if nums[right] % 2 != 0:
                current_odd_count += 1
            
            # Shrink the window from the left if we exceed the target_k
            while current_odd_count > target_k:
                if nums[left] % 2 != 0:
                    current_odd_count -= 1
                left += 1
            
            # The number of subarrays ending at 'right' with at most target_k 
            # odd numbers is equal to the current window size.
            count += (right - left + 1)
            
        return count

    # Exactly k = (At most k) - (At most k-1)
    return count_at_most(k) - count_at_most(k - 1)
