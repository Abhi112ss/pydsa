METADATA = {
    "id": 2461,
    "name": "Maximum Sum of Distinct Subarrays With Length K",
    "slug": "maximum-sum-of-distinct-subarrays-with-length-k",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the maximum sum of all subarrays of length k that contain only distinct elements.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum sum of subarrays of length k where all elements are distinct.

    Args:
        nums: A list of integers.
        k: The required length of the subarrays.

    Returns:
        The maximum sum found, or 0 if no such subarray exists.

    Examples:
        >>> solve([1, 5, 4, 2, 9, 9, 9], 3)
        15
        >>> solve([1, 2, 1, 2, 1, 2, 1], 3)
        0
    """
    max_sum = 0
    current_sum = 0
    # Frequency map to track counts of elements in the current window
    element_counts = {}
    # Pointer for the start of the sliding window
    window_start = 0

    for window_end in range(len(nums)):
        right_val = nums[window_end]
        current_sum += right_val
        element_counts[right_val] = element_counts.get(right_val, 0) + 1

        # If the window size exceeds k, remove the leftmost element
        if window_end - window_start + 1 > k:
            left_val = nums[window_start]
            current_sum -= left_val
            element_counts[left_val] -= 1
            if element_counts[left_val] == 0:
                del element_counts[left_val]
            window_start += 1

        # Check if the current window is valid:
        # 1. It must have exactly k elements.
        # 2. All elements must be distinct (size of map == k).
        if window_end - window_start + 1 == k:
            if len(element_counts) == k:
                max_sum = max(max_sum, current_sum)

    return max_sum
