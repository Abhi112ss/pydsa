METADATA = {
    "id": 462,
    "name": "Minimum Moves to Equal Array Elements II",
    "slug": "minimum-moves-to-equal-array-elements-ii",
    "category": "Math",
    "aliases": [],
    "tags": ["sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves to make all array elements equal, where a move consists of incrementing or decrementing an element by 1.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of moves to make all elements in the array equal.
    A move is defined as incrementing or decrementing an element by 1.

    The optimal target value to minimize the sum of absolute differences 
    is the median of the array.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve([1, 2, 3])
        2
        >>> solve([1, 10, 2, 9])
        16
    """
    if not nums:
        return 0

    # Sort the array to easily find the median
    # Time Complexity: O(n log n)
    nums.sort()

    # The median is the middle element in a sorted array.
    # For even-sized arrays, any value between the two middle elements 
    # (inclusive) works as a median to minimize absolute differences.
    median = nums[len(nums) // 2]

    total_moves = 0
    for num in nums:
        # The number of moves for each element is the distance to the median
        total_moves += abs(num - median)

    return total_moves
