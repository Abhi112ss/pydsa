METADATA = {
    "id": 167,
    "name": "Two Sum II - Input Array Is Sorted",
    "slug": "two-sum-ii-input-array-is-sorted",
    "category": "array",
    "aliases": [],
    "tags": ["two-pointer", "binary-search", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Finds two numbers in a sorted array that add up to a target and returns their 1-indexed positions.",
}

def solve(numbers: list[int], target: int) -> list[int]:
    """
    Finds two numbers in a sorted array that add up to a target and returns their 1-indexed positions.

    Args:
        numbers: A sorted list of integers in non-decreasing order.
        target: The target sum to find.

    Returns:
        A list containing two integers representing the 1-indexed positions of the two numbers.

    Examples:
        >>> solve([2, 7, 11, 15], 9)
        [1, 2]
        >>> solve([2, 3, 4], 6)
        [1, 3]
        >>> solve([-1, 0], -1)
        [1, 2]
    """
    left = 0
    right = len(numbers) - 1
    
    # Use two pointers starting from both ends of the array
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        # If sum matches target, return 1-indexed positions
        if current_sum == target:
            return [left + 1, right + 1]
        
        # If sum is too small, move left pointer right to increase sum
        elif current_sum < target:
            left += 1
        
        # If sum is too large, move right pointer left to decrease sum
        else:
            right -= 1
    
    # The problem guarantees exactly one solution, so we don't handle no-solution case
    return []