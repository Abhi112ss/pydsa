METADATA = {
    "id": 1464,
    "name": "Maximum Product of Two Elements in an Array",
    "slug": "maximum-product-of-two-elements-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of (nums[i]-1)*(nums[j]-1) where i != j.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum product of (nums[i]-1) * (nums[j]-1) for two distinct indices.

    The optimal approach is to find the two largest numbers in the array in a single 
    pass to ensure O(n) time complexity and O(1) space complexity.

    Args:
        nums: A list of integers.

    Returns:
        The maximum product of (nums[i]-1) * (nums[j]-1).

    Examples:
        >>> solve([3, 4, 5, 2])
        24
        >>> solve([1, 5, 4, 5])
        16
    """
    # Initialize the two largest values found so far
    max_one = 0
    max_two = 0

    for num in nums:
        # If current number is larger than the largest found so far
        if num > max_one:
            # The old largest becomes the second largest
            max_two = max_one
            max_one = num
        # If current number is between the largest and second largest
        elif num > max_two:
            max_two = num

    # The problem asks for (nums[i]-1) * (nums[j]-1)
    return (max_one - 1) * (max_two - 1)
