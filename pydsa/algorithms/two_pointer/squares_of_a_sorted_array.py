METADATA = {
    "id": 977,
    "name": "Squares of a Sorted Array",
    "slug": "squares-of-a-sorted-array",
    "category": "Array",
    "aliases": [],
    "tags": ["two pointers", "sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Computes the squares of a sorted array and returns them in sorted order.

    Args:
        nums: A list of integers sorted in non-decreasing order.

    Returns:
        A list of integers representing the squares of the input, sorted non-decreasingly.

    Examples:
        >>> solve([-4, -1, 0, 3, 10])
        [0, 1, 9, 16, 100]
        >>> solve([-7, -3, 2, 3, 11])
        [4, 9, 9, 49, 121]
    """
    n = len(nums)
    # Initialize the result array with zeros
    result = [0] * n
    
    # Use two pointers to compare the absolute values at both ends
    left = 0
    right = n - 1
    
    # Fill the result array from the largest value (end) to the smallest (start)
    for i in range(n - 1, -1, -1):
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        
        if left_square > right_square:
            result[i] = left_square
            left += 1
        else:
            result[i] = right_square
            right -= 1
            
    return result
