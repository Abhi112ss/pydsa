METADATA = {
    "id": 3411,
    "name": "Maximum Subarray With Equal Products",
    "slug": "maximum-subarray-with-equal-products",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "prefix_product"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest contiguous subarray where all elements have the same product value (specifically, where the product of elements is equal to a target or follows a specific pattern).",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest contiguous subarray where all elements 
    result in the same product. 
    
    Note: In the context of 'equal products' for a subarray, if we are looking 
    for a subarray where the product of its elements equals a specific value 
    or if the problem implies elements themselves are equal (since product 
    of a single element is the element), the most common interpretation 
    for 'equal products' in subarray problems is finding segments where 
    the product remains constant or elements are identical. 
    
    Given the constraints and typical LeetCode patterns for this description, 
    this implementation finds the longest subarray where all elements are equal, 
    as that is the only way a contiguous subarray's product remains 'equal' 
    to a target property consistently across sliding windows without 
    exponential growth.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest subarray.

    Examples:
        >>> solve([1, 2, 2, 2, 3, 3])
        3
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([5, 4, 3, 2, 1])
        1
    """
    if not nums:
        return 0

    max_length = 0
    current_length = 0
    previous_value = None

    for num in nums:
        # If the current number is the same as the previous, 
        # it continues the 'equal product' (equal element) sequence.
        if num == previous_value:
            current_length += 1
        else:
            # Otherwise, reset the count to 1 for the new element.
            current_length = 1
            previous_value = num
        
        # Update the global maximum length found so far.
        if current_length > max_length:
            max_length = current_length

    return max_length
