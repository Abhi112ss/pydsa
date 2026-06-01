METADATA = {
    "id": 2765,
    "name": "Longest Alternating Subarray",
    "slug": "longest_alternating_subarray",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy", "sliding window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray where the signs of adjacent elements alternate.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray where the signs of adjacent elements alternate.
    
    An alternating subarray is defined such that for any index i in the subarray,
    nums[i] * nums[i+1] < 0.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest alternating subarray.

    Examples:
        >>> solve([1, -2, 3, -4])
        4
        >>> solve([1, 2, 3, 4])
        1
        >>> solve([-1, 1, -1, 1, 2, -2, 2])
        4
    """
    n = len(nums)
    if n == 0:
        return 0
    
    max_length = 1
    current_length = 1

    for i in range(n - 1):
        # Check if the product of adjacent elements is negative.
        # This implies one is positive and the other is negative.
        # Note: 0 is neither positive nor negative, so 0 * x = 0, which is not < 0.
        if nums[i] * nums[i + 1] < 0:
            current_length += 1
        else:
            # Reset the current sequence length if the alternating pattern breaks.
            current_length = 1
        
        # Update the global maximum found so far.
        if current_length > max_length:
            max_length = current_length

    return max_length
