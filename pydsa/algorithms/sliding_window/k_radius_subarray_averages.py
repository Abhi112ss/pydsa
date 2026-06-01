METADATA = {
    "id": 2090,
    "name": "K Radius Subarray Averages",
    "slug": "k-radius-subarray-averages",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the average of elements within a radius k for each index in an array.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Calculates the average of elements in the range [i-k, i+k] for each index i.
    If the range is out of bounds, the average is set to -1.

    Args:
        nums: A list of integers representing the input array.
        k: The radius of the subarray.

    Returns:
        A list of integers where each element is the floor of the average 
        of the subarray, or -1 if the subarray is out of bounds.

    Examples:
        >>> solve([1, 3, 2, 7, 5, 1], 1)
        [-1, 2, 4, 5, 5, -1]
        >>> solve([1, 1, 1, 1, 1], 0)
        [1, 1, 1, 1, 1]
    """
    n = len(nums)
    averages = [-1] * n
    
    # If the window size (2k + 1) is larger than the array, all averages are -1
    window_size = 2 * k + 1
    if window_size > n:
        return averages

    # Calculate the sum of the first window [0, 2k]
    current_window_sum = 0
    for i in range(window_size):
        current_window_sum += nums[i]

    # The first valid center index is k
    averages[k] = current_window_sum // window_size

    # Slide the window across the array
    # The window moves from [i-k, i+k] to [i+1-k, i+1+k]
    for i in range(k + 1, n - k):
        # Subtract the element that is leaving the window (left side)
        # Add the element that is entering the window (right side)
        left_index_to_remove = i - k - 1
        right_index_to_add = i + k
        
        current_window_sum = current_window_sum - nums[left_index_to_remove] + nums[right_index_to_add]
        averages[i] = current_window_sum // window_size

    return averages
