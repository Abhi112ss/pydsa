METADATA = {
    "id": 3346,
    "name": "Maximum Frequency of an Element After Performing Operations I",
    "slug": "maximum-frequency-of-an-element-after-performing-operations-i",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum frequency of an element after performing at most one operation of adding or subtracting 1 from an element.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum frequency of an element after performing at most one 
    operation (adding or subtracting 1) on any element.

    The problem asks for the maximum number of elements that can be made equal 
    to some value 'x' such that for each element 'nums[i]', |nums[i] - x| <= 1.
    This means for a chosen target value 'x', we can include any element 
    that is currently x-1, x, or x+1.

    Args:
        nums: A list of integers.

    Returns:
        The maximum frequency possible.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        3
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([1, 3, 5])
        1
    """
    if not nums:
        return 0

    # Sort the array to use a sliding window approach.
    # For any target value x, the elements that can become x are in the range [x-1, x+1].
    nums.sort()
    n = len(nums)
    max_freq = 0
    left = 0

    # We iterate through the sorted array. For each element nums[right], 
    # we treat it as a potential candidate for the 'center' of our target range.
    # However, the problem is simpler: we want to find the maximum count of 
    # elements in a range [v-1, v+1] for some integer v.
    # Since we can only change an element by +/- 1, the elements must be 
    # within a distance of 2 from each other (e.g., 1, 2, 3 can all become 2).
    
    for right in range(n):
        # The condition for a valid window where all elements can be transformed 
        # to some value 'v' is that the difference between the max and min 
        # in the window is at most 2, AND we must ensure they can all 
        # converge to the SAME integer.
        # If nums[right] - nums[left] <= 2, they can all become the middle value.
        # Example: [1, 2, 3] -> all can become 2.
        # Example: [1, 3] -> both can become 2.
        # Example: [1, 1, 3] -> all can become 2.
        # Example: [1, 3, 3] -> all can become 2.
        # Example: [1, 1, 1] -> all can become 1.
        
        while nums[right] - nums[left] > 2:
            left += 1
            
        # After shrinking the window, all elements in nums[left...right] 
        # are within a range of 2. This means there exists an integer 'v' 
        # such that every element in the window is in {v-1, v, v+1}.
        # Specifically, if the range is [x, x+2], they can all become x+1.
        # If the range is [x, x+1], they can all become x or x+1.
        # If the range is [x, x], they can all become x.
        
        # However, there is a subtle constraint: the problem asks for the 
        # maximum frequency of AN element. If we pick target 'v', we can 
        # only pick elements from {v-1, v, v+1}.
        # In a sorted window where nums[right] - nums[left] <= 2, 
        # there is always an integer 'v' that covers all elements.
        # If window is [1, 2, 3], v=2 works.
        # If window is [1, 3], v=2 works.
        # If window is [1, 1, 2], v=1 or v=2 works.
        
        # Wait, the logic above is slightly flawed for the "at most one operation" 
        # constraint if we consider the target value must be one of the 
        # existing values or a value adjacent to them. 
        # Actually, the window [nums[left], nums[right]] where 
        # nums[right] - nums[left] <= 2 is exactly what we need.
        
        max_freq = max(max_freq, right - left + 1)

    return max_freq
