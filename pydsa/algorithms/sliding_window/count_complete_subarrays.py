METADATA = {
    "id": 2799,
    "name": "Count Complete Subarrays in an Array",
    "slug": "count-complete-subarrays-in-an-array",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subarrays that contain all the distinct elements present in the original array.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays that contain all distinct elements of the input array.

    A subarray is considered 'complete' if it contains every unique element 
    found in the original array at least once.

    Args:
        nums: A list of integers.

    Returns:
        The total count of complete subarrays.

    Examples:
        >>> solve([1, 3, 2, 2, 5, 4])
        13
        >>> solve([1, 1, 1])
        0
        >>> solve([1, 2, 1, 2])
        4
    """
    # Determine the total number of unique elements in the array
    distinct_elements_count = len(set(nums))
    n = len(nums)
    
    # If there are no elements or only one type of element, 
    # the logic remains consistent, but we handle the base case.
    if distinct_elements_count == 0:
        return 0

    total_complete_subarrays = 0
    current_window_counts: dict[int, int] = {}
    unique_in_window = 0
    left = 0

    # Use a sliding window (two pointers) to find valid subarrays
    for right in range(n):
        # Expand the window by adding the element at the right pointer
        val_right = nums[right]
        current_window_counts[val_right] = current_window_counts.get(val_right, 0) + 1
        
        # If this is the first time we see this element in the current window
        if current_window_counts[val_right] == 1:
            unique_in_window += 1

        # While the current window contains all distinct elements
        while unique_in_window == distinct_elements_count:
            # If the window [left, right] is complete, then all subarrays 
            # starting at 'left' and ending at any index from 'right' to 'n-1'
            # are also complete.
            total_complete_subarrays += (n - right)

            # Shrink the window from the left to find the next smallest complete window
            val_left = nums[left]
            current_window_counts[val_left] -= 1
            if current_window_counts[val_left] == 0:
                unique_in_window -= 1
            
            left += 1

    return total_complete_subarrays
