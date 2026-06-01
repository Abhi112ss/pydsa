METADATA = {
    "id": 3254,
    "name": "Find the Power of K-Size Subarrays I",
    "slug": "find-the-power-of-k-size-subarrays-i",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum power of all k-size subarrays, where power is the product of elements if all elements are strictly increasing, otherwise 0.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum power of all k-size subarrays.
    
    The power of a subarray is defined as the product of its elements if 
    the subarray is strictly increasing. Otherwise, the power is 0.

    Args:
        nums: A list of integers.
        k: The size of the subarray to consider.

    Returns:
        The maximum power found among all k-size subarrays.

    Examples:
        >>> solve([2, 2, 2, 2], 2)
        0
        >>> solve([1, 2, 3, 4], 3)
        24
        >>> solve([1, 5, 2, 3, 4], 3)
        24
    """
    n = len(nums)
    max_power = 0
    
    # current_product stores the product of the current window
    # current_increasing_count tracks how many consecutive elements 
    # satisfy the strictly increasing condition (nums[i] > nums[i-1])
    current_product = 1
    current_increasing_count = 1
    
    for i in range(n):
        # If we are not at the first element, check if it's strictly increasing
        if i > 0:
            if nums[i] > nums[i - 1]:
                current_increasing_count += 1
            else:
                current_increasing_count = 1
        
        # Update the product for the current element
        current_product *= nums[i]
        
        # When the window reaches size k
        if i >= k - 1:
            # If the number of consecutive increasing elements is at least k,
            # it means the entire current window of size k is strictly increasing.
            if current_increasing_count >= k:
                max_power = max(max_power, current_product)
            
            # Prepare for the next iteration: remove the element that is sliding out
            # of the window from the product.
            out_of_window_idx = i - k + 1
            current_product //= nums[out_of_window_idx]
            
            # Note: We don't need to manually decrement current_increasing_count 
            # because the 'if nums[i] > nums[i-1]' logic naturally resets it 
            # based on the current position. However, we must ensure that 
            # if the window slides, the 'increasing' property is evaluated 
            # relative to the new window's start. The current logic handles 
            # this by checking the count at every step.
            
            # Correction: The current_increasing_count tracks the length of the 
            # increasing sequence ending at i. If this length is >= k, 
            # the window [i-k+1, i] is strictly increasing.
            
    return max_power
