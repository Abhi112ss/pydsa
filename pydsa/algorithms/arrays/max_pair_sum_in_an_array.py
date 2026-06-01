METADATA = {
    "id": 2815,
    "name": "Max Pair Sum in an Array",
    "slug": "max-pair-sum-in-an-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of two elements from an array such that each element is used at most once.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of two elements from the given array.
    
    To maximize the sum of a pair, we should pair the largest available 
    elements together. Sorting the array allows us to easily access 
    the largest values at the end of the list.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of two elements from the array.

    Examples:
        >>> solve([2, 4, 3, 5])
        9
        >>> solve([1, 1, 1, 1])
        2
    """
    # Sort the array in ascending order to bring largest elements to the end
    nums.sort()
    
    # The two largest elements will be at the last two indices
    n = len(nums)
    max_sum = nums[n - 1] + nums[n - 2]
    
    return max_sum
