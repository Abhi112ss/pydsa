METADATA = {
    "id": 453,
    "name": "Minimum Moves to Equal Array Elements",
    "slug": "minimum_moves_to_equal_array_elements",
    "category": "Math",
    "aliases": ["min_moves_equal_array_elements"],
    "tags": ["math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves to make all array elements equal, where each move increments n-1 elements by 1.",
}

def solve(nums: list[int]) -> int:
    """Calculate the minimum number of moves to make all array elements equal.

    Each move increments n-1 elements by 1, which is mathematically equivalent
    to decrementing one element by 1. The optimal strategy is to decrement each
    element down to the minimum value.

    Args:
        nums: A list of integers representing the array elements.

    Returns:
        The minimum number of moves required to make all elements equal.

    Examples:
        >>> solve([1, 2, 3])
        3
        >>> solve([1, 1, 1])
        0
        >>> solve([5, 6, 8, 8, 5])
        7
    """
    # Find the minimum element - this is our target value
    min_val = min(nums)
    
    # Sum the differences between each element and the minimum
    # This equals the total number of single-element decrements needed
    total_moves = sum(num - min_val for num in nums)
    
    return total_moves