METADATA = {
    "id": 3936,
    "name": "Minimum Swaps to Move Zeros to End",
    "slug": "minimum_swaps_to_move_zeros_to_end",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum number of swaps required to move all zeros in an array to the end while maintaining the relative order of non-zero elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of swaps to move all zeros to the end of the array.
    
    The algorithm uses a two-pointer approach where one pointer tracks the 
    position where the next non-zero element should be placed, and the other 
    iterates through the array.

    Args:
        nums: A list of integers containing zeros and non-zero values.

    Returns:
        The total number of swaps performed.

    Examples:
        >>> solve([1, 0, 2, 0, 3])
        2
        >>> solve([0, 0, 1])
        2
        >>> solve([1, 2, 3])
        0
    """
    swaps_count = 0
    # next_non_zero_pos tracks the index where the next non-zero element should go
    next_non_zero_pos = 0
    
    for current_pos in range(len(nums)):
        if nums[current_pos] != 0:
            # If the current element is non-zero and not at the target position,
            # it means there is a zero preceding it that needs to be swapped.
            if current_pos != next_non_zero_pos:
                nums[next_non_zero_pos], nums[current_pos] = nums[current_pos], nums[next_non_zero_pos]
                swaps_count += 1
            
            # Move the target position forward for the next non-zero element
            next_non_zero_pos += 1
            
    return swaps_count
