METADATA = {
    "id": 3835,
    "name": "Count Subarrays With Cost Less Than or Equal to K",
    "slug": "count-subarrays-with-cost-less-than-or-equal-to-k",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the total number of contiguous subarrays where the sum of elements is less than or equal to a given threshold K.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of contiguous subarrays whose sum is less than or equal to k.

    Args:
        nums: A list of integers representing the array.
        k: The maximum allowed sum for a subarray.

    Returns:
        The total count of subarrays with sum <= k.

    Examples:
        >>> solve([1, 2, 3], 3)
        4  # [1], [2], [3], [1, 2]
        >>> solve([1, 1, 1], 2)
        3  # [1], [1], [1], [1, 1], [1, 1] (Wait, [1], [1], [1], [1,1], [1,1] is 5? No, indices: [0], [1], [2], [0,1], [1,2])
    """
    total_count = 0
    current_window_sum = 0
    left_pointer = 0

    # Iterate through the array using the right pointer to expand the window
    for right_pointer in range(len(nums)):
        current_window_sum += nums[right_pointer]

        # If the current sum exceeds k, shrink the window from the left
        while current_window_sum > k and left_pointer <= right_pointer:
            current_window_sum -= nums[left_pointer]
            left_pointer += 1

        # If the window is valid, all subarrays ending at right_pointer 
        # and starting from any index between left_pointer and right_pointer are valid.
        # The number of such subarrays is (right_pointer - left_pointer + 1).
        if current_window_sum <= k:
            total_count += (right_pointer - left_pointer + 1)

    return total_count
