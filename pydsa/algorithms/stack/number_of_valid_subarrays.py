METADATA = {
    "id": 1063,
    "name": "Number of Valid Subarrays",
    "slug": "number-of-valid-subarrays",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "arrays", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of non-empty subarrays where the leftmost element is not greater than any other element in the subarray.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the total number of valid subarrays using a monotonic increasing stack.
    
    A subarray is valid if the first element is the minimum element in that subarray.
    This is equivalent to finding the index of the first element to the right 
    that is smaller than the current element.

    Args:
        nums: A list of integers.

    Returns:
        The total count of valid subarrays.

    Examples:
        >>> solve([1, 4, 2, 5, 3])
        11
        # Subarrays starting at index 0: [1], [1,4], [1,4,2], [1,4,2,5], [1,4,2,5,3] (5)
        # Subarrays starting at index 1: [4] (1)
        # Subarrays starting at index 2: [2], [2,5], [2,5,3] (3)
        # Subarrays starting at index 3: [5] (1)
        # Subarrays starting at index 4: [3] (1)
        # Total: 5 + 1 + 3 + 1 + 1 = 11
    """
    total_valid_subarrays = 0
    # The stack will store indices of elements in a non-decreasing order.
    # This allows us to find the 'next smaller element' for each index.
    monotonic_stack: list[int] = []
    n = len(nums)

    for current_index in range(n):
        # While the current element is smaller than the element at the index 
        # on top of the stack, we have found the 'boundary' for the element 
        # at the top of the stack.
        while monotonic_stack and nums[current_index] < nums[monotonic_stack[-1]]:
            smaller_element_index = monotonic_stack.pop()
            # The number of valid subarrays starting at 'smaller_element_index'
            # is the distance to the first element that is strictly smaller.
            total_valid_subarrays += (current_index - smaller_element_index)
        
        monotonic_stack.append(current_index)

    # For elements remaining in the stack, there is no smaller element to their right.
    # Their 'boundary' is effectively the end of the array (index n).
    while monotonic_stack:
        start_index = monotonic_stack.pop()
        total_valid_subarrays += (n - start_index)

    return total_valid_subarrays
