METADATA = {
    "id": 1151,
    "name": "Minimum Swaps to Group All 1's Together",
    "slug": "minimum-swaps-to-group-all-1s-together",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps required to group all 1s together in a binary array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of swaps needed to group all 1s together.

    The strategy is to use a sliding window of size equal to the total number 
    of 1s in the array. The number of swaps required for any window is the 
    number of 0s in that window. To minimize swaps, we maximize the number 
    of 1s in the window.

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The minimum number of swaps required.

    Examples:
        >>> solve([1, 0, 1, 0, 1])
        1
        >>> solve([0, 0, 0, 1, 0])
        0
    """
    total_ones = sum(nums)
    
    # If there are no 1s or only one 1, no swaps are needed.
    if total_ones <= 1:
        return 0

    # Initial window: count 1s in the first 'total_ones' elements.
    current_ones_in_window = 0
    for i in range(total_ones):
        if nums[i] == 1:
            current_ones_in_window += 1
            
    max_ones_in_window = current_ones_in_window

    # Slide the window across the array.
    for i in range(total_ones, len(nums)):
        # Add the new element entering the window from the right.
        if nums[i] == 1:
            current_ones_in_window += 1
        
        # Remove the element leaving the window from the left.
        if nums[i - total_ones] == 1:
            current_ones_in_window -= 1
            
        # Update the maximum number of 1s found in any window.
        if current_ones_in_window > max_ones_in_window:
            max_ones_in_window = current_ones_in_window

    # The minimum swaps is the window size minus the maximum number of 1s found.
    return total_ones - max_ones_in_window
