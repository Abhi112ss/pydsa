METADATA = {
    "id": 2221,
    "name": "Find Triangular Sum of an Array",
    "slug": "find-triangular-sum-of-an-array",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Given an integer array nums, return the triangular sum of nums.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the triangular sum of an array by repeatedly summing adjacent elements modulo 10.

    The process mimics the construction of a Pascal's triangle structure where each 
    new row is derived from the sum of adjacent elements in the previous row.

    Args:
        nums: A list of integers representing the initial row.

    Returns:
        The single integer remaining after the triangular reduction process.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        8
        >>> solve([1, 1, 1])
        3
        >>> solve([2, 5, 1, 3, 9, 12])
        2
    """
    n = len(nums)
    
    # We can perform the reduction in-place to achieve O(1) extra space complexity.
    # Each iteration reduces the effective size of the array by 1.
    for row_length in range(n, 1, -1):
        for i in range(row_length - 1):
            # Update the element at index i with the sum of current and next element mod 10.
            # This simulates the next row of the triangle being built within the same array.
            nums[i] = (nums[i] + nums[i + 1]) % 10
            
    return nums[0]
