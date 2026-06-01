METADATA = {
    "id": 2778,
    "name": "Sum of Squares of Special Elements",
    "slug": "sum-of-squares-of-special-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of squares of elements in an array that are not equal to the element at the same index in a sorted version of the array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the sum of squares of 'special' elements in the array.
    An element is special if it is not equal to the element at the same 
    index in the sorted version of the array.

    Args:
        nums: A list of integers.

    Returns:
        The sum of squares of all special elements.

    Examples:
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([3, 1, 2, 4])
        14
        >>> solve([1, 1, 1, 1])
        0
    """
    # Create a sorted version of the array to compare against
    # This takes O(n log n) time, which is the bottleneck
    sorted_nums = sorted(nums)
    
    total_sum_of_squares = 0
    
    # Iterate through the original array and compare with the sorted array
    for index in range(len(nums)):
        # An element is special if it differs from the element at the same index in sorted order
        if nums[index] != sorted_nums[index]:
            # Accumulate the square of the special element
            total_sum_of_squares += nums[index] ** 2
            
    return total_sum_of_squares
