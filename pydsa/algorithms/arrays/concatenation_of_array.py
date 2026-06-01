METADATA = {
    "id": 1929,
    "name": "Concatenation of Array",
    "slug": "concatenation-of-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an integer array nums, create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Creates a new array that is the concatenation of the input array with itself.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers of length 2n, where the first n elements are 
        the original array and the next n elements are also the original array.

    Examples:
        >>> solve([1, 2, 1])
        [1, 2, 1, 1, 2, 1]
        >>> solve([1])
        [1, 1]
    """
    n = len(nums)
    # Initialize the result array with a fixed size to avoid repeated reallocations
    result = [0] * (2 * n)
    
    for i in range(n):
        # Fill the first half of the result array
        result[i] = nums[i]
        # Fill the second half of the result array using the same index offset
        result[i + n] = nums[i]
        
    return result
