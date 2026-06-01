METADATA = {
    "id": 3038,
    "name": "Maximum Number of Operations With the Same Score I",
    "slug": "maximum-number-of-operations-with-the-same-score-i",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of operations possible where each operation removes elements from either end such that the score remains the same.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum number of operations possible where each operation 
    removes elements from either end such that the score remains the same.

    An operation consists of choosing either the first or the last element, 
    calculating the score (the value of the chosen element), and removing it. 
    The goal is to maximize the number of operations where all scores are equal.

    Args:
        nums: A list of integers representing the initial scores.

    Returns:
        The maximum number of operations with the same score.

    Examples:
        >>> solve([1, 2, 2, 1])
        2
        >>> solve([1, 1, 1, 1])
        4
        >>> solve([1, 2, 3, 4])
        1
    """
    n = len(nums)
    max_operations = 0

    # Since we want the same score for all operations, the score must be 
    # one of the values present at the ends of the array.
    # We check two scenarios: 
    # 1. All operations use the value at the start (nums[0]).
    # 2. All operations use the value at the end (nums[-1]).
    # Note: If nums[0] == nums[-1], both scenarios will yield the same result.

    # Scenario 1: Target score is nums[0]
    target_start = nums[0]
    left = 0
    right = n - 1
    count_start = 0
    
    while left <= right:
        if nums[left] == target_start:
            count_start += 1
            left += 1
        elif nums[right] == target_start:
            count_start += 1
            right -= 1
        else:
            # Cannot perform more operations with this target score
            break
    max_operations = max(max_operations, count_start)

    # Scenario 2: Target score is nums[-1]
    target_end = nums[-1]
    left = 0
    right = n - 1
    count_end = 0
    
    while left <= right:
        if nums[left] == target_end:
            count_end += 1
            left += 1
        elif nums[right] == target_end:
            count_end += 1
            right -= 1
        else:
            # Cannot perform more operations with this target score
            break
    max_operations = max(max_operations, count_end)

    return max_operations
