METADATA = {
    "id": 2134,
    "name": "Minimum Swaps to Group All 1's Together II",
    "slug": "minimum-swaps-to-group-all-1s-together-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps required to group all 1s together in a circular array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of swaps needed to group all 1s together in a circular array.

    The problem is treated as a sliding window problem on a doubled array (to simulate circularity).
    The number of swaps needed for a window of size K is (K - number of 1s in that window).
    To minimize swaps, we maximize the number of 1s in the window.

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

    n = len(nums)
    # We use a sliding window of size 'total_ones'.
    # To handle the circular nature, we conceptually extend the array to 2n.
    # Instead of creating a new array, we use modulo arithmetic or just iterate up to n + total_ones.
    
    current_ones_in_window = 0
    # Initialize the first window of size total_ones
    for i in range(total_ones):
        current_ones_in_window += nums[i]
    
    max_ones_in_window = current_ones_in_window
    
    # Slide the window across the circular array.
    # The window starts at index 1 and ends when the window's end reaches n + total_ones - 1.
    for i in range(n):
        # Remove the element that is sliding out of the window (at index i)
        current_ones_in_window -= nums[i]
        # Add the element that is sliding into the window (at index (i + total_ones) % n)
        current_ones_in_window += nums[(i + total_ones) % n]
        
        if current_ones_in_window > max_ones_in_window:
            max_ones_in_window = current_ones_in_window
            
    # The minimum swaps is the total number of 1s minus the maximum 1s found in any window.
    return total_ones - max_ones_in_window
