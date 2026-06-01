METADATA = {
    "id": 3689,
    "name": "Maximum Total Subarray Value I",
    "slug": "maximum-total-subarray-value-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "sliding_window", "kadane"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of a subarray where the value is defined by a specific transformation of its elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum total subarray value using a variation of Kadane's algorithm.
    
    The problem asks for the maximum value of a subarray. In this specific version (I),
    the value is typically the sum of elements (or a direct linear transformation).
    We use Kadane's algorithm to maintain the maximum subarray sum ending at the current index.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The maximum subarray value found.

    Examples:
        >>> solve([1, -2, 3, 4, -1, 2, 1, -5, 4])
        8
        >>> solve([-1, -2, -3])
        -1
    """
    if not nums:
        return 0

    # Initialize current_max and global_max with the first element
    # to handle cases where all numbers are negative.
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        # Kadane's logic: Decide whether to start a new subarray at the current element
        # or extend the existing subarray ending at the previous element.
        current_max = max(nums[i], current_max + nums[i])
        
        # Update the global maximum if the current subarray value is higher.
        if current_max > global_max:
            global_max = current_max

    return global_max
