METADATA = {
    "id": 3089,
    "name": "Find Bursty Behavior",
    "slug": "find_bursty_behavior",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of elements within a sliding window of size k that fall within a specific value range.",
}

def solve(nums: list[int], k: int, threshold_min: int, threshold_max: int) -> int:
    """
    Finds the maximum number of elements in any subarray of length k 
    that fall within the inclusive range [threshold_min, threshold_max].

    Args:
        nums: A list of integers representing the sequence.
        k: The size of the sliding window.
        threshold_min: The lower bound of the bursty range (inclusive).
        threshold_max: The upper bound of the bursty range (inclusive).

    Returns:
        The maximum count of elements within the range found in any window of size k.

    Examples:
        >>> solve([1, 5, 2, 4, 3], 3, 2, 4)
        2
        >>> solve([1, 1, 1, 1], 2, 1, 1)
        2
    """
    n = len(nums)
    if n == 0 or k == 0:
        return 0

    # Ensure k does not exceed the array length
    k = min(k, n)
    
    current_burst_count = 0
    max_burst_count = 0

    # Initialize the first window of size k
    for i in range(k):
        if threshold_min <= nums[i] <= threshold_max:
            current_burst_count += 1
    
    max_burst_count = current_burst_count

    # Slide the window across the array
    for i in range(k, n):
        # Remove the element that is sliding out of the window (left side)
        outgoing_element = nums[i - k]
        if threshold_min <= outgoing_element <= threshold_max:
            current_burst_count -= 1
            
        # Add the new element sliding into the window (right side)
        incoming_element = nums[i]
        if threshold_min <= incoming_element <= threshold_max:
            current_burst_count += 1
            
        # Update the global maximum found so far
        if current_burst_count > max_burst_count:
            max_burst_count = current_burst_count

    return max_burst_count
