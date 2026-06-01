METADATA = {
    "id": 3847,
    "name": "Find the Score Difference in a Game",
    "slug": "find-the-score-difference-in-a-game",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum possible score difference by picking elements greedily from a sorted array.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum score difference by picking elements greedily.
    
    The strategy is to sort the array in descending order and alternate 
    between adding and subtracting elements to maximize the sum.
    
    Args:
        nums: A list of integers representing the game elements.
        
    Returns:
        The maximum possible score difference.
        
    Examples:
        >>> solve([4, 2, 5, 3])
        2
        >>> solve([1, 1, 1, 1])
        0
    """
    # Sort the array in descending order to pick the largest available values first
    nums.sort(reverse=True)
    
    score_difference = 0
    
    # Iterate through the sorted array and alternate the sign
    # Even indices (0, 2, ...) are added, odd indices (1, 3, ...) are subtracted
    for index in range(len(nums)):
        if index % 2 == 0:
            score_difference += nums[index]
        else:
            score_difference -= nums[index]
            
    return score_difference
