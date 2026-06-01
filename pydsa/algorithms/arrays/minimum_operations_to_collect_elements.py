METADATA = {
    "id": 2869,
    "name": "Minimum Operations to Collect Elements",
    "slug": "minimum-operations-to-collect-elements",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the minimum length of a subarray that contains all elements present in a given target set.",
}

def solve(nums: list[int], target: list[int]) -> int:
    """
    Finds the minimum length of a subarray that contains all elements from the target list.

    Args:
        nums: The source array of integers.
        target: The list of integers that must all be present in the subarray.

    Returns:
        The minimum length of the subarray. Returns -1 if no such subarray exists.

    Examples:
        >>> solve([1, 3, 5, 3, 2, 1], [1, 3, 5])
        3
        >>> solve([1, 2, 3, 4, 5], [1, 6])
        -1
    """
    target_set = set(target)
    required_count = len(target_set)
    
    # If target is empty, the minimum length is 0
    if required_count == 0:
        return 0

    # counts stores the frequency of target elements within the current window
    counts: dict[int, int] = {}
    # unique_elements_in_window tracks how many distinct target elements are currently in the window
    unique_elements_in_window = 0
    
    min_length = float('inf')
    left = 0
    
    for right in range(len(nums)):
        current_val = nums[right]
        
        # If the current element is one we are looking for, update our window state
        if current_val in target_set:
            counts[current_val] = counts.get(current_val, 0) + 1
            if counts[current_val] == 1:
                unique_elements_in_window += 1
        
        # While the window contains all required elements, try to shrink it from the left
        while unique_elements_in_window == required_count:
            # Update the minimum length found so far
            min_length = min(min_length, right - left + 1)
            
            left_val = nums[left]
            if left_val in target_set:
                counts[left_val] -= 1
                if counts[left_val] == 0:
                    unique_elements_in_window -= 1
            
            left += 1
            
    return int(min_length) if min_length != float('inf') else -1
