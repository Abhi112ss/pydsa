METADATA = {
    "id": 3347,
    "name": "Maximum Frequency of an Element After Performing Operations II",
    "slug": "maximum-frequency-of-an-element-after-performing-operations-ii",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum frequency of an element after performing operations to make elements in a window equal within a given budget.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum frequency of an element after performing operations.
    An operation consists of increasing or decreasing an element by 1, costing 1 unit.
    The total cost must not exceed k.

    Args:
        nums: A list of integers representing the available elements.
        k: The maximum total cost allowed for operations.

    Returns:
        The maximum frequency of any single element achievable within the budget k.

    Examples:
        >>> solve([1, 2, 4], 5)
        3
        >>> solve([1, 10, 100], 1)
        1
    """
    # Sorting is necessary to use the sliding window approach effectively,
    # as elements close to each other in value require fewer operations to equalize.
    nums.sort()
    
    n = len(nums)
    max_frequency = 0
    left = 0
    current_cost = 0
    
    # We use a sliding window [left, right]. 
    # We attempt to make all elements in the window equal to nums[right].
    for right in range(n):
        # When moving the right pointer, the cost increases.
        # The new element nums[right] is added. To make all previous elements 
        # in the window equal to nums[right], the cost increases by:
        # (nums[right] - nums[right-1]) * (number of elements in the window before adding nums[right])
        if right > 0:
            current_cost += (nums[right] - nums[right - 1]) * (right - left)
            
        # If the current cost exceeds k, shrink the window from the left.
        # When removing nums[left], the cost decreases by the difference 
        # between the target value (nums[right]) and the removed value.
        while current_cost > k:
            current_cost -= (nums[right] - nums[left])
            left += 1
            
        # Update the maximum frequency found so far.
        max_frequency = max(max_frequency, right - left + 1)
        
    return max_frequency
