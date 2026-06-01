METADATA = {
    "id": 3173,
    "name": "Bitwise OR of Adjacent Elements",
    "slug": "bitwise-or-of-adjacent-elements",
    "category": "Bit Manipulation",
    "aliases": [],
    "tags": ["bit_manipulation", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the bitwise OR of all adjacent elements in an array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the bitwise OR of all adjacent elements in the given array.

    Args:
        nums: A list of integers.

    Returns:
        The bitwise OR result of all adjacent pairs (nums[i] | nums[i+1]).

    Examples:
        >>> solve([1, 2, 4])
        7
        >>> solve([10, 5, 3])
        15
    """
    if not nums or len(nums) < 2:
        return 0

    result = 0
    # Iterate through the array up to the second to last element
    for i in range(len(nums) - 1):
        # Compute the bitwise OR of the current element and its neighbor
        adjacent_or = nums[i] | nums[i + 1]
        
        # Accumulate the result using bitwise OR
        # Note: The problem asks for the OR of adjacent elements. 
        # If the problem implies (nums[0]|nums[1]) | (nums[1]|nums[2]) | ...,
        # it is equivalent to the OR of all elements in the range.
        result |= adjacent_or

    return result
