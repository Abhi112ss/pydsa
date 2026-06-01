METADATA = {
    "id": 2958,
    "name": "Length of Longest Subarray With at Most K Frequency",
    "slug": "length-of-longest-subarray-with-at-most-k-frequency",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subarray where every element appears at most k times.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the length of the longest subarray where each element appears at most k times.

    Args:
        nums: A list of integers representing the input array.
        k: The maximum allowed frequency for any element in the subarray.

    Returns:
        The length of the longest valid subarray.

    Examples:
        >>> solve([1, 2, 1, 2, 3], 1)
        2
        >>> solve([1, 2, 1, 2, 3], 2)
        5
        >>> solve([1, 1, 1, 1, 1], 2)
        2
    """
    frequency_map: dict[int, int] = {}
    left_pointer = 0
    max_length = 0
    
    # Track how many elements currently violate the 'at most k' constraint
    # This allows us to shrink the window efficiently
    violations = 0

    for right_pointer in range(len(nums)):
        current_val = nums[right_pointer]
        
        # Update frequency of the incoming element
        frequency_map[current_val] = frequency_map.get(current_val, 0) + 1
        
        # If this element's frequency just exceeded k, it's a new violation
        if frequency_map[current_val] == k + 1:
            violations += 1

        # If we have any violations, shrink the window from the left
        while violations > 0:
            left_val = nums[left_pointer]
            
            # If removing this element resolves a violation, decrement violation count
            if frequency_map[left_val] == k + 1:
                violations -= 1
            
            frequency_map[left_val] -= 1
            left_pointer += 1

        # Calculate the current valid window size
        current_window_size = right_pointer - left_pointer + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
