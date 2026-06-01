METADATA = {
    "id": 1480,
    "name": "Running Sum of 1d Array",
    "slug": "running_sum_of_1d_array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given an array nums, we define a running sum of an array as the running sum of nums where runningSum[i] = sum(nums[0]…nums[i]).",
}

def solve(nums: list[int]) -> list[int]:
    """
    Calculates the running sum of a 1D array in-place.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers representing the running sum of the input array.

    Examples:
        >>> solve([1, 2, 3, 4])
        [1, 3, 6, 10]
        >>> solve([1, 1, 1, 1, 1])
        [1, 2, 3, 4, 5]
        >>> solve([3, 1, 2, 10, 1])
        [3, 4, 6, 16, 17]
    """
    # Start from the second element (index 1) because the first element 
    # remains the same in a running sum.
    for index in range(1, len(nums)):
        # Update the current element by adding the value of the previous element.
        # This effectively accumulates the sum as we traverse the array.
        nums[index] += nums[index - 1]
        
    return nums
